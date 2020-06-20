print("Poco a poco")

x = input("numerito:")
x = float(x)
if x < 2:
    print ('small')
elif x < 10:
    print ('meduim')
else:
    print('large')
print('all done')

rawstr = input ('enter a number:')
try:
    ival = int (rawstr)
except:
    ival = -1

if ival > 0:
    print ('nice number')
else:
    print ('nice try, is a word')
        
