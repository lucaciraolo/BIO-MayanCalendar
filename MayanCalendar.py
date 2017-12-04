
class MayanDate:
    def __init__(self, dateString):
        split = dateString.split(' ')
        integers = map(lambda x: int(x), split)
        self.baktuns, self.katuns, self.tuns, self.uinals, self.kins = integers

    def days_since_origin(self):
        mayan_origin = MayanDate('13 20 7 16 3')
        # baktun_diff = self.baktuns - mayan_origin.baktuns
        # katun_diff = self.katuns - mayan_origin.katuns
        # tun_diff = self.tuns - mayan_origin.tuns
        # uinal_diff = self.uinals - mayan_origin.uinals
        # kin_diff = self.kins - mayan_origin.kins
        #
        # days_diff = (baktun_diff * 20) + (katun_diff * 20) + (tun_diff * 20) + (uinal_diff * 18) + kin_diff

        while mayan_origin != self:
            myan_origin.add(1)


        return days_diff

    def __cmp__(self, other):
        return self.baktuns == other.baktuns and self.katuns == other.katuns and self.tuns == other.tuns and \
               self.uinals == other.uinals and self.kins == other.kins

    def __str__(self):
        return '{} {} {} {} {}'.format(self.baktuns, self.katuns, self.tuns, self.uinals, self.kins)

    def english(self):
        english_date = EnglishDate(1, 1, 2000)
        days_to_add = self.days_since_origin()
        english_date.add_days(days_to_add)
        return english_date


class EnglishDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def days_in_month(self, month, year):
        options = {
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

        if year % 4 == 0:
            options[2] = 29
        else:
            options[2] = 28

        return options[month]



    def add_days(self, days):
        while days > 0:
            self.day += 1
            days -= 1
            if self.day > self.days_in_month(self.month, self.year):
                self.month += 1
                self.day = 1

            if self.month > 12:
                self.year += 1
                self.month = 1





    def __str__(self):
        return '{} {} {}'.format(self.day, self.month, self.year)



if __name__ == "__main__":
    input = '13 20 9 2 9'
    mayan_date = MayanDate(input)
    print(mayan_date.english())

