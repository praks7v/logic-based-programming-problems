def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


if __name__ == "__mian__":
    year_input = 2024
    if is_leap_year(year_input):
        print(f"{year_input} is the leap year.")
    else:
        print(f"{year_input} is not a leap year.")
