#QUESTION 1

def Hanoi(n , fro , mid, to):
	if n == 0:
		return
	Hanoi(n-1, fro, mid, to)
	print("Move Disk ",n," from rod ",fro," to rod ",to)
	Hanoi(n-1, mid, to, fro)
n = 3
Hanoi(n, 'A', 'C', 'B')                #Calling Function For 3 Disks
print("\n")

Move Disk  1  from rod  A  to rod  B
Move Disk  2  from rod  A  to rod  B
Move Disk  1  from rod  C  to rod  A
Move Disk  3  from rod  A  to rod  B
Move Disk  1  from rod  C  to rod  A
Move Disk  2  from rod  C  to rod  A
Move Disk  1  from rod  B  to rod  C



Process finished with exit code 0




#QUESTION 2

from tracemalloc import start
from math import factorial, remainder
n=int(input("Enter The Size Of The Pascal's Triangle: "))

print("By Recursion Method...")            #Using Recursions

def pascal_triangle(n,length = n):
    if n == 0:
        return
    pascal_triangle(n-1,length)
    print('  '*(length-n), end='')
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        start = start * (n - i) // i      #Bionomial Coefficients
    print()
pascal_triangle(n)
print("\n")

print("By Iterative Method...")           #Using Iterations

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")      #nCr = n!/r!(n-r)!
	print()
print("\n\n")

Enter The Size Of The Pascal's Triangle: 10
By Recursion Method...
                  1   
                1   1   
              1   2   1   
            1   3   3   1   
          1   4   6   4   1   
        1   5   10   10   5   1   
      1   6   15   20   15   6   1   
    1   7   21   35   35   21   7   1   
  1   8   28   56   70   56   28   8   1   
1   9   36   84   126   126   84   36   9   1   


By Iterative Method...
           1 
          1 1 
         1 2 1 
        1 3 3 1 
       1 4 6 4 1 
      1 5 10 10 5 1 
     1 6 15 20 15 6 1 
    1 7 21 35 35 21 7 1 
   1 8 28 56 70 56 28 8 1 
  1 9 36 84 126 126 84 36 9 1 




Process finished with exit code 0

#QUESTION 3

val1, val2 = map(int,input("Enter 2 Numbers: ").split())
Quotient = val1 // val2
Remainder = val1 % val2

#a-Part

print("Callability Check...")                          #Checking The Callability Of Quotient And Remainder
print(callable(Quotient))
print(callable(Remainder))

#b-Part

if (Quotient == 0):
    print("The Quotient Is Zero")
if (Remainder == 0):
    print("The Remainder Is Zero")
if (Quotient != 0 and Remainder != 0):
    print("All Values Are Non-Zero")

#c-Part

c_list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(c_list)):
    if c_list[i] > 4:
        result.append(c_list[i])
print(f"Filtered out numbers that are greater than 4 are : {result}")

#d-Part

setresult = set(result)
print("Set: ",setresult)

#e-Part

immutableSet = frozenset(setresult)                #Making The Set Immutable
print("Immutable set:",immutableSet)

#f-Part

print("Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")

Enter first number: 1
Enter Second number: 5

The quotient and remainder are: (0, 1)
(a)
Checking if the function is callable:  True

(b)
There are zeroes in the list

(c)
Numbers greater than 4 are : {5, 6}

(d)
The immutable set is : frozenset({5, 6})

(e)
Maximum Value in the set is : 6

(f)
Hash of max value is : 6
******************************************************************************************

Process finished with exit code 0



#QUESTION 4

class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object Destroyed!")
student1 = Student("Aashrya", 20104052)
print("Object Created...")
print(f"The Name Of The Student Is {student1.name} And SID Is {student1.roll_no}.")
del student1
print("\n")

Object Created...
The Name Of The Student Is Aashrya And SID Is 20104052.
Object Destroyed!



Process finished with exit code 0


#QUESTION 5

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#a-Part

employee1.salary = 70000
print(f"The Updated Salary Of {employee1.name} Is {employee1.salary} ")

#b-Part

print("Record Of Viren Deleted!", end='')
del employee3
print("\n")


The Updated Salary Of Mehak Is 70000 
Record Of Viren Deleted!


Process finished with exit code 0


#QUESTION 6

word1 = input("Enter Any Word: ")
word1 = word1.lower()
word2 = input("Enter A New Word Using The Exact Same Letters: ")
word2 = word2.lower()
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
def userinput():
    if count_in_dict(word1) != count_in_dict(word2):
        print("The Words Aren't Matching, Friendship Is Fake!")
        return
    ans = input("Does The Word Makes Any Sense?(Y Or N) ")
    if ans == 'y' or ans=='Y':
        print("Passed The Friendship Test!!!")
    elif ans == 'n' or ans=='N':
        print("Meaningless Word , Friendship Is Fake!")
    else:
        print("Invalid Input,Try Again! ")
        userinput()
userinput()


Enter Any Word: lolol
Enter A New Word Using The Exact Same Letters: ololl
Does The Word Makes Any Sense?(Y Or N) N
Meaningless Word , Friendship Is Fake!

Process finished with exit code 0
