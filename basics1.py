a = bin(87)
print a

print(2+2)

print('the answer is:', 2+7)

print(2+5)

import random

b= random.randint(1, 11)
print b

print ('you have rolled', random.randint(1, 6))

import time

print time.localtime()

time.sleep(5)

import time
import random

print ('Welcome to self timer')
print ()
print ('everybody stand up')
print ('stay standing until you think the time has ended')
print ('then sit down')
print ('anyone still standing when the time end loses.')
print ('the last person to sit down before the time ended will win.')

stand_time = random.randint(5, 20)

print ('stay standing for', stand_time, 'seconds.')

time.sleep(stand_time)

print('****TIME UP****')
