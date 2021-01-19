
# Tran Luong Bang - bangtranluong195@gmail.com
# ADM - HW1

#---------------------------------------------------------------------------------------------------------------
# Problem 1
# A. Introduction total: 7/7

# 1. Say "Hello, World!" With Python

print("Hello, World!")

# 2. Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    elif n >= 2 and n <= 5:
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')

# 3. Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# 4. Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a/b))
    print(a/b)

# 5. Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

# 6. Write a Function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    return leap

# 7. Print Function

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end = '')
        
# B. DATA TYPES total: 6/6

# 1. List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n]
    print(result)
    
# 2. Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # using set to remove duplicated elements. 
    arr = list(set(arr))
    # sort the array
    arr = sorted(arr)
    print(arr[-2])
    
# 3. Nested Lists 

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    score = [student[1] for student in students]
    
    score = sorted(set(score))
    second_lowest_score = score[1]

    selected_students = [i for i in students if i[1] == second_lowest_score]

    selected_students = sorted(selected_students, key = lambda x : x[0])

    for i in selected_students:
        print(i[0])

# 4. Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for key, value in student_marks.items():
        if key == query_name:
            average = sum(value)/len(value)
            print(format(average, '.2f'))

# 5. Lists

if __name__ == '__main__':
    N = int(input())
    
    result = []

    while(N != 0):
        command = input()
        clist = command.split()
        method = clist[0]
        if method == 'insert':
            index = int(clist[1])
            value = int(clist[2])
            result.insert(index, value)
        if method == 'print':
            print(result)
        if method == 'remove':
            value = int(clist[1])
            result.remove(value)
        if method == 'append':
            value = int(clist[1])
            result.append(value)
        if method == 'sort':
            result.sort()
        if method == 'pop':
            result.pop()
        if method == 'reverse':
            result.reverse()
        N = N-1

# 6. Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
    
# C. STRING Total: 14/14

# 1. sWap cASE

def swap_case(s):
    return s.swapcase()
 
# 2. String Split and Join

def split_and_join(line):
    line = line.split(' ')
    line = '-'.join(line)
    return  line
 
# 3. What's Your Name

def print_full_name(a, b):
    print("Hello " + a + " " + b + '! You just delved into python.')
   
# 4. Mutations

def mutate_string(string, position, character):
    return string[:position] + character+ string[position+1:]

# 5. Finding a string 

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

# 6. String Validators

if __name__ == '__main__':
    s = input()
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))

# 7. Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# 8. Text Wrap

def wrap(string, max_width):
    i = 0
    str = ''
    while(i < len(string)):
        str = str + string[i:i+max_width] +'\n'
        i = i+max_width
    return str

# 9. Designer Door Mat

s = input()
s = s.split(' ')
n= int(s[0])
m = int(s[1])

for i in range(0,n):
    if i % 2 != 0:
        a = int((m-i*3)/2)
        print('-'*a + '.|.'*i + '-'*a)
print ('-'*int((m-7)/2) + "WELCOME" + '-'*int((m-7)/2))
for i in range(n-1,-1,-1):
    if i % 2 != 0:
      a = int((m-i*3)/2)
      print('-'*a + '.|.'*i + '-'*a)

# 10. String Formatting

def print_formatted(number):
    # your code goes here
    width = len(str(bin(number))[2:])
    for i in range(1, number+1):
        d = str(i).rjust(width)
        o = oct(i)[2:].rjust(width)
        h = hex(i)[2:].upper().rjust(width)
        b = bin(i)[2:].rjust(width)
        print(d, o, h, b)

# 11. Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
    s = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for j in range(size-1,-1,-1):
      n = size -1 
      h = ''
      k = ''
      while n >= j:
        h += s[n]
        n -= 1
      k = h + h[:-1][::-1]
      result.append('-'.join(k).center(4*(size-1)+1,'-'))
    for i in range(size-2, -1,-1):
      result.append(result[i])
    for i in result:
      print(i)
    
# 12. Capitalize!

def solve(s):
    s = [ i.capitalize() for i in s.split(' ')]
    s = ' '.join(s)
    return s

# 13. The Minion Game

def minion_game(string):
    # your code goes here
    vowels =  'UEOAI'
    s1 = 0
    s2 =0 
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            s1 += n - i
        else: s2 += n -i
    if s1 > s2:
        print('Kevin', s1)
    elif s1 == s2:
        print('Draw')
    else: print('Stuart', s2)

