# import os 
# import sys 
# import datetime
# from datetime import date 
# import calendar 
# from math import pi 
# """ print("Hello World")
# ### https://www.w3resource.com/python-exercises/python-basic-exercises.php 
# ###ex 1
# print("""Twinkle, twinkle, little star,
#          How I wonder what you are!
#                  Up above the world so high,
#                  Like a diamond in the sky.
# Twinkle, twinkle, little star,
#          How I wonder what you are
#              """)
# ### ex 2
# # print(sys.version """)
# print(sys.version_info)
# ### ex 3
# now = (datetime.datetime.now())
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# ### ex 4
# r = float(input ("Cual es el radio?"))
# print("El area del circulo es: " , (pi * (r**2)))
# ### ex5 
# name = (input("First name"))
# last = (input("Last name"))
# print("Last: ",  last , "First: ", name)
### ex 6
# csv = (input("enter a few numbers:"))
# list = csv.split(",")
# tuple = tuple(csv)
# print('list: ', list)
# print('tuple: ', tuple)
### ex 7
# file = input('file with extension: ')
# ext = file.split(".")
# print(ext[-1])
## ex 8
# colors = ["red", "green", "white", "black"]
# print("%s %s"%(colors[0],colors[-1]))
### ex 9
# exam = (11, 12, 2014)
# print(" %i / %i / %i" %exam)
## ex 10
# num = (input("un numerito: "))
# num = int(num)
# print("numero x + xx + xxx =", (num + (num**2) + (num**3)))
# print('numero x + xx + xxx asi no mas:', num + ((num)+(num)) + ((num)+(num)+(num)))
# n1 = int( "%s" % num )
# n2 = int( "%s%s" % (num,num) )
# n3 = int( "%s%s%s" % (num, num, num) )
# print(n1+n2+n3)
## ex 11
## ex 12
# print(calendar.month(2020, 5))
# mes = int(input("Mes (en numero): "))
# year = int(input("Año: "))
# print(calendar.month(year, mes))
### ex 13
### ex 14
# print("Enter the first date, like year, month, day:")
# year1 = int(input("Year: "))
# month1 = int(input("Month: "))
# day1 = int(input("Day: "))
# print("Now enter the second set, year, month, day: ")
# year2 = int(input("Year 2: "))
# month2 = int(input("Month 2: "))
# day2 = int(input('day 2'))
# f_date = date(year1, month1, day1)
# l_date = date(year2, month2, day2)
# delta = l_date - f_date
# print(delta.days)
## ex 15
# radius = int(input("Radio de la esfera: "))
# volumen_esfera = 4/3 * pi * radius**3
# print(volumen_esfera)
## 16
# n = 17
# n1 = int(input("numero"))
# if n1 > n:
#     result = ((n1-n) * 2)
#     print(result)
# else:
#     result = ((n - n1))
#     print(result)
## ex 17
# num = int(input("Numerito: "))
# tho = 1000
# twotho = 2000
# deltatho = (tho - num)
# deltatwo = (twotho - num)
# if (deltatho < 100) or (deltatwo  < 100):
#     print("delta is less than 100")
# else:
#     print('we are good')
## ex 19
# line = str(input('enter some text: '))
# if line[:2] == "Is":
#     print(line)
# else:
#     newline = ('Is' + line ) 
#     print(newline)
## ex 20
# word = str(input('Enter a word: '))
# times = int(input('How many times you want to iterate it: '))
# print(word * times)
## ex21
# number = int(input('Number please: '))
# mod = number % 2
# if mod == 0:
#     print('number is even')
# else:
#     print('number is odd')
##ex 22
# cuatros = 0
# lista = input("enter a list of numbers, including 4: ")
# print(lista)
# for x in lista:
#     if x == '4':
#         cuatros = cuatros + 1
# print ('Cuatros: ', cuatros)
## ex 23
# word = str(input('Enter any word :'))
# copia = int(input('cuantas copias de los 2 primeros char :'))
# if word[:2] != " ":
#     f2 = (word[:2])
#     print(f2 * copia)
## ex 24
# word = str(input('Enter any letter :'))
# voc = ("a","e","i","o","u")
# if word in voc:
#     print('vocal')
# else:
#     print('consonante')
### ex 25
# one = (input("Enter a single digit: "))
# data = (input("Enter a list of digits: "))
# if one in data:
#     print("your digit is part of the list")
# else:
#     print("digit is not part of it")
## ex 26
# cha = (input("character to print: "))
# lista = (input("enter una lista de 4 numeros: "))
# for x in lista:
#     print(cha*int(x))
## ex 27
## ex 28
# number = int(input('Number please: '))
# even = []
# odd = []
# lista = (input('lista de numeros'))
# print('The list has ', len(lista), 'elements')
# for number in lista:
#     number = int(number)
#     mod = number % 2
#     if mod == 0:
#         even.append(number)
#         print(number, ' is even ')
#     else:
#         odd.append(number)
#         print(number, ' is odd')
# print('the list has a total of: ', len(lista), 'elements')
# print('of which, ' , len(even), ('elements) are even: ', even))
# print('and a total of:', ((len(lista)) - (len(even))) , 'are odd elements', odd)
## ex 29
# num = input('enter some numbers')
# print(num)
# b = sorted(num)
# print(b)
# a = ['aaa', 'bb', 'cccc', 'd']
# # sort by length
# a = {}
# a = {'a':1,'b':2}
# print (a) 
# print (a.keys())
# print (a.values())
# print (a.items())
# for x in a.items():
#     print(x)
# os.chdir("/Users/joaquin/scr/")
# f = open('generic.txt', 'r')
# for line in f:
#     print(line, end='')
# f.close()
## ex 30
# cat1 = input('cateto 1')
# cat2 = input('cateto 2')
# area = ((int(cat1) * int(cat2))/2)
# print(area)
## ex 31
# n1 = [3]
# n2 = [3]
# num1 = input('primer numero')
# num2 = input('segundo numero')
# num1 = int(num1)
# num2 = int(num2)
# while n1[-1] != 2: 
#     mod12 = (num1 % 2)
#     if mod12 == 0:
#         num12 = (num1 / 2)
#         n1.append(num12)
#         num1 = num12
#     else:
#         print()
#         break
# while n2[-1] != 2:
#     mod22 = (num2 % 2)
#     if mod22 == 0:
#         num22 = (num2 / 2)
#         n2.append(num22)
#         num2 = num22    
#     else:
#         print()
#         break
# print('n1 divisors: ', n1[1:]) 
# print('n2 divisors: ', n2[1:])
# ######
# d1 = n1[1:]
# d2 = n2[1:]
# x = d1[0]
# for x in d1:
#     if x in d2:
#         print('gcd is:' , x)
#         break
#     else:
#         print()
## 32
## ex 33
# v1 = input(('value 1'))
# v2 = input(('value 2'))
# v3 = input(('value 3'))
# v1 = int(v1)
# v2 = int(v2)
# v3 = int(v3)
# if v1 == v2 or v1 == v3 or v2 == v3:
#     print('two values are the same')
# else:
#     sum = (v1 + v2 + v3)
#     print('the sum of ', v1, v2, v3, 'is', sum)
# ## ex 33 list
# lis = []
# lista = []
# lista = lis.append(v1)
# print(lis)
# lista = lis.append(v2)
# print(lis)
# lista = lis.append(v3)
# print(lis)
## ex 34
# v1 = input(('value 1'))
# v2 = input(('value 2'))
# v1 = int(v1)
# v2 = int(v2)
# if ((v1 + v2) <=  20) and ((v1 + v2) >= 15):
#     print('20')
# else:
#     print(v1 + v2)
## ex 35
# v1 = input(('value 1'))
# v2 = input(('value 2'))
# v1 = int(v1)
# v2 = int(v2)
# if v1 == v2 or (v1 - v2) == 5 or (v2 - v1) == 5 or (v1 + v2) == 5:
#     cond = True
# else:
#     cond = False
# print(cond)
## ex 36
# v1 = input(('value 1'))
# v2 = input(('value 2'))
# v1 = int(v1)
# v2 = int(v2)
# if isinstance (v1, int) and isinstance(v2, int):
#     print('sum is', (v1 + v2))
# else:
#     print('values are not integer')
## ex 37
# def personal_details():
#     name, age = (input('name')), (input('age'))
#     address = ' Leesburg '
#     print('Name: {}\nAge: {}\nAddress: {}'.format(name, age, address))
# personal_details()
## ex 38
# x = 4
# y = 3
# print('(4+3)**2: ', ((x+y)**2))
## ex 39
# cap = input('capital')
# rate = input('interest')
# time = input('years')
# cap = int(cap)
# rate = float(rate)
# time = float(time)
# print('total: ', (cap * (1 + ((rate/100)*time))))
## ex 40
# import math 
# x1 = float(input('x1 is: '))
# y1 = float(input('enter y1:'))
# x2 = float(input('now enter x2'))
# y2 = float(input('finally, y2'))
# c1 = (x2 - x1)
# c2 = (y2 - y1)
# print('Distance is: ', (math.sqrt((c1**2)+(c2**2))))
## ex 41
# import os
# file = (input('which file you looking for?: '))
# if file in os.listdir():
#     print('the file is there')
# else:
#     print('file is not found')
## ex 42
# import sys
# print(sys.version)
# import struct
# print(struct.calcsize('P') * 8)
## ex 43
# import os
# import sys
# import platform
# print(os.system)
# print(os.name)
# print(sys.version)
# print(sys.version_info)
# print(platform.architecture)
# print(platform.system())
# print(platform.release())
# ex 44
# import site;
# print(site.getsitepackages())
# ex 45
#from subprocess import call
#call(["ls", "-l"])
#call(["more", "yamaha.txt"])
# import os
# print(os.system('ls -l'))        
# ex 46
#import os
#print("Current File Name: ", os.path.realpath(__file__))
## ex 47
# import multiprocessing
# print('This system has ', multiprocessing.cpu_count(), " CPUs")
# ex 48
# n = float(input('enter a decimal'))
# print(float(n))
# print(int(float(n)))
# ex 49
# import os
# loc = input('Enter the path you need: ')
# print('The files on that path are: ', os.listdir(loc))
# ex 50
# star = range(0,9)
# for i in star:
#     print('x', end='')
# ex 51
# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')
# ex 52
# ex 53
# import os
# print(os.environ)
# print(os.environ['HOME'])
# ex 54
# import os
# print(os.uname())
# ex 55
# import os
# print(os.system('ifconfig -a | grep netmask'))
# import socket
# print(socket.gethostbyname(socket.gethostname()))
# ex 56
# import shutil
# wh = shutil.get_terminal_size()
# print('terminal size is %d x %d' %wh)
## ex 57
## ex 58
# sum = 0
# n = int(input('end number'))
# lis = range(0, n+1)
# for x in lis:
#     sum = sum + x
# print('the sum of elements is: ', sum)
# ex 59
# ft = float(input('enter your height in feet'))
# inc = float(input('how many inches above that?'))
# print('Your height in centimeters is ', ( (ft * 30.48) + (inc * 2.54)))
## ex 68
# sum = 0
# n = (input('enter a number with multiple digits'))
# for x in n:
#     sum = sum + int(x)
# print('The addition of all digits in your number is ', sum)
# ex 69
# n1 = int(input('Enter integer 1'))
# n2 = int(input('Enter integer 2'))
# n3 = int(input('Enter integer 3'))
# list = []
# list.append(n1)
# list.append(n2)
# list.append(n3)
# print('The original lists, as entered by user is: ', list)
# print('That list, now sorted, is :', sorted(list))
## ex 70
#import os
#print(os.system("ls -lt"))
# ex 72
#import math
#math_ls = dir(math)
#print(math_ls)
#help(math)
#ex 74
# word = str(input('Enter any word'))
# import hashlib 
# word = (word.encode('utf-8'))
# print(hashlib.sha256(word).hexdigest())
# ex 78
#help('modules')
# ex 79
byte = (0)
word = (input('Enter any word'))
for x in word:
    x = int(x)
    byte += x
print(byte)