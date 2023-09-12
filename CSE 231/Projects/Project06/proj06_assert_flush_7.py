from proj06 import flush_7
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

H1 = [Card(2,4),Card(5,4),Card(8,3),Card(11,3),Card(13,3),Card(1,3),Card(10,3)]
H2 = [Card(2,4),Card(5,4),Card(8,4),Card(11,3),Card(13,3),Card(1,3),Card(10,3)]

L1 = [Card(8,3),Card(11,3),Card(13,3),Card(1,3),Card(10,3)]
L2 = flush_7(H1)
print("H1:",H1)
print("Instructor's flush_7(H1):",L1)
print("student's flush_7(H1):",L2)
print()
print("H2:",H2)
print("Instructor's flush_7(H2):",False)
print("student's flush_7(H2):",flush_7(H2))

assert compare(flush_7(H1),L1) == True and flush_7(H2) == False