# 14. Merge the Tools!

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    
    for i in range(0,n, k):
        d = dict()
        s = string[i:i+k]
        m = ''
        for j in s:
            d[j] = j
        for key, value in d.items():
            print(key, end = '')
        print()

# D. SET total: 13/13

# 1. Introduction to Sets

def average(array):
    array = set(array)
    n = len(array)
    return sum(array)/n

# 2. No Idea!
nm = input()

arr = input().split(' ')
a = set(input().split(' '))
b = set(input().split(' '))
u = a.union(b)
arr = [i for i in arr if i in u]
s = sum(1 if i in a else -1 for i in arr )
print(s)

# 3. Symmetric Difference

m = int(input())
marr = set(map(int,input().split()))
n =  int(input())
narr = set(map(int,input().split()))

a = marr.difference(narr)
b = narr.difference(marr)

a = a.union(b)
a=sorted(a)

for i in a:
    print(i)

# 4. Set.add()

n = int(input())
s = set()
for i in range(0,n):
    country = input()
    s.add(country)
print(len(s))

# 5. Set .discard(), .remove(), .pop()

n = int(input())
s = set(map(int, input().split()))
m = int(input())

for i in range(0, m):
    text = input()
    if text == 'pop':
        s.pop()
    else: 
        operation, number = text.split(' ')
        number = int(number)
        if operation == 'discard':
            s.discard(number)
        if operation == 'remove':
            s.remove(number)
print(sum(s))

# 6. Set .union() Operation

n = int(input())
students_E = set(input().split(' '))
m = int(input())
students_F = set(input().split(' '))

print(len(students_E.union(students_F)))

# 7. Set .intersection() Operation

n = int(input())
students_E = set(input().split(' '))
m = int(input())
students_F = set(input().split(' '))

print(len(students_E.intersection(students_F)))

# 8. Set .difference() Operation

n = int(input())
students_E = set(input().split(' '))

m = int(input())
students_F = set(input().split(' '))

print(len(students_E.difference(students_F)))

# 9. Set .symmetric_difference() Operation

n = int(input())
students_E = set(input().split(' '))

m = int(input())
students_F = set(input().split(' '))

print(len(students_E.symmetric_difference(students_F)))

# 10. Set Mutations

n = int(input())
A = set(map(int, input().split()))

m = int(input())

for i in range(0,m):
    operation, k = input().split(' ')
    B = set(map(int, input().split()))
    if operation == 'intersection_update':
        A.intersection_update(B)
    elif operation == 'update':
        A.update(B)
    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif operation == 'difference_update':
        A.difference_update(B)

print(sum(A))

# 11. The Captain's Room

n = int(input())
m = list(map(int, input().split()))
s = set(m)

i = int((sum(s)*n - sum(m))/(n-1))
print(i)

# 12. Check Subset

n = int(input())
while(n != 0):
    k = input()
    A = set(input().split(' '))
    l = input()
    B = set(input().split(' '))
    if len(A.difference(B)) != 0:
        print(False)
    else: print(True)
    n -= 1

# 13. Check Strict Superset

A = set(input().split(' '))
n = int(input())
k = 0
for i in range(0,n):
    B = set(input().split(' '))

    if len(B.difference(A)) != 0 or len(B) >= len(A):
        k = 1
        break
if k ==0:
    print(True)
else: print(False)
  
  
# E.  COLLECTIONS total: 8/8
  
# 1. Collections.Counter()

from collections import Counter

n = int(input())

sizes = map(int,input().split())
sizes = Counter(sizes)

customers = int(input())

s = 0

for customer in range(0,customers):
    size, price = map(int, input().split())
    if size in sizes.keys() and sizes[size] != 0:
        s += price
        sizes[size] -= 1
print(s)

# 2. DefaultDict Tutorial

from collections import defaultdict
d = defaultdict(list)

n,m = map(int, input().split())

for i in range(1, n+1):
    word = input()
    d[word].append(i)

for i in range(0,m):
    word = input()
    if word not in d.keys():
        print(-1)
    else:
        print(' '.join(map(str,d[word])))

# 3. Collections.namedtuple()
  
n = int(input())
column = input().split().index('MARKS')
s = 0
for i in range(n):
    mark = float(input().split()[column])
    s += mark

print("{:.2f}".format(s/n))

# 4. Collections.OrderedDict()
  
from collections import OrderedDict
n = int(input())

ordered_dict = OrderedDict()

for i in range(n):
    item = input().split(' ')
    name = ' '.join(item[:-1])
    price = int(item[-1])
    ordered_dict[name] = int(ordered_dict.get(name,0)) + price

