# ROCK,PAPER,SCISSOR GAME
'''
import random
a=['r','p','s']
print('ALL THE BEST PLAYER,WE WISH FOR YOUR WIN!!!')
print('YOU ENTERED THE GAME...')
print('choose first letter of your choice')


com=0
you=0
for i in range(1,4,1):
    c=random.choice(a)
    x=str(input('enter your choice:'))
    if x==c:
        print(f'THE RESULT OF ROUND {i} IS DRAWN')
        if x=='r':
            print('YOUR CHOICE IS ROCK')
            print('COMPUTER CHOICE IS ROCK')
        elif x=='p':
            print('YOUR CHOICE IS PAPER')
            print('COMPUTER CHOICE IS PAPER')
        else:
            print('YOUR CHOICE IS SCISSOR')
            print('COMPUTER CHOICE IS SCISSOR')

    elif x=='r' and c=='p':
        print(f'THE RESULT OF ROUND {i} IS YOU LOSE')
        print('YOUR CHOICE IS ROCK')
        print('COMPUTER CHOICE IS PAPER')
        com+=1
    elif x=='r' and c=='s':
        print(f'THE RESULT OF ROUND {i} IS YOU WIN')
        print('YOUR CHOICE IS ROCK')
        print('COMPUTER CHOICE IS SCISSOR')
        you+=1
    elif x=='s' and c=='p':
        print(f'THE RESULT OF ROUND {i} IS YOU WIN')
        print('YOUR CHOICE IS SCISSOR')
        print('COMPUTER CHOICE IS PAPER')
        you+=1
    elif x=='s' and c=='r':
        print(f'THE RESULT OF ROUND {i} IS YOU LOSE')
        print('YOUR CHOICE IS SCISSOR')
        print('COMPUTER CHOICE IS ROCK')
        com+=1
    elif x=='p' and c=='s':
        print(f'THE RESULT OF ROUND {i} IS YOU LOSE')
        print('YOUR CHOICE IS PAPER')
        print('COMPUTER CHOICE IS SCISSOR')
        com+=1
    else:
        print(f'THE RESULT OF ROUND {i} IS YOU WIN')
        print('YOUR CHOICE IS PAPER')
        print('COMPUTER CHOICE IS ROCK')
        you+=1

if you<com:
    print('SORRY YOU LOST THE GAME,BETTER LUCK NEXT TIME!!')
    print(f'THE SCORE OF THE COMPUTER IS {com} POINTS')
    print(f'YOUR SCORE IS {you} POINTS')
    print(f'YOU LOSE TO COMPUTER BY {com-you} points')
elif com<you:
    print('CONGRATULATIONS!! YOU WON THE GAME...')
    print(f'THE SCORE OF THE COMPUTER IS {com} POINTS')
    print(f'YOUR SCORE IS {you} POINTS')
    print(f'YOU BEAT THE COMPUTER BY {you-com} points')
else:
    print('OOOPS!!! THE MATCH IS DRAWN')
    print(f'THE SCORE OF THE COMPUTER IS {com} POINTS')
    print(f'YOUR SCORE IS {you} POINTS')
    
'''

# guess is number game
'''
import random
a=-1
comp=random.randint(1,100)
time=0
while a!=0:
    x=int(input('enter your number between 1 and 100:'))
    time+=1
    if comp==x:
        print(f'correct guess in {time} try')
        break
    elif x<comp:
        print('guess a big no then this')
    else:
        print('guess a small no then this')
'''

# random password generator:
'''
import random

alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
g=str(random.randint(1,9))
salp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=random.choice(alp)
b=random.choice(salp)
c=random.choice(salp)
d=random.choice(alp)
e=str(random.randint(1,10))
f=random.choice(alp)

pas=a+g+b+c+d+e+f

print(pas)
'''
# captcha checker:
'''
import random

alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
g=str(random.randint(1,9))
salp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=random.choice(alp)
b=random.choice(salp)
c=random.choice(salp)
d=random.choice(alp)
e=str(random.randint(1,10))
f=random.choice(alp)
y=-1
while y!=0:
    captcha=a+b+g+c+d+e+f+g
    print(f'your cptcha is here:{captcha}')
    x=str(input('enter the captcha:'))
    if captcha==x:
        print('you are a human')
        break
    else:
        print('your input is invailid')
'''
