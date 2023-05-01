def quiz():
    print("Welcome to the Python Quiz!")
    score=0
    question_number=0
    start=input("\nLets start the quiz ?")
    if start=='yes':
        question_number = question_number + 1
        ques = input(f'\n{question_number}. What is the correct extension of the Python file? ')
        if ques == '.py':
            print("Correct answer. You are rewarded 1 point")
            score=score+1
        else:
            print("Oops! Your answer is incorrect")
           
        question_number = question_number + 1
        ques = input(f'\n{question_number}. What is used to define a block of code in Python language? ')
        if ques == 'indentation':
            print("Correct answer. You are rewarded 1 point")
            score = score + 1
        else:
            print("Oops! Your answer is incorrect")
           
        question_number = question_number + 1
        ques = input(f'\n{question_number}. Which keyword is used for function in Python language? ')
        if ques == 'def':
            print("Correct answer. You are rewarded 1 point")
            score = score + 1
        else:
            print("Oops! Your answer is incorrect")
           
        question_number = question_number + 1
        ques = input(f'\n{question_number}. Which character is used to give single-line comments in Python? ')
        if ques == '#':
            print("Correct answer. You are rewarded 1 point")
            score = score + 1
        else:
            print("Oops! Your answer is incorrect")    
           
           
        question_number = question_number + 1
        ques = input(f'\n{question_number}. Which type of loops is not supported in Python? ')
        if ques == 'do-while':
            print("Correct answer. You are rewarded 1 point")
            score = score + 1
        else:
            print("Oops! Your answer is incorrect")  
           
        print(f'\nTotal number of question is {question_number}')
        print(f'Your score is {score}')    
quiz()