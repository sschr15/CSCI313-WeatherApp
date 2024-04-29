from datetime import datetime, timedelta
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
        raise ValueError(f"Invalid interval: {interval}")
