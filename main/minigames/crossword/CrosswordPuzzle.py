# crossword puzzle

import time
import random

#display instructions
def cpInstructions():
    block11 = '\033[7;37m 1.1  \033[0;30m'
    block12 = '\033[7;37m 1.2  \033[0;30m'
    block13 = '\033[7;37m 1.3  \033[0;30m'
    block14 = '\033[7;37m 1.4  \033[0;30m'
    block15 = '\033[7;37m 1.5  \033[0;30m'
    block16 = '\033[7;37m 1.6  \033[0;30m'
    block17 = '\033[7;37m 1.7  \033[0;30m'
    block18 = '\033[7;37m 1.8  \033[0;30m'
    block21 = '\033[7;37m 2.1  \033[0;30m'
    block22 = '\033[7;37m 2.2  \033[0;30m'
    block23 = '\033[7;37m 2.3  \033[0;30m'
    block24 = '\033[7;37m 2.4  \033[0;30m'
    block25 = '\033[7;37m 2.5  \033[0;30m'
    block26 = '\033[7;37m 2.6  \033[0;30m'
    block31 = '\033[7;37m 3.1  \033[0;30m'
    block32 = '\033[7;37m 3.2  \033[0;30m'
    block33 = '\033[7;37m 3.3  \033[0;30m'
    block34 = '\033[7;37m 3.4  \033[0;30m'
    block35 = '\033[7;37m 3.5  \033[0;30m'
    block36 = '\033[7;37m 3.6  \033[0;30m'
    block41 = '\033[7;37m 4.1  \033[0;30m'
    block42 = '\033[7;37m 4.2  \033[0;30m'
    block43 = '\033[7;37m 4.3  \033[0;30m'
    block44 = '\033[7;37m 4.4  \033[0;30m'
    block45 = '\033[7;37m 4.5  \033[0;30m'
    block46 = '\033[7;37m 4.6  \033[0;30m'
    space = '\033[7;40m      \033[0;30m'
    print('\033[1;34m********************************************************************')
    print('\t\t\t CROSSWORD PUZZLE')
    print('********************************************************************\033[0;30m')
    time.sleep(1)
    print('Here are the instructions:-')
    time.sleep(1)
    print('1. Fill in the white spaces by typing in your answer letter by letter.')
    time.sleep(2)
    print('2. The order in which space to fill in first follows the order from')
    print('   top to bottom, left to right.')
    time.sleep(2)
    print('3. Your answers should be based on the guides given.')
    time.sleep(2)
    print('4. If your answer consists of more than one word, write them without spaces.')
    time.sleep(2)
    print('5. You have 6 points. Each time you give a wrong answer, your points will be deducted.')
    print('   You need to have a minimum of 4 marks to get the hint.')
    time.sleep(2)
    print('6. Example:-')
    time.sleep(2)
    print('\n', space, space, space, space, block41, space, space, space)
    print('\n', space, space, block31, space, block42, space, space, space)
    print('\n', space, space, block32, space, block43, space, space, space)
    print('\n', block11, block12, block13, block14, block15, block16, block17, block18)
    print('\n', space, space, block34, space, block45, space, space, space)
    print('\n', space, space, block35, space, block46, space, space, space)
    print('\n', space, space, block36, space, space, space, space, space)
    print('\n', space, block21, block22, block23, block24, block25, block26, space)
    time.sleep(1)
    print('\n\033[4mHorizontal\033[0m')
    print('1. Apheresis donation collects ___ components of blood.')
    print('2. The amount of blood collected from each donor depends')
    print('   on their body ___.')
    time.sleep(1)
    print('\n\033[4mVertical\033[0m')
    print('3. The national ___ of blood donors in Malaysia is only')
    print('   2.5% of those who are eligible.')
    print("4. The ___'s blood supply needs our help.")
    time.sleep(1)
    print('\n\t1.1: S')
    print('\t1.2: P')
    print('\t1.3: E')
    print('\t1.4: C')
    print('\t1.5: I')
    print('\t1.6: F')
    print('\t1.7: I')
    print('\t1.8: C')
    time.sleep(1)
    print('\n\t2.1: W')
    print('\t2.2: E')
    print('\t2.3: I')
    print('\t2.4: G')
    print('\t2.5: H')
    print('\t2.6: T')
    time.sleep(1)
    print('\n\t3.1: A')
    print('\t3.2: V')
    print('\t3.3: E')
    print('\t3.4: R')
    print('\t3.5: A')
    print('\t3.6: G')
    print('\t3.7: E')
    time.sleep(1)
    print('\n\t4.1: N')
    print('\t4.2: A')
    print('\t4.3: T')
    print('\t4.4: I')
    print('\t4.5: O')
    print('\t4.6: N')
    time.sleep(2)
    print('\n\033[0;33m...Loading...\033[0;30m')
    time.sleep(3)

#function to determine whether player gets reward
def rewards(x):
    time.sleep(1)
    print('\n\033[0;33m...Loading...\033[0;30m')
    time.sleep(2)
    print('\nYour final points are: \033[0;33m', x, '\033[0;30m')
    if x >= 4:  #player will get reward if points are more than or equal to 4
        return True
    else:
        return False

