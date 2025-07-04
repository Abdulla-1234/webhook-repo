from datetime import datetime

def format_timestamp(iso_timestamp):
    """
    Convert ISO GitHub timestamp to a human-readable format.

    Example:
        Input: '2025-07-04T09:30:45Z'
        Output: '04-Jul-2025 15:00:45' (adjust to IST if needed)
    """
    try:
        # Parse the ISO 8601 timestamp
        dt = datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%SZ")
        
        # Convert to your timezone if needed (e.g., IST)
        # from pytz import timezone, utc
        # dt = utc.localize(dt).astimezone(timezone("Asia/Kolkata"))
        
        return dt.strftime("%d-%b-%Y %H:%M:%S")
    except Exception as e:
        return f"Invalid timestamp: {iso_timestamp} ({e})"
