from ntpath import join
import string

class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
          
    def speak(self):
        print("My name is {}".format(self.name))
  
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
  
# Accessing class methods
Rodger.speak()
Tommy.speak()


print("dont need a class to be able to print.. hmm")

a = "GeeksForGeeks"
print("Reverse is", a[::-1])


a = ["Geeks", "For", "Geeks"]
print("0 at %s" % (a[0]))
print("1 at {}".format(a[1]))
print(" ".join(a))


# https://stackoverflow.com/questions/5319922/check-if-a-word-is-in-a-string-in-python/5319942
def retlistsplitted(mystring):
    # whitespace_chars = " \t\n\r\f" - space, tab, newline, return, formfeed
    # why error
    # list_of_words = mystring.split( \t\n\r\f,.;!?'\"()"')
    # if word in list_of_words:
        print('success')


rere = "sad dqw,r23 24s asd wqqwe"
retlistsplitted(rere)

# Declaring the list geek
geek = ['Geeks', 'Programming', 'Algorithm', 'Article']

print(type(geek))

# Directly printing the list
print ("Simple List:", geek)
   
# Printing the list by join method
print ('List by using join method: %s' % ', ' .join(geek))
   
# Direct use of join method
print ('Direct apply the join method:',(", " .join(geek)))

print('asd also add with format {}'.format('join by this'.join(geek)))

# Declaring the list geek
geek = ['Sun', 'Flowers', 'Peoples', 'Animals', 'Day', 'Night']
 
partition = list(zip (*[iter(geek)] * 2))
print (partition)


# Reads a string from input and type case them to int
# after splitting to white-spaces
 
# formatted_list = list(map(str, input().split()))

formatted_list =  list(map(str, "as dwq 4 1 asc c 23 41 ".split()))

formatted_list1 =  list(map(str, "as dwq 4 1 asc c 23 41 "))

print("i am splitting {}".format('as dwq 4 1 asc c 23 41 '))

print(formatted_list)

print(formatted_list1, '\n^ this goes each char in list')



def myFun(arg11, arg2, arg3):
    print("arg1:", arg11)
    print("arg2:", arg2)
    print("arg3:", arg3)
      
# Now we can use *args or **kwargs to
# pass arguments to this function : 
args = ("Geeks", "for", "Geeks")
myFun(*args)
  
# takes key - value, must match params
kwargs = {"arg11" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
myFun(**kwargs)

def myFun1(**kwargs):
    for k, v in kwargs.items():
        print("{} == {}".format(k, v))

myFun1(arg1 = "Geeks", arg2 = "for", arg3 = "Geeks")

# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y
 
# using the normally
# defined function
print(cube(5))
 
# using the lambda function
print(lambda_cube(5))

print('################# breaker #################')

tables = [lambda x=x: x*10 for x in range(1, 11)]
 
for table in tables:
    print(table())

print('################# breaker #################')


# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

