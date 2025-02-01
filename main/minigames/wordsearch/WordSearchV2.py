# word search game start
import random
import time #to make each line appear slowly

# run instructions
def wsInstructions():
    print('\033[1;34m**************************************************')
    print('\t\t   WORD SEARCH')
    print('**************************************************\033[0;30m')
    time.sleep(1) 
    print('Here are the instructions:-')
    time.sleep(1)
    print('1. Search for the capitalized words.')
    time.sleep(2)
    print('2. To enter your answer, type in the coordinates')
    print('   for each letters in this format: (x,y)')
    time.sleep(2)
    print('3. Your initial points are the maximum points. Everytime you')
    print('   enter a wrong answer, your points will be deducted.')
    time.sleep(2)
    print('4. In order to gain hints, you need to keep the maximum points.')
    time.sleep(2)
    print('5. Example:-')
    print("   Let's donate \033[0;34mBLOOD\033[0;30m to help those in need.")
    time.sleep(2)
    print('\n\t   0 1 2 3 4 ')
    print('\t4 \033[7;37m S L B F P \033[0;30m')
    print('\t3 \033[7;37m O A L E M \033[0;30m')
    print('\t2 \033[7;37m M E O I E \033[0;30m')
    print('\t1 \033[7;37m E N O L W \033[0;30m')
    print('\t0 \033[7;37m A R D T I \033[0;30m')
    print('\n \033[0;34mBLOOD: \033[0;30m(2,4)(2,3)(2,2)(2,1)(2,0)')
    time.sleep(5)
    print('\n\033[0;31m!!! Please make sure you write in the correct format !!!\033[0;30m')

