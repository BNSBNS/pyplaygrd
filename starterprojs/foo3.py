# Suppose this is foo3.py.
import os, sys; sys.path.insert(0, os.path.dirname(__file__)) # needed for some interpreters

def function_a():
    print("func a gona import func b")
    from foo3 import function_b
    print("a2")
    function_b()
    print("a3")

def function_b():
    print("b")


print("m1")
function_a()
print("m2 -end foo3.py")
