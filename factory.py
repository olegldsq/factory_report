from datetime import datetime
from workers import Worker, Role


class Factory:
    workers_list = list()
    workers_count = len(workers_list)

    def __init__(self, name):
        self.name = name

    def add_worker(self, fname, lname, b_day, b_month, b_year, dep, role, day, month, year):
        self.workers_list.append(Worker(fname, lname, b_day, b_month, b_year, dep, role, day, month, year))
        self.workers_count += 1

    def get_workers_list(self):
        try:
            f1 = open('workers_list.txt', 'r', encoding='utf-8')
        except:
            print("Error opening file")
        else:
            self.workers_list = list()
            self.workers_count = len(self.workers_list)
            for l in f1:
                line = l.split()
                fname, lname, b_date, dep, role, fd_date = [item for item in line]
                b_date_int = b_date.split('-')
                b_day, b_month, b_year = [int(item) for item in b_date_int]
                fd_date_int = fd_date.split('-')
                day, month, year = [int(item) for item in fd_date_int]
                self.add_worker(fname, lname, b_day, b_month, b_year, dep, role, day, month, year)
            f1.close()

    def get_workers_hourly_wage(self):
        try:
            f2 = open('roles_list.txt', 'r', encoding='utf-8')
        except:
            print("Error opening file")
        else:
            self.roles_list = []
            for l in f2:
                line = l.split(' ')
                dep, role, wage = [item for item in line]
                wage = float(wage)
                self.roles_list.append(Role(dep, role, wage))
            f2.close()
            for i in range(0, self.workers_count):
                self.workers_list[i].set_hourly_wage(0)
            for i in range(0, self.workers_count):
                for j in range(0, len(self.roles_list)):
                    if self.workers_list[i].department == self.roles_list[j].dep and self.workers_list[i].role ==\
                            self.roles_list[j].role:
                        self.workers_list[i].set_hourly_wage(self.roles_list[j].wage)

    def get_monthly_report(self):
        try:
            f3 = open('monthly_report.txt', 'r', encoding='utf-8')
        except:
            print("Error opening file")
        else:
            for i in range(0, self.workers_count):
                self.workers_list[i].set_monthly_wday(0)
                self.workers_list[i].set_monthly_hday(0)
            for l in f3:
                line = l.split(' ')
                fname, lname, wday, hday = [item for item in line]
                for i in range(0, self.workers_count):
                    if self.workers_list[i].first_name == fname and self.workers_list[i].last_name == lname:
                        self.workers_list[i].set_monthly_wday(wday)
                        self.workers_list[i].set_monthly_hday(hday)
            f3.close()

    def get_monthly_salary(self):
        today = datetime.today()
        self.get_workers_list()
        self.get_workers_hourly_wage()
        self.get_monthly_report()
        self.monthly_total_salary = 0
        f4 = open('monthly_salary.txt', 'w', encoding='utf-8')
        for i in range(0, self.workers_count):
            f4.write(f"{self.workers_list[i].first_name} {self.workers_list[i].last_name} salary:")
            f4.write(f"{format(self.workers_list[i].salary_info(), '.2f')} including premium:")
            f4.write(f"{format(self.workers_list[i].premium, '.2f')}\n")
            self.monthly_total_salary += self.workers_list[i].salary_info()
        f4.write(
            f"\n{self.name} {today.month}th month salary ({self.workers_count} workers): {self.monthly_total_salary}")
        f4.close()
        print(f"{self.name} {today.month}th month salary ({self.workers_count} workers): {self.monthly_total_salary}\n")