import time
from functools import lru_cache
list2=['s','w','g']
comp=0
chance=10
count=0
x=0
print("\nSnake Water Gun Game...")
print("Abbreviation:\n1.s=snake\n2.w=water\n3.g=gun")
print("\n")
print("*************************************")
print("Rules of the game :")
print("U have choosen V/S Computer has choosen")
print("1. Snake==Snake,Water==Water and Gun==Gun (Both are same ,no points will be given to any side)")
print("2. Snake==Water, Water==snake (Snake can swim in water so who have chosen snake will get a one point)")
print("3. Snake==Gun,Gun==Snake (Simple gun will shot snake and who have chosen Gun will get a point)")
print("4. Water==Gun,Gun==Water (Gun will sink in water so who have chosen Water will get a point)")
print("*************************************")
print("\n")
num=30
print(f"lets start the game on the count of {num} meanwhile you can read the rules :")


def snake():
    global chance
    global count
    global comp
    print("\nBest of Luck")
    while chance!=0:
        global x
        x=input("\nchoose any one:\n1. s\n2. w\n3. g")
        print("\nyou have chosen :",x)
        if x not in list2:
            break
        import random
        list = ["snake", "water", "gun"]
        r = random.choice(list)
        print("Computer have chosen:",r)
        if x=='s' and r=="water":
            count=count+1
            print("\nU get a one point")
            chance=chance-1
            continue
        elif x=='s' and r=="snake":
            print("\nBoth have chosen same so brother bhai bhai")
            chance=chance-1
            continue
        elif x=='s' and r=="gun":
            comp=comp+1
            print("\nHere computer get a one point")
            chance=chance-1
            continue
        elif x=='w' and r=="snake":
            comp = comp + 1
            print("\nHere computer get a one point")
            chance = chance - 1
            continue
        elif x=='w' and r=="water":
            print("\nBoth have chosen same so brother bhai bhai")
            chance=chance-1
            continue
        elif x=='w' and r=="gun":
            count=count+1
            print("\nU get a one point")
            chance=chance-1
            continue
        elif x=='g' and r=="snake":
            count = count + 1
            print("\nU get a one point")
            chance = chance - 1
            continue
        elif x=='g' and r=="water":
            comp=comp+1
            print("\nHere computer get a one point")
            chance = chance - 1
            continue
        elif x=='g' and r=="gun":
            print("\nBoth have chosen same so brother bhai bhai")
            chance = chance - 1
            continue
tm=30


while tm>0:

    print("->",end=" ")
    num-=1
    tm-=1
    time.sleep(1)

snake()
if x not in list2:
    print("\nBut the chosen one is wrong character other than [s,w,g]")
    print("So game stops")
    p=input("Want to play again Y/N")
    p.capitalize()
    if p.capitalize()=='Y':
        snake()
    else:
        print("\nGood Bye")

if chance==0:
    if count>comp:
        print(f"\nYour points are :{count}")
        print("U win the Game ..Congratulation")
    elif count==comp:
        print("\nGame Ties")
    else:
        print(f"\nComputer points are {comp-count} than your points")
        print("So here you loose the Game")
    print("*****************************")
    p = input("\nWant to play again Y/N")
    p.capitalize()
    if p.capitalize() == 'Y':
        snake()
    else:
        print("Good Bye")