def ws1():
    # display question
    print('\n\n\033[0;34m################## Game Start! ##################\033[0;30m')
    time.sleep(1)
    print('__________________________________________________')
    print('\n Preparations before donating blood:-')
    print(' 1. Get plenty of \033[0;34mSLEEP\033[0;30m.')
    print(' 2. Eat a healthy \033[0;34mMEAL\033[0;30m and avoid fatty foods.')
    print(' 3. Drink plenty of \033[0;34mWATER\033[0;30m.')
    print(' 4. Check to see if any \033[0;34mMEDICATION\033[0;30m you are taking')
    print('    would prevent you from donating.')
    print('__________________________________________________')
    time.sleep(2)
    print('\n\t   0 1 2 3 4 5 6 7 8 9')
    print('\t9 \033[7;37m S L E F P E E J S N \033[0;30m')
    print('\t8 \033[7;37m O A L E M A L D O T \033[0;30m')
    print('\t7 \033[7;37m M E D I E C T I O N \033[0;30m')
    print('\t6 \033[7;37m E N S L W A T E R S \033[0;30m')
    print('\t5 \033[7;37m A R O T I A D C P M \033[0;30m')
    print('\t4 \033[7;37m L O A N C L A R E S \033[0;30m')
    print('\t3 \033[7;37m A S I I A W A L E R \033[0;30m')
    print('\t2 \033[7;37m E L D C T O P W L E \033[0;30m')
    print('\t1 \033[7;37m N E T F L I C S S E \033[0;30m')
    print('\t0 \033[7;37m M E A T O N E R S P \033[0;30m')
    time.sleep(2)
    # setting variable for input/answer
    sleep = input('\n\033[0;34mSLEEP: \033[0;30m')
    meal = input('\033[0;34mMEAL: \033[0;30m')
    water = input('\033[0;34mWATER: \033[0;30m')
    medication = input('\033[0;34mMEDICATION: \033[0;30m')
    # counter to check the final points accumulated
    initial = 4
    check = 4
    time.sleep(1)
    # to check for correct answer
    if sleep == '(8,1)(8,2)(8,3)(8,4)(8,5)':
        print("\033[1;32mYou found 'SLEEP' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'SLEEP' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)    
    if meal == '(0,7)(0,6)(0,5)(0,4)':
        print("\033[1;32mYou found 'MEAL' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'MEAL' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if water == '(4,6)(5,6)(6,6)(7,6)(8,6)':
        print("\033[1;32mYou found 'WATER' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'WATER' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if medication == '(0,0)(1,1)(2,2)(3,3)(4,4)(5,5)(6,6)(7,7)(8,8)(9,9)':
        print("\033[1;32mYou found 'MEDICATION' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'MEDICATION' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(2)
    #return counter
    return check, initial  # return amount of points deducted and the supposed amount of points to get

def ws2():
    # display question
    print('\n\n\033[0;34m################## Game Start! ##################\033[0;30m')
    time.sleep(1)
    print('__________________________________________________')
    print('\n The process before donating blood:-')
    print(' 1. Fill out a confidential medical \033[0;34mHISTORY\033[0;30m form.')
    print(' 2. Fill up the registration \033[0;34mFORM\033[0;30m.')
    print(' 3. Undergo a brief physical \033[0;34mEXAM\033[0;30m.')
    print(' 4. Have your \033[0;34mBLOOD\033[0;30m tested.')
    print(' 5. Undergo pre-donation \033[0;34mCOUNSELING\033[0;30m.')
    print('__________________________________________________')
    time.sleep(2)
    print('\n\t   0 1 2 3 4 5 6 7 8 9')
    print('\t9 \033[7;37m H I S C O R Y S I H \033[0;30m')
    print('\t8 \033[7;37m B P L O O D E D I T \033[0;30m')
    print('\t7 \033[7;37m C O U U S E L X N G \033[0;30m')
    print('\t6 \033[7;37m R X S N R O F X A M \033[0;30m')
    print('\t5 \033[7;37m O H I S Y O B B C M \033[0;30m')
    print('\t4 \033[7;37m F Y H E S T L R Y X \033[0;30m')
    print('\t3 \033[7;37m X M I L E S O U O C \033[0;30m')
    print('\t2 \033[7;37m A R H I S T O R Y D \033[0;30m')
    print('\t1 \033[7;37m M O C N X S D X Y O \033[0;30m')
    print('\t0 \033[7;37m A F X G O R M H L O \033[0;30m')
    time.sleep(2)
    # setting variable for input/answer
    history = input('\n\033[0;34mHISTORY: \033[0;30m')
    form = input('\033[0;34mFORM: \033[0;30m')
    exam = input('\033[0;34mEXAM: \033[0;30m')
    blood = input('\033[0;34mBLOOD: \033[0;30m')
    counseling = input('\033[0;34mCOUNSELING: \033[0;30m')
    # counter to check the final points accumulated
    initial = 5
    check = 5
    time.sleep(1)
    # to check for correct answer
    if history == '(2,2)(3,2)(4,2)(5,2)(6,2)(7,2)(8,2)':
        print("\033[1;32mYou found 'HISTORY' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'HISTORY' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)    
    if form == '(1,0)(1,1)(1,2)(1,3)':
        print("\033[1;32mYou found 'FORM' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'FORM' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if exam == '(6,8)(7,7)(8,6)(9,5)':
        print("\033[1;32mYou found 'EXAM' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'EXAM' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if blood == '(6,5)(6,4)(6,3)(6,2)(6,1)':
        print("\033[1;32mYou found 'BLOOD' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'BLOOD' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if counseling == '(3,9)(3,8)(3,7)(3,6)(3,5)(3,4)(3,3)(3,2)(3,1)(3,0)':
        print("\033[1;32mYou found 'COUNSELING' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'COUNSELING' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(2)
    return check, initial  # return amount of points deducted and the supposed amount of points to get

def ws3():
    # display question
    print('\n\n\033[0;34m################## Game Start! ##################\033[0;30m')
    time.sleep(1)
    print('____________________________________________________')
    print('\n What to do after donating blood:-')
    print(' 1. Eat light \033[0;34mSNACKS\033[0;30m and drink extra fluids.')
    print(' 2. Avoid \033[0;34mSTRENUOUS\033[0;30m physical activity for 24 hours.')
    print(' 3. Add \033[0;34mIRON\033[0;30m rich foods to your diet.')
    print(' 4. No alcoholic \033[0;34mDRINK\033[0;30m for the first few hours.')
    print(' 5. If feeling lightheaded, \033[0;34mLIE\033[0;30m down with feet up.')
    print('____________________________________________________')
    time.sleep(2)
    print('\n\t   0 1 2 3 4 5 6 7 8 9')
    print('\t9 \033[7;37m N O R J I N K S S I \033[0;30m')
    print('\t8 \033[7;37m A S E L D D I U N R \033[0;30m')
    print('\t7 \033[7;37m D R N I R K U O A U \033[0;30m')
    print('\t6 \033[7;37m B B U I I O O U G N \033[0;30m')
    print('\t5 \033[7;37m R O N K N I R N K L \033[0;30m')
    print('\t4 \033[7;37m I K A E G K B E S I \033[0;30m')
    print('\t3 \033[7;37m N R R O U N E R C E \033[0;30m')
    print('\t2 \033[7;37m K T O U O U N T R S \033[0;30m')
    print('\t1 \033[7;37m S O S N A C K S R O \033[0;30m')
    print('\t0 \033[7;37m F I L I F E I J I E \033[0;30m')
    time.sleep(2)
    # setting variable for input/answer
    snacks = input('\n\033[0;34mSNACKS: \033[0;30m')
    strenuous = input('\033[0;34mSTRENUOUS: \033[0;30m')
    iron = input('\033[0;34mIRON: \033[0;30m')
    drink = input('\033[0;34mDRINK: \033[0;30m')
    lie = input('\033[0;34mLIE: \033[0;30m')
    # counter to check the final points accumulated
    initial = 5
    check = 5
    time.sleep(1)
    # to check for correct answer
    if snacks == '(2,1)(3,1)(4,1)(5,1)(6,1)(7,1)':
        print("\033[1;32mYou found 'SNACKS' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'SNACKS' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)    
    if strenuous == '(7,1)(7,2)(7,3)(7,4)(7,5)(7,6)(7,7)(7,8)(7,9)':
        print("\033[1;32mYou found 'STRENUOUS' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'STRENUOUS' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if iron == '(0,4)(1,3)(2,2)(3,1)':
        print("\033[1;32mYou found 'IRON' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'IRON' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if drink == '(5,8)(4,7)(3,6)(2,5)(1,4)':
        print("\033[1;32mYou found 'DRINK' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'DRINK' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if lie == '(9,5)(9,4)(9,3)':
        print("\033[1;32mYou found 'LIE' right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get 'LIE' right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(2)
    return check, initial  # return amount of points deducted and the supposed amount of points to get

def ws4():
    # display question
    print('\n\n\033[0;34m################## Game Start! ##################\033[0;30m')
    time.sleep(1)
    print('____________________________________________________')
    print('\n\033[0;33mSpecial Question!\033[0;30m \nYou can choose your \033[0;34mown words!\033[0;30m')
    print('Please enter words with \033[0;34mno more than 10\033[0;30m letters.')
    print('____________________________________________________')
    # asking input for custom words and setting it to a variable
    word1 = input('\n\033[0;34mFirst\033[0;30m word: ').upper()
    num1 = len(word1)  # counting the number of letters in word1
    while num1 > 10 or num1 == 0:  # to check if the entered input does not meet stated rules
        print('\n\033[0;31mPlease enter words with no more than 10 letters.\033[0;30m')
        word1 = input('\n\033[0;34mFirst\033[0;30m word: ').upper()
        num1 = len(word1)
    word2 = input('\033[0;34mSecond\033[0;30m word: ').upper()
    num2 = len(word2)  # counting the number of letters in word2
    while num2 > 10 or num2 == 0:  # to check if the entered input does not meet stated rules
        print('\n\033[0;31mPlease enter words with no more than 10 letters.\033[0;30m')
        word2 = input('\033[0;34mSecond\033[0;30m word: ').upper()
        num2 = len(word2)
    word3 = input('\033[0;34mThird\033[0;30m word: ').upper()
    num3 = len(word3)  # counting the number of letters in word3
    while num3 > 10 or num3 == 0:  # to check if the entered input does not meet stated rules
        print('\n\033[0;31mPlease enter words with no more than 10 letters.\033[0;30m')
        word3 = input('\033[0;34mThird\033[0;30m word: ').upper()
        num3 = len(word3)
    word4 = input('\033[0;34mFourth\033[0;30m word: ').upper()
    num4 = len(word4)  # counting the number of letters in word4
    while num4 > 10 or num4 == 0:  # to check if the entered input does not meet stated rules
        print('\n\033[0;31mPlease enter words with no more than 10 letters.\033[0;30m')
        word4 = input('\033[0;34mFourth\033[0;30m word: ').upper()
        num4 = len(word4)
    # turning each letter from the entered words into a list of letters
    listWord1 = list(word1)
    listWord2 = list(word2)
    listWord3 = list(word3)
    listWord4 = list(word4)
    # compiling all letters into one main list
    lettersList = (listWord1 + listWord2 + listWord3 + listWord4)
    maxLetter = 10  # setting the number of maximum letters in one line in the table
    # a function to pick random letters from the main list and to decide how many letters needed
    def table(y):
        return ' '.join(random.choice(lettersList) for x in range(y))
    # function to arrange the letters for each word in a line correctly
    letters = lambda x : ' '.join(x)
    # the variables 'left1/2/3/4' are to determine the number of empty spaces left in the line where the entered words are placed
    left1 = maxLetter - num1
    left2 = maxLetter - num2
    left3 = maxLetter - num3
    left4 = maxLetter - num4
    # displaying the table of letters
    print('\n\t   0 1 2 3 4 5 6 7 8 9')
    print('\t9 \033[7;37m', table(maxLetter), '\033[0;30m')
    print('\t8 \033[7;37m', table(maxLetter), '\033[0;30m')
    print('\t7 \033[7;37m', letters(listWord3), table(left3), '\033[0;30m')
    print('\t6 \033[7;37m', table(maxLetter), '\033[0;30m')
    print('\t5 \033[7;37m', table(left1), letters(listWord1), '\033[0;30m')
    print('\t4 \033[7;37m', table(maxLetter), '\033[0;30m')
    print('\t3 \033[7;37m', table(maxLetter), '\033[0;30m')
    print('\t2 \033[7;37m', letters(listWord4), table(left4), '\033[0;30m')
    print('\t1 \033[7;37m', table(left2), letters(listWord2), '\033[0;30m')
    print('\t0 \033[7;37m', table(maxLetter), '\033[0;30m')
    time.sleep(2)
    # setting variable for input/answer
    print('\n\033[0;34m', word1, ': \033[0;30m')
    word1Ans = input()
    print('\n\033[0;34m', word2, ': \033[0;30m')
    word2Ans = input()
    print('\n\033[0;34m', word3, ': \033[0;30m')
    word3Ans = input()
    print('\n\033[0;34m', word4, ': \033[0;30m')
    word4Ans = input()
    # function to determine the answers for word1 and word2    
    num1 = 'num1'  # need to change the numbers into strings so that if the number of letters in both words are the same, the coordinates would still be different
    num2 = 'num2'  # need to change the numbers into strings so that if the number of letters in both words are the same, the coordinates would still be different
    def ans12(y,z):
        x = z  # setting the counter for when to stop printing and this is also the first coordinate
        finAns = []   # empty list to append the answers later
        while x < 10:  # loop will stop once x = 10
            if y == 'num1':
                line = '5'  # the second coordinate for word1
            elif y == 'num2':
                line = '1'  # the second coordinate for word2
            x = str(x)   # changing x to str to print
            answer = '(' + x + ',' + line + ')'   # setting the answer in the correct format into a variable
            x = int(x)   # changing x back to int to enable the relational operators
            x = x + 1   # increasing counter and the first coordinate
            finAns.append(answer)   # appending the answer into the list
        return finAns
    # function to determine the answers for word3 and word4
    num3 = 'num3'  # need to change the numbers into strings so that if the number of letters in both words are the same, the coordinates would still be different
    num4 = 'num4'  # need to change the numbers into strings so that if the number of letters in both words are the same, the coordinates would still be different
    def ans34(y,z):
        x = 0  # setting the first coordinate
        finAns = []   # empty list to append the answers later
        while z < 10:  # loop will stop once z = 10
            if y == 'num3':
                line = '7'  # the second coordinate for word3
            elif y == 'num4':
                line = '2'  # the second coordinate for word4
            x = str(x)   # changing x to str to print
            answer = '(' + x + ',' + line + ')'   # setting the answer in the correct format into a variable
            x = int(x)   # changing x back to int to enable the relational operators
            x = x + 1   # increasing the first coordinate
            z = z + 1   # # increasing counter
            finAns.append(answer)   # appending the answer into the list
        return finAns
    # changing each answer into str
    answer12Str = lambda x , y : ''.join(ans12(x,y))
    answer34Str = lambda x , y : ''.join(ans34(x,y))
    # counter to check the final points accumulated
    initial = 4
    check = 4
    time.sleep(1)
    # to check for correct answer
    if word1Ans == answer12Str(num1,left1):
        print("\033[1;32mYou found ", word1, " right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get ", word1, " right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)    
    if word2Ans == answer12Str(num2,left2):
        print("\033[1;32mYou found ", word2, " right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get ", word2, " right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if word3Ans == answer34Str(num3,left3):
        print("\033[1;32mYou found ", word3, " right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get ", word3, " right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(1)
    if word4Ans == answer34Str(num4,left4):
        print("\033[1;32mYou found ", word4, " right!\033[0;30m")
    else:
        print("\033[1;31mYou didn't get ", word4, " right.\033[0;30m")
        check = check - 1  # if user get wrong answer, minus 1 point
    time.sleep(2)
    return check, initial  # return amount of points deducted and the supposed amount of points to get

# to check if the points accumulated are enough to get hints
def reward(check, initial):
    time.sleep(2)
    print('\nYour final points are: \033[0;33m', check, '\033[0;30m')
    if check == initial:
        print('\n\033[0;33mCongratulations! You found all words correctly!')
        print('Here is a clue to help you answer the main question:\033[0;30m')
        print('\nHINT')
    else:
        print("\n\033[0;33mUnfortunately, you didn't find all words correctly.")
        print("You won't be getting any hints for now.\033[0;30m")



def execute():
    wsInstructions() # display instructions
    diffQs = [ws1, ws2, ws3, ws4] # putting the different possible questions in a list
    check, initial = random.choice(diffQs)() # choosing random questions from the list and setting the return value to variable 'check' and 'initial'
    reward(check, initial) # check points accumulated

    # word search game end