# decryptify start

import time
import random
# setting the first set of keys
k1 = {'a': '@',
       'b': '6',
       'c': '(',
       'd': '&',
       'e': '3',
       'f': '#',
       'g': '?',
       'h': '=',
       'i': '!',
       'j': '/',
       'k': '[',
       'l': '1',
       'm': '%',
       'n': '^',
       'o': '.',
       'p': '>',
       'q': '9',
       'r': '<',
       's': '$',
       't': '+',
       'u': ':',
       'v': '}',
       'w': '~',
       'x': '*',
       'y': '7',
       'z': '2',
       '0': 'o',
       '1': 'i',
       '2': 's',
       '3': 'e',
       '4': 'a',
       '5': 'b',
       '6': 'q',
       '7': 't',
       '8': 'd',
       '9': 'p',
       ' ': '_',
       '-': '-',
       ',': '`',
       'H': 'A',
       'B': 'L',
       'D': 'W',
       '.': 'R'}
# setting the second set of keys
k2 = {'a': '$',
       'b': '}',
       'c': '@',
       'd': '^',
       'e': '-',
       'f': '?',
       'g': '4',
       'h': '=',
       'i': 'Q',
       'j': '2',
       'k': '5',
       'l': 'X',
       'm': '#',
       'n': '3',
       'o': '[',
       'p': '8',
       'q': '<',
       'r': '1',
       's': '~',
       't': '6',
       'u': 'j',
       'v': '_',
       'w': 'f',
       'x': '+',
       'y': '\\',
       'z': '9',
       '0': 'Y',
       '1': ';',
       '2': 'd',
       '3': '7',
       '4': '&',
       '5': '(',
       '6': '!',
       '7': '>',
       '8': '*',
       '9': 's',
       ' ': '%',
       '-': '`',
       ',': '/',
       'H': 'L',
       'B': 'R',
       'D': 'A',
       '.': 'W'}
