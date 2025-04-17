# pymarkets
This is a simple flask app that exposes `pandas_market_calendars` functionality over HTTP on localhost.  This allows using the awesome functionality of the pandas ecosystem in applications written in languages other than python.

I wrote this for my own personal use as a quality-of-life utility for my algorithmic trading application, so defaults reflect that.  It is intended to be run inside a docker container and exposed only to a trusted localhost environment.

## Howto
1. `git clone`
2. Edit `market.py` to choose your market of interest.  Defaults to Cboe equity options.
3. `docker compose up --build -d`

The app exposes two routes:

### `/today-times`
Returns market open and close datetimes in JSON of the form `{"close":"2025-04-17T20:00:00+00:00","open":"2025-04-17T13:30:00+00:00"}` for "today", i.e. the current day.

### `/market-times/<YYYY-MM-DD>`
Returns market open and close datetimes in JSON, in the same form as above for the date represented by `YYYY-MM-DD`.

### Market Holidays
For dates when the markets are closed, or when the `open` and `close` values will be null, and a `note` parameter is appended.

## WARNING
This just uses the standard internal flask httpd, and performs only minimal input validation.  **This code not even close to robust enough to expose to the public internet.**  Consider yourself warned.
