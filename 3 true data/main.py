def is_valid_date(_day, _month, _year):
    if _month < 1 or _month > 12:
        return False
    if _day < 1:
        return False
    if _month in [4, 6, 9, 11] and _day > 30:
        return False
    if _month == 2:
        if _year % 4 == 0 and (_year % 100 != 0 or _year % 400 == 0):
            if _day > 29:
                return False
        elif _day > 28:
            return False
    if _day > 31:
        return False
    return True


day = 31
month = 12
year = 2023
print(is_valid_date(day, month, year))