# assigning the original/decrypted messages to their variables
oneD = "free outpatient treatment and medical treatment excluding x-ray and surgical charges, and second-class wards for a period of 4 months."
twoD = "free Hepatitis B prevention injections."
threeD = "free outpatient treatment and medical treatment, and second-class wards for a period of 4 months."
fourD = "free 1-year outpatient treatment and second-class wards for a 6-month period."
fiveD = "free 2-year outpatient treatment and medical treatment, and second-class wards for a 1-year period."
sixD = "free outpatient treatment and medical treatment, and second-class wards for a period of 3 years."
sevenD = "free outpatient treatment and medical treatment, and second-class wards for a period of 3 years."
eightD = "free outpatient treatment and medical treatment, and first-class wards for a period of 4 years."
nineD = "free outpatient treatment and medical treatment, and first-class wards for a period of 6 years."
tenD = "free outpatient treatment and first-class medical treatment and wards for 10 years, and second-class wards of life after 10 years in first-class ward."
# changing the messages to encrypted messages and assigning them to their variables
oneE = k1['f']+k1['r']+k1['e']+k1['e']+k1[' ']+k1['o']+k1['u']+k1['t']+k1['p']+k1['a']+k1['t']+k1['i']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['m']+k1['e']+k1['d']+k1['i']+k1['c']+k1['a']+k1['l']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['e']+k1['x']+k1['c']+k1['l']+k1['u']+k1['d']+k1['i']+k1['n']+k1['g']+k1[' ']+k1['x']+k1['-']+k1['r']+k1['a']+k1['y']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['s']+k1['u']+k1['r']+k1['g']+k1['i']+k1['c']+k1['a']+k1['l']+k1[' ']+k1['c']+k1['h']+k1['a']+k1['r']+k1['g']+k1['e']+k1['s']+k1[',']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['s']+k1['e']+k1['c']+k1['o']+k1['n']+k1['d']+k1['-']+k1['c']+k1['l']+k1['a']+k1['s']+k1['s']+k1[' ']+k1['w']+k1['a']+k1['r']+k1['d']+k1['s']+k1[' ']+k1['f']+k1['o']+k1['r']+k1[' ']+k1['a']+k1[' ']+k1['p']+k1['e']+k1['r']+k1['i']+k1['o']+k1['d']+k1[' ']+k1['o']+k1['f']+k1[' ']+k1['4']+k1[' ']+k1['m']+k1['o']+k1['n']+k1['t']+k1['h']+k1['s']+k1['.']
twoE = k2['f']+k2['r']+k2['e']+k2['e']+k2[' ']+k2['H']+k2['e']+k2['p']+k2['a']+k2['t']+k2['i']+k2['t']+k2['i']+k2['s']+k2[' ']+k2['B']+k2[' ']+k2['p']+k2['r']+k2['e']+k2['v']+k2['e']+k2['n']+k2['t']+k2['i']+k2['o']+k2['n']+k2[' ']+k2['i']+k2['n']+k2['j']+k2['e']+k2['c']+k2['t']+k2['i']+k2['o']+k2['n']+k2['s']+k2['.']
threeE = k1['f']+k1['r']+k1['e']+k1['e']+k1[' ']+k1['o']+k1['u']+k1['t']+k1['p']+k1['a']+k1['t']+k1['i']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['m']+k1['e']+k1['d']+k1['i']+k1['c']+k1['a']+k1['l']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[',']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['s']+k1['e']+k1['c']+k1['o']+k1['n']+k1['d']+k1['-']+k1['c']+k1['l']+k1['a']+k1['s']+k1['s']+k1[' ']+k1['w']+k1['a']+k1['r']+k1['d']+k1['s']+k1[' ']+k1['f']+k1['o']+k1['r']+k1[' ']+k1['a']+k1[' ']+k1['p']+k1['e']+k1['r']+k1['i']+k1['o']+k1['d']+k1[' ']+k1['o']+k1['f']+k1[' ']+k1['4']+k1[' ']+k1['m']+k1['o']+k1['n']+k1['t']+k1['h']+k1['s']+k1['.']
fourE = k2['f']+k2['r']+k2['e']+k2['e']+k2[' ']+k2['1']+k2['-']+k2['y']+k2['e']+k2['a']+k2['r']+k2[' ']+k2['o']+k2['u']+k2['t']+k2['p']+k2['a']+k2['t']+k2['i']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['t']+k2['r']+k2['e']+k2['a']+k2['t']+k2['m']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['s']+k2['e']+k2['c']+k2['o']+k2['n']+k2['d']+k2['-']+k2['c']+k2['l']+k2['a']+k2['s']+k2['s']+k2[' ']+k2['w']+k2['a']+k2['r']+k2['d']+k2['s']+k2[' ']+k2['f']+k2['o']+k2['r']+k2[' ']+k2['a']+k2[' ']+k2['6']+k2['-']+k2['m']+k2['o']+k2['n']+k2['t']+k2['h']+k2[' ']+k2['p']+k2['e']+k2['r']+k2['i']+k2['o']+k2['d']+k2['.']
fiveE = k1['f']+k1['r']+k1['e']+k1['e']+k1[' ']+k1['2']+k1['-']+k1['y']+k1['e']+k1['a']+k1['r']+k1[' ']+k1['o']+k1['u']+k1['t']+k1['p']+k1['a']+k1['t']+k1['i']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['m']+k1['e']+k1['d']+k1['i']+k1['c']+k1['a']+k1['l']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[',']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['s']+k1['e']+k1['c']+k1['o']+k1['n']+k1['d']+k1['-']+k1['c']+k1['l']+k1['a']+k1['s']+k1['s']+k1[' ']+k1['w']+k1['a']+k1['r']+k1['d']+k1['s']+k1[' ']+k1['f']+k1['o']+k1['r']+k1[' ']+k1['a']+k1[' ']+k1['1']+k1['-']+k1['y']+k1['e']+k1['a']+k1['r']+k1[' ']+k1['p']+k1['e']+k1['r']+k1['i']+k1['o']+k1['d']+k1['.']
sixE = k2['f']+k2['r']+k2['e']+k2['e']+k2[' ']+k2['o']+k2['u']+k2['t']+k2['p']+k2['a']+k2['t']+k2['i']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['t']+k2['r']+k2['e']+k2['a']+k2['t']+k2['m']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['m']+k2['e']+k2['d']+k2['i']+k2['c']+k2['a']+k2['l']+k2[' ']+k2['t']+k2['r']+k2['e']+k2['a']+k2['t']+k2['m']+k2['e']+k2['n']+k2['t']+k2[',']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['s']+k2['e']+k2['c']+k2['o']+k2['n']+k2['d']+k2['-']+k2['c']+k2['l']+k2['a']+k2['s']+k2['s']+k2[' ']+k2['w']+k2['a']+k2['r']+k2['d']+k2['s']+k2[' ']+k2['f']+k2['o']+k2['r']+k2[' ']+k2['a']+k2[' ']+k2['p']+k2['e']+k2['r']+k2['i']+k2['o']+k2['d']+k2[' ']+k2['o']+k2['f']+k2[' ']+k2['3']+k2[' ']+k2['y']+k2['e']+k2['a']+k2['r']+k2['s']+k2['.']
sevenE = k1['f']+k1['r']+k1['e']+k1['e']+k1[' ']+k1['o']+k1['u']+k1['t']+k1['p']+k1['a']+k1['t']+k1['i']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['m']+k1['e']+k1['d']+k1['i']+k1['c']+k1['a']+k1['l']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[',']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['s']+k1['e']+k1['c']+k1['o']+k1['n']+k1['d']+k1['-']+k1['c']+k1['l']+k1['a']+k1['s']+k1['s']+k1[' ']+k1['w']+k1['a']+k1['r']+k1['d']+k1['s']+k1[' ']+k1['f']+k1['o']+k1['r']+k1[' ']+k1['a']+k1[' ']+k1['p']+k1['e']+k1['r']+k1['i']+k1['o']+k1['d']+k1[' ']+k1['o']+k1['f']+k1[' ']+k1['3']+k1[' ']+k1['y']+k1['e']+k1['a']+k1['r']+k1['s']+k1['.']
eightE = k2['f']+k2['r']+k2['e']+k2['e']+k2[' ']+k2['o']+k2['u']+k2['t']+k2['p']+k2['a']+k2['t']+k2['i']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['t']+k2['r']+k2['e']+k2['a']+k2['t']+k2['m']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['m']+k2['e']+k2['d']+k2['i']+k2['c']+k2['a']+k2['l']+k2[' ']+k2['t']+k2['r']+k2['e']+k2['a']+k2['t']+k2['m']+k2['e']+k2['n']+k2['t']+k2[',']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['f']+k2['i']+k2['r']+k2['s']+k2['t']+k2['-']+k2['c']+k2['l']+k2['a']+k2['s']+k2['s']+k2[' ']+k2['w']+k2['a']+k2['r']+k2['d']+k2['s']+k2[' ']+k2['f']+k2['o']+k2['r']+k2[' ']+k2['a']+k2[' ']+k2['p']+k2['e']+k2['r']+k2['i']+k2['o']+k2['d']+k2[' ']+k2['o']+k2['f']+k2[' ']+k2['4']+k2[' ']+k2['y']+k2['e']+k2['a']+k2['r']+k2['s']+k2['.']
nineE = k1['f']+k1['r']+k1['e']+k1['e']+k1[' ']+k1['o']+k1['u']+k1['t']+k1['p']+k1['a']+k1['t']+k1['i']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['m']+k1['e']+k1['d']+k1['i']+k1['c']+k1['a']+k1['l']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[',']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['f']+k1['i']+k1['r']+k1['s']+k1['t']+k1['-']+k1['c']+k1['l']+k1['a']+k1['s']+k1['s']+k1[' ']+k1['w']+k1['a']+k1['r']+k1['d']+k1['s']+k1[' ']+k1['f']+k1['o']+k1['r']+k1[' ']+k1['a']+k1[' ']+k1['p']+k1['e']+k1['r']+k1['i']+k1['o']+k1['d']+k1[' ']+k1['o']+k1['f']+k1[' ']+k1['6']+k1[' ']+k1['y']+k1['e']+k1['a']+k1['r']+k1['s']+k1['.']
tenE = k2['f']+k2['r']+k2['e']+k2['e']+k2[' ']+k2['o']+k2['u']+k2['t']+k2['p']+k2['a']+k2['t']+k2['i']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['t']+k2['r']+k2['e']+k2['a']+k2['t']+k2['m']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['f']+k2['i']+k2['r']+k2['s']+k2['t']+k2['-']+k2['c']+k2['l']+k2['a']+k2['s']+k2['s']+k2[' ']+k2['m']+k2['e']+k2['d']+k2['i']+k2['c']+k2['a']+k2['l']+k2[' ']+k2['t']+k2['r']+k2['e']+k2['a']+k2['t']+k2['m']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['w']+k2['a']+k2['r']+k2['d']+k2['s']+k2[' ']+k2['f']+k2['o']+k2['r']+k2[' ']+k2['1']+k2['0']+k2[' ']+k2['y']+k2['e']+k2['a']+k2['r']+k2['s']+k2[',']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['s']+k2['e']+k2['c']+k2['o']+k2['n']+k2['d']+k2['-']+k2['c']+k2['l']+k2['a']+k2['s']+k2['s']+k2[' ']+k2['w']+k2['a']+k2['r']+k2['d']+k2['s']+k2[' ']+k2['o']+k2['f']+k2[' ']+k2['l']+k2['i']+k2['f']+k2['e']+k2[' ']+k2['a']+k2['f']+k2['t']+k2['e']+k2['r']+k2[' ']+k2['1']+k2['0']+k2[' ']+k2['y']+k2['e']+k2['a']+k2['r']+k2['s']+k2[' ']+k2['i']+k2['n']+k2[' ']+k2['f']+k2['i']+k2['r']+k2['s']+k2['t']+k2['-']+k2['c']+k2['l']+k2['a']+k2['s']+k2['s']+k2[' ']+k2['w']+k2['a']+k2['r']+k2['d']+k2['.']

