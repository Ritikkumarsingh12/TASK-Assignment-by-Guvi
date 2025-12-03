# =================================================================
# PROBLEM 1: Bank Account (Inheritance & Encapsulation)
# =================================================================

class BankAccount:
    """
    Base class for all bank accounts. Implements encapsulation for the balance.
    """

    def __init__(self, account_number, initial_balance=0.0):
        # Protected attribute to implement encapsulation
        self._account_number = account_number

        self._balance = initial_balance

    def get_account_number(self):
        """Returns the account number."""
        return self._account_number

    def get_balance(self):
        """Returns the current balance."""
        return self._balance

    def deposit(self, amount):
        """Deposits funds into the account."""
        if amount > 0:
            self._balance += amount
            print(f"Deposit successful. New balance: ${self._balance:,.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        # Check against the general balance
        if amount > self._balance:
            print(f"Error: Insufficient funds. Current balance: ${self._balance:,.2f}")
            return False

        self._balance -= amount
        print(f"Withdrawal successful. Remaining balance: ${self._balance:,.2f}")
        return True

    def __str__(self):
        return f"Account #{self._account_number} | Balance: ${self._balance:,.2f}"


class SavingsAccount(BankAccount):
    """
    Subclass for a Savings Account. Adds an interest rate and calculation method.
    """

    def __init__(self, account_number, initial_balance=0.0, interest_rate=0.015):
        # Call the base class constructor (Inheritance)
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """Calculates and adds interest to the balance."""
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(
            f"Interest calculated at {self.interest_rate * 100}%: ${interest:,.2f} added. New balance: ${self._balance:,.2f}")
        return interest

    # Inherits deposit() and withdraw() from BankAccount


class CurrentAccount(BankAccount):
    """
    Subclass for a Current Account. Adds a minimum balance requirement.
    """

    def __init__(self, account_number, initial_balance=0.0, minimum_balance=100.0):
        super().__init__(account_number, initial_balance)
        self._minimum_balance = minimum_balance

    def withdraw(self, amount):
        """
        Overrides the base withdraw method to enforce the minimum balance rule. (Polymorphism)
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        # Check if withdrawal respects the minimum balance requirement
        if self._balance - amount < self._minimum_balance:
            print(
                f"Error: Withdrawal of ${amount:,.2f} would drop the balance below the minimum requirement of ${self._minimum_balance:,.2f}.")
            print(f"Current balance: ${self._balance:,.2f}")
            return False

        # If checks pass, perform the withdrawal
        self._balance -= amount
        print(f"Withdrawal successful. Remaining balance: ${self._balance:,.2f}")
        return True

    # Inherits deposit() and get_balance()


# --- Demonstration for Problem 1 ---
print("--- Problem 1 Demonstration: Bank Account ---")
# Savings Account Demo
savings = SavingsAccount("S12345", 1000.00, 0.02)
print(savings)
savings.deposit(500.00)
savings.calculate_interest()
savings.withdraw(150.00)
savings.withdraw(2000.00)  # Should fail due to insufficient funds
print("-" * 20)

# Current Account Demo
current = CurrentAccount("C67890", 500.00, 200.00)
print(current)
current.withdraw(290.00)  # Should fail because 500 - 290 = 210, which is > min_balance (200)
current.withdraw(
    300.00)  # Should fail because 500 - 300 = 200, which is == min_balance (200). Note: The problem implies remaining balance must not be *less* than min_balance. Let's assume it must be *at least* the minimum balance.
current.withdraw(100.00)  # Should succeed (500 - 100 = 400)
current.withdraw(250.00)  # Should succeed (400 - 250 = 150) -> FAIL because 150 < 200 (Minimum Balance check)
current.withdraw(100.00)  # Should succeed (400 - 100 = 300)
current.withdraw(101.00)  # Should fail (300 - 101 = 199 < 200)
print(current)
print("=" * 50 + "\n")

