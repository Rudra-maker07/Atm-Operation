from ATMExcept import DepositError, WithdrawError, InSuffFundError

bal=500.00
def deposit():
    damt=float(input("Enter the deposit amount: "))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUR AC XXXXXXXX6818 has been credited INR {}".format(damt))
        print("\tNOW UR AC XXXXXXXX6818 balance after deposit is INR{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter the withdraw amount: "))
    if(wamt<=0):
        raise WithdrawError
    else:
        if((wamt+500)>bal):
            raise InSuffFundError
        else:
            bal=bal-wamt
            print("\tUR AC XXXXXXXX6818 has been debited INR {}".format(wamt))
            print("\tNOW UR AC XXXXXXXX6818 balance after withdraw is INR{}".format(bal))
def balenq():
    print("\tUR AC XXXXXXXX6818 balance: {}".format(bal))