def delay(x):  # function to make each character in a string appear one by one
    print('\n')
    for char in x:
        print(char, end='', flush=True)  # print one character from the string
        time.sleep(.05)  # wait for the set period, then repeats

def dExecute():  # the main function
    # display instructions
    print('\033[1;34m********************************************************************')
    print('\t\t\t    DECRYPTIFY')
    print('********************************************************************\033[0;30m')
    time.sleep(1)
    print('Here are the instructions:-')
    time.sleep(1)
    print('1. You will be given an encrypted text.')
    time.sleep(2)
    print('2. You need to decrypt the text correctly.')
    time.sleep(2)
    print('3. The key to decrypt the text can be found by using the hints given for each character.')
    time.sleep(2)
    print('4. All letters are in lowercase unless stated otherwise.')
    time.sleep(2)
    print('\n\033[0;33m...Loading...\033[0;30m')
    time.sleep(2)
    print('\nHere is the encrypted text:-')
    time.sleep(1)
    # making a list of all the possible messages and assigning it to a global variable
    global msg
    msg = [oneE, twoE, threeE, fourE, fiveE, sixE, sevenE, eightE, nineE, tenE]
    global play
    # choosing a random message from the list and setting it to variable 'play'
    play = random.choice(msg)
    # printing different text for each choice
    if play == oneE:
        print('\nDonors who have donated 1 time are privileged to get :\n')
        time.sleep(1)
    elif play == twoE:
        print('\nDonors who have donated 2 times within 12 months are privileged to get :\n')
        time.sleep(1)
    elif play == threeE:
        print('\nDonors who have donated 2 to 5 times are privileged to get :\n')
        time.sleep(1)
    elif play == fourE:
        print('\nDonors who have donated 6 to 10 times are privileged to get :\n')
        time.sleep(1)
    elif play == fiveE:
        print('\nDonors who have donated 11 to 15 times are privileged to get :\n')
        time.sleep(1)
    elif play == sixE:
        print('\nDonors who have donated 16 to 20 times are privileged to get :\n')
        time.sleep(1)
    elif play == sevenE:
        print('\nDonors who have donated 21 to 30 times are privileged to get :\n')
        time.sleep(1)
    elif play == eightE:
        print('\nDonors who have donated 31 to 40 times are privileged to get :\n')
        time.sleep(1)
    elif play == nineE:
        print('\nDonors who have donated 41 to 50 times are privileged to get :\n')
        time.sleep(1)
    elif play == tenE:
        print('\nDonors who have donated over 50 times are privileged to get :\n')
        time.sleep(1)
    # executing the delay() function to display the encrypted message
    delay(play)
    time.sleep(2)
    print('\nHere are the hints:-\n')
    time.sleep(1)
    if play == oneE or play == threeE or play == fiveE or play == sevenE or play == nineE:
        k1hint()  # if either message one, three, five, seven or nine is chosen, function k1hint() is executed to display hints
    elif play == twoE or play == fourE or play == sixE or play == eightE or play == tenE:
        k2hint()  # if either message two, four, six, eight or ten is chosen, funtion k2hint() is executed to display hints
    global message
    message = ans(play)  # executing the ans() function with the item of 'play' as the argument and assigning it to variable 'message'
    reward()  # executing the reward() function to determine whether user get hints for main question

