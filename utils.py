from datetime import datetime

def format_timestamp(iso_timestamp):
    """
    Convert GitHub ISO timestamp to a readable format.
    Example: '2025-07-04T10:25:00Z' -> '04-Jul-2025 10:25:00'
    """
    try:
        dt = datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%SZ")
        return dt.strftime("%d-%b-%Y %H:%M:%S")
    except Exception as e:
        return f"Invalid timestamp ({e})"
