from datetime import datetime

def today():
    today = datetime.now()
    return today

def verify_date(date):
    date_format = datetime.strptime(date, "%d-%m-%Y")
    return date_format

def verify_due(date_ref):
    due_date = verify_date(date=date_ref)
    if today() > date_ref:
        return True
    else:
        return False

