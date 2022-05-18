import cProfile

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

cProfile.run("appendAndReverse()")
cProfile.run("onlyInsert()")


# the output will be...

#         100005 function calls in 0.035 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.022    0.022    0.034    0.034 002_cProfile.py:3(appendAndReverse)
#         1    0.002    0.002    0.035    0.035 <string>:1(<module>)
#         1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
#    100000    0.011    0.000    0.011    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}


#          100004 function calls in 4.885 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.060    0.060    4.883    4.883 002_cProfile.py:10(onlyInsert)
#         1    0.001    0.001    4.885    4.885 <string>:1(<module>)
#         1    0.000    0.000    4.885    4.885 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    100000    4.824    0.000    4.824    0.000 {method 'insert' of 'list' objects}