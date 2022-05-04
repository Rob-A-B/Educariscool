import os
os.system('cls')

atv_bio = 10
atv_his = 10

def barras():
    os.system('cls')
    bio = int(input('Quantas atividades você fez de biologia? '))
    bio = bio *10
    for i in range(101):
        
        if(i<bio):
            print("▣", end="", sep="")
        elif i>bio and i<=100:
            print("▢", end="", sep="")
    print(f'  {bio}%')

    his = int(input('\nQuantas atividades você fez de história? '))
    his = his* 10
    for i in range(101):
        
        if(i<his):
            print("▣", end="", sep="")
        elif i>his and i<=100:
            print("▢", end="", sep="")
    print(f'  {his}%')
