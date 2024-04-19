from factory import Factory
from reports import Reports


x = Factory("Lego_ua")
new_report = Reports(x)
new_report.make_report()
