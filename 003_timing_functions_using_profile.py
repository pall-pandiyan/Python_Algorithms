import profile

def appendAndReverse():
    count = 10**5
    result = []
    for i in range(count):
        result.append(i)
    result.reverse()

def onlyInsert():
    count = 10**5
    result = []
    for i in range(count):
        result.insert(0,i)

profile.run("appendAndReverse()")
profile.run("onlyInsert()")

# the output will be...
#
#        100006 function calls in 0.250 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.094    0.094    0.234    0.234 003_profile.py:3(appendAndReverse)
#    100000    0.140    0.000    0.140    0.000 :0(append)
#         1    0.000    0.000    0.234    0.234 :0(exec)
#         1    0.000    0.000    0.000    0.000 :0(reverse)
#         1    0.016    0.016    0.016    0.016 :0(setprofile)
#         1    0.000    0.000    0.234    0.234 <string>:1(<module>)
#         1    0.000    0.000    0.250    0.250 profile:0(appendAndReverse())
#         0    0.000             0.000          profile:0(profiler)


#          100005 function calls in 4.524 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.094    0.094    4.524    4.524 003_profile.py:10(onlyInsert)
#         1    0.000    0.000    4.524    4.524 :0(exec)
#    100000    4.430    0.000    4.430    0.000 :0(insert)
#         1    0.000    0.000    0.000    0.000 :0(setprofile)
#         1    0.000    0.000    4.524    4.524 <string>:1(<module>)
#         1    0.000    0.000    4.524    4.524 profile:0(onlyInsert())
#         0    0.000             0.000          profile:0(profiler)