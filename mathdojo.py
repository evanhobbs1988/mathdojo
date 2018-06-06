Assignment: MathDojo
Objectives:
Practice creating a class and creating new instances
Practice chaining methods
Practice writing flexible functions that can take a variable number of arguments
HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself(an instance of itself), we can chain methods.

Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

Then create a new instance called md.

class MathDojo(object):
    def __init__(self, start):
        self.start = start
    def add(self, *addends):
        for i in addends:
            if isinstance(i, list): #This allows for lists to be inputted
                for num in i:
                    self.start += num
            elif isinstance(i, tuple): #This allows for tuples to be added
                for num in i:
                    self.start += num
            else: #This is for integers
                self.start += i
        return self
    def subtract(self,*subtrahends): #Same logic as above applied to this function
        for i in subtrahends:
            if isinstance(i,list):
                for num in i:
                    self.start -= num
            elif isinstance(i,tuple):
                for num in i:
                    self.start -= num
            else:
                self.start -= i
        return self
    def result(self):
        print self.start

#Trial
md = MathDojo(2)
md.add((2, 3)).subtract(5).result()