def k1hint():  # function to display hints to help user get the key
    print('@ = the first letter of the alphabet')  #a
    print('! = is a word on its own, and it represents yourself')  #i
    print('# = students hate to see it on their exam paper')  #f
    print('$ = added at the end of plural nouns')  #s
    print('% = appears twice in mama, once in granmy and none in aunt')  #m
    print('^ = common letter in none, nope, nada')  #n
    print('& = the first letter of the king of the fruits')  #d
    print('* = the formerly Twitter app now associates itself with this letter')  #x
    print('( = the letter that rhymes with see')  #c
    print('_ = the default character the split function use to split strings in python')  #' '
    print('+ = the letter in lowercase looks exactly like the symbol')  #t
    print('1 = it appears long and in love')  #l
    print('2 = the letter that represents sleep')  #z
    print("3 = 'Anne with an ___")  #e
    print('6 = couples call each other this in short')  #b
    print('7 = kenapa in english')  #y
    print('9 = lowercase version of a balloon being pricked by a needle')  #q
    print('- = symbol for minus')  #-
    print('= = the consonant in laughs')  #h
    print('q = number of Ive members')  #6
    print('e = the number that rhymes with tree')  #3
    print('t = Snow White and the ___ Dwarfs')  #7
    print('i = what Rose calls her fans')  #1
    print('o = the digit that appears the most in 1 to 1000')  #0
    print('p = in emergencies, this number comes to mind')  #9
    print('s = the number of a couple')  #2
    print('d = the infinity number')  #8
    print('b = One Direction but it is ___ Direction now')  #5
    print('W = this uppercase letter is often used as the mouth of the big smile in text emoji')  #D
    print('R = fullstop')  #.
    print('A = still the consonant in laughs but its a big laugh')  #H
    print('L = an uppercase letter that rhymes with the second half of baby')  #B
    print('/ = the video editing style trend among malaysian teens that often involves flashing lights and EDM music')  #j
    print('[ = they start in kids and end in work')  #k
    print('. = the name of the main character in the movie Home')
    print('> = the first in the past')  #p
    print('a = Good ___ U by Olivia Rodrigo')  #4
    print("< = lowercase version of the title of Rose's first mini album")  #r
    print(': = often used to replace you')  #u
    print('} = the name of a member of BTS')  #v
    print("~ = this letter's name and shape is twice of another letter")  #w
    print("` = a character that shares a house with the 'less than' symbol")  #,
    print('? = the seventh letter of the alphabet')  #g