for name, price in ordered_dict.items():
    print(name, price)
   
# 5. Word Order

n = int(input())
dict = {}
for i in range(n):
    m = input()
    dict[m] = dict.get(m, 0) + 1

print(len(dict))
s = ''
for key, value in dict.items():
    s = s + str(value) + " "
print(s)

# 6. Collections.deque()

from collections import deque
n = int(input())
d = deque()

for i in range(n):
    text = input().split(' ')
    method = text[0]
    if len(text) != 1:
        value = text[-1]
    if method == 'append':
        d.append(value)
    elif method == 'appendleft':
        d.appendleft(value)
    elif method == 'pop':
        d.pop()
    elif method == 'popleft':
        d.popleft()
    elif method == 'clear':
        d.clear()
    elif method == 'extend':
        d.extend(value)
    elif method == 'extendleft':
        d.extendleft(value)
    elif method == 'count':
        d.count(value)
    elif method == 'remove':
        d.remove(value)
    elif method == 'reverse':
        d.reverse()
    elif method == 'rotate':
        d.rotate(value)
print(' '.join(d))

 # 7. Company Logo

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    
    frequent = Counter(s)

    y = sorted(frequent.items(), key = lambda x: (-x[1], x[0]))[:3]
   
    for item in y:
        print(item[0], item[1])
        
# 8. Piling Up!

from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    sideLength = list(map(int, input().split()))
    index = sideLength.index(min(sideLength))
    left = sideLength[:index]
    right = sideLength[index+1:]

    if left == sorted(left, reverse = True) and right == sorted(right):
        print('Yes')
    else: print('No')

# F. DATE AND TIME total: 2/2

# 1. Calendar Module

import calendar

month, day, year = map(int,input().split(' '))

stt = calendar.weekday(year, month, day)

print(calendar.day_name[stt].upper())

# 2. Time Delta

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    fm = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, fm)
    t2 = datetime.strptime(t2, fm) 
    different = (t1-t2).total_seconds()  
    return str(abs(int(different)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# G. EXCEPTIONS total 1/1

# 1. Exception

n = int(input())

for i in range(n):
    try:
        a,b = input().split(' ')
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)
        
# H. BUILT-INS total: 3/3

# 1. Zipped!

n, m = map(int, input().split(' '))
X = []
for i in range(m):
    A = map(float, input().split(' '))
    X.append(A)

Y = zip(*X)

for i in Y: 
    print(sum(i)/m)
 
# 2. Athlete Sort

#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input())

    a = sorted(arr, key = lambda x: x[k])

    for i in a:
        i = map(str, i)
        print(' '.join(i))

# 3. ginortS

s = input()
lower = []
upper = []
num_even = []
num_odd = []
for i in range(len(s)):
    if s[i].islower():
        lower.append(s[i])
    elif s[i].isupper():
        upper.append(s[i])
    elif s[i].isdigit() and int(s[i]) % 2 ==0:
        num_even.append(s[i])
    elif s[i].isdigit() and int(s[i]) % 2 !=0:
        num_odd.append(s[i])
    
sort = sorted(lower) + sorted(upper) + sorted(num_odd) + sorted(num_even)
print(''.join(sort))

# I. PYTHON FUNCTIONS total 1/1
# 1. Map and Lambda Function

cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0, 1] 
  
    for i in range(2,n):
        fib.append(sum(fib[-2:]))
  
    return fib[:n]
  
  
# K. REGEX AND PARSING CHALLENGES total: 17/17

# 1. Detect Floating Point Number

import re

pattern = '^(\+|\-)?[0-9]*\.[0-9]+$'

n = int(input())

for i in range(n):
    f = input()
    if re.search(pattern, f):
        print('True')
    else: print('False')

# 2. Re.split()

regex_pattern = r"[,.]"	# Do not delete 'r'.

# 3. Group(), Groups() and Groupdict()

import re

s = input()

pattern = r'([A-Za-z0-9])\1+'

n = re.search(pattern,s)

if n:
    print(n.group(1))
else: print(-1)

# 4. Re.findall() & Re.finditer()

import re
s = input()

pattern =  r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM ])[ueaoaiUEOAI]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM ])'


result = re.findall(pattern,s)
if result:
    for i in result:
        print(i)
else: print(-1)

# 5. Re.start() & Re.end()

import re
s= input()
k= input()
pattern = re.compile(k)
n = {}
result = re.search(pattern, s)
if not result:
  print((-1,-1))
