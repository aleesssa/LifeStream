# decryptify start

import time
import random
# setting the keys for encryption
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

k3 = {'a': '>',
       'b': '6',
       'c': '_',
       'd': '<',
       'e': '2',
       'f': 'X',
       'g': '!',
       'h': '@',
       'i': 'Q',
       'j': '4',
       'k': '(',
       'l': '7',
       'm': 'Y',
       'n': '8',
       'o': '*',
       'p': '%',
       'q': '+',
       'r': '`',
       's': 'f',
       't': '9',
       'u': '/',
       'v': ';',
       'w': '-',
       'x': '5',
       'y': '1',
       'z': '^',
       '0': '~',
       '1': '$',
       '2': '\\',
       '3': '#',
       '4': '?',
       '5': 'j',
       '6': '=',
       '7': '[',
       '8': 'd',
       '9': '3',
       ' ': 's',
       '-': '}',
       ',': '&',
       'H': 'R',
       'B': 'A',
       'D': 'L',
       '.': 'W'}

k4 = {'a': '8',
       'b': '(',
       'c': '%',
       'd': 'Q',
       'e': '@',
       'f': '1',
       'g': '<',
       'h': '~',
       'i': '#',
       'j': 'j',
       'k': '2',
       'l': '3',
       'm': '^',
       'n': '>',
       'o': '!',
       'p': '}',
       'q': 's',
       'r': '-',
       's': '`',
       't': ';',
       'u': 'd',
       'v': '$',
       'w': '/',
       'x': '?',
       'y': '6',
       'z': '\\',
       '0': 'f',
       '1': '+',
       '2': '7',
       '3': '9',
       '4': 'Y',
       '5': '[',
       '6': '5',
       '7': '_',
       '8': '*',
       '9': '&',
       ' ': 'X',
       '-': '4',
       ',': '=',
       'H': 'L',
       'B': 'A',
       'D': 'R',
       '.': 'W'}

k5 = {'a': '%',
       'b': '@',
       'c': '\\',
       'd': '/',
       'e': '8',
       'f': 's',
       'g': 'Q',
       'h': '^',
       'i': '+',
       'j': '!',
       'k': ';',
       'l': '`',
       'm': '4',
       'n': '?',
       'o': '}',
       'p': 'd',
       'q': '>',
       'r': '[',
       's': '-',
       't': '9',
       'u': '7',
       'v': '2',
       'w': '(',
       'x': 'j',
       'y': '3',
       'z': '=',
       '0': '#',
       '1': '1',
       '2': '6',
       '3': 'X',
       '4': '$',
       '5': '5',
       '6': '<',
       '7': '_',
       '8': 'f',
       '9': '*',
       ' ': '&',
       '-': 'Y',
       ',': '~',
       'H': 'W',
       'B': 'R',
       'D': 'A',
       '.': 'L'}
# assigning the original messages to their variables
oneD = "Donors who have donated 1 time are privileged to get free outpatient treatment and medical treatment excluding x-ray and surgical charges, and second-class wards for a period of 4 months."
twoD = "Donors who have donated 2 times within 12 months are privileged to get free Hepatitis B prevention injections."
threeD = "Donors who have donated 2 to 5 times are privileged to get free outpatient treatment and medical treatment, and second-class wards for a period of 4 months."
fourD = "Donors who have donated 6 to 10 times are privileged to get free 1-year outpatient treatment and second-class wards for a 6-month period."
fiveD = "Donors who have donated 11 to 15 times are privileged to get free 2-year outpatient treatment and medical treatment, and second-class wards for a 1-year period."
sixD = "Donors who have donated 16 to 20 times are privileged to get free outpatient treatment and medical treatment, and second-class wards for a period of 3 years."
sevenD = "Donors who have donated 21 to 30 times are privileged to get free outpatient treatment and medical treatment, and second-class wards for a period of 3 years."
eightD = "Donors who have donated 31 to 40 times are privileged to get free outpatient treatment and medical treatment, and first-class wards for a period of 4 years."
nineD = "Donors who have donated 41 to 50 times are privileged to get free outpatient treatment and medical treatment, and first-class wards for a period of 6 years."
tenD = "Donors who have donated over 50 times are privileged to get free outpatient treatment and first-class medical treatment and wards for 10 years, and second-class wards of life after 10 years in first-class ward."

