from datetime import datetime


class Person:
    def __init__(self, fname, lname, b_day, b_month, b_year):
        self.first_name = fname
        self.last_name = lname
        self.birthday = datetime(b_year, b_month, b_day)

    def age_info(self):
        today = datetime.today()
        this_year_birthday = datetime(today.year, self.birthday.month, self.birthday.day)
        if this_year_birthday < today:
            self.age = today.year - self.birthday.year
        else:
            self.age = today.year - self.birthday.year - 1
        return self.age


class Worker(Person):
    def __init__(self, fname, lname, b_day, b_month, b_year, dep, role, day, month, year):
        self.first_name = fname
        self.last_name = lname
        self.department = dep
        self.role = role
        self.birthday = datetime(b_year, b_month, b_day)
        self.first_day = datetime(year, month, day)

    def experience_info(self):
        today = datetime.today()
        this_year_first_day = datetime(today.year, self.first_day.month, self.first_day.day)
        if this_year_first_day < today:
            self.experience = today.year - self.first_day.year
        else:
            self.experience = today.year - self.first_day.year - 1
        return self.experience

    # working day
    def set_monthly_wday(self, wday):
        self.monthly_wday = int(wday)

    # hospital's day
    def set_monthly_hday(self, hday):
        self.monthly_hday = int(hday)

    # hourly wage
    def set_hourly_wage(self, wage):
        self.hourly_wage = float(wage)

    def salary_info(self):
        self.salary = 0
        if self.monthly_wday <= 22:
            self.salary = 8 * self.monthly_wday * self.hourly_wage + 8 * self.monthly_hday * 0.75 * self.hourly_wage
        else:
            self.salary = 8 * 22 * self.hourly_wage + 8 * self.monthly_hday * 0.75 * self.hourly_wage
            self.salary += 8 * (self.monthly_wday - 22) * 1.5 * self.hourly_wage
        # premium
        if self.experience_info() > 5:
            self.premium = 0.1 * self.salary
        elif self.experience_info() > 3:
            self.premium = 0.05 * self.salary
        else:
            self.premium = 0
        # final salary
        self.salary += self.premium
        return self.salary


class Role:
    def __init__(self, dep, role, wage):
        self.dep = dep
        self.role = role
        self.wage = float(wage)