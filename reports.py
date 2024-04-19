import matplotlib.pyplot as plt
from factory import Factory


class Reports:
    reported_factory: Factory
    dep = "total"

    def __init__(self, fac: Factory):
        self.reported_factory = fac

    def update_factory_info(self):
        self.reported_factory.get_monthly_salary()

    def choose_dep(self):
        dep_list = ["total"]
        for i in range(0, len(self.reported_factory.roles_list)):
            if not (self.reported_factory.roles_list[i].dep in dep_list):
                dep_list.append(self.reported_factory.roles_list[i].dep)
        print("Which department do you want to receive additional information about?")
        key = True
        while key:
            for i in range(0, len(dep_list)):
                print(f"{i} - {dep_list[i]}")
            print("Your choice (put the number): ")
            i = int(input())
            if i in list(range(0, len(dep_list))):
                self.dep = dep_list[i]
                key = False

    def sort_by_age(self):
        for i in range(0, self.reported_factory.workers_count):
            self.reported_factory.workers_list[i].age_info()
        if self.dep == "total":
            sorted_list = sorted(self.reported_factory.workers_list, key=lambda worker: worker.age)
        else:
            sorted_list = []
            for i in range(0, self.reported_factory.workers_count):
                if self.reported_factory.workers_list[i].department == self.dep:
                    sorted_list.append(self.reported_factory.workers_list[i])
            sorted_list = sorted(sorted_list, key=lambda worker: worker.age)
        plt.title(f"{self.reported_factory.name} information about AGE of workers in {self.dep} department")
        worker_age = []
        worker_name = []
        for i in range(0, len(sorted_list)):
            worker_name.append(sorted_list[i].last_name)
            worker_age.append(int(sorted_list[i].age))
        plt.xlabel('Workers', color='gray')
        plt.ylabel('Years', color='gray')
        plt.grid(True)
        plt.bar(worker_name, worker_age)
        for w, a in zip(worker_name, worker_age):
            plt.text(w, a + 0.2, a)
        ax = plt.subplot()
        ax.set_xticks(range(len(worker_name)))
        ax.set_xticklabels(worker_name, rotation=30)
        plt.show()

    def sort_by_experience(self):
        for i in range(0, self.reported_factory.workers_count):
            self.reported_factory.workers_list[i].experience_info()
        if self.dep == "total":
            sorted_list = sorted(self.reported_factory.workers_list, key=lambda worker: worker.experience)
        else:
            sorted_list = []
            for i in range(0, self.reported_factory.workers_count):
                if self.reported_factory.workers_list[i].department == self.dep:
                    sorted_list.append(self.reported_factory.workers_list[i])
            sorted_list = sorted(sorted_list, key=lambda worker: worker.experience)
        plt.title(f"{self.reported_factory.name} information about EXPERIENCE of workers in {self.dep} department")
        worker_experience = []
        worker_name = []
        for i in range(0, len(sorted_list)):
            worker_name.append(sorted_list[i].last_name)
            worker_experience.append(int(sorted_list[i].experience))
        plt.xlabel('Workers', color='gray')
        plt.ylabel('Years', color='gray')
        plt.grid(True)
        plt.bar(worker_name, worker_experience)
        for w, a in zip(worker_name, worker_experience):
            plt.text(w, a + 0.2, a)
        ax = plt.subplot()
        ax.set_xticks(range(len(worker_name)))
        ax.set_xticklabels(worker_name, rotation=30)
        plt.show()

    def sort_by_salary(self):
        for i in range(0, self.reported_factory.workers_count):
            self.reported_factory.workers_list[i].salary_info()
        if self.dep == "total":
            sorted_list = sorted(self.reported_factory.workers_list, key=lambda worker: worker.salary)
        else:
            sorted_list = []
            for i in range(0, self.reported_factory.workers_count):
                if self.reported_factory.workers_list[i].department == self.dep:
                    sorted_list.append(self.reported_factory.workers_list[i])
            sorted_list = sorted(sorted_list, key=lambda worker: worker.salary)
        plt.title(f"{self.reported_factory.name} information about SALARY of workers in {self.dep} department")
        worker_salary = []
        worker_name = []
        for i in range(0, len(sorted_list)):
            worker_name.append(sorted_list[i].last_name)
            worker_salary.append(int(sorted_list[i].salary))
        plt.xlabel('Workers', color='gray')
        plt.ylabel('Salary', color='gray')
        plt.grid(True)
        plt.bar(worker_name, worker_salary)
        for w, a in zip(worker_name, worker_salary):
            plt.text(w, a + 0.2, a)
        ax = plt.subplot()
        ax.set_xticks(range(len(worker_name)))
        ax.set_xticklabels(worker_name, rotation=30)
        plt.show()

    def sort_by_hardworking(self):
        for i in range(0, self.reported_factory.workers_count):
            self.reported_factory.workers_list[i].monthly_wday
        if self.dep == "total":
            sorted_list = sorted(self.reported_factory.workers_list, key=lambda worker: worker.monthly_wday)
        else:
            sorted_list = []
            for i in range(0, self.reported_factory.workers_count):
                if self.reported_factory.workers_list[i].department == self.dep:
                    sorted_list.append(self.reported_factory.workers_list[i])
            sorted_list = sorted(sorted_list, key=lambda worker: worker.monthly_wday)
        plt.title(f"{self.reported_factory.name} information about HARDWORKING of workers in {self.dep} department")
        worker_hardworking = []
        worker_name = []
        for i in range(0, len(sorted_list)):
            worker_name.append(sorted_list[i].last_name)
            worker_hardworking.append(int(sorted_list[i].monthly_wday))
        plt.xlabel('Workers', color='gray')
        plt.ylabel('Workdays', color='gray')
        plt.grid(True)
        plt.bar(worker_name, worker_hardworking)
        for w, a in zip(worker_name, worker_hardworking):
            plt.text(w, a + 0.2, a)
        ax = plt.subplot()
        ax.set_xticks(range(len(worker_name)))
        ax.set_xticklabels(worker_name, rotation=30)
        plt.show()

    def make_report(self):
        self.update_factory_info()
        self.choose_dep()
        self.sort_by_hardworking()
        self.sort_by_salary()
        self.sort_by_experience()
        self.sort_by_age()
