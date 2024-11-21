from datetime import datetime, timezone

filename_date=datetime.now(timezone.utc)
print (filename_date)
filename_date=datetime.now(timezone.utc).strftime("%Y-%m-%d")
print (filename_date)