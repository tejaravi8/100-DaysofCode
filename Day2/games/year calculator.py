Days=372
years=Days//365
remaing_days=Days-years*365
weeks=remaing_days//7
remaing_days=remaing_days-weeks*7
day=remaing_days

print(f"{Days} are divided into {years}year(s) and {weeks}week(s) and {day} days")
