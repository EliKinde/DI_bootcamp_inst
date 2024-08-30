'''
from collections import Counter
import itertools
list = [1,2,3,4,1,2,6,7,3,8,1,2,2]
answer=Counter()
answer = Counter(list)
print(answer[int(input("Enter a: "))])


result = itertools.cycle('12345')
counter = 0

for number in result:
# termination condition
    if counter < 10 :
        print (number)
        counter = counter + 1
    else:
        break

'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()
