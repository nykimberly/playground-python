import datetime
import pytz


def get_friendly_time(datetime_obj):
    """Given a datetime object, return a time formatted like 6:00 AM.
    >>> from datetime import datetime as dt
    >>> three_pm = dt(day=20, month=9, year=2000, hour=15)
    >>> get_friendly_time(three_pm)
    '3:00 PM'
    >>> ten_pm = dt(day=20, month=9, year=2000, hour=22)
    >>> get_friendly_time(ten_pm)
    '10:00 PM'
    >>> one_am = dt(day=20, month=9, year=2000, hour=1, minute=37)
    >>> get_friendly_time(one_am)
    '1:37 AM'
    """
    h = datetime_obj.hour
    m = datetime_obj.minute
    meridiem = "AM"
    if h > 12:
        h -= 12
        meridiem = "PM"
    if m < 10:
        m = "0" + str(m)
    friendly_time = str(h) + ":" + str(m) + " " + meridiem
    return friendly_time

def is_after(date1, date2):
    """Given two strings like MM-DD-YYYY, return True if date1 is after date2.
    >>> is_after('03-03-2018', '04-04-2018')
    False
    >>> is_after('05-05-2018', '04-04-2018')
    True
    """
    d1 = datetime.datetime.strptime(date1, "%m-%d-%Y")
    d2 = datetime.datetime.strptime(date2, "%m-%d-%Y")
    return d1 > d2

def get_verbose_format(iso_date):
    """Given a string like 2018-10-01, return October 1, 2018.
    >>> get_verbose_format('2018-10-01')
    'October 1, 2018'
    >>> get_verbose_format('2000-01-11')
    'January 11, 2000'
    """
    d = datetime.datetime.strptime(iso_date, '%Y-%m-%d')
    return d.strftime('%B %-d, %Y')

def get_two_days_later(iso_date):
    """Given a string, return an ISO-formatted string that's 2 days later.
    >>> get_two_days_later('2018-08-02')
    '2018-08-04'
    >>> get_two_days_later('2017-12-31')
    '2018-01-02'
    >>> get_two_days_later('2017-12-31')
    '2018-01-02'
    """
    d = datetime.datetime.strptime(iso_date, '%Y-%m-%d')
    later_d = d + datetime.timedelta(days=2)
    return later_d.strftime('%Y-%m-%d')

def get_next_four_hours(datetime_obj):
    """Given a datetime object, return a list of +1, +2, +3, and +4 hours.
    >>> from datetime import datetime
    >>> valentines = datetime(hour=21, year=2018, month=2, day=14)
    >>> my_hours = get_next_four_hours(valentines)
    >>> my_hours[0].hour
    22
    >>> my_hours[1].hour
    23
    >>> my_hours[2].hour
    0
    >>> my_hours[3].hour
    1
    """
    dt_4h = []
    for i in range(1, 5):
        dt_4h.append(datetime_obj + datetime.timedelta(hours=i))
    return dt_4h

def round_to_hour(time_obj):
    """Given a time object, round to the nearest hour.
    >>> from datetime import time
    >>> nine_oh_three = time(minute=3, hour=9)
    >>> three_thirty_one = time(minute=31, hour=3)
    >>> result = round_to_hour(nine_oh_three)
    >>> result.hour
    9
    >>> result.minute
    0
    >>> result = round_to_hour(three_thirty_one)
    >>> result.hour
    4
    >>> result.minute
    0
    """
    h = time_obj.hour
    m = time_obj.minute
    if m > 30:
        h += 1
    m = 0
    return datetime.time(h, m)

def get_nearest_monday(datetime_obj):
    """Given a datetime object, return the nearest Monday (same time).
    >>> from datetime import datetime as dt
    >>> get_nearest_monday(dt(day=29, month=9, year=2018, hour=1))
    datetime.datetime(2018, 10, 1, 1, 0)
    >>> get_nearest_monday(dt(day=27, month=9, year=2018, hour=1))
    datetime.datetime(2018, 9, 24, 1, 0)
    >>> get_nearest_monday(dt(day=23, month=9, year=2018, hour=1))
    datetime.datetime(2018, 9, 24, 1, 0)
    """
    wd = datetime_obj.weekday()
    # 0 1 2 3 4 5 6 0
    # m t w t f s s
    # x 1 2 3 3 2 1 x
    if wd < 4:
        nearest_mon = datetime_obj - datetime.timedelta(days=wd)
    else:
        nearest_mon = datetime_obj + datetime.timedelta(days=(7-wd))
    return nearest_mon

def convert_to_pst(datetime_obj):
    """Given a timezone-aware datetime obj convert it to PST.
    >>> import pytz
    >>> from datetime import datetime as dt
    >>> eastern = pytz.timezone('US/Eastern')
    >>> tmrw = dt(day=23, month=9, year=2018, hour=13)
    >>> tmrw_eastern = eastern.localize(tmrw)
    >>> result = convert_to_pst(tmrw_eastern)
    >>> result.hour
    10
    """
    return datetime_obj.astimezone(pytz.timezone('US/Pacific'))

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print('ALL TESTS PASSED. HOPE YOU HAD A GOOD "TIME"')