# encrypted messages are assigned to their variables
oneE = k1['D']+k1['o']+k1['n']+k1['o']+k1['r']+k1['s']+k1[' ']+k1['w']+k1['h']+k1['o']+k1[' ']+k1['h']+k1['a']+k1['v']+k1['e']+k1[' ']+k1['d']+k1['o']+k1['n']+k1['a']+k1['t']+k1['e']+k1['d']+k1[' ']+k1['1']+k1[' ']+k1['t']+k1['i']+k1['m']+k1['e']+k1[' ']+k1['a']+k1['r']+k1['e']+k1[' ']+k1['p']+k1['r']+k1['i']+k1['v']+k1['i']+k1['l']+k1['e']+k1['g']+k1['e']+k1['d']+k1[' ']+k1['t']+k1['o']+k1[' ']+k1['g']+k1['e']+k1['t']+k1[' ']+k1['f']+k1['r']+k1['e']+k1['e']+k1[' ']+k1['o']+k1['u']+k1['t']+k1['p']+k1['a']+k1['t']+k1['i']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['m']+k1['e']+k1['d']+k1['i']+k1['c']+k1['a']+k1['l']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['e']+k1['x']+k1['c']+k1['l']+k1['u']+k1['d']+k1['i']+k1['n']+k1['g']+k1[' ']+k1['x']+k1['-']+k1['r']+k1['a']+k1['y']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['s']+k1['u']+k1['r']+k1['g']+k1['i']+k1['c']+k1['a']+k1['l']+k1[' ']+k1['c']+k1['h']+k1['a']+k1['r']+k1['g']+k1['e']+k1['s']+k1[',']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['s']+k1['e']+k1['c']+k1['o']+k1['n']+k1['d']+k1['-']+k1['c']+k1['l']+k1['a']+k1['s']+k1['s']+k1[' ']+k1['w']+k1['a']+k1['r']+k1['d']+k1['s']+k1[' ']+k1['f']+k1['o']+k1['r']+k1[' ']+k1['a']+k1[' ']+k1['p']+k1['e']+k1['r']+k1['i']+k1['o']+k1['d']+k1[' ']+k1['o']+k1['f']+k1[' ']+k1['4']+k1[' ']+k1['m']+k1['o']+k1['n']+k1['t']+k1['h']+k1['s']+k1['.']
twoE = k2['D']+k2['o']+k2['n']+k2['o']+k2['r']+k2['s']+k2[' ']+k2['w']+k2['h']+k2['o']+k2[' ']+k2['h']+k2['a']+k2['v']+k2['e']+k2[' ']+k2['d']+k2['o']+k2['n']+k2['a']+k2['t']+k2['e']+k2['d']+k2[' ']+k2['2']+k2[' ']+k2['t']+k2['i']+k2['m']+k2['e']+k2['s']+k2[' ']+k2['w']+k2['i']+k2['t']+k2['h']+k2['i']+k2['n']+k2[' ']+k2['1']+k2['2']+k2[' ']+k2['m']+k2['o']+k2['n']+k2['t']+k2['h']+k2['s']+k2[' ']+k2['a']+k2['r']+k2['e']+k2[' ']+k2['p']+k2['r']+k2['i']+k2['v']+k2['i']+k2['l']+k2['e']+k2['g']+k2['e']+k2['d']+k2[' ']+k2['t']+k2['o']+k2[' ']+k2['g']+k2['e']+k2['t']+k2[' ']+k2['f']+k2['r']+k2['e']+k2['e']+k2[' ']+k2['H']+k2['e']+k2['p']+k2['a']+k2['t']+k2['i']+k2['t']+k2['i']+k2['s']+k2[' ']+k2['B']+k2[' ']+k2['p']+k2['r']+k2['e']+k2['v']+k2['e']+k2['n']+k2['t']+k2['i']+k2['o']+k2['n']+k2[' ']+k2['i']+k2['n']+k2['j']+k2['e']+k2['c']+k2['t']+k2['i']+k2['o']+k2['n']+k2['s']+k2['.']
threeE = k3['D']+k3['o']+k3['n']+k3['o']+k3['r']+k3['s']+k3[' ']+k3['w']+k3['h']+k3['o']+k3[' ']+k3['h']+k3['a']+k3['v']+k3['e']+k3[' ']+k3['d']+k3['o']+k3['n']+k3['a']+k3['t']+k3['e']+k3['d']+k3[' ']+k3['2']+k3[' ']+k3['t']+k3['o']+k3[' ']+k3['5']+k3[' ']+k3['t']+k3['i']+k3['m']+k3['e']+k3['s']+k3[' ']+k3['a']+k3['r']+k3['e']+k3[' ']+k3['p']+k3['r']+k3['i']+k3['v']+k3['i']+k3['l']+k3['e']+k3['g']+k3['e']+k3['d']+k3[' ']+k3['t']+k3['o']+k3[' ']+k3['g']+k3['e']+k3['t']+k3[' ']+k3['f']+k3['r']+k3['e']+k3['e']+k3[' ']+k3['o']+k3['u']+k3['t']+k3['p']+k3['a']+k3['t']+k3['i']+k3['e']+k3['n']+k3['t']+k3[' ']+k3['t']+k3['r']+k3['e']+k3['a']+k3['t']+k3['m']+k3['e']+k3['n']+k3['t']+k3[' ']+k3['a']+k3['n']+k3['d']+k3[' ']+k3['m']+k3['e']+k3['d']+k3['i']+k3['c']+k3['a']+k3['l']+k3[' ']+k3['t']+k3['r']+k3['e']+k3['a']+k3['t']+k3['m']+k3['e']+k3['n']+k3['t']+k3[',']+k3[' ']+k3['a']+k3['n']+k3['d']+k3[' ']+k3['s']+k3['e']+k3['c']+k3['o']+k3['n']+k3['d']+k3['-']+k3['c']+k3['l']+k3['a']+k3['s']+k3['s']+k3[' ']+k3['w']+k3['a']+k3['r']+k3['d']+k3['s']+k3[' ']+k3['f']+k3['o']+k3['r']+k3[' ']+k3['a']+k3[' ']+k3['p']+k3['e']+k3['r']+k3['i']+k3['o']+k3['d']+k3[' ']+k3['o']+k3['f']+k3[' ']+k3['4']+k3[' ']+k3['m']+k3['o']+k3['n']+k3['t']+k3['h']+k3['s']+k3['.']
fourE = k4['D']+k4['o']+k4['n']+k4['o']+k4['r']+k4['s']+k4[' ']+k4['w']+k4['h']+k4['o']+k4[' ']+k4['h']+k4['a']+k4['v']+k4['e']+k4[' ']+k4['d']+k4['o']+k4['n']+k4['a']+k4['t']+k4['e']+k4['d']+k4[' ']+k4['6']+k4[' ']+k4['t']+k4['o']+k4[' ']+k4['1']+k4['0']+k4[' ']+k4['t']+k4['i']+k4['m']+k4['e']+k4['s']+k4[' ']+k4['a']+k4['r']+k4['e']+k4[' ']+k4['p']+k4['r']+k4['i']+k4['v']+k4['i']+k4['l']+k4['e']+k4['g']+k4['e']+k4['d']+k4[' ']+k4['t']+k4['o']+k4[' ']+k4['g']+k4['e']+k4['t']+k4[' ']+k4['f']+k4['r']+k4['e']+k4['e']+k4[' ']+k4['1']+k4['-']+k4['y']+k4['e']+k4['a']+k4['r']+k4[' ']+k4['o']+k4['u']+k4['t']+k4['p']+k4['a']+k4['t']+k4['i']+k4['e']+k4['n']+k4['t']+k4[' ']+k4['t']+k4['r']+k4['e']+k4['a']+k4['t']+k4['m']+k4['e']+k4['n']+k4['t']+k4[' ']+k4['a']+k4['n']+k4['d']+k4[' ']+k4['s']+k4['e']+k4['c']+k4['o']+k4['n']+k4['d']+k4['-']+k4['c']+k4['l']+k4['a']+k4['s']+k4['s']+k4[' ']+k4['w']+k4['a']+k4['r']+k4['d']+k4['s']+k4[' ']+k4['f']+k4['o']+k4['r']+k4[' ']+k4['a']+k4[' ']+k4['6']+k4['-']+k4['m']+k4['o']+k4['n']+k4['t']+k4['h']+k4[' ']+k4['p']+k4['e']+k4['r']+k4['i']+k4['o']+k4['d']+k4['.']
fiveE = k5['D']+k5['o']+k5['n']+k5['o']+k5['r']+k5['s']+k5[' ']+k5['w']+k5['h']+k5['o']+k5[' ']+k5['h']+k5['a']+k5['v']+k5['e']+k5[' ']+k5['d']+k5['o']+k5['n']+k5['a']+k5['t']+k5['e']+k5['d']+k5[' ']+k5['1']+k5['1']+k5[' ']+k5['t']+k5['o']+k5[' ']+k5['1']+k5['5']+k5[' ']+k5['t']+k5['i']+k5['m']+k5['e']+k5['s']+k5[' ']+k5['a']+k5['r']+k5['e']+k5[' ']+k5['p']+k5['r']+k5['i']+k5['v']+k5['i']+k5['l']+k5['e']+k5['g']+k5['e']+k5['d']+k5[' ']+k5['t']+k5['o']+k5[' ']+k5['g']+k5['e']+k5['t']+k5[' ']+k5['f']+k5['r']+k5['e']+k5['e']+k5[' ']+k5['2']+k5['-']+k5['y']+k5['e']+k5['a']+k5['r']+k5[' ']+k5['o']+k5['u']+k5['t']+k5['p']+k5['a']+k5['t']+k5['i']+k5['e']+k5['n']+k5['t']+k5[' ']+k5['t']+k5['r']+k5['e']+k5['a']+k5['t']+k5['m']+k5['e']+k5['n']+k5['t']+k5[' ']+k5['a']+k5['n']+k5['d']+k5[' ']+k5['m']+k5['e']+k5['d']+k5['i']+k5['c']+k5['a']+k5['l']+k5[' ']+k5['t']+k5['r']+k5['e']+k5['a']+k5['t']+k5['m']+k5['e']+k5['n']+k5['t']+k5[',']+k5[' ']+k5['a']+k5['n']+k5['d']+k5[' ']+k5['s']+k5['e']+k5['c']+k5['o']+k5['n']+k5['d']+k5['-']+k5['c']+k5['l']+k5['a']+k5['s']+k5['s']+k5[' ']+k5['w']+k5['a']+k5['r']+k5['d']+k5['s']+k5[' ']+k5['f']+k5['o']+k5['r']+k5[' ']+k5['a']+k5[' ']+k5['1']+k5['-']+k5['y']+k5['e']+k5['a']+k5['r']+k5[' ']+k5['p']+k5['e']+k5['r']+k5['i']+k5['o']+k5['d']+k5['.']
sixE = k1['D']+k1['o']+k1['n']+k1['o']+k1['r']+k1['s']+k1[' ']+k1['w']+k1['h']+k1['o']+k1[' ']+k1['h']+k1['a']+k1['v']+k1['e']+k1[' ']+k1['d']+k1['o']+k1['n']+k1['a']+k1['t']+k1['e']+k1['d']+k1[' ']+k1['1']+k1['6']+k1[' ']+k1['t']+k1['o']+k1[' ']+k1['2']+k1['0']+k1[' ']+k1['t']+k1['i']+k1['m']+k1['e']+k1['s']+k1[' ']+k1['a']+k1['r']+k1['e']+k1[' ']+k1['p']+k1['r']+k1['i']+k1['v']+k1['i']+k1['l']+k1['e']+k1['g']+k1['e']+k1['d']+k1[' ']+k1['t']+k1['o']+k1[' ']+k1['g']+k1['e']+k1['t']+k1[' ']+k1['f']+k1['r']+k1['e']+k1['e']+k1[' ']+k1['o']+k1['u']+k1['t']+k1['p']+k1['a']+k1['t']+k1['i']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['m']+k1['e']+k1['d']+k1['i']+k1['c']+k1['a']+k1['l']+k1[' ']+k1['t']+k1['r']+k1['e']+k1['a']+k1['t']+k1['m']+k1['e']+k1['n']+k1['t']+k1[',']+k1[' ']+k1['a']+k1['n']+k1['d']+k1[' ']+k1['s']+k1['e']+k1['c']+k1['o']+k1['n']+k1['d']+k1['-']+k1['c']+k1['l']+k1['a']+k1['s']+k1['s']+k1[' ']+k1['w']+k1['a']+k1['r']+k1['d']+k1['s']+k1[' ']+k1['f']+k1['o']+k1['r']+k1[' ']+k1['a']+k1[' ']+k1['p']+k1['e']+k1['r']+k1['i']+k1['o']+k1['d']+k1[' ']+k1['o']+k1['f']+k1[' ']+k1['3']+k1[' ']+k1['y']+k1['e']+k1['a']+k1['r']+k1['s']+k1['.']
sevenE = k2['D']+k2['o']+k2['n']+k2['o']+k2['r']+k2['s']+k2[' ']+k2['w']+k2['h']+k2['o']+k2[' ']+k2['h']+k2['a']+k2['v']+k2['e']+k2[' ']+k2['d']+k2['o']+k2['n']+k2['a']+k2['t']+k2['e']+k2['d']+k2[' ']+k2['2']+k2['1']+k2[' ']+k2['t']+k2['o']+k2[' ']+k2['3']+k2['0']+k2[' ']+k2['t']+k2['i']+k2['m']+k2['e']+k2['s']+k2[' ']+k2['a']+k2['r']+k2['e']+k2[' ']+k2['p']+k2['r']+k2['i']+k2['v']+k2['i']+k2['l']+k2['e']+k2['g']+k2['e']+k2['d']+k2[' ']+k2['t']+k2['o']+k2[' ']+k2['g']+k2['e']+k2['t']+k2[' ']+k2['f']+k2['r']+k2['e']+k2['e']+k2[' ']+k2['o']+k2['u']+k2['t']+k2['p']+k2['a']+k2['t']+k2['i']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['t']+k2['r']+k2['e']+k2['a']+k2['t']+k2['m']+k2['e']+k2['n']+k2['t']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['m']+k2['e']+k2['d']+k2['i']+k2['c']+k2['a']+k2['l']+k2[' ']+k2['t']+k2['r']+k2['e']+k2['a']+k2['t']+k2['m']+k2['e']+k2['n']+k2['t']+k2[',']+k2[' ']+k2['a']+k2['n']+k2['d']+k2[' ']+k2['s']+k2['e']+k2['c']+k2['o']+k2['n']+k2['d']+k2['-']+k2['c']+k2['l']+k2['a']+k2['s']+k2['s']+k2[' ']+k2['w']+k2['a']+k2['r']+k2['d']+k2['s']+k2[' ']+k2['f']+k2['o']+k2['r']+k2[' ']+k2['a']+k2[' ']+k2['p']+k2['e']+k2['r']+k2['i']+k2['o']+k2['d']+k2[' ']+k2['o']+k2['f']+k2[' ']+k2['3']+k2[' ']+k2['y']+k2['e']+k2['a']+k2['r']+k2['s']+k2['.']
eightE = k3['D']+k3['o']+k3['n']+k3['o']+k3['r']+k3['s']+k3[' ']+k3['w']+k3['h']+k3['o']+k3[' ']+k3['h']+k3['a']+k3['v']+k3['e']+k3[' ']+k3['d']+k3['o']+k3['n']+k3['a']+k3['t']+k3['e']+k3['d']+k3[' ']+k3['3']+k3['1']+k3[' ']+k3['t']+k3['o']+k3[' ']+k3['4']+k3['0']+k3[' ']+k3['t']+k3['i']+k3['m']+k3['e']+k3['s']+k3[' ']+k3['a']+k3['r']+k3['e']+k3[' ']+k3['p']+k3['r']+k3['i']+k3['v']+k3['i']+k3['l']+k3['e']+k3['g']+k3['e']+k3['d']+k3[' ']+k3['t']+k3['o']+k3[' ']+k3['g']+k3['e']+k3['t']+k3[' ']+k3['f']+k3['r']+k3['e']+k3['e']+k3[' ']+k3['o']+k3['u']+k3['t']+k3['p']+k3['a']+k3['t']+k3['i']+k3['e']+k3['n']+k3['t']+k3[' ']+k3['t']+k3['r']+k3['e']+k3['a']+k3['t']+k3['m']+k3['e']+k3['n']+k3['t']+k3[' ']+k3['a']+k3['n']+k3['d']+k3[' ']+k3['m']+k3['e']+k3['d']+k3['i']+k3['c']+k3['a']+k3['l']+k3[' ']+k3['t']+k3['r']+k3['e']+k3['a']+k3['t']+k3['m']+k3['e']+k3['n']+k3['t']+k3[',']+k3[' ']+k3['a']+k3['n']+k3['d']+k3[' ']+k3['f']+k3['i']+k3['r']+k3['s']+k3['t']+k3['-']+k3['c']+k3['l']+k3['a']+k3['s']+k3['s']+k3[' ']+k3['w']+k3['a']+k3['r']+k3['d']+k3['s']+k3[' ']+k3['f']+k3['o']+k3['r']+k3[' ']+k3['a']+k3[' ']+k3['p']+k3['e']+k3['r']+k3['i']+k3['o']+k3['d']+k3[' ']+k3['o']+k3['f']+k3[' ']+k3['4']+k3[' ']+k3['y']+k3['e']+k3['a']+k3['r']+k3['s']+k3['.']
nineE = k4['D']+k4['o']+k4['n']+k4['o']+k4['r']+k4['s']+k4[' ']+k4['w']+k4['h']+k4['o']+k4[' ']+k4['h']+k4['a']+k4['v']+k4['e']+k4[' ']+k4['d']+k4['o']+k4['n']+k4['a']+k4['t']+k4['e']+k4['d']+k4[' ']+k4['4']+k4['1']+k4[' ']+k4['t']+k4['o']+k4[' ']+k4['5']+k4['0']+k4[' ']+k4['t']+k4['i']+k4['m']+k4['e']+k4['s']+k4[' ']+k4['a']+k4['r']+k4['e']+k4[' ']+k4['p']+k4['r']+k4['i']+k4['v']+k4['i']+k4['l']+k4['e']+k4['g']+k4['e']+k4['d']+k4[' ']+k4['t']+k4['o']+k4[' ']+k4['g']+k4['e']+k4['t']+k4[' ']+k4['f']+k4['r']+k4['e']+k4['e']+k4[' ']+k4['o']+k4['u']+k4['t']+k4['p']+k4['a']+k4['t']+k4['i']+k4['e']+k4['n']+k4['t']+k4[' ']+k4['t']+k4['r']+k4['e']+k4['a']+k4['t']+k4['m']+k4['e']+k4['n']+k4['t']+k4[' ']+k4['a']+k4['n']+k4['d']+k4[' ']+k4['m']+k4['e']+k4['d']+k4['i']+k4['c']+k4['a']+k4['l']+k4[' ']+k4['t']+k4['r']+k4['e']+k4['a']+k4['t']+k4['m']+k4['e']+k4['n']+k4['t']+k4[',']+k4[' ']+k4['a']+k4['n']+k4['d']+k4[' ']+k4['f']+k4['i']+k4['r']+k4['s']+k4['t']+k4['-']+k4['c']+k4['l']+k4['a']+k4['s']+k4['s']+k4[' ']+k4['w']+k4['a']+k4['r']+k4['d']+k4['s']+k4[' ']+k4['f']+k4['o']+k4['r']+k4[' ']+k4['a']+k4[' ']+k4['p']+k4['e']+k4['r']+k4['i']+k4['o']+k4['d']+k4[' ']+k4['o']+k4['f']+k4[' ']+k4['6']+k4[' ']+k4['y']+k4['e']+k4['a']+k4['r']+k4['s']+k4['.']
tenE = k5['D']+k5['o']+k5['n']+k5['o']+k5['r']+k5['s']+k5[' ']+k5['w']+k5['h']+k5['o']+k5[' ']+k5['h']+k5['a']+k5['v']+k5['e']+k5[' ']+k5['d']+k5['o']+k5['n']+k5['a']+k5['t']+k5['e']+k5['d']+k5[' ']+k5['o']+k5['v']+k5['e']+k5['r']+k5[' ']+k5['5']+k5['0']+k5[' ']+k5['t']+k5['i']+k5['m']+k5['e']+k5['s']+k5[' ']+k5['a']+k5['r']+k5['e']+k5[' ']+k5['p']+k5['r']+k5['i']+k5['v']+k5['i']+k5['l']+k5['e']+k5['g']+k5['e']+k5['d']+k5[' ']+k5['t']+k5['o']+k5[' ']+k5['g']+k5['e']+k5['t']+k5[' ']+k5['f']+k5['r']+k5['e']+k5['e']+k5[' ']+k5['o']+k5['u']+k5['t']+k5['p']+k5['a']+k5['t']+k5['i']+k5['e']+k5['n']+k5['t']+k5[' ']+k5['t']+k5['r']+k5['e']+k5['a']+k5['t']+k5['m']+k5['e']+k5['n']+k5['t']+k5[' ']+k5['a']+k5['n']+k5['d']+k5[' ']+k5['f']+k5['i']+k5['r']+k5['s']+k5['t']+k5['-']+k5['c']+k5['l']+k5['a']+k5['s']+k5['s']+k5[' ']+k5['m']+k5['e']+k5['d']+k5['i']+k5['c']+k5['a']+k5['l']+k5[' ']+k5['t']+k5['r']+k5['e']+k5['a']+k5['t']+k5['m']+k5['e']+k5['n']+k5['t']+k5[' ']+k5['a']+k5['n']+k5['d']+k5[' ']+k5['w']+k5['a']+k5['r']+k5['d']+k5['s']+k5[' ']+k5['f']+k5['o']+k5['r']+k5[' ']+k5['1']+k5['0']+k5[' ']+k5['y']+k5['e']+k5['a']+k5['r']+k5['s']+k5[',']+k5[' ']+k5['a']+k5['n']+k5['d']+k5[' ']+k5['s']+k5['e']+k5['c']+k5['o']+k5['n']+k5['d']+k5['-']+k5['c']+k5['l']+k5['a']+k5['s']+k5['s']+k5[' ']+k5['w']+k5['a']+k5['r']+k5['d']+k5['s']+k5[' ']+k5['o']+k5['f']+k5[' ']+k5['l']+k5['i']+k5['f']+k5['e']+k5[' ']+k5['a']+k5['f']+k5['t']+k5['e']+k5['r']+k5[' ']+k5['1']+k5['0']+k5[' ']+k5['y']+k5['e']+k5['a']+k5['r']+k5['s']+k5[' ']+k5['i']+k5['n']+k5[' ']+k5['f']+k5['i']+k5['r']+k5['s']+k5['t']+k5['-']+k5['c']+k5['l']+k5['a']+k5['s']+k5['s']+k5[' ']+k5['w']+k5['a']+k5['r']+k5['d']+k5['.']

