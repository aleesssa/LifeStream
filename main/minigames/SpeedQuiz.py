# speed quiz start

import cv2
import time
import random
from threading import Timer

def sqExecute():
    # display instructions
    print('\033[1;34m********************************************************************')
    print('\t\t\t    SPEED QUIZ')
    print('********************************************************************\033[0;30m')
    time.sleep(1)
    print('Here are the instructions:-')
    time.sleep(1)
    print('1. You will be shown a picture for 1.5 or 5 seconds depending on the type of picture.')
    time.sleep(2)
    print('2. You need to identify the picture or answer the question asked in the picture.')
    time.sleep(2)
    print('3. You will be given 3 or 5 seconds to enter your answer depending on the type of picture.')
    time.sleep(2)
    print('4. All answers should be written in one word.')
    time.sleep(2)
    print('5. For each correct answer, you will get 1 point.')
    time.sleep(2)
    print('6. To win, you need at least 10 points.')
    time.sleep(2)
    print('7. You need to answer as many questions as you can within a minute.')
    time.sleep(2)
    print('\n\033[0;33m...Loading...\033[0;30m')
    time.sleep(2)
    print('\nAre you ready?')
    time.sleep(1)
    print('\nHere we go!')
    time.sleep(1)
    global points
    points = 0  # setting intial points
    t = Timer(60, reward)  # setting timer function for 60 seconds (1 minute) and to execute reward function when timer is done
    t.start() # timer starts
    print('\nThe timer has started.')
    time.sleep(1)
    global diffQs
    # putting all possible questions in a list and the list is set to variable diffQs
    diffQs = [q1, q2, q3, q4, q5, qt6, qt7, qt8, qt9, qt10, qt11, qt12, qt13, qt14, qt15, qt16, qt17, qt18, qt19, qt20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60]
    # shuffling the diffQs list into random order
    random.shuffle(diffQs)
    while len(diffQs) > 0:  # loop to keep executing the question functions while there are still questions in the list
        point = diffQs.pop()()  # removing the last item from the list which is also the item that is executed, then setting it to variable 'point'
        points = point  # changing the global points to the current point
    t.join()  # function to connect the threads once timer is done

def pic(x):  # function to show image
    path = str('sqStuff/images/' + x)  # file path string set to variable 'path'
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)  # cv2 funtion to read the image file, set to variable 'img'
    img = cv2.resize(img, (600,600))  # cv2 function to resize the image
    cv2.imshow('Picture', img)  # cv2 function to display the image and setting the name of the window to 'Picture'
    cv2.waitKey(1500)  # cv2 function to display the image for 1.5 seconds, the time unit is in miliseconds
    cv2.destroyAllWindows()  # cv2 function to close the image window

