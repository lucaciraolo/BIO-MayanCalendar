target_baktuns = 13
target_katuns = 20
target_tuns = 9
target_uinals = 2
target_kins = 9

baktuns = 13
katuns = 20
tuns = 7
uinals = 16
kins = 3

year = 2000
month = 1
day = 1

days_in_month = {
        1: 31,
        # feb later
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 9,
        10: 31,
        11: 30,
        12: 31
    }

while not (target_baktuns != baktuns and target_katuns != katuns and target_tuns != tuns and target_uinals != uinals and target_kins != katuns):

    kins += 1
    day += 1

    if kins > 20:
        uinals += 1
        kins = 1
    if uinals > 18:
        tuns += 1
        uinals = 1
    if tuns > 20:
        katuns += 1
        tuns = 1
    if katuns > 20:
        baktuns += 1
        katuns = 1



    if year % 4 == 0:
        days_in_month[2] = 29
    else:
        days_in_month[2] = 28

    max_days = days_in_month[month]

    if day > max_days:
        month += 1
        day = 1
    if month > 12:
        year += 1
        month = 1

print('{} {} {}'.format(day, month, year))