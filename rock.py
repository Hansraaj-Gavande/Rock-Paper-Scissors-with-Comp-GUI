rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

yr= int(input("whats your input"))

comp = random.randint(0,2 )

print(f"computer's choice {comp}")

if yr == 0 :
    print( '''
             _______
         ---'   ____)
               (_____)
               (_____)
               (____)
         ---.__(___)
         ''')
elif yr == 1 :
    print('''
             _______
         ---'   ____)____
                   ______)
                   _______)
                  _______)
         ---.__________)
         ''' )
elif yr == 2:
    print('''
             _______
         ---'   ____)____
                   ______)
                __________)
               (____)
         ---.__(___)
         ''')


print("THIS WAS YOUR CHOICE")


if comp == 0 :
    print( '''
             _______
         ---'   ____)
               (_____)
               (_____)
               (____)
         ---.__(___)
         ''')
elif comp == 1 :
    print('''
             _______
         ---'   ____)____
                   ______)
                   _______)
                  _______)
         ---.__________)
         ''' )
elif comp == 2:
    print('''
             _______
         ---'   ____)____
                   ______)
                __________)
               (____)
         ---.__(___)
         ''')


print("THIS WAS Computer's CHOICE")


if yr == 0 and comp == 1:
    print("u win")
elif yr ==1 and comp == 0:
    print("u win")
elif yr ==2 and comp ==1  :
    print("u win")
elif yr == comp :
    print("lucky , draw")
else :
    print("u lose ")