def cp1(): #question 1
    #assigning each numbered blocks into their own variable
    block11 = '\033[7;37m 1.1  \033[0;30m'
    block12 = '\033[7;37m 1.2  \033[0;30m'
    block13 = '\033[7;37m 1.3  \033[0;30m'
    block14 = '\033[7;37m 1.4  \033[0;30m'
    block21 = '\033[7;37m 2.1  \033[0;30m'
    block22 = '\033[7;37m 2.2  \033[0;30m'
    block23 = '\033[7;37m 2.3  \033[0;30m'
    block24 = '\033[7;37m 2.4  \033[0;30m'
    block25 = '\033[7;37m 2.5  \033[0;30m'
    block26 = '\033[7;37m 2.6  \033[0;30m'
    block27 = '\033[7;37m 2.7  \033[0;30m'
    block28 = '\033[7;37m 2.8  \033[0;30m'
    block29 = '\033[7;37m 2.9  \033[0;30m'
    block210 = '\033[7;37m 2.10 \033[0;30m'
    block31 = '\033[7;37m 3.1  \033[0;30m'
    block32 = '\033[7;37m 3.2  \033[0;30m'
    block33 = '\033[7;37m 3.3  \033[0;30m'
    block34 = '\033[7;37m 3.4  \033[0;30m'
    block35 = '\033[7;37m 3.5  \033[0;30m'
    block36 = '\033[7;37m 3.6  \033[0;30m'
    block37 = '\033[7;37m 3.7  \033[0;30m'
    block41 = '\033[7;37m 4.1  \033[0;30m'
    block42 = '\033[7;37m 4.2  \033[0;30m'
    block43 = '\033[7;37m 4.3  \033[0;30m'
    block44 = '\033[7;37m 4.4  \033[0;30m'
    block45 = '\033[7;37m 4.5  \033[0;30m'
    block46 = '\033[7;37m 4.6  \033[0;30m'
    block47 = '\033[7;37m 4.7  \033[0;30m'
    block48 = '\033[7;37m 4.8  \033[0;30m'
    block49 = '\033[7;37m 4.9  \033[0;30m'
    block410 = '\033[7;37m 4.10 \033[0;30m'
    block411 = '\033[7;37m 4.11 \033[0;30m'
    block412 = '\033[7;37m 4.12 \033[0;30m'
    block413 = '\033[7;37m 4.13 \033[0;30m'
    block51 = '\033[7;37m 5.1  \033[0;30m'
    block52 = '\033[7;37m 5.2  \033[0;30m'
    block53 = '\033[7;37m 5.3  \033[0;30m'
    block61 = '\033[7;37m 6.1  \033[0;30m'
    block62 = '\033[7;37m 6.2  \033[0;30m'
    block63 = '\033[7;37m 6.3  \033[0;30m'
    block64 = '\033[7;37m 6.4  \033[0;30m'
    block65 = '\033[7;37m 6.5  \033[0;30m'
    block66 = '\033[7;37m 6.6  \033[0;30m'
    block67 = '\033[7;37m 6.7  \033[0;30m'
    space = '\033[7;40m      \033[0;30m'
    points = 6 #initial points are set to 6
    print('\n\033[0;34m################### GAME STARTS ###################\033[0;30m')
    time.sleep(1)
    #questions to guide player
    print('\n\033[4mHorizontal\033[0m')
    print('1. The Malaysian Ministry of Health has targeted to recruit at')
    print('   least ___ percent of Malaysian population to become blood donors.')
    print('2. There is no ___ for human blood.')
    print('3. Every two ___, someone needs blood.')
    time.sleep(2)
    print('\n\033[4mVertical\033[0m')
    print('4. Blood components cannot be ___ made.')
    print('5. Only ___ out of forty (40) Malaysians who are physically')
    print('   capable of donating blood do so.')
    print('6. Blood components have ___ shelf life.')
    time.sleep(1)
    print('\n\033[0;33m...Loading...\033[0;30m')
    time.sleep(2)
    #display the crossword puzzle blocks
    print('\n', space, space, space, space, space, space, space, space, block61, space, space)
    print('\n', space, space, space, space, block41, space, space, block11, block12, block13, block14)
    print('\n', space, space, space, space, block42, space, space, space, block63, space, space)
    print('\n', space, space, space, space, block43, space, space, space, block64, space, space)
    print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, space)
    print('\n', space, space, space, space, block45, space, space, space, block66, space, space)
    print('\n', space, space, space, space, block46, space, space, space, block67, space, space)
    print('\n', space, space, space, space, block47, space, space, space, space, space, space)
    print('\n', space, space, space, space, block48, space, block51, space, space, space, space)
    print('\n', space, space, block31, block32, block33, block34, block35, block36, block37, space, space)
    print('\n', space, space, space, space, block410, space, block53, space, space, space, space)
    print('\n', space, space, space, space, block411, space, space, space, space, space, space)
    print('\n', space, space, space, space, block412, space, space, space, space, space, space)
    print('\n', space, space, space, space, block413, space, space, space, space, space, space)
    #loop that will keep asking the player to give input if answer given is wrong
    while block11 == '\033[7;37m 1.1  \033[0;30m' or block12 == '\033[7;37m 1.2  \033[0;30m' or block13 == '\033[7;37m 1.3  \033[0;30m' or block14 == '\033[7;37m 1.4  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('1. The Malaysian Ministry of Health has targeted to recruit at')
        print('   least ___ percent of Malaysian population to become blood donors.')
        #assigning each input given to a variable and changing it to uppercase
        fiveF = input('\n\t1.1: ').upper()
        fiveI = input('\t1.2: ').upper()
        fiveV = input('\t1.3: ').upper()
        fiveE = input('\t1.4: ').upper()
        #if answer given is correct, the numbered blocks will change to blocks with the correct letters
        if fiveF == 'F':
            block11 = "\033[7;37m  F   \033[0;30m"
        if fiveI == 'I':
            block12 = "\033[7;37m  I   \033[0;30m"
        if fiveV == 'V':
            block13 = "\033[7;37m  V   \033[0;30m"
        if fiveE == 'E':
            block14 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, space, space, block41, space, space, block11, block12, block13, block14)
        print('\n', space, space, space, space, block42, space, space, space, block63, space, space)
        print('\n', space, space, space, space, block43, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, space)
        print('\n', space, space, space, space, block45, space, space, space, block66, space, space)
        print('\n', space, space, space, space, block46, space, space, space, block67, space, space)
        print('\n', space, space, space, space, block47, space, space, space, space, space, space)
        print('\n', space, space, space, space, block48, space, block51, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, block35, block36, block37, space, space)
        print('\n', space, space, space, space, block410, space, block53, space, space, space, space)
        print('\n', space, space, space, space, block411, space, space, space, space, space, space)
        print('\n', space, space, space, space, block412, space, space, space, space, space, space)
        print('\n', space, space, space, space, block413, space, space, space, space, space, space)
        #if answer given is wrong, the numbered blocks will not change and a message will be displayed, points will be deducted
        if block11 == '\033[7;37m 1.1  \033[0;30m' :
            print('\n\033[0;31mYou got 1.1 wrong.\033[0;30m')
            points = points - (1/4)
        if block12 == '\033[7;37m 1.2  \033[0;30m' :
            print('\n\033[0;31mYou got 1.2 wrong.\033[0;30m')
            points = points - (1/4)
        if block13 == '\033[7;37m 1.3  \033[0;30m' :
            print('\n\033[0;31mYou got 1.3 wrong.\033[0;30m')
            points = points - (1/4)
        if block14 == '\033[7;37m 1.4  \033[0;30m' :
            print('\n\033[0;31mYou got 1.4 wrong.\033[0;30m')
            points = points - (1/4)

    while block21 == '\033[7;37m 2.1  \033[0;30m' or block22 == '\033[7;37m 2.2  \033[0;30m' or block23 == '\033[7;37m 2.3  \033[0;30m' or block24 == '\033[7;37m 2.4  \033[0;30m' or block25 == '\033[7;37m 2.5  \033[0;30m' or block26 == '\033[7;37m 2.6  \033[0;30m' or block27 == '\033[7;37m 2.7  \033[0;30m' or block28 == '\033[7;37m 2.8  \033[0;30m' or block29 == '\033[7;37m 2.9  \033[0;30m' or block210 == '\033[7;37m 2.10  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('2. There is no ___ for human blood.')
        substituteS1 = input('\n\t2.1: ').upper()
        substituteU1 = input('\t2.2: ').upper()
        substituteB = input('\t2.3: ').upper()
        substituteS2 = input('\t2.4: ').upper()
        substituteT1 = input('\t2.5: ').upper()
        substituteI = input('\t2.6: ').upper()
        substituteT2 = input('\t2.7: ').upper()
        substituteU2 = input('\t2.8: ').upper()
        substituteT3 = input('\t2.9: ').upper()
        substituteE = input('\t2.10: ').upper()
        if substituteS1 == 'S':
            block21 = "\033[7;37m  S   \033[0;30m"
        if substituteU1 == 'U':
            block22 = "\033[7;37m  U   \033[0;30m"
        if substituteB == 'B':
            block23 = "\033[7;37m  B   \033[0;30m"
        if substituteS2 == 'S':
            block24 = "\033[7;37m  S   \033[0;30m"
        if substituteT1 == 'T':
            block25 = "\033[7;37m  T   \033[0;30m"
        if substituteI == 'I':
            block26 = "\033[7;37m  I   \033[0;30m"
        if substituteT2 == 'T':
            block27 = "\033[7;37m  T   \033[0;30m"
        if substituteU2 == 'U':
            block28 = "\033[7;37m  U   \033[0;30m"
        if substituteT3 == 'T':
            block29 = "\033[7;37m  T   \033[0;30m"
        if substituteE == 'E':
            block210 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, space, space, block41, space, space, block11, block12, block13, block14)
        print('\n', space, space, space, space, block42, space, space, space, block63, space, space)
        print('\n', space, space, space, space, block43, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, space)
        print('\n', space, space, space, space, block45, space, space, space, block66, space, space)
        print('\n', space, space, space, space, block46, space, space, space, block67, space, space)
        print('\n', space, space, space, space, block47, space, space, space, space, space, space)
        print('\n', space, space, space, space, block48, space, block51, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, block35, block36, block37, space, space)
        print('\n', space, space, space, space, block410, space, block53, space, space, space, space)
        print('\n', space, space, space, space, block411, space, space, space, space, space, space)
        print('\n', space, space, space, space, block412, space, space, space, space, space, space)
        print('\n', space, space, space, space, block413, space, space, space, space, space, space)
        if block21 == '\033[7;37m 2.1  \033[0;30m' :
            print('\n\033[0;31mYou got 2.1 wrong.\033[0;30m')
            points = points - (1/10)
        if block22 == '\033[7;37m 2.2  \033[0;30m' :
            print('\n\033[0;31mYou got 2.2 wrong.\033[0;30m')
            points = points - (1/10)
        if block23 == '\033[7;37m 2.3  \033[0;30m' :
            print('\n\033[0;31mYou got 2.3 wrong.\033[0;30m')
            points = points - (1/10)
        if block24 == '\033[7;37m 2.4  \033[0;30m' :
            print('\n\033[0;31mYou got 2.4 wrong.\033[0;30m')
            points = points - (1/10)
        if block25 == '\033[7;37m 2.5  \033[0;30m' :
            print('\n\033[0;31mYou got 2.5 wrong.\033[0;30m')
            points = points - (1/10)
        if block26 == '\033[7;37m 2.6  \033[0;30m' :
            print('\n\033[0;31mYou got 2.6 wrong.\033[0;30m')
            points = points - (1/10)
        if block27 == '\033[7;37m 2.7  \033[0;30m' :
            print('\n\033[0;31mYou got 2.7 wrong.\033[0;30m')
            points = points - (1/10)
        if block28 == '\033[7;37m 2.8  \033[0;30m' :
            print('\n\033[0;31mYou got 2.8 wrong.\033[0;30m')
            points = points - (1/10)
        if block29 == '\033[7;37m 2.9  \033[0;30m' :
            print('\n\033[0;31mYou got 2.9 wrong.\033[0;30m')
            points = points - (1/10)
        if block210 == '\033[7;37m 2.10  \033[0;30m' :
            print('\n\033[0;31mYou got 2.10 wrong.\033[0;30m')
            points = points - (1/10)

    while block31 == '\033[7;37m 3.1  \033[0;30m' or block32 == '\033[7;37m 3.2  \033[0;30m' or block33 == '\033[7;37m 3.3  \033[0;30m' or block34 == '\033[7;37m 3.4  \033[0;30m' or block35 == '\033[7;37m 3.5  \033[0;30m' or block36 == '\033[7;37m 3.6  \033[0;30m' or block37 == '\033[7;37m 3.7  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('3. Every two ___, someone needs blood.')
        secondsS1 = input('\n\t3.1: ').upper()
        secondsE = input('\t3.2: ').upper()
        secondsC = input('\t3.3: ').upper()
        secondsO = input('\t3.4: ').upper()
        secondsN = input('\t3.5: ').upper()
        secondsD = input('\t3.6: ').upper()
        secondsS2 = input('\t3.7: ').upper()
        if secondsS1 == 'S':
            block31 = "\033[7;37m  S   \033[0;30m"
        if secondsE == 'E':
            block32 = "\033[7;37m  E   \033[0;30m"
        if secondsC == 'C':
            block33 = "\033[7;37m  C   \033[0;30m"
        if secondsO == 'O':
            block34 = "\033[7;37m  O   \033[0;30m"
        if secondsN == 'N':
            block35 = "\033[7;37m  N   \033[0;30m"
        if secondsD == 'D':
            block36 = "\033[7;37m  D   \033[0;30m"
        if secondsS2 == 'S':
            block37 = "\033[7;37m  S   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, space, space, block41, space, space, block11, block12, block13, block14)
        print('\n', space, space, space, space, block42, space, space, space, block63, space, space)
        print('\n', space, space, space, space, block43, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, space)
        print('\n', space, space, space, space, block45, space, space, space, block66, space, space)
        print('\n', space, space, space, space, block46, space, space, space, block67, space, space)
        print('\n', space, space, space, space, block47, space, space, space, space, space, space)
        print('\n', space, space, space, space, block48, space, block51, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, block35, block36, block37, space, space)
        print('\n', space, space, space, space, block410, space, block53, space, space, space, space)
        print('\n', space, space, space, space, block411, space, space, space, space, space, space)
        print('\n', space, space, space, space, block412, space, space, space, space, space, space)
        print('\n', space, space, space, space, block413, space, space, space, space, space, space)
        if block31 == '\033[7;37m 3.1  \033[0;30m' :
            print('\n\033[0;31mYou got 3.1 wrong.\033[0;30m')
            points = points - (1/7)
        if block32 == '\033[7;37m 3.2  \033[0;30m' :
            print('\n\033[0;31mYou got 3.2 wrong.\033[0;30m')
            points = points - (1/7)
        if block33 == '\033[7;37m 3.3  \033[0;30m' :
            print('\n\033[0;31mYou got 3.3 wrong.\033[0;30m')
            points = points - (1/7)
        if block34 == '\033[7;37m 3.4  \033[0;30m' :
            print('\n\033[0;31mYou got 3.4 wrong.\033[0;30m')
            points = points - (1/7)
        if block35 == '\033[7;37m 3.5  \033[0;30m' :
            print('\n\033[0;31mYou got 3.5 wrong.\033[0;30m')
            points = points - (1/7)
        if block36 == '\033[7;37m 3.6  \033[0;30m' :
            print('\n\033[0;31mYou got 3.6 wrong.\033[0;30m')
            points = points - (1/7)
        if block37 == '\033[7;37m 3.7  \033[0;30m' :
            print('\n\033[0;31mYou got 3.7 wrong.\033[0;30m')
            points = points - (1/7)

    while block41 == '\033[7;37m 4.1  \033[0;30m' or block42 == '\033[7;37m 4.2  \033[0;30m' or block43 == '\033[7;37m 4.3  \033[0;30m' or block44 == '\033[7;37m 4.4  \033[0;30m' or block45 == '\033[7;37m 4.5  \033[0;30m' or block46 == '\033[7;37m 4.6  \033[0;30m' or block47 == '\033[7;37m 4.7  \033[0;30m' or block48 == '\033[7;37m 4.8  \033[0;30m' or block49 == '\033[7;37m 4.9  \033[0;30m' or block410 == '\033[7;37m 4.10  \033[0;30m' or block411 == '\033[7;37m 4.11  \033[0;30m' or block412 == '\033[7;37m 4.12  \033[0;30m' or block413 == '\033[7;37m 4.13  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('4. Blood components cannot be ___ made.')
        syntheticallyS = input('\n\t4.1: ').upper()
        syntheticallyY1 = input('\t4.2: ').upper()
        syntheticallyN = input('\t4.3: ').upper()
        syntheticallyT1 = input('\t4.4: ').upper()
        syntheticallyH = input('\t4.5: ').upper()
        syntheticallyE = input('\t4.6: ').upper()
        syntheticallyT2 = input('\t4.7: ').upper()
        syntheticallyI = input('\t4.8: ').upper()
        syntheticallyC = input('\t4.9: ').upper()
        syntheticallyA = input('\t4.10: ').upper()
        syntheticallyL1 = input('\t4.11: ').upper()
        syntheticallyL2 = input('\t4.12: ').upper()
        syntheticallyY2 = input('\t4.13: ').upper()
        if syntheticallyS == 'S':
            block41 = "\033[7;37m  S   \033[0;30m"
        if syntheticallyY1 == 'Y':
            block42 = "\033[7;37m  Y   \033[0;30m"
        if syntheticallyN == 'N':
            block43 = "\033[7;37m  N   \033[0;30m"
        if syntheticallyT1 == 'T':
            block44 = "\033[7;37m  T   \033[0;30m"
        if syntheticallyH == 'H':
            block45 = "\033[7;37m  H   \033[0;30m"
        if syntheticallyE == 'E':
            block46 = "\033[7;37m  E   \033[0;30m"
        if syntheticallyT2 == 'T':
            block47 = "\033[7;37m  T   \033[0;30m"
        if syntheticallyI == 'I':
            block48 = "\033[7;37m  I   \033[0;30m"
        if syntheticallyC == 'C':
            block49 = "\033[7;37m  C   \033[0;30m"
        if syntheticallyA == 'A':
            block410 = "\033[7;37m  A   \033[0;30m"
        if syntheticallyL1 == 'L':
            block411 = "\033[7;37m  L   \033[0;30m"
        if syntheticallyL2 == 'L':
            block412 = "\033[7;37m  L   \033[0;30m"
        if syntheticallyY2 == 'Y':
            block413 = "\033[7;37m  Y   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, space, space, block41, space, space, block11, block12, block13, block14)
        print('\n', space, space, space, space, block42, space, space, space, block63, space, space)
        print('\n', space, space, space, space, block43, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, space)
        print('\n', space, space, space, space, block45, space, space, space, block66, space, space)
        print('\n', space, space, space, space, block46, space, space, space, block67, space, space)
        print('\n', space, space, space, space, block47, space, space, space, space, space, space)
        print('\n', space, space, space, space, block48, space, block51, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, block35, block36, block37, space, space)
        print('\n', space, space, space, space, block410, space, block53, space, space, space, space)
        print('\n', space, space, space, space, block411, space, space, space, space, space, space)
        print('\n', space, space, space, space, block412, space, space, space, space, space, space)
        print('\n', space, space, space, space, block413, space, space, space, space, space, space)
        if block41 == '\033[7;37m 4.1  \033[0;30m' :
            print('\n\033[0;31mYou got 4.1 wrong.\033[0;30m')
            points = points - (1/13)
        if block42 == '\033[7;37m 4.2  \033[0;30m' :
            print('\n\033[0;31mYou got 4.2 wrong.\033[0;30m')
            points = points - (1/13)
        if block43 == '\033[7;37m 4.3  \033[0;30m' :
            print('\n\033[0;31mYou got 4.3 wrong.\033[0;30m')
            points = points - (1/13)
        if block44 == '\033[7;37m 4.4  \033[0;30m' :
            print('\n\033[0;31mYou got 4.4 wrong.\033[0;30m')
            points = points - (1/13)
        if block45 == '\033[7;37m 4.5  \033[0;30m' :
            print('\n\033[0;31mYou got 4.5 wrong.\033[0;30m')
            points = points - (1/13)
        if block46 == '\033[7;37m 4.6  \033[0;30m' :
            print('\n\033[0;31mYou got 4.6 wrong.\033[0;30m')
            points = points - (1/13)
        if block47 == '\033[7;37m 4.7  \033[0;30m' :
            print('\n\033[0;31mYou got 4.7 wrong.\033[0;30m')
            points = points - (1/13)
        if block48 == '\033[7;37m 4.8  \033[0;30m' :
            print('\n\033[0;31mYou got 4.8 wrong.\033[0;30m')
            points = points - (1/13)
        if block49 == '\033[7;37m 4.9  \033[0;30m' :
            print('\n\033[0;31mYou got 4.9 wrong.\033[0;30m')
            points = points - (1/13)
        if block410 == '\033[7;37m 4.10  \033[0;30m' :
            print('\n\033[0;31mYou got 4.10 wrong.\033[0;30m')
            points = points - (1/13)
        if block411 == '\033[7;37m 4.11  \033[0;30m' :
            print('\n\033[0;31mYou got 4.11 wrong.\033[0;30m')
            points = points - (1/13)
        if block412 == '\033[7;37m 4.12  \033[0;30m' :
            print('\n\033[0;31mYou got 4.12 wrong.\033[0;30m')
            points = points - (1/13)
        if block413 == '\033[7;37m 4.13  \033[0;30m' :
            print('\n\033[0;31mYou got 4.13 wrong.\033[0;30m')
            points = points - (1/13)

    while block51 == '\033[7;37m 5.1  \033[0;30m' or block52 == '\033[7;37m 5.2  \033[0;30m' or block53 == '\033[7;37m 5.3  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('5. Only ___ out of forty (40) Malaysians who are physically')
        print('   capable of donating blood do so.')
        oneO = input('\n\t5.1: ').upper()
        oneN = input('\t5.2: ').upper()
        oneE = input('\t5.3: ').upper()
        if oneO == 'O':
            block51 = "\033[7;37m  O   \033[0;30m"
        if oneN == 'N':
            block52 = "\033[7;37m  N   \033[0;30m"
        if oneE == 'E':
            block53 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, space, space, block41, space, space, block11, block12, block13, block14)
        print('\n', space, space, space, space, block42, space, space, space, block63, space, space)
        print('\n', space, space, space, space, block43, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, space)
        print('\n', space, space, space, space, block45, space, space, space, block66, space, space)
        print('\n', space, space, space, space, block46, space, space, space, block67, space, space)
        print('\n', space, space, space, space, block47, space, space, space, space, space, space)
        print('\n', space, space, space, space, block48, space, block51, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, block35, block36, block37, space, space)
        print('\n', space, space, space, space, block410, space, block53, space, space, space, space)
        print('\n', space, space, space, space, block411, space, space, space, space, space, space)
        print('\n', space, space, space, space, block412, space, space, space, space, space, space)
        print('\n', space, space, space, space, block413, space, space, space, space, space, space)
        if block51 == '\033[7;37m 5.1  \033[0;30m' :
            print('\n\033[0;31mYou got 5.1 wrong.\033[0;30m')
            points = points - (1/3)
        if block52 == '\033[7;37m 5.2  \033[0;30m' :
            print('\n\033[0;31mYou got 5.2 wrong.\033[0;30m')
            points = points - (1/3)
        if block53 == '\033[7;37m 5.3  \033[0;30m' :
            print('\n\033[0;31mYou got 5.3 wrong.\033[0;30m')
            points = points - (1/3)

    while block61 == '\033[7;37m 6.1  \033[0;30m' or block62 == '\033[7;37m 6.2  \033[0;30m' or block63 == '\033[7;37m 6.3  \033[0;30m' or block64 == '\033[7;37m 6.4  \033[0;30m' or block65 == '\033[7;37m 6.5  \033[0;30m' or block66 == '\033[7;37m 6.6  \033[0;30m' or block67 == '\033[7;37m 6.7  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('6. Blood components have ___ shelf life.')
        limitedL = input('\n\t6.1: ').upper()
        limitedI1 = input('\t6.2: ').upper()
        limitedM = input('\t6.3: ').upper()
        limitedI2 = input('\t6.4: ').upper()
        limitedT = input('\t6.5: ').upper()
        limitedE = input('\t6.6: ').upper()
        limitedD = input('\t6.7: ').upper()
        if limitedL == 'L':
            block61 = "\033[7;37m  L   \033[0;30m"
        if limitedI1 == 'I':
            block62 = "\033[7;37m  I   \033[0;30m"
        if limitedM == 'M':
            block63 = "\033[7;37m  M   \033[0;30m"
        if limitedI2 == 'I':
            block64 = "\033[7;37m  I   \033[0;30m"
        if limitedT == 'T':
            block65 = "\033[7;37m  T   \033[0;30m"
        if limitedE == 'E':
            block66 = "\033[7;37m  E   \033[0;30m"
        if limitedD == 'D':
            block67 = "\033[7;37m  D   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, space, space, block41, space, space, block11, block12, block13, block14)
        print('\n', space, space, space, space, block42, space, space, space, block63, space, space)
        print('\n', space, space, space, space, block43, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, space)
        print('\n', space, space, space, space, block45, space, space, space, block66, space, space)
        print('\n', space, space, space, space, block46, space, space, space, block67, space, space)
        print('\n', space, space, space, space, block47, space, space, space, space, space, space)
        print('\n', space, space, space, space, block48, space, block51, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, block35, block36, block37, space, space)
        print('\n', space, space, space, space, block410, space, block53, space, space, space, space)
        print('\n', space, space, space, space, block411, space, space, space, space, space, space)
        print('\n', space, space, space, space, block412, space, space, space, space, space, space)
        print('\n', space, space, space, space, block413, space, space, space, space, space, space)
        if block61 == '\033[7;37m 6.1  \033[0;30m' :
            print('\n\033[0;31mYou got 6.1 wrong.\033[0;30m')
            points = points - (1/7)
        if block62 == '\033[7;37m 6.2  \033[0;30m' :
            print('\n\033[0;31mYou got 6.2 wrong.\033[0;30m')
            points = points - (1/7)
        if block63 == '\033[7;37m 6.3  \033[0;30m' :
            print('\n\033[0;31mYou got 6.3 wrong.\033[0;30m')
            points = points - (1/7)
        if block64 == '\033[7;37m 6.4  \033[0;30m' :
            print('\n\033[0;31mYou got 6.4 wrong.\033[0;30m')
            points = points - (1/7)
        if block65 == '\033[7;37m 6.5  \033[0;30m' :
            print('\n\033[0;31mYou got 6.5 wrong.\033[0;30m')
            points = points - (1/7)
        if block66 == '\033[7;37m 6.6  \033[0;30m' :
            print('\n\033[0;31mYou got 6.6 wrong.\033[0;30m')
            points = points - (1/7)
        if block67 == '\033[7;37m 6.7  \033[0;30m' :
            print('\n\033[0;31mYou got 6.7 wrong.\033[0;30m')
            points = points - (1/7)
    time.sleep(2)
    rewards(points)

