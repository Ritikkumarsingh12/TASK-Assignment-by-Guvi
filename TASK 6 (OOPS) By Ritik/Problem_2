# =================================================================
# PROBLEM 2: Employee Management (Inheritance & Polymorphism)
# =================================================================

class Employee:
    """
    Base class for all employees.
    """
    def __init__(self, name, base_salary):
        self.name = name
        # Using a protected attribute for base salary
        self._base_salary = base_salary

    def calculate_salary(self):
        """
        Base method for salary calculation. Must be overridden by subclasses.
        (Polymorphism)
        """
        # Return base salary as a default calculation
        return self._base_salary

    def __str__(self):
        return f"{self.name} (Base: ${self._base_salary:,.2f})"


class RegularEmployee(Employee):
    """
    Regular employees receive base salary plus a fixed bonus.
    """
    def __init__(self, name, base_salary, annual_bonus_rate=0.10):
        super().__init__(name, base_salary)
        self.annual_bonus_rate = annual_bonus_rate

    def calculate_salary(self):
        """Calculate total annual salary including bonus."""
        bonus = self._base_salary * self.annual_bonus_rate
        total_salary = self._base_salary + bonus
        return total_salary


class ContractEmployee(Employee):
    """
    Contract employees are paid per hour and only receive payment for hours worked.
    """
    def __init__(self, name, hourly_rate, hours_worked_per_month):
        # We pass a base salary of 0.0 to the base class, as their salary is calculated differently.
        super().__init__(name, 0.0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked_per_month

    def calculate_salary(self):
        """Calculate monthly salary based on hourly rate and hours worked."""
        # Calculate monthly salary for demonstration
        monthly_salary = self.hourly_rate * self.hours_worked
        # We will annualize it for consistency with others (assuming 12 months)
        return monthly_salary * 12


class Manager(Employee):
    """
    Managers receive a base salary plus a commission on team performance.
    """
    def __init__(self, name, base_salary, team_performance_commission=0.05):
        super().__init__(name, base_salary)
        self.commission_rate = team_performance_commission
        # Example: Managers might have a protected attribute for team sales performance
        self._team_sales = 50000.00

    def calculate_salary(self):
        """Calculate total annual salary including team commission."""
        commission = self._team_sales * self.commission_rate
        total_salary = self._base_salary + commission
        return total_salary


# --- Demonstration for Problem 2 (Polymorphism via a list) ---
print("--- Problem 2 Demonstration: Employee Management ---")

employees = [
    RegularEmployee("Ritik", 60000, 0.10),
    ContractEmployee("Kartik", 30.00, 160), # 160 hours/month
    Manager("puja", 90000, 0.03)
]

# We can iterate over the list and call the same method, calculate_salary,
# but get different results based on the object's class (Polymorphism).
for emp in employees:
    annual_salary = emp.calculate_salary()
    print(f"Employee: {emp.name:20} | Type: {emp.__class__.__name__:18} | Annual Salary: ${annual_salary:,.2f}")

print("=" * 50 + "\n")
