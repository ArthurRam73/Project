import datetime

def date_in_range(start, end, userdate):
    """Returns whether userdate is in the range [start, end]"""
    return start <= userdate <= end
    if start <= end:
        return start <= userdate <= end
    else:
        return start <= x or x <= end



start = datetime(1, 1, 2010)
end = datetime(1, 1, 2018)
userdate = datetime()

print(date_in_range(start, end, userdate))
