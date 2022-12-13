def timeConversion(s):
    # Write your code here
    from datetime import datetime 
    time_24h = datetime.strptime(s, "%I:%M:%S%p")
    time_24h_str =time_24h.strftime("%H:%M:%S")
    return time_24h_str