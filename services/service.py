from datetime import datetime, timedelta


def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return str(datetime.strptime(date_str, date_format).date())


def get_time(time_period,start_date):
    start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
    if time_period == 'day':
        end_date = start_date+ timedelta(days=1)
    elif time_period == 'week':
        end_date = start_date + timedelta(weeks=1)
    elif time_period == 'month':
        end_date = start_date + timedelta(days=30)
    else:
        raise ValueError("Invalid time period. Must be 'day', 'week', or 'month'.")

    return  start_date,end_date