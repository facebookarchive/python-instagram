from datetime import datetime

def timestamp_to_datetime(ts):
    return datetime.utcfromtimestamp(float(ts))
