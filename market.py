from flask import Flask, jsonify
import pandas_market_calendars as mcal
from datetime import date, datetime

app = Flask(__name__)
cboe = mcal.get_calendar('CBOE_Equity_Options')

@app.route("/today-times", methods=["GET"])
def get_today_times():
    today = date.today()
    schedule = cboe.schedule(start_date=today, end_date=today)

    if schedule.empty:
        return jsonify({"open": None, "close": None, "note": "Market closed."})

    open_time = schedule.iloc[0]['market_open'].isoformat()
    close_time = schedule.iloc[0]['market_close'].isoformat()
    return jsonify({"open": open_time, "close": close_time})

@app.route("/market-times/<datestr>", methods=["GET"])
def get_market_times(datestr):
    try:
        target_date = datetime.strptime(datestr, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format, expected YYYY-MM-DD"}), 400

    schedule = cboe.schedule(start_date=target_date, end_date=target_date)

    if schedule.empty:
        return jsonify({"open": None, "close": None, "note": "Market closed."})

    open_time = schedule.iloc[0]['market_open'].isoformat()
    close_time = schedule.iloc[0]['market_close'].isoformat()
    return jsonify({"open": open_time, "close": close_time})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
