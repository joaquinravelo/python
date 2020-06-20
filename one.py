x = 35
if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
elif x < 20 :
    print ('big')
elif x < 40 :
    print ('large')
print "all done"

astr = 'hello bob'
try:
    istr = int(astr)
except :
    istr = -1

print('first', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('second',istr)
    
