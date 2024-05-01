from datetime import datetime, timedelta
from typing import Type, TypeVar, Any
import inspect
import re

_iso_time_pattern = re.compile(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:?\d{2}?)|NOW)')
_iso_duration_pattern = re.compile(r'P(\d+Y)?(\d+M)?(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?)?')

_start_and_end = re.compile(r'(?P<start>{time})/(?P<end>{time})'.format(time=_iso_time_pattern.pattern))
_start_and_duration = re.compile(r'(?P<start>{time})/(?P<duration>{duration})'.format(time=_iso_time_pattern.pattern, duration=_iso_duration_pattern.pattern))
_duration_and_end = re.compile(r'(?P<duration>{duration})/(?P<end>{time})'.format(time=_iso_time_pattern.pattern, duration=_iso_duration_pattern.pattern))


def parse_iso_duration(duration: str) -> timedelta:
    """Parse an ISO 8601 duration string into a datetime.
    This is not accurate for durations that include months or years,
    as it assumes exactly 4 weeks per month and 52 weeks per year.
    """
    if match := _iso_duration_pattern.match(duration):
        years = int(match.group(1)[:-1]) if match.group(1) else 0
        months = int(match.group(2)[:-1]) if match.group(2) else 0
        days = int(match.group(3)[:-1]) if match.group(3) else 0
        hours = int(match.group(5)[:-1]) if match.group(5) else 0
        minutes = int(match.group(6)[:-1]) if match.group(6) else 0
        seconds = int(match.group(7)[:-1]) if match.group(7) else 0
        return timedelta(days=days, seconds=seconds, minutes=minutes, hours=hours, weeks=4*months+52*years)
    else:
        raise ValueError(f"Invalid duration: {duration}")


def parse_iso_interval(interval: str) -> tuple[datetime, datetime]:
    """Parse an ISO 8601 interval string into a tuple of datetimes."""
    if match := _start_and_end.match(interval):
        start = match.group('start')
        end = match.group('end')
        return datetime.fromisoformat(start), datetime.fromisoformat(end)
    elif match := _start_and_duration.match(interval):
        start = match.group('start')
        duration = match.group('duration')
        return datetime.fromisoformat(start), datetime.fromisoformat(start) + parse_iso_duration(duration)
    elif match := _duration_and_end.match(interval):
        duration = match.group('duration')
        end = match.group('end')
        return datetime.fromisoformat(end) - parse_iso_duration(duration), datetime.fromisoformat(end)
    else:
        raise ValueError(f'Invalid interval: {interval}')


_T = TypeVar('_T')


class _Quantifiable:
    def __init__(self, type_: Type[_T]):
        self.type = type_


class _NoaaQuantifiable:
    def __getitem__(self, item: Type[_T]) -> _Quantifiable:
        return _Quantifiable(item)


NoaaQuantifiable = _NoaaQuantifiable()
"""Indicates that NOAA wraps this value in a JSON object with a 'value' key."""


def noaa_data(class_arg=None, *, ignored_fields: list[str] | None = None):
    """A decorator to indicate that a class represents data from the NOAA API.
    This is used for unwrapping NOAA quantities, parsing datetimes, and other non-JSON-capable information.
    """
    ignored = ignored_fields or []

    def generator(cls):
        from .types import TimePeriod  # Placed here to avoid circular imports

        annotations = inspect.get_annotations(cls)
        fields = {}
        quantifiables: set[str] = set()
        datetimes: set[str] = set()
        time_ranges: set[str] = set()
        for field_name, type_ in annotations.items():
            if isinstance(type_, str):
                type_ = eval(type_)
            fields[field_name] = type_
            if type_ is _Quantifiable or type(type_) is _Quantifiable:
                fields[field_name] = type_.type
                quantifiables.add(field_name)
            elif type_ is datetime or type(type_) is datetime:
                datetimes.add(field_name)
            elif type_ is TimePeriod or type(type_) is TimePeriod:
                time_ranges.add(field_name)

        setattr(cls, '_noaa_fields', fields)

        def __init__(self, data=None, /, **kwargs):
            if not data:
                data = kwargs

            self._noaa_quantifiable_types = {}

            for field in fields:
                if field not in data and field not in ignored:
                    raise TypeError(f'Missing required field: {field}')
                if field in quantifiables:
                    value = data[field]['value']
                    self._noaa_quantifiable_types[field] = data[field]['unitCode']
                elif field in datetimes:
                    value = datetime.fromisoformat(data[field])
                elif field in time_ranges:
                    value = parse_iso_interval(data[field])
                elif field in ignored:
                    continue
                else:
                    value = data[field]

                setattr(self, field, value)

            for field in data.keys():
                if field not in fields and globals().get('__noaa_debug__'):
                    print(f'Warning: Ignoring unknown field: {field}')

            if hasattr(self, '_post_init'):
                self._post_init(data)

        def __repr__(self):
            return f'{cls.__name__}({", ".join(f"{field}={getattr(self, field)!r}" for field in fields)})'

        cls.__init__ = __init__

        if cls.__repr__ is object.__repr__:  # Only set the repr if it's the default
            cls.__repr__ = __repr__

        return cls

    return generator(class_arg) if class_arg else generator