def delay(x):  #function to make the ecrypted messages appear letter by letter
    print('\n')
    for char in x:  # loop to keep printing the characters in the string
        print(char, end='', flush=True)  # print one character at a time
        time.sleep(.05)  # wait for .05 seconds, then repeat until no more character in the string

def dExecute():
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
    global msg  # putting all encrypted messages into a list
    msg = [oneE, twoE, threeE, fourE, fiveE, sixE, sevenE, eightE, nineE, tenE]
    global play
    play = random.choice(msg)  # choosing a random message
    delay(play)  # execute the function to print the encrypted message
    time.sleep(2)
    print('\nHere are the hints:-\n')
    time.sleep(1)
    if play == oneE or play == sixE:
        k1hint()  # prints this set of hints if the chosen message is msg one or six
    elif play == twoE or play == sevenE:
        k2hint()  # prints this set of hints if the chosen message is msg two or seven
    elif play == threeE or play == eightE:
        k3hint()  # prints this set of hints if the chosen message is msg three or eight
    elif play == fourE or play == nineE:
        k4hint()  # prints this set of hints if the chosen message is msg four or nine
    elif play == fiveE or play == tenE:
        k5hint()  # prints this set of hints if the chosen message is msg five or ten
    # executing the ans() function to ask for input and assigning it to a variable
    finAns = ans(oneE)
    finAns = ans(twoE)
    finAns = ans(threeE)
    finAns = ans(fourE)
    finAns = ans(fiveE)
    finAns = ans(sixE)
    finAns = ans(sevenE)
    finAns = ans(eightE)
    finAns = ans(nineE)
    finAns = ans(tenE)
    # executing the reward() function to determine if user can get hints for main question
    reward(finAns)

