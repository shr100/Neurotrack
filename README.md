# Neurotrack Vending Machine

**Overview:**
  A Python program that implements the functionality of a vending machine. It displays the vending machine menu, where the user can interact with the system with the help of a keyboard. The user can select items from the menu, as well as the quantity needed. Multiple items can also be selected. After the selection, the items selected, and the total cost are displayed. The user is then prompted to enter the total money fed into the vending machine, and the machine counts out the change given, and displays it on the screen. The change is dispensed in such a way that it uses a minimal number of coins to dispense the exact change.

**Assumptions:** 
  1. There is an infinite supply of coins.
  2. System accepts only cash
  
**Additional functionality:**
Accounts for typos in the user's selection from the menu. For example, if the user types in "chibs" instead of Chips, the system knows that it has to choose Chips.

This system could have had some added functionality, if there had been more time. I could have implemented features that would account for a finite number of coins. I also would have worked on improving the "minimal change dispensary" system, where the system dispenses the exact change using the smallest number of coins it can use. 

A small demo video has been attached, in order to demonstrate what the input should look like.
The program can be run using the command **"python3 vending_machine.py"**.
