"""Classes for melon orders."""

class AbstractMelonOrder():
    """Abstract base class that Melon order inherits from.""" 
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
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

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, order_type="international", tax=0.17)
        """Initialize melon order attributes."""
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type="government", tax=0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = bool(passed)