from proj06 import four_7
from cards import Card

def compare(L1,L2):
    ''' Check for equality irregardless of order.'''
    if len(L1) != len(L2):
        return False
    for item in L1:
        if item not in L2:
            return False
    else:
        return True

H1 = [Card(10,4),Card(2,1),Card(2,4),Card(2,2),Card(2,3),Card(4,3),Card(6,3)]
H2 = [Card(2,4),Card(3,4),Card(3,1),Card(3,3),Card(13,3),Card(11,3),Card(10,3)]

L1 = [Card(2,1),Card(2,2),Card(2,3),Card(2,4)]
L2 = four_7(H1)
print("H1:",H1)
print("Instructor's four_7(H1):",L1)
print("Student's four_7(H1):",L2)
print()
print("H2:",H2)
print("Instructor's four_7(H2):",False)
print("Student's four_7(H2):",four_7(H2))
assert compare(four_7(H1),L1) == True and four_7(H2) == False