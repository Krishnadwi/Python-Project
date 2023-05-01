print("Welcome to Nimble Tech Playstore!")
signUp_details = {"Name": [], "Username": [], "Password":[]}
def sign_up():
    name = input("Enter your name: ")
    signUp_details["Name"].append(name)
    username = input("Enter email-id: ")
    signUp_details["Username"].append(username)
    password = input("Enter password: ")
    signUp_details["Password"].append(password)
    print("Login")
    sign_in()
def sign_in():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
   
    if username in signUp_details["Username"]:
        index = signUp_details["Username"].index(username)
        if signUp_details["Password"][index] == password:
            print("Login Successful")
            game()
        else:
            print("Invalid Password")
    else:
        print("Username not found")


def game():
    
    print("1-2048")
    print("2:Stone Paper and Scissior:")
    print("3-Scrapping")
    print("4-quiz")
    print("5-hangman")
    print("6-tic tac toe")
    print("7-snake-leader")
    print("8-blackjack")
    choose=int(input("Choose the game you want to play"))
    while True:
        if choose==1:
            print("2048 game")
            import random
            def start_game():
                return [[0 for i in range(4)] for i in range(4)]
            def reverse(mat):
                new_mat=[]
                for i in range(4):
                    new_mat.append([])
                    for j in range(4):
                        new_mat[i].append(mat[i][3-j])
                return new_mat
            def transp(mat):
                for i in range(4):
                    for j in range(3):
                        if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                            mat[i][j]+=mat[i][j]
                            mat[i][j+1]=0
        
                return mat
            def compress(mat):
                new_mat=[[0 for i in range(4)] for i in range(4)]
                for i in range(4):
                    pos=0
                    for j in range(4):
                        if mat[i][j]!=0:
                            new_mat[i][pos]=mat[i][j]
                            pos+=1
                return new_mat
            def moveLeft(arr):
                st1=compress(arr)
                st2=merge(st1)
                st3=compress(st2)
                return st3
            def moveRight(arr):
                st0=reverse(arr)
                st1=compress(st0)
                st2=merge(st1)
                st3=compress(st2)
                st4=reverse(st3)
   
                return st4
            def moveUp(arr):
                st0=transp(arr)
                st1=compress(st0)
                st2=merge(st1)
                st3=compress(st2)
                st4=transp(st3)
        
                return st4
            def moveDown(arr):
                st0=transp(arr)
                st=reverse(st0)
                st1=compress(st)
                st2=merge(st1)
                st3=compress(st2)
                st3=reverse(st3)
                st4=transp(st3)
                return st4
            a=list(map(int,input().split()))
            arr=start_game()
            arr[1][3]=2                       #initial array setup, choosen random numbers at random places.
            arr[2][2]=2
            arr[3][0]=4
            arr[3][1]=8
            arr[2][1]=4
            for i in a:
                if i==1:
                    arr=moveUp(arr)
                       #move Up
                
                elif i==2:                       #move Down
                    arr=moveDown(arr)
                elif i==3:                       #move left
                    arr=moveLeft(arr)
                elif i==4:                       #move right
                    arr=moveRight(arr)
            print(arr)
    
        if choose==2:
        
            import random 
            import string
            user_chance=input('Enter your option from [rock,paper,scissor]:')
            entrys=['rock','paper','scissor']
            computer_chance=random.choice(entrys)
            print(f"\nI chose {user_chance}, computer chose {computer_chance}\n")
            
            if user_chance==computer_chance:
                print("Game is tie")
            elif user_chance=='rock' and computer_chance=='paper':
                print("computer's win")
            elif user_chance=='paper' and computer_chance=='scissor':
                print("computer's win")
            elif user_chance=='scissor' and computer_chance=='rock':
                print("computer's win")
            else:
                if user_chance=='paper' and computer_chance=='rock':
                    print('you win')
                elif user_chance=='scissor' and computer_chance=='paper':
                    print('you win')
                elif user_chance=='rock' and computer_chance=='scissor':
                    print('you win')
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again != "y":
                break
        if choose==3:
            import pandas as pd
            url ='https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
            data=pd.read_html(url)
            type(data)
            len(data)
            
            print(data[1].loc[:,["State","Administrative/Executive capital"]])
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again != "y":
                break
        if choose==4:
            import python2
            python2.quiz()
        if choose==5:
            import python3
            python3.hang_man()
        if choose==6:
            import python4
            python4.tic_tac_toe()
        if choose==7:
            import python5
            python5.snake_ladder()
        if choose==8:
            import python6
            python6.black_jack()
            break
print("\nMENU")
print("1. Sign in")
print("2. Sign up")
print("3. Exit!")
choice = int(input("Enter your choice: "))
if choice == 1:
    while True:
        sign_in()
elif choice == 2:

        sign_up()
elif choice == 3:
    print("Goodbye!")
else:
    print("Invalid choice")