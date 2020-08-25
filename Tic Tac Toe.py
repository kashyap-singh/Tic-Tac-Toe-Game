#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import msvcrt
def check():
    if Table['1']=='x' and Table['2']=='x' and Table['3']=='x':
        print("\n WOW!!! {} Won the Match \n".format(P_1))
        display()
        return 1
    elif Table['4']=='x' and Table['5']=='x' and Table['6']=='x':
        print("\n WOW!!! {} Won the Match \n".format(P_1))
        display()
        return 1
    elif Table['7']=='x' and Table['8']=='x' and Table['9']=='x':
        print("\n WOW!!! {} Won the Match\n".format(P_1))
        display()
        return 1
    elif Table['1']=='x' and Table['4']=='x' and Table['7']=='x':
        print("\n WOW!!! {} Won the Match\n".format(P_1))
        display()
        return 1
    elif Table['5']=='x' and Table['2']=='x' and Table['8']=='x':
        print("\n WOW!!! {} Won the Match\n".format(P_1))
        display()
        return 1
    elif Table['3']=='x' and Table['6']=='x' and Table['9']=='x':
        print("\n WOW!!! {} Won the Match\n".format(P_1))
        display()
        return 1
    elif Table['1']=='x' and Table['5']=='x' and Table['9']=='x':
        print("\n WOW!!! {} Won the Match\n".format(P_1))
        display()
        return 1
    elif Table['3']=='x' and Table['5']=='x' and Table['7']=='x':
        print("\n WOW!!! {} Won the Match\n".format(P_1))
        display()
        return 1
    elif Table['1']=='o' and Table['2']=='o' and Table['3']=='o':
        print("\n WOW!!! {} Won the Match\n".format(P_2))
        display()
        return 1
    elif Table['4']=='o' and Table['5']=='o' and Table['6']=='o':
        print("\n WOW!!! {} Won the Match\n".format(P_2))
        display()
        return 1
    elif Table['9']=='o' and Table['8']=='o' and Table['7']=='o':
        print("\n WOW!!! {} Won the Match\n".format(P_2))
        display()
        return 1
    elif Table['1']=='o' and Table['4']=='o' and Table['7']=='o':
        print("\n WOW!!! {} Won the Match\n".format(P_2))
        display()
        return 1
    elif Table['5']=='o' and Table['2']=='o' and Table['8']=='o':
        print("\n WOW!!! {} Won the Match\n".format(P_2))
        display()
        return 1
    elif Table['3']=='o' and Table['6']=='o' and Table['9']=='o':
        print("\n WOW!!! {} Won the Match\n".format(P_2))
        display()
        return 1
    elif Table['1']=='o' and Table['5']=='o' and Table['9']=='o':
        print("\n WOW!!! {} Won the Match \n".format(P_2))
        display()
        return 1
    elif Table['7']=='o' and Table['5']=='o' and Table['3']=='o':
        print("\n WOW!!! {} Won the Match \n".format(P_2))
        display()
        return 1
    return 0
def display():
    print(" {} | {} | {}".format(Table['1'],Table['2'],Table['3']))
    print("__  ___  __")
    print(" {} | {} | {}".format(Table['4'],Table['5'],Table['6']))
    print("__  ___  __")
    print(" {} | {} | {}".format(Table['7'],Table['8'],Table['9']))

Table={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
print("TIC TAC TOE \n\n")
print(" 1 | 2 | 3")
print("__  ___  __")
print(" 4 | 5 | 6")
print("__  ___  __")
print(" 7 | 8 | 9")
print("EVERY PLAYER WILL FILL THE ENTRY WITH RESPECT TO THE NUMBER GIVEN \n")
print("ALL THE BEST TO BOTH THE PLAYERS \n \tGAME BEGINS \n\n")
P_1=input("PLAYER 1 ENTER YOUR NAME :")
P_2=input("PLAYER 2 ENTER YOUR NAME :")
player=1
count=0
dis=0
while True:
    if check()==1:
        msvcrt.getwch()
        break;
    count+=1
    if count>9:
        print("Match Draw!!!")
        break
    if dis>0:
        display()
    if player==1:
        n=input("PLAYER 1 ENTER THE BOX NUMBER: ")
        if Table[n]==' ':
            Table[n]='x'
            player=2
        else:
            print("\n INVALID INPUT !! TRY AGAIN \n")
            count-=1
            continue
    else:
        n=input("PLAYER 2 ENTER THE BOX NUMBER: ")
        if Table[n]==' ':
            Table[n]='o'
            player=1
        else:
            print("\n INVALID INPUT !! TRY AGAIN \n")
            count-=1
            continue
    dis=1


# In[ ]:




