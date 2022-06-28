import random
def game_win(comp,you):
    tie=0
    if (comp==you):
        return 0
    elif (comp=='s'):
        if you=='c':
            return True
    elif (comp=='s'):
        if you=='p':
            return False
    elif (comp=='c'):
        if you=='p':
            return True
    elif (comp=='c'):
        if you=='s':
            return False
    elif (comp=='c'):
        if you=='p':
            return True
    elif (comp=='p'):
        if you=='s':
            return True
    elif (comp=='p'):
        if you=='c':
            return False
comp=random.randint(1,3)
if comp==1:
    comp='s'
elif comp==2:
    comp='p'
elif comp==3:
    comp='c'
you=input("choose stone(s), paper(p), scissor(c)?")
print("computer choice ",comp)
print("your choice",you)
a=game_win(comp,you)
if a==0:
    print("it is a tie")
elif a:
    print("computer win")
else:
    print("you win")