def cp2(): #question 2
    block11 = '\033[7;37m 1.1  \033[0;30m'
    block12 = '\033[7;37m 1.2  \033[0;30m'
    block13 = '\033[7;37m 1.3  \033[0;30m'
    block14 = '\033[7;37m 1.4  \033[0;30m'
    block15 = '\033[7;37m 1.5  \033[0;30m'
    block16 = '\033[7;37m 1.6  \033[0;30m'
    block17 = '\033[7;37m 1.7  \033[0;30m'
    block18 = '\033[7;37m 1.8  \033[0;30m'
    block21 = '\033[7;37m 2.1  \033[0;30m'
    block22 = '\033[7;37m 2.2  \033[0;30m'
    block23 = '\033[7;37m 2.3  \033[0;30m'
    block24 = '\033[7;37m 2.4  \033[0;30m'
    block25 = '\033[7;37m 2.5  \033[0;30m'
    block26 = '\033[7;37m 2.6  \033[0;30m'
    block27 = '\033[7;37m 2.7  \033[0;30m'
    block31 = '\033[7;37m 3.1  \033[0;30m'
    block32 = '\033[7;37m 3.2  \033[0;30m'
    block33 = '\033[7;37m 3.3  \033[0;30m'
    block34 = '\033[7;37m 3.4  \033[0;30m'
    block41 = '\033[7;37m 4.1  \033[0;30m'
    block42 = '\033[7;37m 4.2  \033[0;30m'
    block43 = '\033[7;37m 4.3  \033[0;30m'
    block44 = '\033[7;37m 4.4  \033[0;30m'
    block45 = '\033[7;37m 4.5  \033[0;30m'
    block51 = '\033[7;37m 5.1  \033[0;30m'
    block52 = '\033[7;37m 5.2  \033[0;30m'
    block53 = '\033[7;37m 5.3  \033[0;30m'
    block54 = '\033[7;37m 5.4  \033[0;30m'
    block55 = '\033[7;37m 5.5  \033[0;30m'
    block61 = '\033[7;37m 6.1  \033[0;30m'
    block62 = '\033[7;37m 6.2  \033[0;30m'
    block63 = '\033[7;37m 6.3  \033[0;30m'
    block64 = '\033[7;37m 6.4  \033[0;30m'
    block65 = '\033[7;37m 6.5  \033[0;30m'
    block66 = '\033[7;37m 6.6  \033[0;30m'
    block67 = '\033[7;37m 6.7  \033[0;30m'
    space = '\033[7;40m      \033[0;30m'
    points = 6
    print('\n\033[0;34m################### GAME STARTS ###################\033[0;30m')
    time.sleep(1)
    print('\n\033[4mHorizontal\033[0m')
    print('1. According to Pusat Darah Negara, there is a shortage in blood')
    print('   supplies for the B and O ___ blood types.')
    print('2. Your body will ___ the fluids donated.')
    print('3. Most healthy adults can donate about ___ a liter safely.')
    time.sleep(2)
    print('\n\033[4mVertical\033[0m')
    print('4. Apheresis donation can be done more frequently, which is every')
    print('   two ___.')
    print('5. Whole blood donors may donate as frequently as every ___ months.')
    print('6. Donating blood is safe; ___, disposable equipment is used')
    print('   for each donor.')
    time.sleep(1)
    print('\n\033[0;33m...Loading...\033[0;30m')
    time.sleep(2)
    print('\n', space, block41, space, space, space, space, space, space, space, space, space)
    print('\n', space, block42, space, space, block61, space, space, space, space, space, space)
    print('\n', block11, block12, block13, block14, block15, block16, block17, block18, space, space, space)
    print('\n', space, block44, space, space, block63, space, space, space, space, space, space)
    print('\n', space, block45, space, space, block21, block22, block23, block24, block25, block26, block27)
    print('\n', space, space, block51, space, block65, space, space, space, space, space, space)
    print('\n', space, space, block31, block32, block33, block34, space, space, space, space, space)
    print('\n', space, space, block53, space, block67, space, space, space, space, space, space)
    print('\n', space, space, block54, space, space, space, space, space, space, space, space)
    print('\n', space, space, block55, space, space, space, space, space, space, space, space)

    while block11 == '\033[7;37m 1.1  \033[0;30m' or block12 == '\033[7;37m 1.2  \033[0;30m' or block13 == '\033[7;37m 1.3  \033[0;30m' or block14 == '\033[7;37m 1.4  \033[0;30m' or block15 == '\033[7;37m 1.5  \033[0;30m' or block16 == '\033[7;37m 1.6  \033[0;30m' or block17 == '\033[7;37m 1.7  \033[0;30m' or block18 == '\033[7;37m 1.8  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('1. According to Pusat Darah Negara, there is a shortage in blood')
        print('   supplies for the B and O ___ blood types.')
        negativeN = input('\n\t1.1: ').upper()
        negativeE1 = input('\t1.2: ').upper()
        negativeG = input('\t1.3: ').upper()
        negativeA = input('\t1.4: ').upper()
        negativeT = input('\t1.5: ').upper()
        negativeI = input('\t1.6: ').upper()
        negativeV = input('\t1.7: ').upper()
        negativeE2 = input('\t1.8: ').upper()
        if negativeN == 'N':
            block11 = "\033[7;37m  N   \033[0;30m"
        if negativeE1 == 'E':
            block12 = "\033[7;37m  E   \033[0;30m"
        if negativeG == 'G':
            block13 = "\033[7;37m  G   \033[0;30m"
        if negativeA == 'A':
            block14 = "\033[7;37m  A   \033[0;30m"
        if negativeT == 'T':
            block15 = "\033[7;37m  T   \033[0;30m"
        if negativeI == 'I':
            block16 = "\033[7;37m  I   \033[0;30m"
        if negativeV == 'V':
            block17 = "\033[7;37m  V   \033[0;30m"
        if negativeE2 == 'E':
            block18 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, block41, space, space, space, space, space, space, space, space, space)
        print('\n', space, block42, space, space, block61, space, space, space, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, space, space, space)
        print('\n', space, block44, space, space, block63, space, space, space, space, space, space)
        print('\n', space, block45, space, space, block21, block22, block23, block24, block25, block26, block27)
        print('\n', space, space, block51, space, block65, space, space, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, space, space, space, space, space)
        print('\n', space, space, block53, space, block67, space, space, space, space, space, space)
        print('\n', space, space, block54, space, space, space, space, space, space, space, space)
        print('\n', space, space, block55, space, space, space, space, space, space, space, space)
        if block11 == '\033[7;37m 1.1  \033[0;30m' :
            print('\n\033[0;31mYou got 1.1 wrong.\033[0;30m')
            points = points - (1/8)
        if block12 == '\033[7;37m 1.2  \033[0;30m' :
            print('\n\033[0;31mYou got 1.2 wrong.\033[0;30m')
            points = points - (1/8)
        if block13 == '\033[7;37m 1.3  \033[0;30m' :
            print('\n\033[0;31mYou got 1.3 wrong.\033[0;30m')
            points = points - (1/8)
        if block14 == '\033[7;37m 1.4  \033[0;30m' :
            print('\n\033[0;31mYou got 1.4 wrong.\033[0;30m')
            points = points - (1/8)
        if block15 == '\033[7;37m 1.5  \033[0;30m' :
            print('\n\033[0;31mYou got 1.5 wrong.\033[0;30m')
            points = points - (1/8)
        if block16 == '\033[7;37m 1.6  \033[0;30m' :
            print('\n\033[0;31mYou got 1.6 wrong.\033[0;30m')
            points = points - (1/8)
        if block17 == '\033[7;37m 1.7  \033[0;30m' :
            print('\n\033[0;31mYou got 1.7 wrong.\033[0;30m')
            points = points - (1/8)
        if block18 == '\033[7;37m 1.8  \033[0;30m' :
            print('\n\033[0;31mYou got 1.8 wrong.\033[0;30m')
            points = points - (1/8)

    while block21 == '\033[7;37m 2.1  \033[0;30m' or block22 == '\033[7;37m 2.2  \033[0;30m' or block23 == '\033[7;37m 2.3  \033[0;30m' or block24 == '\033[7;37m 2.4  \033[0;30m' or block25 == '\033[7;37m 2.5  \033[0;30m' or block26 == '\033[7;37m 2.6  \033[0;30m' or block27 == '\033[7;37m 2.7  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('2. Your body will ___ the fluids donated.')
        replaceR = input('\n\t2.1: ').upper()
        replaceE1 = input('\t2.2: ').upper()
        replaceP = input('\t2.3: ').upper()
        replaceL = input('\t2.4: ').upper()
        replaceA = input('\t2.5: ').upper()
        replaceC = input('\t2.6: ').upper()
        replaceE2 = input('\t2.7: ').upper()
        if replaceR == 'R':
            block21 = "\033[7;37m  R   \033[0;30m"
        if replaceE1 == 'E':
            block22 = "\033[7;37m  E   \033[0;30m"
        if replaceP == 'P':
            block23 = "\033[7;37m  P   \033[0;30m"
        if replaceL == 'L':
            block24 = "\033[7;37m  L   \033[0;30m"
        if replaceA == 'A':
            block25 = "\033[7;37m  A   \033[0;30m"
        if replaceC == 'C':
            block26 = "\033[7;37m  C   \033[0;30m"
        if replaceE2 == 'E':
            block27 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, block41, space, space, space, space, space, space, space, space, space)
        print('\n', space, block42, space, space, block61, space, space, space, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, space, space, space)
        print('\n', space, block44, space, space, block63, space, space, space, space, space, space)
        print('\n', space, block45, space, space, block21, block22, block23, block24, block25, block26, block27)
        print('\n', space, space, block51, space, block65, space, space, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, space, space, space, space, space)
        print('\n', space, space, block53, space, block67, space, space, space, space, space, space)
        print('\n', space, space, block54, space, space, space, space, space, space, space, space)
        print('\n', space, space, block55, space, space, space, space, space, space, space, space)
        if block21 == '\033[7;37m 2.1  \033[0;30m' :
            print('\n\033[0;31mYou got 2.1 wrong.\033[0;30m')
            points = points - (1/7)
        if block22 == '\033[7;37m 2.2  \033[0;30m' :
            print('\n\033[0;31mYou got 2.2 wrong.\033[0;30m')
            points = points - (1/7)
        if block23 == '\033[7;37m 2.3  \033[0;30m' :
            print('\n\033[0;31mYou got 2.3 wrong.\033[0;30m')
            points = points - (1/7)
        if block24 == '\033[7;37m 2.4  \033[0;30m' :
            print('\n\033[0;31mYou got 2.4 wrong.\033[0;30m')
            points = points - (1/7)
        if block25 == '\033[7;37m 2.5  \033[0;30m' :
            print('\n\033[0;31mYou got 2.5 wrong.\033[0;30m')
            points = points - (1/7)
        if block26 == '\033[7;37m 2.6  \033[0;30m' :
            print('\n\033[0;31mYou got 2.6 wrong.\033[0;30m')
            points = points - (1/7)
        if block27 == '\033[7;37m 2.7  \033[0;30m' :
            print('\n\033[0;31mYou got 2.7 wrong.\033[0;30m')
            points = points - (1/7)

    while block31 == '\033[7;37m 3.1  \033[0;30m' or block32 == '\033[7;37m 3.2  \033[0;30m' or block33 == '\033[7;37m 3.3  \033[0;30m' or block34 == '\033[7;37m 3.4  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('3. Most healthy adults can donate about ___ a liter safely.')
        halfH = input('\n\t3.1: ').upper()
        halfA = input('\t3.2: ').upper()
        halfL = input('\t3.3: ').upper()
        halfF = input('\t3.4: ').upper()
        if halfH == 'H':
            block31 = "\033[7;37m  H   \033[0;30m"
        if halfA == 'A':
            block32 = "\033[7;37m  A   \033[0;30m"
        if halfL == 'L':
            block33 = "\033[7;37m  L   \033[0;30m"
        if halfF == 'F':
            block34 = "\033[7;37m  F   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, block41, space, space, space, space, space, space, space, space, space)
        print('\n', space, block42, space, space, block61, space, space, space, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, space, space, space)
        print('\n', space, block44, space, space, block63, space, space, space, space, space, space)
        print('\n', space, block45, space, space, block21, block22, block23, block24, block25, block26, block27)
        print('\n', space, space, block51, space, block65, space, space, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, space, space, space, space, space)
        print('\n', space, space, block53, space, block67, space, space, space, space, space, space)
        print('\n', space, space, block54, space, space, space, space, space, space, space, space)
        print('\n', space, space, block55, space, space, space, space, space, space, space, space)
        if block31 == '\033[7;37m 3.1  \033[0;30m' :
            print('\n\033[0;31mYou got 3.1 wrong.\033[0;30m')
            points = points - (1/4)
        if block32 == '\033[7;37m 3.2  \033[0;30m' :
            print('\n\033[0;31mYou got 3.2 wrong.\033[0;30m')
            points = points - (1/4)
        if block33 == '\033[7;37m 3.3  \033[0;30m' :
            print('\n\033[0;31mYou got 3.3 wrong.\033[0;30m')
            points = points - (1/4)
        if block34 == '\033[7;37m 3.4  \033[0;30m' :
            print('\n\033[0;31mYou got 3.4 wrong.\033[0;30m')
            points = points - (1/4)

    while block41 == '\033[7;37m 4.1  \033[0;30m' or block42 == '\033[7;37m 4.2  \033[0;30m' or block43 == '\033[7;37m 4.3  \033[0;30m' or block44 == '\033[7;37m 4.4  \033[0;30m' or block45 == '\033[7;37m 4.5  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('4. Apheresis donation can be done more frequently, which is every')
        print('   two ___.')
        weeksW = input('\n\t4.1: ').upper()
        weeksE1 = input('\t4.2: ').upper()
        weeksE2 = input('\t4.3: ').upper()
        weeksK = input('\t4.4: ').upper()
        weeksS = input('\t4.5: ').upper()
        if weeksW == 'W':
            block41 = "\033[7;37m  W   \033[0;30m"
        if weeksE1 == 'E':
            block42 = "\033[7;37m  E   \033[0;30m"
        if weeksE2 == 'E':
            block43 = "\033[7;37m  E   \033[0;30m"
        if weeksK == 'K':
            block44 = "\033[7;37m  K   \033[0;30m"
        if weeksS == 'S':
            block45 = "\033[7;37m  S   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, block41, space, space, space, space, space, space, space, space, space)
        print('\n', space, block42, space, space, block61, space, space, space, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, space, space, space)
        print('\n', space, block44, space, space, block63, space, space, space, space, space, space)
        print('\n', space, block45, space, space, block21, block22, block23, block24, block25, block26, block27)
        print('\n', space, space, block51, space, block65, space, space, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, space, space, space, space, space)
        print('\n', space, space, block53, space, block67, space, space, space, space, space, space)
        print('\n', space, space, block54, space, space, space, space, space, space, space, space)
        print('\n', space, space, block55, space, space, space, space, space, space, space, space)
        if block41 == '\033[7;37m 4.1  \033[0;30m' :
            print('\n\033[0;31mYou got 4.1 wrong.\033[0;30m')
            points = points - (1/5)
        if block42 == '\033[7;37m 4.2  \033[0;30m' :
            print('\n\033[0;31mYou got 4.2 wrong.\033[0;30m')
            points = points - (1/5)
        if block43 == '\033[7;37m 4.3  \033[0;30m' :
            print('\n\033[0;31mYou got 4.3 wrong.\033[0;30m')
            points = points - (1/5)
        if block44 == '\033[7;37m 4.4  \033[0;30m' :
            print('\n\033[0;31mYou got 4.4 wrong.\033[0;30m')
            points = points - (1/5)
        if block45 == '\033[7;37m 4.5  \033[0;30m' :
            print('\n\033[0;31mYou got 4.5 wrong.\033[0;30m')
            points = points - (1/5)

    while block51 == '\033[7;37m 5.1  \033[0;30m' or block52 == '\033[7;37m 5.2  \033[0;30m' or block53 == '\033[7;37m 5.3  \033[0;30m' or block54 == '\033[7;37m 5.4  \033[0;30m' or block55 == '\033[7;37m 5.5  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('5. Whole blood donors may donate as frequently as every ___ months.')
        threeT = input('\n\t5.1: ').upper()
        threeH = input('\t5.2: ').upper()
        threeR = input('\t5.3: ').upper()
        threeE1 = input('\t5.4: ').upper()
        threeE2 = input('\t5.5: ').upper()
        if threeT == 'T':
            block51 = "\033[7;37m  T   \033[0;30m"
        if threeH == 'H':
            block52 = "\033[7;37m  H   \033[0;30m"
        if threeR == 'R':
            block53 = "\033[7;37m  R   \033[0;30m"
        if threeE1 == 'E':
            block54 = "\033[7;37m  E   \033[0;30m"
        if threeE2 == 'E':
            block55 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, block41, space, space, space, space, space, space, space, space, space)
        print('\n', space, block42, space, space, block61, space, space, space, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, space, space, space)
        print('\n', space, block44, space, space, block63, space, space, space, space, space, space)
        print('\n', space, block45, space, space, block21, block22, block23, block24, block25, block26, block27)
        print('\n', space, space, block51, space, block65, space, space, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, space, space, space, space, space)
        print('\n', space, space, block53, space, block67, space, space, space, space, space, space)
        print('\n', space, space, block54, space, space, space, space, space, space, space, space)
        print('\n', space, space, block55, space, space, space, space, space, space, space, space)
        if block51 == '\033[7;37m 5.1  \033[0;30m' :
            print('\n\033[0;31mYou got 5.1 wrong.\033[0;30m')
            points = points - (1/5)
        if block52 == '\033[7;37m 5.2  \033[0;30m' :
            print('\n\033[0;31mYou got 5.2 wrong.\033[0;30m')
            points = points - (1/5)
        if block53 == '\033[7;37m 5.3  \033[0;30m' :
            print('\n\033[0;31mYou got 5.3 wrong.\033[0;30m')
            points = points - (1/5)
        if block54 == '\033[7;37m 5.4  \033[0;30m' :
            print('\n\033[0;31mYou got 5.4 wrong.\033[0;30m')
            points = points - (1/5)
        if block55 == '\033[7;37m 5.5  \033[0;30m' :
            print('\n\033[0;31mYou got 5.5 wrong.\033[0;30m')
            points = points - (1/5)

    while block61 == '\033[7;37m 6.1  \033[0;30m' or block62 == '\033[7;37m 6.2  \033[0;30m' or block63 == '\033[7;37m 6.3  \033[0;30m' or block64 == '\033[7;37m 6.4  \033[0;30m' or block65 == '\033[7;37m 6.5  \033[0;30m' or block66 == '\033[7;37m 6.6  \033[0;30m' or block67 == '\033[7;37m 6.7  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('6. Donating blood is safe; ___, disposable equipment is used')
        print('   for each donor.')
        sterileS = input('\n\t6.1: ').upper()
        sterileT = input('\t6.2: ').upper()
        sterileE1 = input('\t6.3: ').upper()
        sterileR = input('\t6.4: ').upper()
        sterileI = input('\t6.5: ').upper()
        sterileL = input('\t6.6: ').upper()
        sterileE2 = input('\t6.7: ').upper()
        if sterileS == 'S':
            block61 = "\033[7;37m  S   \033[0;30m"
        if sterileT == 'T':
            block62 = "\033[7;37m  T   \033[0;30m"
        if sterileE1 == 'E':
            block63 = "\033[7;37m  E   \033[0;30m"
        if sterileR == 'R':
            block64 = "\033[7;37m  R   \033[0;30m"
        if sterileI == 'I':
            block65 = "\033[7;37m  I   \033[0;30m"
        if sterileL == 'L':
            block66 = "\033[7;37m  L   \033[0;30m"
        if sterileE2 == 'E':
            block67 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, block41, space, space, space, space, space, space, space, space, space)
        print('\n', space, block42, space, space, block61, space, space, space, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, space, space, space)
        print('\n', space, block44, space, space, block63, space, space, space, space, space, space)
        print('\n', space, block45, space, space, block21, block22, block23, block24, block25, block26, block27)
        print('\n', space, space, block51, space, block65, space, space, space, space, space, space)
        print('\n', space, space, block31, block32, block33, block34, space, space, space, space, space)
        print('\n', space, space, block53, space, block67, space, space, space, space, space, space)
        print('\n', space, space, block54, space, space, space, space, space, space, space, space)
        print('\n', space, space, block55, space, space, space, space, space, space, space, space)
        if block61 == '\033[7;37m 6.1  \033[0;30m' :
            print('\n\033[0;31mYou got 6.1 wrong.\033[0;30m')
            points = points - (1/7)
        if block62 == '\033[7;37m 6.2  \033[0;30m' :
            print('\n\033[0;31mYou got 6.2 wrong.\033[0;30m')
            points = points - (1/7)
        if block63 == '\033[7;37m 6.3  \033[0;30m' :
            print('\n\033[0;31mYou got 6.3 wrong.\033[0;30m')
            points = points - (1/7)
        if block64 == '\033[7;37m 6.4  \033[0;30m' :
            print('\n\033[0;31mYou got 6.4 wrong.\033[0;30m')
            points = points - (1/7)
        if block65 == '\033[7;37m 6.5  \033[0;30m' :
            print('\n\033[0;31mYou got 6.5 wrong.\033[0;30m')
            points = points - (1/7)
        if block66 == '\033[7;37m 6.6  \033[0;30m' :
            print('\n\033[0;31mYou got 6.6 wrong.\033[0;30m')
            points = points - (1/7)
        if block67 == '\033[7;37m 6.7  \033[0;30m' :
            print('\n\033[0;31mYou got 6.7 wrong.\033[0;30m')
            points = points - (1/7)
    time.sleep(2)
    rewards(points)