def k1hint():  # function to print hints
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
    print('+ = looks exactly like it in lowercase')  #t
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

def k2hint():  # function to print hints
    print('~ = the sound snakes make')  #s
    print('! = there are ___ months in half of a year')  #6
    print('@ = in English, this letter sometimes sounds like the letter k')  #c
    print('# = the start of miracles and the end of doom')  #m
    print('$ = this letter is for apples')  #a
    print('% = when you want to write this character, you press the biggest key on the keyboard')  #' '
    print('^ = the second worst grade students can get in their exam paper')  #d
    print('& = 4')
    print('* = between u and i but a key above')  #8
    print('( = 5')
    print('_ = this letter is also known as the peace sign pose when taking pictures')  #v
    print('+ = marks the spot on a treasure map')  #x
    print('` = -')
    print('1 = r')
    print('2 = between u and i but a key below')  #j
    print('3 = n')
    print('4 = g')
    print('5 = k')
    print('6 = t')
    print('7 = 3')
    print('8 = p')
    print('9 = it is positioned above the window')  #z
    print('- = starting from the bottom left corner, move three boxes to the right and three boxes above.')  #e
    print('= = h')
    print('W = .')
    print('R = B')
    print('A = D')
    print('L = H')
    print('Q = i')
    print('X = l')
    print('Y = 0')
    print('j = u')
    print('f = w')
    print("d = the number of neelofa's children as of 2024")
    print('s = 9')
    print('/ = ,')
    print('\\ = y')
    print('[ = o')
    print('> = 7')
    print('< = barisan in english')
    print('; = 1')
    print('} = b')
    print('? = f')

