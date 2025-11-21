from ATMExcept import DepositError, WithdrawError, InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
while(True):

   try:
      menu()
      ch =int(input("Enter your choice:"))
      match(ch):
        case 1:
          try:
              deposit()
          except DepositError:
              print("\tDONT ENTER ZERO OR -VE AMOUNT FOR DEPOSIT")
          except ValueError:
              print("\tDONT ENTER ALNUMS STR AND SYMBOL...")
        case 2:
          try:
              withdraw()
          except WithdrawError:
              print("\tDONT ENTER ZERO OR -VE AMOUNT FOR WITHDRAW...")
          except ValueError:
              print("\tDONT ENTER ALNUMS STR AND SYMBOL...")
          except InSuffFundError:
              print("\tUR AC Does not contain Suff Fund")
        case 3:
            balenq()
        case 4:
            print("\tTHANKS FOR USING ATM VISIT AGAIN")
        case _:
            print("\tYou have entered wrong choice")
   except ValueError:
     print("\tDONT ENTER ALNUMS STR AND SYMBOL...")



