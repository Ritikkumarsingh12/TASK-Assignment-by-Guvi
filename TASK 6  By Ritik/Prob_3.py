# =================================================================
# PROBLEM 3: Vehicle Rental (Inheritance & Polymorphism)
# =================================================================

class Vehicle:
    """
    Base class for all rental vehicles.
    """

    def __init__(self, model, base_rental_rate):
        self.model = model
        # Protected attribute for the base rate
        self._base_rental_rate = base_rental_rate

    def calculate_rental(self, days):
        """
        Base method to calculate the total rental cost.
        Total cost = base rate * number of days.
        """
        if days <= 0:
            return 0.0
        return self._base_rental_rate * days

    def __str__(self):
        return f"{self.model} (Rate: ${self._base_rental_rate:,.2f} / day)"


class Car(Vehicle):
    """
    Car subclass. Adds a fixed cleaning fee.
    """

    def __init__(self, model, base_rental_rate, cleaning_fee=25.0):
        super().__init__(model, base_rental_rate)
        self.cleaning_fee = cleaning_fee

    def calculate_rental(self, days):
        """
        Overrides to include a one-time cleaning fee. (Polymorphism)
        """
        base_cost = super().calculate_rental(days)  # Reuse base class calculation
        total_cost = base_cost + self.cleaning_fee
        return total_cost


class Bike(Vehicle):
    """
    Bike subclass. Offers a discount for rentals of 7 days or more.
    """

    def __init__(self, model, base_rental_rate, weekly_discount_rate=0.15):
        super().__init__(model, base_rental_rate)
        self.weekly_discount_rate = weekly_discount_rate

    def calculate_rental(self, days):
        """
        Overrides to apply a weekly discount if rental is 7+ days.
        """
        base_cost = super().calculate_rental(days)

        if days >= 7:
            discount = base_cost * self.weekly_discount_rate
            print(f"(Bike Rental: Applied {self.weekly_discount_rate * 100}% weekly discount: -${discount:,.2f})")
            return base_cost - discount

        return base_cost


class Truck(Vehicle):
    """
    Truck subclass. Adds a weight limit and a surcharge if the limit is exceeded.
    """

    def __init__(self, model, base_rental_rate, max_payload_kg=5000, surcharge_per_day=50.0):
        super().__init__(model, base_rental_rate)
        self.max_payload_kg = max_payload_kg
        self.surcharge_per_day = surcharge_per_day

    def calculate_rental(self, days, payload_kg=0):
        """
        Extends the calculation to include a daily surcharge for heavy loads.
        """
        base_cost = super().calculate_rental(days)

        if payload_kg > self.max_payload_kg:
            surcharge = self.surcharge_per_day * days
            print(f"(Truck Rental: Applied daily heavy-load surcharge: +${surcharge:,.2f})")
            return base_cost + surcharge

        return base_cost


# --- Demonstration for Problem 3 ---
print("--- Problem 3 Demonstration: Vehicle Rental ---")

car = Car("Toyota Corolla", 50.0)
bike = Bike("Mountain Bike", 15.0)
truck = Truck("Ford F-350", 120.0, 4000)

print(f"{car.model} rental for 3 days: ${car.calculate_rental(3):,.2f}")
print(f"{bike.model} rental for 4 days: ${bike.calculate_rental(4):,.2f}")
print(f"{bike.model} rental for 10 days: ${bike.calculate_rental(10):,.2f}")  # Should get discount
print(f"{truck.model} rental for 2 days (Light Load): ${truck.calculate_rental(2):,.2f}")
print(
    f"{truck.model} rental for 2 days (Heavy Load - 5500kg): ${truck.calculate_rental(2, 5500):,.2f}")  # Should get surcharge