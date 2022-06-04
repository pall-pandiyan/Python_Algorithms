from datetime import datetime as dt

startTime = dt.now()
count = 10**5
result = []
for i in range(count):
    result.append(i)
result.reverse()
print("time for append() and reverse() is:", (dt.now()-startTime))

startTime = dt.now()
for i in range(count):
    result.insert(0,i)
print("time for insert() is:", (dt.now()-startTime))


# the output will be...

# time for append() and reverse() is: 0:00:00.018001
# time for insert() is: 0:00:13.697131