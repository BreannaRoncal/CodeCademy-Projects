"""
You are developing a mobile ATM application that will handle bank transactions such as deposits and withdrawals. 
With the original design of this application, you used print statements to print helpful information to the console, 
such as amounts entered for each transaction, transaction status, and date and timestamps to see when each 
transaction occurred.

The goal of this project is to modify the existing BankAccount methods to utilize the logging module instead of 
print statements. Using the logging module over print statements will help make the project code more readable 
and maintainable after these modifications are made.


"""

import random
import logging
import sys
from datetime import datetime
# Logger object
logger = logging.getLogger(__name__)
# This will output the log to the console
stream_handler = logging.StreamHandler(sys.stdout)

# This will output the log a file called 'formatted.log'
file_handler = logging.FileHandler('formatted.log')

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
stream_handler.setFormatter(formatter)

class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      if pin != 1234:
        logger.error("Error! Invalid pin.")
        pin = int(input("\nTry again: "))
      else:
        return None
 
  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      if amount < 0:
        logger.warning("Warning! You entered a negative number to deposit.")
      self.balance += amount
      logger.info("Amount Deposited: ${amount}".format(amount=amount))
      logger.info("Transaction Info:")
      logger.info("Status: Successful")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
    except ValueError:
      logger.error("Error! You entered a non-number value to deposit.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        logger.info("You withdrew: ${amount}".format( amount=amount))
        logger.info("Transaction Info:")
        logger.info("Status: Successful")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      else:
        logger.error("Error! Insufficient balance to complete withdraw.")
        logger.info("Transaction Info:")
        logger.info("Status: Failed")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.error("Error! You entered a non-number value to withdraw.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def display(self):
    logger.info("Available Balance = ${balance}".format(balance=self.balance))
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()
