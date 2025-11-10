thonfrom datetime import datetime

def convert_time_format(time_string: str):
    """Convert time to a specific format"""
    try:
        time_object = datetime.strptime(time_string, "%b %d, %Y")
        return time_object.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return time_string  # Return the original string if parsing fails