def pict(x):  # similar function to pic() but with longer duration to display image
    path = str('sqStuff/images/' + x)
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    img = cv2.resize(img, (600,600))
    cv2.imshow('Picture', img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

def longpict(x):  # similar function to pic() but with different image size and longer duration to display image
    path = str('sqStuff/images/' + x)
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    img = cv2.resize(img, (600,400))
    cv2.imshow('Picture', img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

def longpic(x):  # similar function to pic() but with different image size
    path = str('sqStuff/images/' + x)
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    img = cv2.resize(img, (600,400))
    cv2.imshow('Picture', img)
    cv2.waitKey(1500)
    cv2.destroyAllWindows()

def check(x,y):  # function to check the time taken for user to enter answer, and to check if answer is correct
    start = time.time()  # records start time
    ans = input('\n\033[1;34mAnswer: \033[1;30m').upper()  # asking user for input, changing it to uppercase and set to variable 'ans'
    end = time.time()  # records end time
    diff = end-start  # calculates the time taken for user input which is the difference between end time and start time
    if diff > 3:  # conditional to check if the time taken is more than, equal to, or less than 3 seconds
        print('\n\033[1;31mYou exceeded the time limit.\033[1;30m')
        point = y  # the point doesn't change if time is more than 3 seconds
    else:  # if the time taken for user input is less than or equal to 3 seconds,
        if ans != x:  # conditional to check if the answer given is correct or wrong
            print('\n\033[1;31mWrong answer.\033[1;30m')
            point = y  # point doesn't change if asnwer is wrong
        else:
            print('\n\033[1;32mCorrect answer!\033[1;30m')
            point = y + 1  # adds 1 to point if answer is correct
    return point  # returns point value

def checkt(x,y):  # similar function to check() but with longer duration to give input
    start = time.time()
    ans = input('\n\033[1;34mAnswer: \033[1;30m').upper()
    end = time.time()
    diff = end-start
    if diff > 5:
        print('\n\033[1;31mYou exceeded the time limit.\033[1;30m')
        point = y
    else:
        if ans != x:
            print('\n\033[1;31mWrong answer.\033[1;30m')
            point = y
        else:
            print('\n\033[1;32mCorrect answer!\033[1;30m')
            point = y + 1
    return point

def q(x,y):  # function to execute pic() function and check() function
    point = points  # set point to the global points
    print('\nPicture: ')
    pic(x)  # execute pic() function
    point = check(y, point)  # execute check() function and setting the return value of the function (which is 'point') as the new point
    return point  # returns point value

def qt(x,y):  # similar function to q() but with pict() function and checkt() function
    point = points
    print('\nPicture: ')
    pict(x)
    point = checkt(y, point)
    return point

def longqt(x,y):  # similar function to q() but with longpict() function and checkt() function
    point = points
    print('\nPicture: ')
    longpict(x)
    point = checkt(y, point)
    return point

def longq(x,y):  # similar function to q() but with longpic() function
    point = points
    print('\nPicture: ')
    longpic(x)
    point = check(y, point)
    return point

# functions to execute q() function with different arguments to make different questions
def q1():
    point = q('ironman.jpg','IRONMAN')
    return point
def q2():
    point = q('hulk.jpg','HULK')
    return point
def q3():
    point = q('hawkeye.jpg','HAWKEYE')
    return point
def q4():
    point = q('thor.jpg','THOR')
    return point
def q5():
    point = q('spiderman.jpg','SPIDERMAN')
    return point
def qt6():
    point = longqt('a.png','WEIGH')
    return point
def qt7():
    point = longqt('b.png','GOOD')
    return point
def qt8():
    point = longqt('c.png','18')
    return point
def qt9():
    point = longqt('d.png','SLEEP')
    return point
def qt10():
    point = longqt('e.png','ILLNESSES')
    return point
def qt11():
    point = longqt('f.png','MONTHS')
    return point
def qt12():
    point = longqt('g.png','PREGNANT')
    return point
def qt13():
    point = longqt('h.png','DAYS')
    return point
def qt14():
    point = longqt('i.png','HOURS')
    return point
def qt15():
    point = longqt('j.png','HETERO')
    return point
def qt16():
    point = longqt('k.png','DRUG')
    return point
def qt17():
    point = longqt('l.png','MONTHS')
    return point
def qt18():
    point = longqt('m.png','YEARS')
    return point
def qt19():
    point = longqt('n.png','NOT')
    return point
def qt20():
    point = longqt('o.png','IDENTIFICATION')
    return point
def q21():
    point = q('chongwei.jpg','LEECHONGWEI')
    return point
def q22():
    point = q('nicol.png','NICOLANNDAVID')
    return point
def q23():
    point = q('neelofa.jpg','NEELOFA')
    return point
def q24():
    point = q('siti.jpg','SITINURHALIZA')
    return point
def q25():
    point = q('zizan.jpg','ZIZANRAZAK')
    return point
def q26():
    point = longq('sarawak.jpg','SARAWAK')
    return point
def q27():
    point = longq('sabah.jpg','SABAH')
    return point
def q28():
    point = longq('terengganu.png','TERENGGANU')
    return point
def q29():
    point = longq('kelantan.jpg','KELANTAN')
    return point
def q30():
    point = longq('pahang.png','PAHANG')
    return point
def q31():
    point = longq('johor.jpg','JOHOR')
    return point
def q32():
    point = longq('melaka.png','MELAKA')
    return point
def q33():
    point = longq('selangor.jpg','SELANGOR')
    return point
def q34():
    point = longq('perak.jpg','PERAK')
    return point
def q35():
    point = longq('kedah.jpg','KEDAH')
    return point
def q36():
    point = longq('perlis.jpg','PERLIS')
    return point
def q37():
    point = q('snoopy.png','SNOOPY')
    return point
def q38():
    point = q('mrbean.jpg','MRBEAN')
    return point
def q39():
    point = q('phineas.jpg','PHINEAS')
    return point
def q40():
    point = q('shrek.jpg','SHREK')
    return point
def q41():
    point = q('garfield.jpg','GARFIELD')
    return point
def q42():
    point = q('mickey.jpg','MICKEY')
    return point
def q43():
    point = q('doraemon.jpg','DORAEMON')
    return point
def q44():
    point = q('kwangsoo.jpg','KWANGSOO')
    return point
def q45():
    point = q('pikachu.jpg','PIKACHU')
    return point
def q46():
    point = q('byeonwooseok.jpg','BYEONWOOSEOK')
    return point
def q47():
    point = q('kimjiwon.jpg','KIMJIWON')
    return point
def q48():
    point = q('jennie.jpg','JENNIE')
    return point
def q49():
    point = q('gongyoo.jpg','GONGYOO')
    return point
def q50():
    point = q('p.png','9.8')
    return point
def q51():
    point = q('q.png','9')
    return point
def q52():
    point = q('r.png','110')
    return point
def q53():
    point = q('s.png','14')
    return point
def q54():
    point = q('t.png','2')
    return point
def q55():
    point = q('emmawatson.jpg','EMMAWATSON')
    return point
def q56():
    point = q('ryanreynolds.jpg','RYANREYNOLDS')
    return point
def q57():
    point = q('zendaya.jpg','ZENDAYA')
    return point
def q58():
    point = q('jackiechan.jpg','JACKIECHAN')
    return point
def q59():
    point = q('taylorswift.jpg','TAYLORSWIFT')
    return point
def q60():
    point = q('u.png','-3')
    return point

def reward():  # function to give hint to user if points are enough
    zerolist = diffQs  # setting the diffQs list to variable 'zerolist'
    zerolist.clear()  # emptying the zerolist list which is the diffQs list to stop the earlier while loop in sqExecute()
    print('\nA minute has passed.')
    time.sleep(2)
    print('\nYour points: ', points)  # display user's final points
    time.sleep(2)
    if points < 10:  # conditional to check if the points accumulated are enough to get reward
        return False  # if points collected are less than 10, no hints/reward is given
    else:
        return True  # if points collected are equal to or more than 10, hints/reward is given

sqExecute()  # run sqExecute() function

# speed quiz end