def k2hint():  # function to display hints to help user get the key
    print('~ = the sound snakes make')  #s
    print('! = there are ___ months in half of a year')  #6
    print('@ = in English, this letter sometimes sounds like the letter k')  #c
    print('# = the start of miracles and the end of doom')  #m
    print('$ = this letter is for apples')  #a
    print('% = when you want to write this character, you press the biggest key on the keyboard')  #' '
    print('^ = the second worst grade students can get in their exam paper')  #d
    print('& = how many toe beans do cats have on their hind paw')  #4
    print('* = between u and i but a key above')  #8
    print('( = the number of members in the boyband in Turning Red')  #5
    print('_ = this letter is also known as the peace sign pose when taking pictures')  #v
    print('+ = marks the spot on a treasure map')  #x
    print('` = this symbol is flat and short')  #-
    print('1 = this letter is the start of the light refraction phenomenon that happens when light meets water')  #r
    print('2 = between u and i but a key below')  #j
    print('3 = the start of new-beginnings')  #n
    print('4 = people say this letter twice in a row to indicate good sportsmanship')  #g
    print('5 = the silent letter in knowledge')  #k
    print('6 = spill the ___ they say')  #t
    print('7 = the number used to write the uwu text emoji')  #3
    print('8 = the silent letter in the longest word in english')  #p
    print('9 = it is positioned above the window')  #z
    print('- = starting from the bottom left corner, move three boxes to the right and three boxes above.')  #e
    print('= = the silent character of characters')  #h
    print('W = the character often used to indicate the end of a sentence')  #.
    print('R = this uppercase letter is used to represent shades in text emojis')  #B
    print('A = this uppercase letter is the start of a famous pink and orange donut store franchise')  #D
    print('L = this uppercase letter is the start of the name of the brother in Hansel and Gretel')  #H
    print('Q = this letter looks like a person without hands and legs')  #i
    print('X = the 12th letter of the alphabet')  #l
    print('Y = the RGB code for the color black')  #0
    print('j = in english, this letter is sometimes pronounced like the letter a')  #u
    print('f = this letter is the mouth of the uwu text emoji')  #w
    print("d = the number of neelofa's children as of 2024")  #2
    print('s = the number in the name of a kpop girlgroup that is formed through Idol School')  #9
    print('/ = this character is often used to write lists in one sentence')  #,
    print('\\ = the end of humanity')  #y
    print('[ = people say this letter represents hugs when writing messages')  #o
    print('> = the number that appears when you hold out your right hand, point your index finger downwards and straighten your thumb')  #7
    print('< = barisan in english')  #q
    print('; = the first number that appears on a keyboard')  #1
    print('} = this letter rhymes with bee')  #b
    print("? = in Malay, this letter is used to replace 'ph'")  #f