def k3hint():  # function to print hints
    print('~ = 0')
    print('! = g')
    print('@ = h')
    print('# = 3')
    print('$ = 1')
    print('% = p')
    print('^ = z')
    print('& = ,')
    print('* = o')
    print('( = k')
    print('_ = c')
    print('+ = q')
    print('` = r')
    print('1 = y')
    print('2 = e')
    print('3 = 9')
    print('4 = j')
    print('5 = x')
    print('6 = b')
    print('7 = l')
    print('8 = n')
    print('9 = t')
    print('- = w')
    print('= = 6')
    print('W = .')
    print('R = H')
    print('A = B')
    print('L = D')
    print('Q = i')
    print('X = f')
    print('Y = m')
    print('j = 5')
    print('f = s')
    print('d = 8')
    print('s =  ')
    print('/ = u')
    print('\\ = 2')
    print('[ = 7')
    print('> = a')
    print('< = d')
    print('; = v')
    print('} = -')
    print('? = 4')

def k4hint():  # function to print hints
    print('~ = h')
    print('! = o')
    print('@ = e')
    print('# = i')
    print('$ = v')
    print('% = c')
    print('^ = m')
    print('& = 9')
    print('* = 8')
    print('( = b')
    print('_ = 7')
    print('+ = 1')
    print('` = s')
    print('1 = f')
    print('2 = k')
    print('3 = l')
    print('4 = -')
    print('5 = 6')
    print('6 = y')
    print('7 = 2')
    print('8 = a')
    print('9 = 3')
    print('- = r')
    print('= = ,')
    print('W = .')
    print('R = D')
    print('A = B')
    print('L = H')
    print('Q = d')
    print('X =  ')
    print('Y = 4')
    print('j = j')
    print('f = 0')
    print('d = u')
    print('s = q')
    print('/ = w')
    print('\\ = z')
    print('[ = 5')
    print('> = n')
    print('< = g')
    print('; = t')
    print('} = p')
    print('? = x')

