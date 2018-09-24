############
# Part 1   #
############

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', True, False, 'Casaba')
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', True, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', True, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with: ")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print("")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melons_by_code = {}
    for melon in melon_types:
        if melon.code not in melons_by_code:
           melons_by_code[melon.code] = melon

    return melons_by_code

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field,
            harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons = []
    melon_by_code = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melon_by_code['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_by_code['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_by_code['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_by_code['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_by_code['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_by_code['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_by_code['cren'], 6, 7, 4, 'Michael')
    melon_8 = Melon(melon_by_code['musk'], 7, 10, 3, 'Sheila')
    melon_9 = Melon(melon_by_code['musk'], 7, 10, 3, 'Sheila')
    melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5,melon_6, melon_7, melon_8, melon_9])
    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.shape_rating > 5  and melon.color_rating > 5 and melon.field != 3:
            sellable = "CAN BE SOLD"
        else:
            sellable = "NOT SELLABLE"
        print(f"Harvested by {melon.harvester} from Field {melon.field} {sellable}")


if __name__ == "__main__":
    all_melon_types = make_melon_types()
    print_pairing_info(all_melon_types)
    harvest = make_melons(all_melon_types)
    get_sellability_report(harvest)
