# -----------------
# normal
# -----------------
a = ""
a = 1

#? int()
a
#? []
a.append

a = list

b = 1; b = ""
#? str()
b

a = 1
temp = b;
b = a
a = temp
#? int()
b
#? int()
b
#? str()
a

a = tuple
if 1:
    a = list

#? ['append']
a.append
#? ['index']
a.index

# -----------------
# tuples exchanges
# -----------------
a, b = 1, ""
#? int()
a
#? str()
b

b, a = a, b
#? int()
b
#? str()
a

b, a = a, b
#? int()
a
#? str()
b

# -----------------
# function stuff
# -----------------
def a(a=3):
    #? int()
    a
    #? []
    a.func
    return a

#? int()
a(2)
#? []
a(2).func
# -----------------
# class stuff
# -----------------
class A(object):
    a = ""
    a = 3
    #? int()
    a
    a = list()
    def __init__(self):
        self.b = ""
        self.b = 3
        # TODO should this be so?
        #? int() str() list()
        self.b

        self.b = list

    def before(self):
        self.a = 1
        #? list() str() int()
        self.a

        #? ['after']
        self.after

        self.c = 3
        #? set() int()
        self.c

    def after(self):
        self.a = ''

    c = set()

#? list()
A.a

a = A()
#? ['after']
a.after
#? []
a.upper
#? []
a.append
#? []
a.real

#? list() str() int()
a.a

# -----------------
# class stuff
# -----------------

math = 3
import math
#? ['cosh']
math.cosh
#? []
math.real

math = 3
#? int()
math
#? []
math.cos

# do the same for star imports
cosh = 3
from math import *
# This doesn't work, but that's not a problem, star imports should be at the
# start of EVERY script!
##? []
cosh.real

cosh = 3
#? int()
cosh
