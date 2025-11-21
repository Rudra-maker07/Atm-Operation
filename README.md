# ATM Console Application (Python)

A simple console-based **ATM simulation** written in Python.
It supports deposit, withdraw, and balance enquiry operations and demonstrates use of modular code and custom exceptions.

---

## ▶️ Features

* Deposit money (validates positive amount)
* Withdraw money (validates positive amount and minimum balance constraint)
* Check account balance
* Uses custom exception classes for clear error handling
* Simple text-based menu for interaction

---

## 📁 Project Structure

```
atm-project/
├── ATMExcept.py          # Custom exception classes
├── ATMMenu.py            # Prints the interactive menu
├── ATMOperations.py      # deposit, withdraw, balance enquiry logic
└── <main>.py             # Main loop that ties everything together
```

**Module details**

* `ATMExcept.py` defines custom exceptions used by the app (DepositError, WithdrawError, InSuffFundError). 
* The main program contains the interactive loop and dispatches menu choices to operations. 
* `ATMMenu.py` prints the menu and user prompts. 
* `ATMOperations.py` implements `deposit()`, `withdraw()`, and `balenq()` and maintains the account balance. 

---

## 🛠️ Requirements

* Python 3.x

No external libraries required.

---

## ▶️ How to run

1. Place all `.py` files in the same folder.
2. From that folder run the main script (the file that contains the interactive loop):

```bash
python <main_script_name>.py
```

Replace `<main_script_name>.py` with the filename you uploaded that contains the main loop. The main loop calls the menu and operation functions. 

---

## ⚙️ Example interaction

```
Welcome to ATM
**************************************************
   1.Deposit
   2.Withdraw
   3.Bal Enq
   4.Exit
**************************************************
Enter your choice: 1
Enter the deposit amount: 1000
    UR AC XXXXXXXX6818 has been credited INR 1000.0
    NOW UR AC XXXXXXXX6818 balance after deposit is INR1500.0
```

Errors are handled via exceptions (e.g., depositing 0 or negative raises `DepositError`). 

---

## 🧾 Notes on behavior & validation

* Deposit: amount must be > 0 — if not, `DepositError` is raised. 
* Withdraw: amount must be > 0 and account must keep a required minimum (implemented as a 500 unit buffer in the code). If insufficient, `InSuffFundError` is raised. 
* Balance enquiry prints the current `bal` variable. 

---

## ✅ Suggestions / Possible Improvements

* Persist balance to a file so balance survives program restarts.
* Replace the hard-coded account number display with parameterized account(s).
* Add authentication (PIN) before allowing transactions.
* Improve user input parsing and messages for internationalization.
* Add unit tests for deposit/withdraw/enquiry and exception cases.

---

## 📄 License

Add an appropriate license (e.g., MIT) if you plan to share publicly.

---

If you want, I can:

* Produce a cleaned and commented version of the main script, or
* Implement persistence (save/load balance to a file), or
* Add PIN-based authentication — pick one and I’ll generate the code.
