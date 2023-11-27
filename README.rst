aerarium
============

A simple command line interface for managing my finances.


Features
--------

- Check account balance

  Use the ``--balance`` flag to print the current account balance.

- Withdraw amount

  Use the ``--withdraw <amount>`` option to withdraw money, along with a description and category prompt.
  Prints new account balance.

- Deposit amount
  
  Use the ``--deposit <amount>`` option to deposit money, along with a description and category prompt.
  Prints new account balance.  

- Help information

  Use ``--help`` to print usage help.

Usage
-----

Some examples:

.. code-block::

   $ python -m scripts.aerarium --balance
   Current balance: $1000
   
   $ python -m scripts.aerarium --withdraw 100
   Enter withdrawal description: Groceries  
   Enter withdrawal category: Food
   Balance: 900
   
   $ python -m scripts.aerarium --deposit 500
   Enter deposit description: Salary
   Enter deposit category: Income
   Balance: 1400

The configuration file contains the account name and starting balance.

**Note**: This project is under active development.