def ans(x):  # function to get input and display the given input
    ansList = []  # an empty list to append the answers into later
    i = 0  # setting the counter
    while i < len(list(x)):  # loop to keep asking user for input for each symbol in the encrypted message
        symbol = list(x)[i]  # assigning a symbol to variable 'symbol'
        print('\n', symbol, 'represents :')
        answer = input()  # asking for input and assigning it to variable 'answer'
        ansList.append(answer)  # appending the input into the list earlier
        i += 1  # increase counter
    finAns = ''.join(ansList)  # joining each item in the list into a single string
    print('\nThe message that you decrypted is: ', finAns)  # printing the string of the answer given by user
    return finAns  # returning the value of the answer string

def reward():  # function to determine whether the user gets the hint for the main question
    if play == oneE:  # if the message chosen from the random choice in the dExecute() function is one,
        print('The original text is :', oneD)  # the original text is displayed
        if message == oneD:  # if user's input is the same as the original text,
            return True  #return True
        else:  # if not (user's input is different than the original text),
            return False  # return False
    elif play == twoE:
        print('The original text is :', twoD)           # same as above
        if message == twoD:
            return True
        else:
            return False
    elif play == threeE:
        print('The original text is :', threeD)           # same as above
        if message == threeD:
            return True
        else:
            return False
    elif play == fourE:
        print('The original text is :', fourD)           # same as above
        if message == fourD:
            return True
        else:
            return False
    elif play == fiveE:
        print('The original text is :', fiveD)           # same as above
        if message == fiveD:
            return True
        else:
            return False
    elif play == sixE:
        print('The original text is :', sixD)           # same as above
        if message == sixD:
            return True
        else:
            return False
    elif play == sevenE:
        print('The original text is :', sevenD)           # same as above
        if message == sevenD:
            return True
        else:
            return False
    elif play == eightE:
        print('The original text is :', eightD)           # same as above
        if message == eightD:
            return True
        else:
            return False
    elif play == nineE:
        print('The original text is :', nineD)           # same as above
        if message == nineD:
            return True
        else:
            return False
    elif play == tenE:
        print('The original text is :', tenD)           # same as above
        if message == tenD:
            return True
        else:
            return False

dExecute()  # executing the main function

# decryptify end
