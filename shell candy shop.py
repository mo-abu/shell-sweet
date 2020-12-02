import time

def delete():
    exit()

numone  = 0
name = input("Enter Your Name: ")

time.sleep(1)

print('\nWelcome to my store', name)

time.sleep(1)

print('\nThis is our menu')

time.sleep(0.5)

def choco():
    print('\n(1) Kinder Bueno - £1.29\n(2) Galaxy - £1.49\n(3) Bounty - £1.49\n(4) Snickers - £1.49\n(5) Twix - £1.29')
choco()

time.sleep(1)

KB = float(1.29)
GA = float(1.49)
BO = float(1.49)
SN = float(1.49)
TW = float(1.29)
EI = float(1.00)

def thanks():
    while True:
        order = input('\nWould you like to make a chocolate order?(Y/N): ')
        if order == 'yes' or order == 'y':
            sysLoop()
        elif order == 'no' or order == 'n':
            print('\nThanks for coming into the Sea Front Sweet and Candy Shop')
            delete()
    thanks()

time.sleep(1)

def kinderpay():
    ki_pay = float(numone) * float(KB)
    ki_pay1 = float(numone) * float(KB) + float(EI)

    table = input('\nWould you like to checkout?(Y/N): ')
    if table == 'yes' or table == 'y':
        print('\nOkay, your total is £' + str(ki_pay1))
        thanks()
    elif table == 'no' or 'n':
        print('\nOkay, your total is £' + str(ki_pay))
        thanks()
    else:
        error1()

def galaxypay():
    ga_pay = float(numone) * float(GA)
    ga_pay1 = float(numone) * float(GA) + float(EI)

    table = input('\nWould you like to checkout?(Y/N): ')
    if table == 'yes' or table == 'y':
        print('\nOkay, your total is £' + str(ga_pay1))
        thanks()
    elif table == 'no' or 'n':
        print('\nOkay, your total is £' + str(ga_pay))
        thanks()
    else:
        error2()

def bountypay():
    bo_pay = float(numone) * float(BO)
    bo_pay1 = float(numone) * float(BO) + float(EI)

    table = input('\nWould you like to checkout?(Y/N): ')
    if table == 'yes' or table == 'y':
        print('\nOkay, your total is £' + str(bo_pay1))
        thanks()
    elif table == 'no' or 'n':
        print('\nOkay, your total is £' + str(bo_pay))
        thanks()
    else:
        error3()

def snickerspay():
    sn_pay = float(numone) * float(SN)
    sn_pay1 = float(numone) * float(SN) + float(EI)

    table = input('\nWould you like to checkout?(Y/N): ')
    if table == 'yes' or table == 'y':
        print('\nOkay, your total is £' + str(sn_pay1))
        thanks()
    elif table == 'no' or 'n':
        print('\nOkay, your total is £' + str(sn_pay))
        thanks()
    else:
        error4()

def twixpay():
    tw_pay = float(numone) * float(TW)
    tw_pay1 = float(numone) * float(TW) + float(EI)

    table = input('\nWould you like to checkout?(Y/N): ')
    if table == 'yes' or table == 'y':
        print('\nOkay, your total is £' + str(tw_pay1))
        thanks()
    elif table == 'no' or 'n':
        print('\nOkay, your total is £' + str(tw_pay))
        thanks()
    else:
        error5()

def kinder():
    kb_opt = input('\nWould you like to purchase a Kinder Bueno?(Y/N): ')
    global opt1
    opt1 = kb_opt
    kinderpay()

def galaxy():
    ga_opt = input('\nWould you like to purchase a Galaxy?(Y/N): ')
    global opt2
    opt2 = ga_opt
    galaxypay()

def bounty():
    bo_opt = input('\nWould you like to purchase a Bounty?(Y/N): ')
    global opt3
    opt3 = bo_opt
    bountypay()

def snickers():
    sn_opt = input('\nWould you like to purchase a Snickers?(Y/N): ')
    global opt4
    opt4 = sn_opt
    snickerspay()

def twix():
    tw_opt = input('\nWould you like to purchase a Twix?(Y/N): ')
    global opt5
    opt5 = tw_opt
    twixpay()

def sysStart():
    user_input = input('\nSelect a chocolate number: ')
    if user_input == '1':
        kinder()
    elif user_input == '2':
        galaxy()
    elif user_input == '3':
        bounty()
    elif user_input == '4':
        snickers()
    elif user_input == '5':
        twix()
    else:
        sorry()

def sysLoop():
    while True:
        sysStart()
        break

def error():
    thanks()

def error1():
    print('\nThat is not an option. Try again')
    kinderpay()

def error2():
    print('\nThat is not an option. Try again') 
    galaxypay()

def error3():
    print('\nThat is not an option. Try again')
    bountypay()

def error4():
    print('\nThat is not an option. Try again')
    snickerspay()

def error5():
    print('\nThat is not an option. Try again')
    twixpay()

def sorry():
    print("Sorry, that option isn't on our menu please try again")
    sysStart()

sysStart()