def animals(): #question on topic of animals
    block11 = '\033[7;37m 1.1  \033[0;30m'
    block12 = '\033[7;37m 1.2  \033[0;30m'
    block13 = '\033[7;37m 1.3  \033[0;30m'
    block14 = '\033[7;37m 1.4  \033[0;30m'
    block15 = '\033[7;37m 1.5  \033[0;30m'
    block16 = '\033[7;37m 1.6  \033[0;30m'
    block17 = '\033[7;37m 1.7  \033[0;30m'
    block18 = '\033[7;37m 1.8  \033[0;30m'
    block19 = '\033[7;37m 1.9  \033[0;30m'
    block21 = '\033[7;37m 2.1  \033[0;30m'
    block22 = '\033[7;37m 2.2  \033[0;30m'
    block23 = '\033[7;37m 2.3  \033[0;30m'
    block24 = '\033[7;37m 2.4  \033[0;30m'
    block25 = '\033[7;37m 2.5  \033[0;30m'
    block26 = '\033[7;37m 2.6  \033[0;30m'
    block27 = '\033[7;37m 2.7  \033[0;30m'
    block28 = '\033[7;37m 2.8  \033[0;30m'
    block31 = '\033[7;37m 3.1  \033[0;30m'
    block32 = '\033[7;37m 3.2  \033[0;30m'
    block33 = '\033[7;37m 3.3  \033[0;30m'
    block34 = '\033[7;37m 3.4  \033[0;30m'
    block35 = '\033[7;37m 3.5  \033[0;30m'
    block41 = '\033[7;37m 4.1  \033[0;30m'
    block42 = '\033[7;37m 4.2  \033[0;30m'
    block43 = '\033[7;37m 4.3  \033[0;30m'
    block51 = '\033[7;37m 5.1  \033[0;30m'
    block52 = '\033[7;37m 5.2  \033[0;30m'
    block53 = '\033[7;37m 5.3  \033[0;30m'
    block54 = '\033[7;37m 5.4  \033[0;30m'
    block61 = '\033[7;37m 6.1  \033[0;30m'
    block62 = '\033[7;37m 6.2  \033[0;30m'
    block63 = '\033[7;37m 6.3  \033[0;30m'
    block64 = '\033[7;37m 6.4  \033[0;30m'
    block65 = '\033[7;37m 6.5  \033[0;30m'
    block66 = '\033[7;37m 6.6  \033[0;30m'
    space = '\033[7;40m      \033[0;30m'
    points = 6
    time.sleep(1)
    print('\n\t\033[0;34mTopic: Animals\033[0;30m')
    time.sleep(1)
    print('\n\033[4mHorizontal\033[0m')
    print('1. What fish are all born male?')
    print('2. Which sea creature is known for its ability to regrow its arms?')
    print('3. What is a female donkey called?')
    time.sleep(2)
    print('\n\033[4mVertical\033[0m')
    print('4. What animal has four compartments in its stomach?')
    print('5. What animal has rectangular pupils?')
    print('6. Which mammal has no vocal cords?')
    time.sleep(1)
    print('\n\033[0;33m...Loading...\033[0;30m')
    time.sleep(2)
    print('\n', space, space, block51, space, space, space, block61, space, space, space)
    print('\n', block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
    print('\n', block42, space, block53, space, space, space, block63, space, space, space)
    print('\n', block43, space, block54, space, space, space, block64, space, space, space)
    print('\n', space, space, block21, block22, block23, block24, block25, block26, block27, block28)
    print('\n', space, space, space, space, space, space, block66, space, space, space)
    print('\n', space, space, space, space, space, block31, block32, block33, block34, block35)

    while block11 == '\033[7;37m 1.1  \033[0;30m' or block12 == '\033[7;37m 1.2  \033[0;30m' or block13 == '\033[7;37m 1.3  \033[0;30m' or block14 == '\033[7;37m 1.4  \033[0;30m' or block15 == '\033[7;37m 1.5  \033[0;30m' or block16 == '\033[7;37m 1.6  \033[0;30m' or block17 == '\033[7;37m 1.7  \033[0;30m' or block18 == '\033[7;37m 1.8  \033[0;30m' or block19 == '\033[7;37m 1.9  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('1. What fish are all born male?')
        clownfishC = input('\n\t1.1: ').upper()
        clownfishL = input('\t1.2: ').upper()
        clownfishO = input('\t1.3: ').upper()
        clownfishW = input('\t1.4: ').upper()
        clownfishN = input('\t1.5: ').upper()
        clownfishF = input('\t1.6: ').upper()
        clownfishI = input('\t1.7: ').upper()
        clownfishS = input('\t1.8: ').upper()
        clownfishH = input('\t1.9: ').upper()
        if clownfishC == 'C':
            block11 = "\033[7;37m  C   \033[0;30m"
        if clownfishL == 'L':
            block12 = "\033[7;37m  L   \033[0;30m"
        if clownfishO == 'O':
            block13 = "\033[7;37m  O   \033[0;30m"
        if clownfishW == 'W':
            block14 = "\033[7;37m  W   \033[0;30m"
        if clownfishN == 'N':
            block15 = "\033[7;37m  N   \033[0;30m"
        if clownfishF == 'F':
            block16 = "\033[7;37m  F   \033[0;30m"
        if clownfishI == 'I':
            block17 = "\033[7;37m  I   \033[0;30m"
        if clownfishS == 'S':
            block18 = "\033[7;37m  S   \033[0;30m"
        if clownfishH == 'H':
            block19 = "\033[7;37m  H   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, block51, space, space, space, block61, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', block42, space, block53, space, space, space, block63, space, space, space)
        print('\n', block43, space, block54, space, space, space, block64, space, space, space)
        print('\n', space, space, block21, block22, block23, block24, block25, block26, block27, block28)
        print('\n', space, space, space, space, space, space, block66, space, space, space)
        print('\n', space, space, space, space, space, block31, block32, block33, block34, block35)
        if block11 == '\033[7;37m 1.1  \033[0;30m' :
            print('\n\033[0;31mYou got 1.1 wrong.\033[0;30m')
            points = points - (1/9)
        if block12 == '\033[7;37m 1.2  \033[0;30m' :
            print('\n\033[0;31mYou got 1.2 wrong.\033[0;30m')
            points = points - (1/9)
        if block13 == '\033[7;37m 1.3  \033[0;30m' :
            print('\n\033[0;31mYou got 1.3 wrong.\033[0;30m')
            points = points - (1/9)
        if block14 == '\033[7;37m 1.4  \033[0;30m' :
            print('\n\033[0;31mYou got 1.4 wrong.\033[0;30m')
            points = points - (1/9)
        if block15 == '\033[7;37m 1.5  \033[0;30m' :
            print('\n\033[0;31mYou got 1.5 wrong.\033[0;30m')
            points = points - (1/9)
        if block16 == '\033[7;37m 1.6  \033[0;30m' :
            print('\n\033[0;31mYou got 1.6 wrong.\033[0;30m')
            points = points - (1/9)
        if block17 == '\033[7;37m 1.7  \033[0;30m' :
            print('\n\033[0;31mYou got 1.7 wrong.\033[0;30m')
            points = points - (1/9)
        if block18 == '\033[7;37m 1.8  \033[0;30m' :
            print('\n\033[0;31mYou got 1.8 wrong.\033[0;30m')
            points = points - (1/9)
        if block19 == '\033[7;37m 1.9  \033[0;30m' :
            print('\n\033[0;31mYou got 1.9 wrong.\033[0;30m')
            points = points - (1/9)

    while block21 == '\033[7;37m 2.1  \033[0;30m' or block22 == '\033[7;37m 2.2  \033[0;30m' or block23 == '\033[7;37m 2.3  \033[0;30m' or block24 == '\033[7;37m 2.4  \033[0;30m' or block25 == '\033[7;37m 2.5  \033[0;30m' or block26 == '\033[7;37m 2.6  \033[0;30m' or block27 == '\033[7;37m 2.7  \033[0;30m' or block28 == '\033[7;37m 2.8  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('2. Which sea creature is known for its ability to regrow its arms?')
        starfishS1 = input('\n\t2.1: ').upper()
        starfishT = input('\t2.2: ').upper()
        starfishA = input('\t2.3: ').upper()
        starfishR = input('\t2.4: ').upper()
        starfishF = input('\t2.5: ').upper()
        starfishI = input('\t2.6: ').upper()
        starfishS2 = input('\t2.7: ').upper()
        starfishH = input('\t2.8: ').upper()
        if starfishS1 == 'S':
            block21 = "\033[7;37m  S   \033[0;30m"
        if starfishT == 'T':
            block22 = "\033[7;37m  T   \033[0;30m"
        if starfishA == 'A':
            block23 = "\033[7;37m  A   \033[0;30m"
        if starfishR == 'R':
            block24 = "\033[7;37m  R   \033[0;30m"
        if starfishF == 'F':
            block25 = "\033[7;37m  F   \033[0;30m"
        if starfishI == 'I':
            block26 = "\033[7;37m  I   \033[0;30m"
        if starfishS2 == 'S':
            block27 = "\033[7;37m  S   \033[0;30m"
        if starfishH == 'H':
            block28 = "\033[7;37m  H   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, block51, space, space, space, block61, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', block42, space, block53, space, space, space, block63, space, space, space)
        print('\n', block43, space, block54, space, space, space, block64, space, space, space)
        print('\n', space, space, block21, block22, block23, block24, block25, block26, block27, block28)
        print('\n', space, space, space, space, space, space, block66, space, space, space)
        print('\n', space, space, space, space, space, block31, block32, block33, block34, block35)
        if block21 == '\033[7;37m 2.1  \033[0;30m' :
            print('\n\033[0;31mYou got 2.1 wrong.\033[0;30m')
            points = points - (1/8)
        if block22 == '\033[7;37m 2.2  \033[0;30m' :
            print('\n\033[0;31mYou got 2.2 wrong.\033[0;30m')
            points = points - (1/8)
        if block23 == '\033[7;37m 2.3  \033[0;30m' :
            print('\n\033[0;31mYou got 2.3 wrong.\033[0;30m')
            points = points - (1/8)
        if block24 == '\033[7;37m 2.4  \033[0;30m' :
            print('\n\033[0;31mYou got 2.4 wrong.\033[0;30m')
            points = points - (1/8)
        if block25 == '\033[7;37m 2.5  \033[0;30m' :
            print('\n\033[0;31mYou got 2.5 wrong.\033[0;30m')
            points = points - (1/8)
        if block26 == '\033[7;37m 2.6  \033[0;30m' :
            print('\n\033[0;31mYou got 2.6 wrong.\033[0;30m')
            points = points - (1/8)
        if block27 == '\033[7;37m 2.7  \033[0;30m' :
            print('\n\033[0;31mYou got 2.7 wrong.\033[0;30m')
            points = points - (1/8)
        if block28 == '\033[7;37m 2.8  \033[0;30m' :
            print('\n\033[0;31mYou got 2.8 wrong.\033[0;30m')
            points = points - (1/8)

    while block31 == '\033[7;37m 3.1  \033[0;30m' or block32 == '\033[7;37m 3.2  \033[0;30m' or block33 == '\033[7;37m 3.3  \033[0;30m' or block34 == '\033[7;37m 3.4  \033[0;30m' or block35 == '\033[7;37m 3.5  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('3. What is a female donkey called?')
        jennyJ = input('\n\t3.1: ').upper()
        jennyE = input('\t3.2: ').upper()
        jennyN1 = input('\t3.3: ').upper()
        jennyN2 = input('\t3.4: ').upper()
        jennyY = input('\t3.5: ').upper()
        if jennyJ == 'J':
            block31 = "\033[7;37m  J   \033[0;30m"
        if jennyE == 'E':
            block32 = "\033[7;37m  E   \033[0;30m"
        if jennyN1 == 'N':
            block33 = "\033[7;37m  N   \033[0;30m"
        if jennyN2 == 'N':
            block34 = "\033[7;37m  N   \033[0;30m"
        if jennyY == 'Y':
            block35 = "\033[7;37m  Y   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, block51, space, space, space, block61, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', block42, space, block53, space, space, space, block63, space, space, space)
        print('\n', block43, space, block54, space, space, space, block64, space, space, space)
        print('\n', space, space, block21, block22, block23, block24, block25, block26, block27, block28)
        print('\n', space, space, space, space, space, space, block66, space, space, space)
        print('\n', space, space, space, space, space, block31, block32, block33, block34, block35)
        if block31 == '\033[7;37m 3.1  \033[0;30m' :
            print('\n\033[0;31mYou got 3.1 wrong.\033[0;30m')
            points = points - (1/5)
        if block32 == '\033[7;37m 3.2  \033[0;30m' :
            print('\n\033[0;31mYou got 3.2 wrong.\033[0;30m')
            points = points - (1/5)
        if block33 == '\033[7;37m 3.3  \033[0;30m' :
            print('\n\033[0;31mYou got 3.3 wrong.\033[0;30m')
            points = points - (1/5)
        if block34 == '\033[7;37m 3.4  \033[0;30m' :
            print('\n\033[0;31mYou got 3.4 wrong.\033[0;30m')
            points = points - (1/5)
        if block35 == '\033[7;37m 3.5  \033[0;30m' :
            print('\n\033[0;31mYou got 3.5 wrong.\033[0;30m')
            points = points - (1/5)

    while block41 == '\033[7;37m 4.1  \033[0;30m' or block42 == '\033[7;37m 4.2  \033[0;30m' or block43 == '\033[7;37m 4.3  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('4. What animal has four compartments in its stomach?')
        cowC = input('\n\t4.1: ').upper()
        cowO = input('\t4.2: ').upper()
        cowW = input('\t4.3: ').upper()
        if cowC == 'C':
            block41 = "\033[7;37m  C   \033[0;30m"
        if cowO == 'O':
            block42 = "\033[7;37m  O   \033[0;30m"
        if cowW == 'W':
            block43 = "\033[7;37m  W   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, block51, space, space, space, block61, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', block42, space, block53, space, space, space, block63, space, space, space)
        print('\n', block43, space, block54, space, space, space, block64, space, space, space)
        print('\n', space, space, block21, block22, block23, block24, block25, block26, block27, block28)
        print('\n', space, space, space, space, space, space, block66, space, space, space)
        print('\n', space, space, space, space, space, block31, block32, block33, block34, block35)
        if block41 == '\033[7;37m 4.1  \033[0;30m' :
            print('\n\033[0;31mYou got 4.1 wrong.\033[0;30m')
            points = points - (1/3)
        if block42 == '\033[7;37m 4.2  \033[0;30m' :
            print('\n\033[0;31mYou got 4.2 wrong.\033[0;30m')
            points = points - (1/3)
        if block43 == '\033[7;37m 4.3  \033[0;30m' :
            print('\n\033[0;31mYou got 4.3 wrong.\033[0;30m')
            points = points - (1/3)

    while block51 == '\033[7;37m 5.1  \033[0;30m' or block52 == '\033[7;37m 5.2  \033[0;30m' or block53 == '\033[7;37m 5.3  \033[0;30m' or block54 == '\033[7;37m 5.4  \033[0;30m' or block55 == '\033[7;37m 5.5  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('5. What animal has rectangular pupils?')
        goatsG = input('\n\t5.1: ').upper()
        goatsO = input('\t5.2: ').upper()
        goatsA = input('\t5.3: ').upper()
        goatsT = input('\t5.4: ').upper()
        goatsS = input('\t5.5: ').upper()
        if goatsG == 'G':
            block51 = "\033[7;37m  G   \033[0;30m"
        if goatsO == 'O':
            block52 = "\033[7;37m  O   \033[0;30m"
        if goatsA == 'A':
            block53 = "\033[7;37m  A   \033[0;30m"
        if goatsT == 'T':
            block54 = "\033[7;37m  T   \033[0;30m"
        if goatsS == 'S':
            block55 = "\033[7;37m  S   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, block51, space, space, space, block61, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', block42, space, block53, space, space, space, block63, space, space, space)
        print('\n', block43, space, block54, space, space, space, block64, space, space, space)
        print('\n', space, space, block21, block22, block23, block24, block25, block26, block27, block28)
        print('\n', space, space, space, space, space, space, block66, space, space, space)
        print('\n', space, space, space, space, space, block31, block32, block33, block34, block35)
        if block51 == '\033[7;37m 5.1  \033[0;30m' :
            print('\n\033[0;31mYou got 5.1 wrong.\033[0;30m')
            points = points - (1/5)
        if block52 == '\033[7;37m 5.2  \033[0;30m' :
            print('\n\033[0;31mYou got 5.2 wrong.\033[0;30m')
            points = points - (1/5)
        if block53 == '\033[7;37m 5.3  \033[0;30m' :
            print('\n\033[0;31mYou got 5.3 wrong.\033[0;30m')
            points = points - (1/5)
        if block54 == '\033[7;37m 5.4  \033[0;30m' :
            print('\n\033[0;31mYou got 5.4 wrong.\033[0;30m')
            points = points - (1/5)
        if block55 == '\033[7;37m 5.5  \033[0;30m' :
            print('\n\033[0;31mYou got 5.5 wrong.\033[0;30m')
            points = points - (1/5)

    while block61 == '\033[7;37m 6.1  \033[0;30m' or block62 == '\033[7;37m 6.2  \033[0;30m' or block63 == '\033[7;37m 6.3  \033[0;30m' or block64 == '\033[7;37m 6.4  \033[0;30m' or block65 == '\033[7;37m 6.5  \033[0;30m' or block66 == '\033[7;37m 6.6  \033[0;30m' or block67 == '\033[7;37m 6.7  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('6. Which mammal has no vocal cords?')
        giraffeG = input('\n\t6.1: ').upper()
        giraffeI = input('\t6.2: ').upper()
        giraffeR = input('\t6.3: ').upper()
        giraffeA = input('\t6.4: ').upper()
        giraffeF1 = input('\t6.5: ').upper()
        giraffeF2 = input('\t6.6: ').upper()
        giraffeE = input('\t6.7: ').upper()
        if giraffeG == 'G':
            block61 = "\033[7;37m  G   \033[0;30m"
        if giraffeI == 'I':
            block62 = "\033[7;37m  I   \033[0;30m"
        if giraffeR == 'R':
            block63 = "\033[7;37m  R   \033[0;30m"
        if giraffeA == 'A':
            block64 = "\033[7;37m  A   \033[0;30m"
        if giraffeF1 == 'F':
            block65 = "\033[7;37m  F   \033[0;30m"
        if giraffeF2 == 'F':
            block66 = "\033[7;37m  F   \033[0;30m"
        if giraffeE == 'E':
            block67 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, block51, space, space, space, block61, space, space, space)
        print('\n', block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', block42, space, block53, space, space, space, block63, space, space, space)
        print('\n', block43, space, block54, space, space, space, block64, space, space, space)
        print('\n', space, space, block21, block22, block23, block24, block25, block26, block27, block28)
        print('\n', space, space, space, space, space, space, block66, space, space, space)
        print('\n', space, space, space, space, space, block31, block32, block33, block34, block35)
        if block61 == '\033[7;37m 6.1  \033[0;30m' :
            print('\n\033[0;31mYou got 6.1 wrong.\033[0;30m')
            points = points - (1/7)
        if block62 == '\033[7;37m 6.2  \033[0;30m' :
            print('\n\033[0;31mYou got 6.2 wrong.\033[0;30m')
            points = points - (1/7)
        if block63 == '\033[7;37m 6.3  \033[0;30m' :
            print('\n\033[0;31mYou got 6.3 wrong.\033[0;30m')
            points = points - (1/7)
        if block64 == '\033[7;37m 6.4  \033[0;30m' :
            print('\n\033[0;31mYou got 6.4 wrong.\033[0;30m')
            points = points - (1/7)
        if block65 == '\033[7;37m 6.5  \033[0;30m' :
            print('\n\033[0;31mYou got 6.5 wrong.\033[0;30m')
            points = points - (1/7)
        if block66 == '\033[7;37m 6.6  \033[0;30m' :
            print('\n\033[0;31mYou got 6.6 wrong.\033[0;30m')
            points = points - (1/7)
        if block67 == '\033[7;37m 6.7  \033[0;30m' :
            print('\n\033[0;31mYou got 6.7 wrong.\033[0;30m')
            points = points - (1/7)
    time.sleep(2)
    rewards(points)

def food(): #question on topic of food
    block11 = '\033[7;37m 1.1  \033[0;30m'
    block12 = '\033[7;37m 1.2  \033[0;30m'
    block13 = '\033[7;37m 1.3  \033[0;30m'
    block14 = '\033[7;37m 1.4  \033[0;30m'
    block15 = '\033[7;37m 1.5  \033[0;30m'
    block16 = '\033[7;37m 1.6  \033[0;30m'
    block17 = '\033[7;37m 1.7  \033[0;30m'
    block18 = '\033[7;37m 1.8  \033[0;30m'
    block19 = '\033[7;37m 1.9  \033[0;30m'
    block21 = '\033[7;37m 2.1  \033[0;30m'
    block22 = '\033[7;37m 2.2  \033[0;30m'
    block23 = '\033[7;37m 2.3  \033[0;30m'
    block24 = '\033[7;37m 2.4  \033[0;30m'
    block25 = '\033[7;37m 2.5  \033[0;30m'
    block26 = '\033[7;37m 2.6  \033[0;30m'
    block27 = '\033[7;37m 2.7  \033[0;30m'
    block28 = '\033[7;37m 2.8  \033[0;30m'
    block29 = '\033[7;37m 2.9  \033[0;30m'
    block210 = '\033[7;37m 2.10 \033[0;30m'
    block211 = '\033[7;37m 2.11 \033[0;30m'
    block212 = '\033[7;37m 2.12 \033[0;30m'
    block31 = '\033[7;37m 3.1  \033[0;30m'
    block32 = '\033[7;37m 3.2  \033[0;30m'
    block33 = '\033[7;37m 3.3  \033[0;30m'
    block34 = '\033[7;37m 3.4  \033[0;30m'
    block35 = '\033[7;37m 3.5  \033[0;30m'
    block36 = '\033[7;37m 3.6  \033[0;30m'
    block37 = '\033[7;37m 3.7  \033[0;30m'
    block41 = '\033[7;37m 4.1  \033[0;30m'
    block42 = '\033[7;37m 4.2  \033[0;30m'
    block43 = '\033[7;37m 4.3  \033[0;30m'
    block44 = '\033[7;37m 4.4  \033[0;30m'
    block45 = '\033[7;37m 4.5  \033[0;30m'
    block46 = '\033[7;37m 4.6  \033[0;30m'
    block47 = '\033[7;37m 4.7  \033[0;30m'
    block51 = '\033[7;37m 5.1  \033[0;30m'
    block52 = '\033[7;37m 5.2  \033[0;30m'
    block53 = '\033[7;37m 5.3  \033[0;30m'
    block54 = '\033[7;37m 5.4  \033[0;30m'
    block55 = '\033[7;37m 5.5  \033[0;30m'
    block56 = '\033[7;37m 5.6  \033[0;30m'
    block61 = '\033[7;37m 6.1  \033[0;30m'
    block62 = '\033[7;37m 6.2  \033[0;30m'
    block63 = '\033[7;37m 6.3  \033[0;30m'
    block64 = '\033[7;37m 6.4  \033[0;30m'
    block65 = '\033[7;37m 6.5  \033[0;30m'
    block66 = '\033[7;37m 6.6  \033[0;30m'
    space = '\033[7;40m      \033[0;30m'
    points = 6
    time.sleep(1)
    print('\n\t\033[0;34mTopic: Food\033[0;30m')
    time.sleep(1)
    print('\n\033[4mHorizontal\033[0m')
    print('1. What is the primary ingredient of falafel?')
    print('2. Arachibutyrophobia is the fear of what sticking to the roof of your mouth?')
    print('3. Which nut is used to make marzipan?')
    time.sleep(2)
    print('\n\033[4mVertical\033[0m')
    print('4. What is the base ingredient of gummy bears?')
    print('5. Which fruit is known as the king of fruits?')
    print('6. What is the most expensive spice in the world?')
    time.sleep(1)
    print('\n\033[0;33m...Loading...\033[0;30m')
    time.sleep(2)
    print('\n', space, space, space, space, space, space, space, space, space, space, space, block61, space, space)
    print('\n', space, space, block41, space, block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
    print('\n', space, space, block42, space, space, space, space, space, space, space, space, block63, space, space)
    print('\n', space, space, block43, space, block51, space, space, space, space, space, space, block64, space, space)
    print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, block211, block212, space, space)
    print('\n', space, space, block45, space, block53, space, space, space, space, space, space, block66, space, space)
    print('\n', space, space, block46, space, block54, space, space, block31, block32, block33, block34, block35, block36, block37)
    print('\n', space, space, block47, space, block55, space, space, space, space, space, space, space, space, space)
    print('\n', space, space, space, space, block56, space, space, space, space, space, space, space, space, space)

    while block11 == '\033[7;37m 1.1  \033[0;30m' or block12 == '\033[7;37m 1.2  \033[0;30m' or block13 == '\033[7;37m 1.3  \033[0;30m' or block14 == '\033[7;37m 1.4  \033[0;30m' or block15 == '\033[7;37m 1.5  \033[0;30m' or block16 == '\033[7;37m 1.6  \033[0;30m' or block17 == '\033[7;37m 1.7  \033[0;30m' or block18 == '\033[7;37m 1.8  \033[0;30m' or block19 == '\033[7;37m 1.9  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('1. What is the primary ingredient of falafel?')
        chickpeasC1 = input('\n\t1.1: ').upper()
        chickpeasH = input('\t1.2: ').upper()
        chickpeasI = input('\t1.3: ').upper()
        chickpeasC2 = input('\t1.4: ').upper()
        chickpeasK = input('\t1.5: ').upper()
        chickpeasP = input('\t1.6: ').upper()
        chickpeasE = input('\t1.7: ').upper()
        chickpeasA = input('\t1.8: ').upper()
        chickpeasS = input('\t1.9: ').upper()
        if chickpeasC1 == 'C':
            block11 = "\033[7;37m  C   \033[0;30m"
        if chickpeasH == 'H':
            block12 = "\033[7;37m  H   \033[0;30m"
        if chickpeasI == 'I':
            block13 = "\033[7;37m  I   \033[0;30m"
        if chickpeasC2 == 'C':
            block14 = "\033[7;37m  C   \033[0;30m"
        if chickpeasK == 'K':
            block15 = "\033[7;37m  K   \033[0;30m"
        if chickpeasP == 'P':
            block16 = "\033[7;37m  P   \033[0;30m"
        if chickpeasE == 'E':
            block17 = "\033[7;37m  E   \033[0;30m"
        if chickpeasA == 'A':
            block18 = "\033[7;37m  A   \033[0;30m"
        if chickpeasS == 'S':
            block19 = "\033[7;37m  S   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, block41, space, block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', space, space, block42, space, space, space, space, space, space, space, space, block63, space, space)
        print('\n', space, space, block43, space, block51, space, space, space, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, block211, block212, space, space)
        print('\n', space, space, block45, space, block53, space, space, space, space, space, space, block66, space, space)
        print('\n', space, space, block46, space, block54, space, space, block31, block32, block33, block34, block35, block36, block37)
        print('\n', space, space, block47, space, block55, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, space, block56, space, space, space, space, space, space, space, space, space)
        if block11 == '\033[7;37m 1.1  \033[0;30m' :
            print('\n\033[0;31mYou got 1.1 wrong.\033[0;30m')
            points = points - (1/9)
        if block12 == '\033[7;37m 1.2  \033[0;30m' :
            print('\n\033[0;31mYou got 1.2 wrong.\033[0;30m')
            points = points - (1/9)
        if block13 == '\033[7;37m 1.3  \033[0;30m' :
            print('\n\033[0;31mYou got 1.3 wrong.\033[0;30m')
            points = points - (1/9)
        if block14 == '\033[7;37m 1.4  \033[0;30m' :
            print('\n\033[0;31mYou got 1.4 wrong.\033[0;30m')
            points = points - (1/9)
        if block15 == '\033[7;37m 1.5  \033[0;30m' :
            print('\n\033[0;31mYou got 1.5 wrong.\033[0;30m')
            points = points - (1/9)
        if block16 == '\033[7;37m 1.6  \033[0;30m' :
            print('\n\033[0;31mYou got 1.6 wrong.\033[0;30m')
            points = points - (1/9)
        if block17 == '\033[7;37m 1.7  \033[0;30m' :
            print('\n\033[0;31mYou got 1.7 wrong.\033[0;30m')
            points = points - (1/9)
        if block18 == '\033[7;37m 1.8  \033[0;30m' :
            print('\n\033[0;31mYou got 1.8 wrong.\033[0;30m')
            points = points - (1/9)
        if block19 == '\033[7;37m 1.9  \033[0;30m' :
            print('\n\033[0;31mYou got 1.9 wrong.\033[0;30m')
            points = points - (1/9)

    while block21 == '\033[7;37m 2.1  \033[0;30m' or block22 == '\033[7;37m 2.2  \033[0;30m' or block23 == '\033[7;37m 2.3  \033[0;30m' or block24 == '\033[7;37m 2.4  \033[0;30m' or block25 == '\033[7;37m 2.5  \033[0;30m' or block26 == '\033[7;37m 2.6  \033[0;30m' or block27 == '\033[7;37m 2.7  \033[0;30m' or block28 == '\033[7;37m 2.8  \033[0;30m' or block29 == '\033[7;37m 2.9  \033[0;30m' or block210 == '\033[7;37m 2.10  \033[0;30m' or block211 == '\033[7;37m 2.11  \033[0;30m' or block212 == '\033[7;37m 2.12  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('2. Arachibutyrophobia is the fear of what sticking to the roof of your mouth?')
        peanutbutterP = input('\n\t2.1: ').upper()
        peanutbutterE1 = input('\t2.2: ').upper()
        peanutbutterA = input('\t2.3: ').upper()
        peanutbutterN = input('\t2.4: ').upper()
        peanutbutterU1 = input('\t2.5: ').upper()
        peanutbutterT1 = input('\t2.6: ').upper()
        peanutbutterB = input('\t2.7: ').upper()
        peanutbutterU2 = input('\t2.8: ').upper()
        peanutbutterT2 = input('\t2.9: ').upper()
        peanutbutterT3 = input('\t2.10: ').upper()
        peanutbutterE2 = input('\t2.11: ').upper()
        peanutbutterR = input('\t2.12: ').upper()
        if peanutbutterP == 'P':
            block21 = "\033[7;37m  P   \033[0;30m"
        if peanutbutterE1 == 'E':
            block22 = "\033[7;37m  E   \033[0;30m"
        if peanutbutterA == 'A':
            block23 = "\033[7;37m  A   \033[0;30m"
        if peanutbutterN == 'N':
            block24 = "\033[7;37m  N   \033[0;30m"
        if peanutbutterU1 == 'U':
            block25 = "\033[7;37m  U   \033[0;30m"
        if peanutbutterT1 == 'T':
            block26 = "\033[7;37m  T   \033[0;30m"
        if peanutbutterB == 'B':
            block27 = "\033[7;37m  B   \033[0;30m"
        if peanutbutterU2 == 'U':
            block28 = "\033[7;37m  U   \033[0;30m"
        if peanutbutterT2 == 'T':
            block29 = "\033[7;37m  T   \033[0;30m"
        if peanutbutterT3 == 'T':
            block210 = "\033[7;37m  T   \033[0;30m"
        if peanutbutterE2 == 'E':
            block211 = "\033[7;37m  E   \033[0;30m"
        if peanutbutterR == 'R':
            block212 = "\033[7;37m  R   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, block41, space, block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', space, space, block42, space, space, space, space, space, space, space, space, block63, space, space)
        print('\n', space, space, block43, space, block51, space, space, space, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, block211, block212, space, space)
        print('\n', space, space, block45, space, block53, space, space, space, space, space, space, block66, space, space)
        print('\n', space, space, block46, space, block54, space, space, block31, block32, block33, block34, block35, block36, block37)
        print('\n', space, space, block47, space, block55, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, space, block56, space, space, space, space, space, space, space, space, space)
        if block21 == '\033[7;37m 2.1  \033[0;30m' :
            print('\n\033[0;31mYou got 2.1 wrong.\033[0;30m')
            points = points - (1/12)
        if block22 == '\033[7;37m 2.2  \033[0;30m' :
            print('\n\033[0;31mYou got 2.2 wrong.\033[0;30m')
            points = points - (1/12)
        if block23 == '\033[7;37m 2.3  \033[0;30m' :
            print('\n\033[0;31mYou got 2.3 wrong.\033[0;30m')
            points = points - (1/12)
        if block24 == '\033[7;37m 2.4  \033[0;30m' :
            print('\n\033[0;31mYou got 2.4 wrong.\033[0;30m')
            points = points - (1/12)
        if block25 == '\033[7;37m 2.5  \033[0;30m' :
            print('\n\033[0;31mYou got 2.5 wrong.\033[0;30m')
            points = points - (1/12)
        if block26 == '\033[7;37m 2.6  \033[0;30m' :
            print('\n\033[0;31mYou got 2.6 wrong.\033[0;30m')
            points = points - (1/12)
        if block27 == '\033[7;37m 2.7  \033[0;30m' :
            print('\n\033[0;31mYou got 2.7 wrong.\033[0;30m')
            points = points - (1/12)
        if block28 == '\033[7;37m 2.8  \033[0;30m' :
            print('\n\033[0;31mYou got 2.8 wrong.\033[0;30m')
            points = points - (1/12)
        if block29 == '\033[7;37m 2.9  \033[0;30m' :
            print('\n\033[0;31mYou got 2.9 wrong.\033[0;30m')
            points = points - (1/12)
        if block210 == '\033[7;37m 2.10  \033[0;30m' :
            print('\n\033[0;31mYou got 2.10 wrong.\033[0;30m')
            points = points - (1/12)
        if block211 == '\033[7;37m 2.11  \033[0;30m' :
            print('\n\033[0;31mYou got 2.11 wrong.\033[0;30m')
            points = points - (1/12)
        if block212 == '\033[7;37m 2.12  \033[0;30m' :
            print('\n\033[0;31mYou got 2.12 wrong.\033[0;30m')
            points = points - (1/12)

    while block31 == '\033[7;37m 3.1  \033[0;30m' or block32 == '\033[7;37m 3.2  \033[0;30m' or block33 == '\033[7;37m 3.3  \033[0;30m' or block34 == '\033[7;37m 3.4  \033[0;30m' or block35 == '\033[7;37m 3.5  \033[0;30m' or block36 == '\033[7;37m 3.6  \033[0;30m' or block37 == '\033[7;37m 3.7  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('3. Which nut is used to make marzipan?')
        almondsA = input('\n\t3.1: ').upper()
        almondsL = input('\t3.2: ').upper()
        almondsM = input('\t3.3: ').upper()
        almondsO = input('\t3.4: ').upper()
        almondsN = input('\t3.5: ').upper()
        almondsD = input('\t3.6: ').upper()
        almondsS = input('\t3.7: ').upper()
        if almondsA == 'A':
            block31 = "\033[7;37m  A   \033[0;30m"
        if almondsL == 'L':
            block32 = "\033[7;37m  L   \033[0;30m"
        if almondsM == 'M':
            block33 = "\033[7;37m  M   \033[0;30m"
        if almondsO == 'O':
            block34 = "\033[7;37m  O   \033[0;30m"
        if almondsN == 'N':
            block35 = "\033[7;37m  N   \033[0;30m"
        if almondsD == 'D':
            block36 = "\033[7;37m  D   \033[0;30m"
        if almondsS == 'S':
            block37 = "\033[7;37m  S   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, block41, space, block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', space, space, block42, space, space, space, space, space, space, space, space, block63, space, space)
        print('\n', space, space, block43, space, block51, space, space, space, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, block211, block212, space, space)
        print('\n', space, space, block45, space, block53, space, space, space, space, space, space, block66, space, space)
        print('\n', space, space, block46, space, block54, space, space, block31, block32, block33, block34, block35, block36, block37)
        print('\n', space, space, block47, space, block55, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, space, block56, space, space, space, space, space, space, space, space, space)
        if block31 == '\033[7;37m 3.1  \033[0;30m' :
            print('\n\033[0;31mYou got 3.1 wrong.\033[0;30m')
            points = points - (1/7)
        if block32 == '\033[7;37m 3.2  \033[0;30m' :
            print('\n\033[0;31mYou got 3.2 wrong.\033[0;30m')
            points = points - (1/7)
        if block33 == '\033[7;37m 3.3  \033[0;30m' :
            print('\n\033[0;31mYou got 3.3 wrong.\033[0;30m')
            points = points - (1/7)
        if block34 == '\033[7;37m 3.4  \033[0;30m' :
            print('\n\033[0;31mYou got 3.4 wrong.\033[0;30m')
            points = points - (1/7)
        if block35 == '\033[7;37m 3.5  \033[0;30m' :
            print('\n\033[0;31mYou got 3.5 wrong.\033[0;30m')
            points = points - (1/7)
        if block36 == '\033[7;37m 3.6  \033[0;30m' :
            print('\n\033[0;31mYou got 3.6 wrong.\033[0;30m')
            points = points - (1/7)
        if block37 == '\033[7;37m 3.7  \033[0;30m' :
            print('\n\033[0;31mYou got 3.7 wrong.\033[0;30m')
            points = points - (1/7)

    while block41 == '\033[7;37m 4.1  \033[0;30m' or block42 == '\033[7;37m 4.2  \033[0;30m' or block43 == '\033[7;37m 4.3  \033[0;30m' or block44 == '\033[7;37m 4.4  \033[0;30m' or block45 == '\033[7;37m 4.5  \033[0;30m' or block46 == '\033[7;37m 4.6  \033[0;30m' or block47 == '\033[7;37m 4.7  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('4. What is the base ingredient of gummy bears?')
        gelatinG = input('\n\t4.1: ').upper()
        gelatinE = input('\t4.2: ').upper()
        gelatinL = input('\t4.3: ').upper()
        gelatinA = input('\t4.4: ').upper()
        gelatinT = input('\t4.5: ').upper()
        gelatinI = input('\t4.6: ').upper()
        gelatinN = input('\t4.7: ').upper()
        if gelatinG == 'G':
            block41 = "\033[7;37m  G   \033[0;30m"
        if gelatinE == 'E':
            block42 = "\033[7;37m  E   \033[0;30m"
        if gelatinL == 'L':
            block43 = "\033[7;37m  L   \033[0;30m"
        if gelatinA == 'A':
            block44 = "\033[7;37m  A   \033[0;30m"
        if gelatinT == 'T':
            block45 = "\033[7;37m  T   \033[0;30m"
        if gelatinI == 'I':
            block46 = "\033[7;37m  I   \033[0;30m"
        if gelatinN == 'N':
            block47 = "\033[7;37m  N   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, block41, space, block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', space, space, block42, space, space, space, space, space, space, space, space, block63, space, space)
        print('\n', space, space, block43, space, block51, space, space, space, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, block211, block212, space, space)
        print('\n', space, space, block45, space, block53, space, space, space, space, space, space, block66, space, space)
        print('\n', space, space, block46, space, block54, space, space, block31, block32, block33, block34, block35, block36, block37)
        print('\n', space, space, block47, space, block55, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, space, block56, space, space, space, space, space, space, space, space, space)
        if block41 == '\033[7;37m 4.1  \033[0;30m' :
            print('\n\033[0;31mYou got 4.1 wrong.\033[0;30m')
            points = points - (1/7)
        if block42 == '\033[7;37m 4.2  \033[0;30m' :
            print('\n\033[0;31mYou got 4.2 wrong.\033[0;30m')
            points = points - (1/7)
        if block43 == '\033[7;37m 4.3  \033[0;30m' :
            print('\n\033[0;31mYou got 4.3 wrong.\033[0;30m')
            points = points - (1/7)
        if block44 == '\033[7;37m 4.4  \033[0;30m' :
            print('\n\033[0;31mYou got 4.4 wrong.\033[0;30m')
            points = points - (1/7)
        if block45 == '\033[7;37m 4.5  \033[0;30m' :
            print('\n\033[0;31mYou got 4.5 wrong.\033[0;30m')
            points = points - (1/7)
        if block46 == '\033[7;37m 4.6  \033[0;30m' :
            print('\n\033[0;31mYou got 4.6 wrong.\033[0;30m')
            points = points - (1/7)
        if block47 == '\033[7;37m 4.7  \033[0;30m' :
            print('\n\033[0;31mYou got 4.7 wrong.\033[0;30m')
            points = points - (1/7)

    while block51 == '\033[7;37m 5.1  \033[0;30m' or block52 == '\033[7;37m 5.2  \033[0;30m' or block53 == '\033[7;37m 5.3  \033[0;30m' or block54 == '\033[7;37m 5.4  \033[0;30m' or block55 == '\033[7;37m 5.5  \033[0;30m' or block56 == '\033[7;37m 5.6  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('5. Which fruit is known as the king of fruits?')
        durianD = input('\n\t5.1: ').upper()
        durianU = input('\t5.2: ').upper()
        durianR = input('\t5.3: ').upper()
        durianI = input('\t5.4: ').upper()
        durianA = input('\t5.5: ').upper()
        durianN = input('\t5.6: ').upper()
        if durianD == 'D':
            block51 = "\033[7;37m  D   \033[0;30m"
        if durianU == 'U':
            block52 = "\033[7;37m  U   \033[0;30m"
        if durianR == 'R':
            block53 = "\033[7;37m  R   \033[0;30m"
        if durianI == 'I':
            block54 = "\033[7;37m  I   \033[0;30m"
        if durianA == 'A':
            block55 = "\033[7;37m  A   \033[0;30m"
        if durianN == 'N':
            block56 = "\033[7;37m  N   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, block41, space, block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', space, space, block42, space, space, space, space, space, space, space, space, block63, space, space)
        print('\n', space, space, block43, space, block51, space, space, space, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, block211, block212, space, space)
        print('\n', space, space, block45, space, block53, space, space, space, space, space, space, block66, space, space)
        print('\n', space, space, block46, space, block54, space, space, block31, block32, block33, block34, block35, block36, block37)
        print('\n', space, space, block47, space, block55, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, space, block56, space, space, space, space, space, space, space, space, space)
        if block51 == '\033[7;37m 5.1  \033[0;30m' :
            print('\n\033[0;31mYou got 5.1 wrong.\033[0;30m')
            points = points - (1/6)
        if block52 == '\033[7;37m 5.2  \033[0;30m' :
            print('\n\033[0;31mYou got 5.2 wrong.\033[0;30m')
            points = points - (1/6)
        if block53 == '\033[7;37m 5.3  \033[0;30m' :
            print('\n\033[0;31mYou got 5.3 wrong.\033[0;30m')
            points = points - (1/6)
        if block54 == '\033[7;37m 5.4  \033[0;30m' :
            print('\n\033[0;31mYou got 5.4 wrong.\033[0;30m')
            points = points - (1/6)
        if block55 == '\033[7;37m 5.5  \033[0;30m' :
            print('\n\033[0;31mYou got 5.5 wrong.\033[0;30m')
            points = points - (1/6)
        if block56 == '\033[7;37m 5.6  \033[0;30m' :
            print('\n\033[0;31mYou got 5.6 wrong.\033[0;30m')
            points = points - (1/6)

    while block61 == '\033[7;37m 6.1  \033[0;30m' or block62 == '\033[7;37m 6.2  \033[0;30m' or block63 == '\033[7;37m 6.3  \033[0;30m' or block64 == '\033[7;37m 6.4  \033[0;30m' or block65 == '\033[7;37m 6.5  \033[0;30m' or block66 == '\033[7;37m 6.6  \033[0;30m' or block67 == '\033[7;37m 6.7  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('6. What is the most expensive spice in the world?')
        saffronS = input('\n\t6.1: ').upper()
        saffronA = input('\t6.2: ').upper()
        saffronF1 = input('\t6.3: ').upper()
        saffronF2 = input('\t6.4: ').upper()
        saffronR = input('\t6.5: ').upper()
        saffronO = input('\t6.6: ').upper()
        saffronN = input('\t6.7: ').upper()
        if saffronS == 'S':
            block61 = "\033[7;37m  S   \033[0;30m"
        if saffronA == 'A':
            block62 = "\033[7;37m  A   \033[0;30m"
        if saffronF1 == 'F':
            block63 = "\033[7;37m  F   \033[0;30m"
        if saffronF2 == 'F':
            block64 = "\033[7;37m  F   \033[0;30m"
        if saffronR == 'R':
            block65 = "\033[7;37m  R   \033[0;30m"
        if saffronO == 'O':
            block66 = "\033[7;37m  O   \033[0;30m"
        if saffronN == 'N':
            block67 = "\033[7;37m  N   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, space, block61, space, space)
        print('\n', space, space, block41, space, block11, block12, block13, block14, block15, block16, block17, block18, block19, space)
        print('\n', space, space, block42, space, space, space, space, space, space, space, space, block63, space, space)
        print('\n', space, space, block43, space, block51, space, space, space, space, space, space, block64, space, space)
        print('\n', block21, block22, block23, block24, block25, block26, block27, block28, block29, block210, block211, block212, space, space)
        print('\n', space, space, block45, space, block53, space, space, space, space, space, space, block66, space, space)
        print('\n', space, space, block46, space, block54, space, space, block31, block32, block33, block34, block35, block36, block37)
        print('\n', space, space, block47, space, block55, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, space, block56, space, space, space, space, space, space, space, space, space)
        if block61 == '\033[7;37m 6.1  \033[0;30m' :
            print('\n\033[0;31mYou got 6.1 wrong.\033[0;30m')
            points = points - (1/7)
        if block62 == '\033[7;37m 6.2  \033[0;30m' :
            print('\n\033[0;31mYou got 6.2 wrong.\033[0;30m')
            points = points - (1/7)
        if block63 == '\033[7;37m 6.3  \033[0;30m' :
            print('\n\033[0;31mYou got 6.3 wrong.\033[0;30m')
            points = points - (1/7)
        if block64 == '\033[7;37m 6.4  \033[0;30m' :
            print('\n\033[0;31mYou got 6.4 wrong.\033[0;30m')
            points = points - (1/7)
        if block65 == '\033[7;37m 6.5  \033[0;30m' :
            print('\n\033[0;31mYou got 6.5 wrong.\033[0;30m')
            points = points - (1/7)
        if block66 == '\033[7;37m 6.6  \033[0;30m' :
            print('\n\033[0;31mYou got 6.6 wrong.\033[0;30m')
            points = points - (1/7)
        if block67 == '\033[7;37m 6.7  \033[0;30m' :
            print('\n\033[0;31mYou got 6.7 wrong.\033[0;30m')
            points = points - (1/7)
    time.sleep(2)
    rewards(points)

def movies(): #question on topic of movies
    block11 = '\033[7;37m 1.1  \033[0;30m'
    block12 = '\033[7;37m 1.2  \033[0;30m'
    block13 = '\033[7;37m 1.3  \033[0;30m'
    block14 = '\033[7;37m 1.4  \033[0;30m'
    block15 = '\033[7;37m 1.5  \033[0;30m'
    block16 = '\033[7;37m 1.6  \033[0;30m'
    block17 = '\033[7;37m 1.7  \033[0;30m'
    block21 = '\033[7;37m 2.1  \033[0;30m'
    block22 = '\033[7;37m 2.2  \033[0;30m'
    block23 = '\033[7;37m 2.3  \033[0;30m'
    block24 = '\033[7;37m 2.4  \033[0;30m'
    block25 = '\033[7;37m 2.5  \033[0;30m'
    block26 = '\033[7;37m 2.6  \033[0;30m'
    block27 = '\033[7;37m 2.7  \033[0;30m'
    block28 = '\033[7;37m 2.8  \033[0;30m'
    block29 = '\033[7;37m 2.9  \033[0;30m'
    block31 = '\033[7;37m 3.1  \033[0;30m'
    block32 = '\033[7;37m 3.2  \033[0;30m'
    block33 = '\033[7;37m 3.3  \033[0;30m'
    block34 = '\033[7;37m 3.4  \033[0;30m'
    block35 = '\033[7;37m 3.5  \033[0;30m'
    block36 = '\033[7;37m 3.6  \033[0;30m'
    block37 = '\033[7;37m 3.7  \033[0;30m'
    block38 = '\033[7;37m 3.8  \033[0;30m'
    block39 = '\033[7;37m 3.9  \033[0;30m'
    block41 = '\033[7;37m 4.1  \033[0;30m'
    block42 = '\033[7;37m 4.2  \033[0;30m'
    block43 = '\033[7;37m 4.3  \033[0;30m'
    block44 = '\033[7;37m 4.4  \033[0;30m'
    block45 = '\033[7;37m 4.5  \033[0;30m'
    block46 = '\033[7;37m 4.6  \033[0;30m'
    block47 = '\033[7;37m 4.7  \033[0;30m'
    block48 = '\033[7;37m 4.8  \033[0;30m'
    block51 = '\033[7;37m 5.1  \033[0;30m'
    block52 = '\033[7;37m 5.2  \033[0;30m'
    block53 = '\033[7;37m 5.3  \033[0;30m'
    block54 = '\033[7;37m 5.4  \033[0;30m'
    block55 = '\033[7;37m 5.5  \033[0;30m'
    block56 = '\033[7;37m 5.6  \033[0;30m'
    block61 = '\033[7;37m 6.1  \033[0;30m'
    block62 = '\033[7;37m 6.2  \033[0;30m'
    block63 = '\033[7;37m 6.3  \033[0;30m'
    block64 = '\033[7;37m 6.4  \033[0;30m'
    block65 = '\033[7;37m 6.5  \033[0;30m'
    block66 = '\033[7;37m 6.6  \033[0;30m'
    block67 = '\033[7;37m 6.7  \033[0;30m'
    block68 = '\033[7;37m 6.8  \033[0;30m'
    block69 = '\033[7;37m 6.9  \033[0;30m'
    space = '\033[7;40m      \033[0;30m'
    points = 6
    time.sleep(1)
    print('\n\t\033[0;34mTopic: Movies\033[0;30m')
    time.sleep(1)
    print('\n\033[4mHorizontal\033[0m')
    print('1. What is the name of the fictional African country in the movie Black Panther?')
    print('2. What do Katniss and Peeta attempt to poison themselves with in The Hunger Games?')
    print('3. What is the name of the male main character in LaLaLand?')
    time.sleep(2)
    print('\n\033[4mVertical\033[0m')
    print('4. What gift does Rose find in her coat pocket at the end of Titanic?')
    print("5. Which of Voldemort's Horcruxes was destroyed last in Harry Potter?")
    print('6. What was the name of the fictional kingdom where Frozen takes place?')
    time.sleep(1)
    print('\n\033[0;33m...Loading...\033[0;30m')
    time.sleep(2)
    print('\n', space, space, space, space, space, space, space, space, space, space, block61, space, space, space)
    print('\n', space, space, space, space, space, space, space, space, space, space, block62, space, space, space)
    print('\n', space, space, space, space, space, space, space, space, space, space, block63, space, space, space)
    print('\n', space, space, space, block41, space, space, block51, space, space, space, block64, space, space, space)
    print('\n', space, space, space, block42, space, block11, block12, block13, block14, block15, block16, block17, space, space)
    print('\n', space, space, space, block43, space, space, block53, space, space, space, block66, space, space, space)
    print('\n', space, space, space, block44, space, block21, block22, block23, block24, block25, block26, block27, block28, block29)
    print('\n', space, space, space, block45, space, space, block55, space, space, space, block68, space, space, space)
    print('\n', block31, block32, block33, block34, block35, block36, block37, block38, block39, space, block69, space, space, space)
    print('\n', space, space, space, block47, space, space, space, space, space, space, space, space, space, space)
    print('\n', space, space, space, block48, space, space, space, space, space, space, space, space, space, space)

    while block11 == '\033[7;37m 1.1  \033[0;30m' or block12 == '\033[7;37m 1.2  \033[0;30m' or block13 == '\033[7;37m 1.3  \033[0;30m' or block14 == '\033[7;37m 1.4  \033[0;30m' or block15 == '\033[7;37m 1.5  \033[0;30m' or block16 == '\033[7;37m 1.6  \033[0;30m' or block17 == '\033[7;37m 1.7  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('1. What is the name of the fictional African country in the movie Black Panther?')
        wakandaW = input('\n\t1.1: ').upper()
        wakandaA1 = input('\t1.2: ').upper()
        wakandaK = input('\t1.3: ').upper()
        wakandaA2 = input('\t1.4: ').upper()
        wakandaN = input('\t1.5: ').upper()
        wakandaD = input('\t1.6: ').upper()
        wakandaA3 = input('\t1.7: ').upper()
        if wakandaW == 'W':
            block11 = "\033[7;37m  W   \033[0;30m"
        if wakandaA1 == 'A':
            block12 = "\033[7;37m  A   \033[0;30m"
        if wakandaK == 'K':
            block13 = "\033[7;37m  K   \033[0;30m"
        if wakandaA2 == 'A':
            block14 = "\033[7;37m  A   \033[0;30m"
        if wakandaN == 'N':
            block15 = "\033[7;37m  N   \033[0;30m"
        if wakandaD == 'D':
            block16 = "\033[7;37m  D   \033[0;30m"
        if wakandaA3 == 'A':
            block17 = "\033[7;37m  A   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, block61, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block62, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block63, space, space, space)
        print('\n', space, space, space, block41, space, space, block51, space, space, space, block64, space, space, space)
        print('\n', space, space, space, block42, space, block11, block12, block13, block14, block15, block16, block17, space, space)
        print('\n', space, space, space, block43, space, space, block53, space, space, space, block66, space, space, space)
        print('\n', space, space, space, block44, space, block21, block22, block23, block24, block25, block26, block27, block28, block29)
        print('\n', space, space, space, block45, space, space, block55, space, space, space, block68, space, space, space)
        print('\n', block31, block32, block33, block34, block35, block36, block37, block38, block39, space, block69, space, space, space)
        print('\n', space, space, space, block47, space, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, block48, space, space, space, space, space, space, space, space, space, space)
        if block11 == '\033[7;37m 1.1  \033[0;30m' :
            print('\n\033[0;31mYou got 1.1 wrong.\033[0;30m')
            points = points - (1/7)
        if block12 == '\033[7;37m 1.2  \033[0;30m' :
            print('\n\033[0;31mYou got 1.2 wrong.\033[0;30m')
            points = points - (1/7)
        if block13 == '\033[7;37m 1.3  \033[0;30m' :
            print('\n\033[0;31mYou got 1.3 wrong.\033[0;30m')
            points = points - (1/7)
        if block14 == '\033[7;37m 1.4  \033[0;30m' :
            print('\n\033[0;31mYou got 1.4 wrong.\033[0;30m')
            points = points - (1/7)
        if block15 == '\033[7;37m 1.5  \033[0;30m' :
            print('\n\033[0;31mYou got 1.5 wrong.\033[0;30m')
            points = points - (1/7)
        if block16 == '\033[7;37m 1.6  \033[0;30m' :
            print('\n\033[0;31mYou got 1.6 wrong.\033[0;30m')
            points = points - (1/7)
        if block17 == '\033[7;37m 1.7  \033[0;30m' :
            print('\n\033[0;31mYou got 1.7 wrong.\033[0;30m')
            points = points - (1/7)

    while block21 == '\033[7;37m 2.1  \033[0;30m' or block22 == '\033[7;37m 2.2  \033[0;30m' or block23 == '\033[7;37m 2.3  \033[0;30m' or block24 == '\033[7;37m 2.4  \033[0;30m' or block25 == '\033[7;37m 2.5  \033[0;30m' or block26 == '\033[7;37m 2.6  \033[0;30m' or block27 == '\033[7;37m 2.7  \033[0;30m' or block28 == '\033[7;37m 2.8  \033[0;30m' or block29 == '\033[7;37m 2.9  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('2. What do Katniss and Peeta attempt to poison themselves with in The Hunger Games?')
        nightlockN = input('\n\t2.1: ').upper()
        nightlockI = input('\t2.2: ').upper()
        nightlockG = input('\t2.3: ').upper()
        nightlockH = input('\t2.4: ').upper()
        nightlockT = input('\t2.5: ').upper()
        nightlockL = input('\t2.6: ').upper()
        nightlockO = input('\t2.7: ').upper()
        nightlockC = input('\t2.8: ').upper()
        nightlockK = input('\t2.9: ').upper()
        if nightlockN == 'N':
            block21 = "\033[7;37m  N   \033[0;30m"
        if nightlockI == 'I':
            block22 = "\033[7;37m  I   \033[0;30m"
        if nightlockG == 'G':
            block23 = "\033[7;37m  G   \033[0;30m"
        if nightlockH == 'H':
            block24 = "\033[7;37m  H   \033[0;30m"
        if nightlockT == 'T':
            block25 = "\033[7;37m  T   \033[0;30m"
        if nightlockL == 'L':
            block26 = "\033[7;37m  L   \033[0;30m"
        if nightlockO == 'O':
            block27 = "\033[7;37m  O   \033[0;30m"
        if nightlockC == 'C':
            block28 = "\033[7;37m  C   \033[0;30m"
        if nightlockK == 'K':
            block29 = "\033[7;37m  K   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, block61, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block62, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block63, space, space, space)
        print('\n', space, space, space, block41, space, space, block51, space, space, space, block64, space, space, space)
        print('\n', space, space, space, block42, space, block11, block12, block13, block14, block15, block16, block17, space, space)
        print('\n', space, space, space, block43, space, space, block53, space, space, space, block66, space, space, space)
        print('\n', space, space, space, block44, space, block21, block22, block23, block24, block25, block26, block27, block28, block29)
        print('\n', space, space, space, block45, space, space, block55, space, space, space, block68, space, space, space)
        print('\n', block31, block32, block33, block34, block35, block36, block37, block38, block39, space, block69, space, space, space)
        print('\n', space, space, space, block47, space, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, block48, space, space, space, space, space, space, space, space, space, space)
        if block21 == '\033[7;37m 2.1  \033[0;30m' :
            print('\n\033[0;31mYou got 2.1 wrong.\033[0;30m')
            points = points - (1/9)
        if block22 == '\033[7;37m 2.2  \033[0;30m' :
            print('\n\033[0;31mYou got 2.2 wrong.\033[0;30m')
            points = points - (1/9)
        if block23 == '\033[7;37m 2.3  \033[0;30m' :
            print('\n\033[0;31mYou got 2.3 wrong.\033[0;30m')
            points = points - (1/9)
        if block24 == '\033[7;37m 2.4  \033[0;30m' :
            print('\n\033[0;31mYou got 2.4 wrong.\033[0;30m')
            points = points - (1/9)
        if block25 == '\033[7;37m 2.5  \033[0;30m' :
            print('\n\033[0;31mYou got 2.5 wrong.\033[0;30m')
            points = points - (1/9)
        if block26 == '\033[7;37m 2.6  \033[0;30m' :
            print('\n\033[0;31mYou got 2.6 wrong.\033[0;30m')
            points = points - (1/9)
        if block27 == '\033[7;37m 2.7  \033[0;30m' :
            print('\n\033[0;31mYou got 2.7 wrong.\033[0;30m')
            points = points - (1/9)
        if block28 == '\033[7;37m 2.8  \033[0;30m' :
            print('\n\033[0;31mYou got 2.8 wrong.\033[0;30m')
            points = points - (1/9)
        if block29 == '\033[7;37m 2.9  \033[0;30m' :
            print('\n\033[0;31mYou got 2.9 wrong.\033[0;30m')
            points = points - (1/9)

    while block31 == '\033[7;37m 3.1  \033[0;30m' or block32 == '\033[7;37m 3.2  \033[0;30m' or block33 == '\033[7;37m 3.3  \033[0;30m' or block34 == '\033[7;37m 3.4  \033[0;30m' or block35 == '\033[7;37m 3.5  \033[0;30m' or block36 == '\033[7;37m 3.6  \033[0;30m' or block37 == '\033[7;37m 3.7  \033[0;30m' or block38 == '\033[7;37m 3.8  \033[0;30m' or block39 == '\033[7;37m 3.9  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mHorizontal\033[0m')
        print('3. What is the name of the male main character in LaLaLand?')
        sebastianS1 = input('\n\t3.1: ').upper()
        sebastianE = input('\t3.2: ').upper()
        sebastianB = input('\t3.3: ').upper()
        sebastianA1 = input('\t3.4: ').upper()
        sebastianS2 = input('\t3.5: ').upper()
        sebastianT = input('\t3.6: ').upper()
        sebastianI = input('\t3.7: ').upper()
        sebastianA2 = input('\t3.8: ').upper()
        sebastianN = input('\t3.9: ').upper()
        if sebastianS1 == 'S':
            block31 = "\033[7;37m  S   \033[0;30m"
        if sebastianE == 'E':
            block32 = "\033[7;37m  E   \033[0;30m"
        if sebastianB == 'B':
            block33 = "\033[7;37m  B   \033[0;30m"
        if sebastianA1 == 'A':
            block34 = "\033[7;37m  A   \033[0;30m"
        if sebastianS2 == 'S':
            block35 = "\033[7;37m  S   \033[0;30m"
        if sebastianT == 'T':
            block36 = "\033[7;37m  T   \033[0;30m"
        if sebastianI == 'I':
            block37 = "\033[7;37m  I   \033[0;30m"
        if sebastianA2 == 'A':
            block38 = "\033[7;37m  A   \033[0;30m"
        if sebastianN == 'N':
            block39 = "\033[7;37m  N   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, block61, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block62, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block63, space, space, space)
        print('\n', space, space, space, block41, space, space, block51, space, space, space, block64, space, space, space)
        print('\n', space, space, space, block42, space, block11, block12, block13, block14, block15, block16, block17, space, space)
        print('\n', space, space, space, block43, space, space, block53, space, space, space, block66, space, space, space)
        print('\n', space, space, space, block44, space, block21, block22, block23, block24, block25, block26, block27, block28, block29)
        print('\n', space, space, space, block45, space, space, block55, space, space, space, block68, space, space, space)
        print('\n', block31, block32, block33, block34, block35, block36, block37, block38, block39, space, block69, space, space, space)
        print('\n', space, space, space, block47, space, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, block48, space, space, space, space, space, space, space, space, space, space)
        if block31 == '\033[7;37m 3.1  \033[0;30m' :
            print('\n\033[0;31mYou got 3.1 wrong.\033[0;30m')
            points = points - (1/9)
        if block32 == '\033[7;37m 3.2  \033[0;30m' :
            print('\n\033[0;31mYou got 3.2 wrong.\033[0;30m')
            points = points - (1/9)
        if block33 == '\033[7;37m 3.3  \033[0;30m' :
            print('\n\033[0;31mYou got 3.3 wrong.\033[0;30m')
            points = points - (1/9)
        if block34 == '\033[7;37m 3.4  \033[0;30m' :
            print('\n\033[0;31mYou got 3.4 wrong.\033[0;30m')
            points = points - (1/9)
        if block35 == '\033[7;37m 3.5  \033[0;30m' :
            print('\n\033[0;31mYou got 3.5 wrong.\033[0;30m')
            points = points - (1/9)
        if block36 == '\033[7;37m 3.6  \033[0;30m' :
            print('\n\033[0;31mYou got 3.6 wrong.\033[0;30m')
            points = points - (1/9)
        if block37 == '\033[7;37m 3.7  \033[0;30m' :
            print('\n\033[0;31mYou got 3.7 wrong.\033[0;30m')
            points = points - (1/9)
        if block38 == '\033[7;37m 3.8  \033[0;30m' :
            print('\n\033[0;31mYou got 3.8 wrong.\033[0;30m')
            points = points - (1/9)
        if block39 == '\033[7;37m 3.9  \033[0;30m' :
            print('\n\033[0;31mYou got 3.9 wrong.\033[0;30m')
            points = points - (1/9)

    while block41 == '\033[7;37m 4.1  \033[0;30m' or block42 == '\033[7;37m 4.2  \033[0;30m' or block43 == '\033[7;37m 4.3  \033[0;30m' or block44 == '\033[7;37m 4.4  \033[0;30m' or block45 == '\033[7;37m 4.5  \033[0;30m' or block46 == '\033[7;37m 4.6  \033[0;30m' or block47 == '\033[7;37m 4.7  \033[0;30m' or block48 == '\033[7;37m 4.8  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('4. What gift does Rose find in her coat pocket at the end of Titanic?')
        necklaceN = input('\n\t4.1: ').upper()
        necklaceE1 = input('\t4.2: ').upper()
        necklaceC1 = input('\t4.3: ').upper()
        necklaceK = input('\t4.4: ').upper()
        necklaceL = input('\t4.5: ').upper()
        necklaceA = input('\t4.6: ').upper()
        necklaceC2 = input('\t4.7: ').upper()
        necklaceE2 = input('\t4.8: ').upper()
        if necklaceN == 'N':
            block41 = "\033[7;37m  N   \033[0;30m"
        if necklaceE1 == 'E':
            block42 = "\033[7;37m  E   \033[0;30m"
        if necklaceC1 == 'C':
            block43 = "\033[7;37m  C   \033[0;30m"
        if necklaceK == 'K':
            block44 = "\033[7;37m  K   \033[0;30m"
        if necklaceL == 'L':
            block45 = "\033[7;37m  L   \033[0;30m"
        if necklaceA == 'A':
            block46 = "\033[7;37m  A   \033[0;30m"
        if necklaceC2 == 'C':
            block47 = "\033[7;37m  C   \033[0;30m"
        if necklaceE2 == 'E':
            block48 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, block61, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block62, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block63, space, space, space)
        print('\n', space, space, space, block41, space, space, block51, space, space, space, block64, space, space, space)
        print('\n', space, space, space, block42, space, block11, block12, block13, block14, block15, block16, block17, space, space)
        print('\n', space, space, space, block43, space, space, block53, space, space, space, block66, space, space, space)
        print('\n', space, space, space, block44, space, block21, block22, block23, block24, block25, block26, block27, block28, block29)
        print('\n', space, space, space, block45, space, space, block55, space, space, space, block68, space, space, space)
        print('\n', block31, block32, block33, block34, block35, block36, block37, block38, block39, space, block69, space, space, space)
        print('\n', space, space, space, block47, space, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, block48, space, space, space, space, space, space, space, space, space, space)
        if block41 == '\033[7;37m 4.1  \033[0;30m' :
            print('\n\033[0;31mYou got 4.1 wrong.\033[0;30m')
            points = points - (1/8)
        if block42 == '\033[7;37m 4.2  \033[0;30m' :
            print('\n\033[0;31mYou got 4.2 wrong.\033[0;30m')
            points = points - (1/8)
        if block43 == '\033[7;37m 4.3  \033[0;30m' :
            print('\n\033[0;31mYou got 4.3 wrong.\033[0;30m')
            points = points - (1/8)
        if block44 == '\033[7;37m 4.4  \033[0;30m' :
            print('\n\033[0;31mYou got 4.4 wrong.\033[0;30m')
            points = points - (1/8)
        if block45 == '\033[7;37m 4.5  \033[0;30m' :
            print('\n\033[0;31mYou got 4.5 wrong.\033[0;30m')
            points = points - (1/8)
        if block46 == '\033[7;37m 4.6  \033[0;30m' :
            print('\n\033[0;31mYou got 4.6 wrong.\033[0;30m')
            points = points - (1/8)
        if block47 == '\033[7;37m 4.7  \033[0;30m' :
            print('\n\033[0;31mYou got 4.7 wrong.\033[0;30m')
            points = points - (1/8)
        if block48 == '\033[7;37m 4.8  \033[0;30m' :
            print('\n\033[0;31mYou got 4.8 wrong.\033[0;30m')
            points = points - (1/8)

    while block51 == '\033[7;37m 5.1  \033[0;30m' or block52 == '\033[7;37m 5.2  \033[0;30m' or block53 == '\033[7;37m 5.3  \033[0;30m' or block54 == '\033[7;37m 5.4  \033[0;30m' or block55 == '\033[7;37m 5.5  \033[0;30m' or block56 == '\033[7;37m 5.6  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print("5. Which of Voldemort's Horcruxes was destroyed last in Harry Potter?")
        naginiN1 = input('\n\t5.1: ').upper()
        naginiA = input('\t5.2: ').upper()
        naginiG = input('\t5.3: ').upper()
        naginiI1 = input('\t5.4: ').upper()
        naginiN2 = input('\t5.5: ').upper()
        naginiI2 = input('\t5.6: ').upper()
        if naginiN1 == 'N':
            block51 = "\033[7;37m  N   \033[0;30m"
        if naginiA == 'A':
            block52 = "\033[7;37m  A   \033[0;30m"
        if naginiG == 'G':
            block53 = "\033[7;37m  G   \033[0;30m"
        if naginiI1 == 'I':
            block54 = "\033[7;37m  I   \033[0;30m"
        if naginiN2 == 'N':
            block55 = "\033[7;37m  N   \033[0;30m"
        if naginiI2 == 'I':
            block56 = "\033[7;37m  I   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, block61, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block62, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block63, space, space, space)
        print('\n', space, space, space, block41, space, space, block51, space, space, space, block64, space, space, space)
        print('\n', space, space, space, block42, space, block11, block12, block13, block14, block15, block16, block17, space, space)
        print('\n', space, space, space, block43, space, space, block53, space, space, space, block66, space, space, space)
        print('\n', space, space, space, block44, space, block21, block22, block23, block24, block25, block26, block27, block28, block29)
        print('\n', space, space, space, block45, space, space, block55, space, space, space, block68, space, space, space)
        print('\n', block31, block32, block33, block34, block35, block36, block37, block38, block39, space, block69, space, space, space)
        print('\n', space, space, space, block47, space, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, block48, space, space, space, space, space, space, space, space, space, space)
        if block51 == '\033[7;37m 5.1  \033[0;30m' :
            print('\n\033[0;31mYou got 5.1 wrong.\033[0;30m')
            points = points - (1/6)
        if block52 == '\033[7;37m 5.2  \033[0;30m' :
            print('\n\033[0;31mYou got 5.2 wrong.\033[0;30m')
            points = points - (1/6)
        if block53 == '\033[7;37m 5.3  \033[0;30m' :
            print('\n\033[0;31mYou got 5.3 wrong.\033[0;30m')
            points = points - (1/6)
        if block54 == '\033[7;37m 5.4  \033[0;30m' :
            print('\n\033[0;31mYou got 5.4 wrong.\033[0;30m')
            points = points - (1/6)
        if block55 == '\033[7;37m 5.5  \033[0;30m' :
            print('\n\033[0;31mYou got 5.5 wrong.\033[0;30m')
            points = points - (1/6)
        if block56 == '\033[7;37m 5.6  \033[0;30m' :
            print('\n\033[0;31mYou got 5.6 wrong.\033[0;30m')
            points = points - (1/6)

    while block61 == '\033[7;37m 6.1  \033[0;30m' or block62 == '\033[7;37m 6.2  \033[0;30m' or block63 == '\033[7;37m 6.3  \033[0;30m' or block64 == '\033[7;37m 6.4  \033[0;30m' or block65 == '\033[7;37m 6.5  \033[0;30m' or block66 == '\033[7;37m 6.6  \033[0;30m' or block67 == '\033[7;37m 6.7  \033[0;30m' or block68 == '\033[7;37m 6.8  \033[0;30m' or block69 == '\033[7;37m 6.9  \033[0;30m':
        time.sleep(1)
        print('\n\033[4mVertical\033[0m')
        print('6. What was the name of the fictional kingdom where Frozen takes place?')
        arendelleA = input('\n\t6.1: ').upper()
        arendelleR = input('\t6.2: ').upper()
        arendelleE1 = input('\t6.3: ').upper()
        arendelleN = input('\t6.4: ').upper()
        arendelleD = input('\t6.5: ').upper()
        arendelleE2 = input('\t6.6: ').upper()
        arendelleL1 = input('\t6.7: ').upper()
        arendelleL2 = input('\t6.8: ').upper()
        arendelleE3 = input('\t6.9: ').upper()
        if arendelleA == 'A':
            block61 = "\033[7;37m  A   \033[0;30m"
        if arendelleR == 'R':
            block62 = "\033[7;37m  R   \033[0;30m"
        if arendelleE1 == 'E':
            block63 = "\033[7;37m  E   \033[0;30m"
        if arendelleN == 'N':
            block64 = "\033[7;37m  N   \033[0;30m"
        if arendelleD == 'D':
            block65 = "\033[7;37m  D   \033[0;30m"
        if arendelleE2 == 'E':
            block66 = "\033[7;37m  E   \033[0;30m"
        if arendelleL1 == 'L':
            block67 = "\033[7;37m  L   \033[0;30m"
        if arendelleL2 == 'L':
            block68 = "\033[7;37m  L   \033[0;30m"
        if arendelleE3 == 'E':
            block69 = "\033[7;37m  E   \033[0;30m"
        time.sleep(1)
        print('\n\033[0;33m...Loading...\033[0;30m')
        time.sleep(2)
        print('\n', space, space, space, space, space, space, space, space, space, space, block61, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block62, space, space, space)
        print('\n', space, space, space, space, space, space, space, space, space, space, block63, space, space, space)
        print('\n', space, space, space, block41, space, space, block51, space, space, space, block64, space, space, space)
        print('\n', space, space, space, block42, space, block11, block12, block13, block14, block15, block16, block17, space, space)
        print('\n', space, space, space, block43, space, space, block53, space, space, space, block66, space, space, space)
        print('\n', space, space, space, block44, space, block21, block22, block23, block24, block25, block26, block27, block28, block29)
        print('\n', space, space, space, block45, space, space, block55, space, space, space, block68, space, space, space)
        print('\n', block31, block32, block33, block34, block35, block36, block37, block38, block39, space, block69, space, space, space)
        print('\n', space, space, space, block47, space, space, space, space, space, space, space, space, space, space)
        print('\n', space, space, space, block48, space, space, space, space, space, space, space, space, space, space)
        if block61 == '\033[7;37m 6.1  \033[0;30m' :
            print('\n\033[0;31mYou got 6.1 wrong.\033[0;30m')
            points = points - (1/9)
        if block62 == '\033[7;37m 6.2  \033[0;30m' :
            print('\n\033[0;31mYou got 6.2 wrong.\033[0;30m')
            points = points - (1/9)
        if block63 == '\033[7;37m 6.3  \033[0;30m' :
            print('\n\033[0;31mYou got 6.3 wrong.\033[0;30m')
            points = points - (1/9)
        if block64 == '\033[7;37m 6.4  \033[0;30m' :
            print('\n\033[0;31mYou got 6.4 wrong.\033[0;30m')
            points = points - (1/9)
        if block65 == '\033[7;37m 6.5  \033[0;30m' :
            print('\n\033[0;31mYou got 6.5 wrong.\033[0;30m')
            points = points - (1/9)
        if block66 == '\033[7;37m 6.6  \033[0;30m' :
            print('\n\033[0;31mYou got 6.6 wrong.\033[0;30m')
            points = points - (1/9)
        if block67 == '\033[7;37m 6.7  \033[0;30m' :
            print('\n\033[0;31mYou got 6.7 wrong.\033[0;30m')
            points = points - (1/9)
        if block68 == '\033[7;37m 6.8  \033[0;30m' :
            print('\n\033[0;31mYou got 6.8 wrong.\033[0;30m')
            points = points - (1/9)
        if block69 == '\033[7;37m 6.9  \033[0;30m' :
            print('\n\033[0;31mYou got 6.9 wrong.\033[0;30m')
            points = points - (1/9)
    time.sleep(2)
    rewards(points)

def cp3(): #question 3
    print('\n\033[0;34m################### GAME STARTS ###################\033[0;30m')
    time.sleep(1)
    print('\033[0;33mSpecial question!\033[0;30m \nYou can choose a theme for the topic of the puzzle.')
    print('Choose a theme:- \033[0;34m\n\t1. Animals\n\t2. Food\n\t3. Movies\033[0;30m')
    #loop to keep asking player to enter the right number to choose a theme
    while True:
        #assign the input given to a variable
        theme = input('Enter a number: ')
        if theme == '1': #if 1 chosen, the animals function will run and the q3 function breaks
            animals()
            break
        elif theme == '2': #if 2 chosen, the food function will run and the q3 function breaks
            food()
            break
        elif theme == '3': #if 3 chosen, the movies function will run and the q3 function breaks
            movies()
            break
        else: #if other characters or numbers given, a message to enter the right number will display
            print('Please enter a number from 1 to 3.')


def execute():
    cpInstructions() #display instructions
    diffQs = [cp1, cp2, cp3] #put all possible questins in a list and assigning it to a variable
    random.choice(diffQs)() #choosing a random question from the list

    # crossword puzzle end
    
