from proj06 import full_house_7
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
    
H1 = [Card(7,4),Card(5,1),Card(11,4),Card(3,2),Card(11,3),Card(7,2),Card(7,3)]
H2 = [Card(2,4),Card(5,4),Card(2,1),Card(3,3),Card(13,3),Card(11,3),Card(10,3)]

L1 = [Card(11,3),Card(11,4),Card(7,2),Card(7,3),Card(7,4)]
L2 = full_house_7(H1)
print("H1:",H1)
print("Instructor's full_house_7(H1):",L1)
print("Student's full_house_7(H1):",L2)
print()
print("H2:",H2)
print("Instructor's full_house_7(H2):",False)
print("Student's full_house_7(H2):",full_house_7(H2))

assert compare(full_house_7(H1),L1) == True and full_house_7(H2) == False