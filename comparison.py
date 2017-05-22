from time import time
import gc
gc.disable()
upper_bound = 50000000
runs = 30


timer = time()
from purepython_loop import test as python_test
print "Python import:" + str(time() - timer)
sum = 0.0
result_python = 0
for i in range(1, runs+1):
    timer = time()
    result_python += python_test(upper_bound)
    runtime = time() - timer
    sum += runtime
    print "{0}th python run took {1}".format(i, runtime)
print('-'*15)
print "python run took {0} average".format(sum / runs)

print('\n\n\n')

timer = time()
import pyximport
pyximport.install(inplace=True)
from cython_loop import test as cython_test
print "CPython import:" + str(time() - timer)
sum = 0.0
result_cython = 0
for i in range(1, runs+1):
    timer = time()
    result_cython += cython_test(upper_bound)
    runtime = time() - timer
    sum += runtime
    print "{0}th cpython run took {1}".format(i, runtime)
print('-'*15)
print "cpython run took {0} average".format(sum / runs)

print("Same result: {0}".format(result_cython==result_python))