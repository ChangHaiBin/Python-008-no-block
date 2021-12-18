import datetime

numbers1 = [x for x in range(1,10000000)]
print(f"Process 1 starts: {datetime.datetime.utcnow()}")

for i in range(9999900, 9999999):
    if i in numbers1:
        print(i)

print(f"Process 1 ends: {datetime.datetime.utcnow()}")
print("====================")



print(f"Process 2 starts: {datetime.datetime.utcnow()}")

numbers2 = set(range(1,10000000))
for i in range(9999900, 9999999):
    if i in numbers2:
        print(i)

print(f"Process 2 ends: {datetime.datetime.utcnow()}")