else: 
  for i in range(len(s)-len(k)-1):
      result = re.search(pattern, s[i:])
      n[i+result.start()] = i+result.end()-1
  for start, end in n.items():
    print('({}, {})'.format(start,end))

# 6. Regex Substitution

import re

pattern1 = r'(?<= )\|\|(?= )'
pattern2 = r'(?<= )\&\&(?= )'
n = int(input())
for i in range(n):
    s = input()
    result1 = re.sub(pattern1, 'or', s)
    result2 = re.sub(pattern2, 'and', result1)
    print(result2)

# 7. Validating Roman Numerals

regex_pattern = r'^M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$'

# 8. Validating phone numbers

import re

n = int(input())

pattern = r'^[789]\d{9}$'

for i in range(n):
    s = input()
    match = re.match(pattern,s)
    if match:
        print('YES')
    else: print('NO')

# 9. Validating and Parsing Email Addresse

import re
n = int(input())

pattern = r'<([a-z][a-z0-9-._]+@([a-zA-Z])+\.[a-z]{1,3})>'

for i in range(n):
    s = input()
    result = re.search(pattern, s)
    if result:
        print(s)

# 10. Hex Coler Code

import re
n = int(input())

pattern = r'(?<=[ :,])#[0-9a-fA-f]+(?=[^\w])'

for i in range(n):
    s = input()
    result = re.findall(pattern, s)
    if result:
        print('\n'.join(i for i in result))

# 11. HTML Parser - Part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        if len(attrs) != 0:
            for i in attrs:
                print('->', i[0], '>', i[1])
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        if len(attrs) != 0:
            for i in attrs:
                print('->', i[0], '>', i[1])

parser = MyHTMLParser()

n = int(input())
for i in range(n):
    m = input()
    parser.feed(m)

# 12. HTML Parse - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
        else: 
            print('>>> Single-line Comment')
            print(data)
        
    def handle_data(self, data):
        if data != '\n':
            print (">>> Data")
            print(data)

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# 13. Detect HTML, Tags, Attributes and Attribute Values

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if len(attrs) != 0:
            for i in attrs:
                print('->', i[0], '>', i[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if len(attrs) != 0:
            for i in attrs:
                print('->', i[0], '>', i[1])
    

parser = MyHTMLParser()

n = int(input())
for i in range(n):
    m = input()
    parser.feed(m)

# 14. Validation UID

import re

n = int(input())

patterns = [r'(.*[A-Z].*){2,}', r'(.*[0-9].*){3,}', r"[A-Za-z0-9]{10}"]

for i in range (n):
    s = input()
    k = 0
    for j in patterns:
        if bool(re.search(j,s)) == False:
            k = 1
            break
    if bool(re.search(r'.*(.).*\1', s)):
        k = 1
    if k == 0:
        print('Valid')
    else: print('Invalid')
    

# 15. Validating Credit Card Numbers

import re
from collections import Counter
n = int(input())

pattern = r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$'

for i in range(n):
    s = input()
    l = s.replace('-','')
    k = 0
    for i in range(10):
        if str(i)*4 in l:
            k =1
    if re.match(pattern, s) and k == 0:
        print('Valid')
    else: print('Invalid')

# 16. Validating Postal Codes

regex_integer_in_range = r"[1-9][0-9]{5}$"	
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	

# 17. Matrix Script 
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
s = ''
for _ in range(n):
    matrix_item = input()
    matrix.append([i for i in matrix_item])
for i in range(m):
    for arr in matrix:
        s += arr[i]

pattern = r'(?<=[a-zA-Z])[!@#$%&\s]+(?=[a-zA-Z])'
print(re.sub(pattern, ' ', s))
    
  
# J. XML total: 2/2

# 1. XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    s = 0
    for i in node.iter():
        s += len(i.items())
    return s
 # 2. XML 2 - Find the Maximun Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)
  
# K. CLOSURES AND DECORATIONS total :2/2

# 1. Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        # complete the function
        number = ['+91 {} {}'.format(i[-10: -5], i[-5:]) for i in l]
        return f(number)
    return fun

# 2. Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        arr = []
        for person in sorted(people, key=lambda x: int(x[-2])):
            arr.append(f(person))
        return arr

    return inner

# L. NUMPY total: 15/15
  
# 1. Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr, dtype = 'f')
    return numpy.flip(arr)

# 2. Shape and Reshape

import numpy

arr = input().strip().split(' ')

arr = numpy.array(arr, dtype = 'int64')

print(numpy.reshape(arr, (3,3)))

# 3. Transpose and Flatten 

import numpy

n,m = map(int, input().split(' '))

arr = []

for i in range(n):
    arr += input().split(' ')

arr = numpy.array(arr, dtype = 'int64')

arr = numpy.reshape(arr, (n,m))

print(numpy.transpose(arr))
print(arr.flatten())

# 4. Concatenate

import numpy

n, m, p = map(int, input().split(' '))

arr1 = []
arr2 = []

for i in range(n):
    arr1 += input().split(' ')

arr1 = numpy.array(arr1, dtype='int64')

arr1 = numpy.reshape(arr1, (n,p))

for i in range(m):
    arr2 += input().split(' ')

arr2 = numpy.array(arr2, dtype='int64')

arr2 = numpy.reshape(arr2, (m,p))

print(numpy.concatenate((arr1, arr2), axis = 0))


# 5. Zeros and Omes

import numpy

d = list(map(int, input().strip().split(' ')))

print(numpy.zeros((d), dtype = numpy.int))
print(numpy.ones((d), dtype = numpy.int))


# 6. Eye and Identity

import numpy

n, m = map(int, input().split(' '))
numpy.set_printoptions(sign=' ')
print(numpy.eye(n, m, k=0))

# 7. Array Mathematics

import numpy

n, m = map(int, input().split(' '))

A = numpy.array([input().split() for i in range(n)], dtype = 'int64')

B = numpy.array([input().split() for i in range(n)], dtype = 'int64')

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)

# 8. Floor, Ceil and Rint

import numpy
numpy.set_printoptions(sign=' ')
arr = numpy.array(input().split(' '), dtype = 'f')

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

# 9. Sum and Prod

import numpy
n,m = map(int, input().split())
arr = numpy.array([input().split() for i in range(n)], int).reshape(n,m)

print(numpy.prod(numpy.sum(arr, axis = 0)))

# 10. Min and Max

import numpy

n,m = map(int, input().split())

arr = numpy.array([input().split() for i in range(n)], int)

arr_min = numpy.min(arr, axis=1)

print(numpy.max(arr_min))

# 11. Mena, Var, and Std

import numpy

#https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html
numpy.set_printoptions(legacy='1.13')

n,m = map(int, input().split())

arr = numpy.array([input().split() for i in range(n)], int)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr))

