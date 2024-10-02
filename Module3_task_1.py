from datetime import datetime, date

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(string_date):
    try:
        obj_date = string_to_date(string_date)
        today = date.today()
        return (obj_date - today).days
    except ValueError:
        return "You have entered wrong date format!"
     
print(get_days_from_today("2021-10-09"))
