# APIs and how to use them

## Location

Geolocation:

```ts
window.navigator.geolocation.getCurrentPosition(position => {
    // ...
});
```

Geocoding:

[Account as necessary](https://geocode.maps.co/join/)

GET `https://geocode.maps.co/search?q=[ADDRESS]&key=[API_KEY]`

```json5
[
    {
        "lat": "string",
        "lon": "string",
        "importance": 0.5,
        // ...
    }
]
```

## Weather

### USA

Using the [National Weather Service](https://www.weather.gov/documentation/services-web-api).
All API calls should receive a unique-for-project `User-Agent` header.
Likely for us: `User-Agent: Spring 2023 CSCI-313 students (steven.schreifels@ndsu.edu)`

#### Weather at location:

GET `https://api.weather.gov/points/[LATITUDE],[LONGITUDE]`

```json5
{
    "properties": {
        "cwa": "string",
        "forecast": "string", // Future data with descriptions
        "forecastHourly": "string", // Future hourly data
        "forecastGridData": "string",
    }
}
```
