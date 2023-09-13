from datetime import datetime

date_dict = {
    "date1": "2023-09-03",
    "date2": "2023-09-11",
    "date3": "2023-09-17",
    "date4": "2023-09-23",
}

def is_sunday(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.weekday() == 6

sundays = []

for key, date_str in date_dict.items():
    if is_sunday(date_str):
        sundays.append(f"{key}: {date_str}")
        
if sundays:
    print("List of Sundays:")
    for sunday in sundays:
        print(sunday)
else:
    print("No Sundays found in the given dates.")