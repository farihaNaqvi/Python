# time_interval in python
#how time interval works in python
import time
n=10
def test(i,n):
    k=' '
    print('* '*i,k*(n-(i+i)),'* '*i)
for i in range(n):
    test(i,n)
    time.sleep(1)
for i in range(n,0,-1):
    test(i,n)
    time.sleep(1)
