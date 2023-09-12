from proj06 import one_pair_7
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

H1 = [Card(10,4),Card(3,1),Card(11,4),Card(7,2),Card(11,3),Card(5,2),Card(6,3)]
H2 = [Card(2,4),Card(5,4),Card(7,1),Card(3,3),Card(13,3),Card(11,3),Card(10,3)]

L1 = [Card(11,3),Card(11,4)]
L2 = one_pair_7(H1)
print("H1:",H1)
print("Instructor's one_pair_7(H1):",L1)
print("Student's one_pair_7(H1):",L2)
print()
print("H2:",H2)
print("Instructor's one_pair_7(H1):",False)
print("Student's one_pair_7(H1):",one_pair_7(H2))

assert compare(one_pair_7(H1),L1) == True and one_pair_7(H2) == False