# 12. Dot and Cross

import numpy

n = int(input())

A = numpy.array([input().split() for i in range(n)], int)

B = numpy.array([input().split() for i in range(n)], int)

print(A.dot(B))

# 13. Inner and Outer

import numpy

A = numpy.array(input().split(), int)

B = numpy.array(input().split(), int)

print(numpy.inner(A,B))

print(numpy.outer(A,B))


# 14. Polynomials

import numpy

cof = numpy.array(input().split(), float)

x = int(input())

print(numpy.polyval(cof,x))


# 15. Linear Algebra

import numpy
# https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html
numpy.set_printoptions(legacy='1.13')

n = int(input())

arr = numpy.array([input().split() for i in range(n)], float)

print(numpy.linalg.det(arr))

# ----------------------------------------------------------------------------------------------------

# Promblem 2  total 6/6

# 1. Birthday Cake Candels

import math
import os
import random
import re
import sys
from collections import Counter

def birthdayCakeCandles(candles):
    # Write your code here
    candles = sorted(candles)

    counter = Counter(candles)

    return counter[candles[-1]]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

    
 # 2. Number Line Jumps

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# 3. Viral Advertising

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    shared = 5
    liked = 2
    cul = 2
    while(n-1 > 0):
        shared = 3*int(shared/2)
        liked = int(shared/2)
        cul += liked
        n -= 1
    return cul
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# 4. Recursive Digit Sum

import math
import os
import random
import re
import sys

def superDigit(n, k):
    s = sum([int(i) for i in str(n)])*k
    if s < 10:
        return s
    else: return superDigit(s,1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# 5.  Insertion Sort - Part 1

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    s = arr[-1]
    for i in range(n-1, 0, -1):
        if s < arr[i-1] :
            arr[i] = arr[i-1]
            print(' '.join([str(i) for i in arr]))
            if i-1 ==0:
              arr[0] = s
              print(' '.join([str(i) for i in arr]))
        if s > arr[i-1]:
            arr[i] = s
            print(' '.join([str(i) for i in arr]))
            break

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# 6. Insertion Sort - Part 2

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(1, n):
        s = arr[i]
        j = i-1
        while j >= 0 and s < arr[j]: 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = s
        print(' '.join([str(i) for i in arr]))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


