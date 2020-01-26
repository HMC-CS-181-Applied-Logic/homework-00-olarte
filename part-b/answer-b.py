from propositional_logic import *

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')

# write code using A, B, and C, along with 
# the classes from propositional_logic.py
# and the .format() method to output the
# following expression:

# (((A => B) & (B => C)) => (A => C))

imp1 = Implies(A,B)
imp2 = Implies(B,C)
imp3 = Implies(A,C)
and1 = And(imp1,imp2)
output = Implies(and1,imp3)
print(output.format())