def k5hint():  # function to print hints
    print('~ = ,')
    print('! = j')
    print('@ = b')
    print('# = 0')
    print('$ = 4')
    print('% = a')
    print('^ = h')
    print('& =  ')
    print('* = 9')
    print('( = w')
    print('_ = 7')
    print('+ = i')
    print('` = l')
    print('1 = 1')
    print('2 = v')
    print('3 = y')
    print('4 = m')
    print('5 = 5')
    print('6 = 2')
    print('7 = u')
    print('8 = e')
    print('9 = t')
    print('- = s')
    print('= = z')
    print('W = H')
    print('R = B')
    print('A = D')
    print('L = .')
    print('Q = g')
    print('X = 3')
    print('Y = -')
    print('j = x')
    print('f = 8')
    print('d = p')
    print('s = f')
    print('/ = d')
    print('\\ = c')
    print('[ = r')
    print('> = q')
    print('< = 6')
    print('; = k')
    print('} = o')
    print('? = n')

def ans(x):  # function to ask for input
    ansList = []  # an empty list to append the answers later
    if play == x:  # the following codes will only execute if the chosen message from earlier is the same as the argument x
        i = 0  # setting counter to 0
        while i < len(list(x)):  # loop to keep asking user for input
            symbol = list(x)[i]  # assigning the iterated character to variable 'symbol'
            print('\n', symbol, 'represents :')
            answer = input()  #asking for input
            ansList.append(answer)  # appending answer to the list earlier
            i += 1  # add counter by 1
    finAns = ''.join(ansList)  # changing the list of answers into a string (a full sentence)
    return finAns

