import statistics as s
import numpy as np

year_1 = [77,54.2,81.7,69.6,80,89.3,72.7,53.8]
year_2 = [73, 78.2, 81.9, 87.5, 40, 75,78.6,77.9]
year_3 = [90.3, 76.7,79.3,81.5,75,92.6,78.2,75.9]
year_4 = np.ones(8)*57
year_weights = [6.25, 18.75,37.5,37.5]

grades = [year_1, year_2, year_3, year_4]
i = 1
for year in grades:
    print("avg for year:" +str(i)+ " is: " + str(s.mean(year)))
    i+=1
net_grade = 0
for i in range(0,4):
    net_grade +=(s.mean(grades[i]))*(year_weights[i]/100)
print(net_grade)

if net_grade >=70:
    print("First class!!!")
elif net_grade >=60 and net_grade<=69.9:
    print("second class")
elif net_grade>=50 and net_grade<=59.9:
    print("second class lower")
elif net_grade >=40 and net_grade<=49.9:
    print("third class")
else:
    print("class not found")


