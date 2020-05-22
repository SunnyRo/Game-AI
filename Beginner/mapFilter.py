import math
import statistics


def areaCal(r):
    return math.pi * (r ** 2)


radii = [2, 5, 7.1, 0.3, 10]
# method 2 using map
newList = list(map(areaCal, radii))
print(newList)
temps = [
    ("berlin", 29),
    ("cairo", 36),
    ("buenos aires", 19),
    ("london angeles", 26),
    ("tokyo", 27),
]

c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)
toCelcius = list(map(c_to_f, temps))
print(toCelcius)
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)

newList1 = list(filter(lambda x: x > avg, data))
print(newList1)
countries = ["", "argentina", "", "brazil", "chile", "", "Colombia"]
print(list(filter(None, countries)))
