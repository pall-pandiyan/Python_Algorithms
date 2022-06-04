import profile

count = 10**5
result = []

def inFunction(a):
    if (a in result):
        return True

def main():    
    for i in range(count):
        result.append(i)

    for i in range(0,count,2):
        if( inFunction(i) ):
            continue


profile.run('main()')



# the output will be...

# Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.250    0.250   57.814   57.814 004_in.py:10(main)
#     50000   57.471    0.001   57.471    0.001 004_in.py:6(inFunction)
#    100000    0.094    0.000    0.094    0.000 :0(append)
#         1    0.000    0.000   57.814   57.814 :0(exec)
#         1    0.016    0.016    0.016    0.016 :0(setprofile)
#         1    0.000    0.000   57.814   57.814 <string>:1(<module>)
#         1    0.000    0.000   57.830   57.830 profile:0(main())
#         0    0.000             0.000          profile:0(profiler)