def reward(x):
    print('\nThe message that you decrypted is: ', x)  # print the answer given by user
    if play == oneE:  # the following code will only execute if the chosen msg is oneE
        if ans(oneE) == oneD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! You successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', oneD, '\033[0;30m')
    elif play == twoE:  # the following code will only execute if the chosen msg is twoE
        if ans(twoE) == twoD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! You successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', twoD, '\033[0;30m')
    elif play == threeE:  # the following code will only execute if the chosen msg is threeE
        if ans(threeE) == threeD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! You successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', threeD, '\033[0;30m')
    elif play == fourE:  # the following code will only execute if the chosen msg is fourE
        if ans(fourE) == fourD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! You successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', fourD, '\033[0;30m')
    elif play == fiveE:  # the following code will only execute if the chosen msg is fiveE
        if ans(fiveE) == fiveD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', fiveD, '\033[0;30m')
    elif play == sixE:  # the following code will only execute if the chosen msg is sixE
        if ans(sixE) == sixD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', sixD, '\033[0;30m')
    elif play == sevenE:  # the following code will only execute if the chosen msg is sevenE
        if ans(sevenE) == sevenD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', sevenD, '\033[0;30m')
    elif play == eightE:  # the following code will only execute if the chosen msg is eightE
        if ans(eightE) == eightD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! You successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', eightD, '\033[0;30m')
    elif play == nineE:  # the following code will only execute if the chosen msg is nineE
        if ans(nineE) == nineD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! You successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', nineD, '\033[0;30m')
    elif play == tenE:  # the following code will only execute if the chosen msg is tenE
        if ans(tenE) == tenD:  # if the input given by user is the same as the original message then user get hint
            print('\n\033[0;33mCongratulations! You successfully decrypted the message!')
            print('Here is a clue to help you answer the main question:\033[0;30m')
            print('\nHINT')
        else:
            print("\n\033[0;33mUnfortunately, you didn't decrypt the message correctly.")
            print("You won't be getting any hints for now.")
            print('\nThe correct answer is: ', tenD, '\033[0;30m')

dExecute()
