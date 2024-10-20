# package: object oriented programming --> encapsulation --> combining or group or
# Waraping
#
# 1 to 100 ---> 5 lines code 3 times repeat
#          ---> 3 lines code 3 times repeat
#          ----> 4 lines code 4 times repeat
# 1 to 100 lines code --> Requirement 20 lines code required to execute
#                     --> phase line number 30 to 50th line
#
# Grouping the related module in a single unit is called a package
#
# default directory or foloder -- or module ---> __init__.py

--> go to the folder or dirctory location right click --> new option --> choose Python package --> given name to the package_ex
--> its generate default dirctory file __init__.py
--> under to create new python file that will be consider as a module
--> now we can create new file outside of package directory to access that package
-->
from test_pack.package_madule1 import *

test_module()
test_module2()

# Package module executed...
# Package module2



















# math module :
# 1)sqrt(x)
# 2)	ceil(x)
# 3)	floor(x)
# 4)	fabs(x)
# 5)	log(x)
# 6)	sin(x)
# 7)	tan(x)
# import math
# from math import *
# res = math.sqrt(5)
# print(res)



# random module:
# •	This module defines several functions to generate random numbers.
# •	We can use these functions while developing games,in cryptography and to generate random numbers on fly for authentication.
# # This function always generate some float value between 0 and 1(not inclusive)
# 1) random():

# from random import *
# for i in range(10):
#     print(random())

# 2)randint() Function:
# To generate random integer between two given numbers(inclusive)
# from random import *
# for i in range(5):
#     print(randint(1, 100))

# 3)	uniform() Function:
# It returns random float values between 2 given numbers (not inclusive)

# from random import *
# for i in range(5):
#     print(uniform(1, 10))

# 4)	randrange ([start], stop, [step])
# •	Returns a random number from range
# •	start <= x < stop
# •	start argument is optional and default value is 0
# •	step argument is optional and default value is 1
#
# •	randrange(10)  generates a number from 0 to 9
# •	randrange(1,11)  generates a number from 1 to 10
# •	randrange(1,11,2)  generates a number from 1,3,5,7,9

# from random import *
# for i in range(5):
#     print(randrange(2, 20, 2))


# 5)choice() Function:
# •	It won’t return random number.
# •	It will return a random object from the given list or tuple.


# from random import *
# students = ["ajay", "kumar", "Himajesh", "Mokshagna", "Sruthi", "Suneetha", "Aparna", "Renuka"]
# for i in range(5):
#     print(choice(students))
# output:
# Suneetha
# kumar
# Aparna
# Renuka
# Sruthi













