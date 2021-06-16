import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        if you=='g':
            return  True
    elif comp=='w':
        if you=='g':
            return False
        if you=='s':
            return  True
    elif comp=='g':
        if you=='s':
            return False
        if you=='w':
            return  True


print("Comp turn: Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input("your turn: Snake(s) Water(w) or Gun(g)  ")
a=gameWin(comp,you)

print(f"Comp choose {comp}")
print(f"you choose {you}")

if a==None:
    print('this game is tie.')
elif a:
    print('you win!')
else:
    print('you lose!')