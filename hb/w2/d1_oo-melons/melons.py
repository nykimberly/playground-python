"""Classes for melon orders."""

import random
import datetime
import melon_errors

class AbstractMelonOrder():
    """Abstract base class that Melon order inherits from.""" 

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        if self.qty > 100:
            msg = "Orders cannot be over 100!"
            raise melon_errors.TooManyMelonsError(msg)
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_base_price(self):
        base_price = random.randint(5,10)
        current = datetime.datetime.now()
        current_hour = current.time().hour
        current_day = current.weekday()
        if current_day < 6 and current_hour >= 8 and current_hour <= 11:
            base_price += 4
        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        if self.species == "christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total += 3
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type="domestic", tax=0.08)

    def __repr__(self):
        return f"<DomesticMelonOrder: species={self.species},"\
                "quantity={self.qty}, shipped={self.shipped}>"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, order_type="international", tax=0.17)
        """Initialize melon order attributes."""
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

    def __repr__(self):
        return f"<InternationalMelonOrder: species={self.species},"\
                "quantity={self.qty}, country_code={self.country_code}, shipped={self.shipped}>"


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type="government", tax=0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = bool(passed)

    def __repr__(self):
        return f"<GovernmentMelonOrder: species={self.species},"\
                "quantity={self.qty}, inspection={self.passed_inspection},  shipped={self.shipped}>"




