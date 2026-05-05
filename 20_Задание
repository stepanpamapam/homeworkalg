time_pool = 0
finish_time = 0

participants = [
    ("a", 10, 50, 20),
    ("b", 5, 10, 5),
    ("c", 15, 30, 10)
]

participants.sort(key=lambda x: x[2] + x[3], reverse=True)

print("Оптимальный порядок:")

for name, swim, bike, run in participants:
    print(name)

for name, swim, bike, run in participants:
    time_pool = time_pool + swim
    finish = time_pool + bike + run
    finish_time = max(finish_time, finish)

print("Время окончания соревнования:", finish_time)
