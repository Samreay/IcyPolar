import datetime as dt

def decimal_date_to_iso(dd):
    if isinstance(dd, str):
        dd = float(dd)

    year = int(dd)
    days = dt.timedelta((dd - year) * 365.25)
    return (days + dt.datetime(year, 1, 1)).isoformat() + 'Z'
