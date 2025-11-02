from random import randint
from dataclasses import dataclass, asdict

# --- NPC Data ---
male_names = ["Arin", "Baldur", "Cedric", "Dain", "Eldon"]
female_names = ["Ayla", "Brina", "Celia", "Dara", "Elora"]
races = ["Human", "Elf", "Dwarf", "Halfling", "Tiefling"]
classes = ["Fighter", "Wizard", "Rogue", "Cleric", "Ranger"]
alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral"]
backgrounds = ["Acolyte", "Criminal", "Folk Hero", "Noble", "Sage"]
quirks = ["Always humming", "Afraid of heights", "Collects shiny rocks"]
npc_features = ["Has a glowing tattoo", "Wears a mysterious amulet", "Missing an eye"]

# --- Chest Data ---
COIN_TABLE = {
    "Common": lambda: f"{randint(10, 60)} gp",
    "Uncommon": lambda: f"{randint(50, 200)} gp, {randint(10, 40)} pp",
    "Rare": lambda: f"{randint(200, 1000)} gp, {randint(50, 200)} pp",
    "Very Rare": lambda: f"{randint(1000, 5000)} gp, {randint(200, 1000)} pp",
    "Legendary": lambda: f"{randint(5000, 20000)} gp, {randint(1000, 5000)} pp",
}
GEMS_TABLE = {
    "Common": ["None", "1d4 x 10 gp gems"],
    "Uncommon": ["1d6 x 50 gp gems", "1d4 x 100 gp gems"],
    "Rare": ["1d6 x 250 gp gems", "1d4 x 500 gp gems"],
    "Very Rare": ["1d6 x 1000 gp gems", "1d4 x 5000 gp gems"],
    "Legendary": ["1d6 x 10000 gp gems", "1d4 x 25000 gp gems"],
}
MAGIC_ITEMS_TABLE = {
    "Common": ["Potion of Healing", "Spell Scroll (cantrip)", "Ammunition, +1"],
    "Uncommon": ["+1 Weapon", "Bag of Holding", "Potion of Greater Healing"],
    "Rare": ["+2 Weapon", "Cloak of Protection", "Ring of Evasion"],
    "Very Rare": ["+3 Weapon", "Staff of Power", "Ring of Regeneration"],
    "Legendary": ["Vorpal Sword", "Staff of the Magi", "Ring of Three Wishes"],
}
mundane_weapons = ["Shortsword", "Longsword", "Dagger", "Battleaxe", "Mace", "Spear", "Warhammer", "Light Crossbow"]

# --- Shop Data (new) ---
SHOP_TYPES = {
    "General": {
        "items": [
            "Torch", "Rations (1 day)", "Rope (50 ft)", "Backpack", "Waterskin",
            "Bedroll", "Lantern", "Crowbar", "Fishing tackle", "Ink & quill"
        ],
        "price_range": (1, 20)
    },
    "Blacksmith": {
        "items": [
            "Iron Dagger", "Shortsword (steel)", "Longsword (steel)", "Battleaxe (iron)",
            "Warhammer (iron)", "Nails & hinges", "Horseshoes", "Tool kit (smith's)"
        ],
        "price_range": (5, 200)
    },
    "Armorer": {
        "items": [
            "Padded Armor", "Leather Armor", "Studded Leather", "Chain Shirt",
            "Scale Mail", "Chain Mail", "Plate (used)", "Shield"
        ],
        "price_range": (10, 1500)
    },
    "Fletcher": {
        "items": [
            "Shortbow", "Longbow", "Quiver (20 arrows)", "Crossbow bolts (20)",
            "Arrows (10)", "Bow string", "Arrowheads (20)"
        ],
        "price_range": (1, 120)
    },
    "Alchemist": {
        "items": [
            "Alchemist's Fire (vial)", "Antitoxin", "Tanglefoot Bag", "Smokestick",
            "Acid (vial)", "Glassware set", "Herbal components"
        ],
        "price_range": (5, 500)
    },
    "Magic Shop": {
        "items": [
            "Cantrip Scroll", "Potion of Healing", "Lesser Wand", "Spellbook (common spells)",
            "Enchanted trinket", "Mystic ink", "Scroll of Detect Magic"
        ],
        "price_range": (20, 2000)
    },
    "Jeweler": {
        "items": [
            "Silver ring", "Gold necklace", "Gemstone (small)", "Pearl",
            "Earring", "Watch (ornamental)"
        ],
        "price_range": (10, 5000)
    },
    "Temple": {
        "items": [
            "Holy water", "Prayer beads", "Healing poultice", "Religious icon",
            "Blessed incense", "Cleric scroll (minor)"
        ],
        "price_range": (1, 200)
    }
}

# --- Event Data ---
events = [
    "A sudden storm rolls in.",
    "A mysterious traveler arrives.",
    "A local festival begins.",
    "Bandits ambush the party.",
    "A magical portal opens nearby.",
    "A lost child asks for help.",
    "A merchant offers a rare item.",
    "A rival adventuring party appears.",
    "A monster attacks the village.",
    "A treasure map is discovered."
]

@dataclass
class NPC:
    Name: str
    Gender: str
    Race: str
    Class: str
    Age: int
    Alignment: str
    Lawful: bool
    Background: str
    Feature: str 
    Quirk: str
    Strength: int
    Dexterity: int
    Constitution: int
    Intelligence: int
    Wisdom: int
    Charisma: int

def ability_modifier(score):
    return (score - 10) // 2

def random_from_list(lst):
    return lst[randint(0, len(lst) - 1)]

def generate_npc():
    gender = random_from_list(["Male", "Female"])
    name = random_from_list(male_names) if gender == "Male" else random_from_list(female_names)
    race = random_from_list(races)
    cls = random_from_list(classes)
    age = randint(16, 80)
    alignment = random_from_list(alignments)
    lawful_val = alignment.startswith("Lawful")
    background = random_from_list(backgrounds)
    quirk = random_from_list(quirks)
    feature = random_from_list(npc_features)
    stats = {stat: randint(3, 18) for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]}
    return NPC(name, gender, race, cls, age, alignment, lawful_val, background, quirk, feature, **stats)

def print_npc(npc):
    print("\n--- NPC Generated ---")
    for k, v in asdict(npc).items():
        if k in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            mod = ability_modifier(v)
            print(f"{k}: {v} ({mod:+d})")
        else:
            print(f"{k}: {v}")

def roll_gems(tier):
    entry = random_from_list(GEMS_TABLE[tier])
    if "None" in entry:
        return "None"
    num, value = entry.split(" x ")
    dice, mult = num.split("d")
    gems = sum(randint(1, int(mult)) for _ in range(int(dice)))
    return f"{gems} gems worth {value} each"

def roll_magic_items(tier):
    return random_from_list(MAGIC_ITEMS_TABLE[tier])

def generate_chest():
    tiers = list(COIN_TABLE.keys())
    print("\nChoose chest tier:")
    for i, t in enumerate(tiers, 1):
        print(f"{i}. {t}")
    while True:
        try:
            choice = int(input("Tier (1-5): "))
            if 1 <= choice <= 5:
                break
        except ValueError:
            pass
        print("Invalid input. Please enter a number from 1 to 5.")
    tier = tiers[choice - 1]
    chest = {}
    if randint(1, 100) <= 80:  # 80% chance for coins
        chest["Coins"] = COIN_TABLE[tier]()
    if randint(1, 100) <= 50:  # 50% chance for gems
        chest["Gems"] = roll_gems(tier)
    if randint(1, 100) <= 30:  # 30% chance for magic items
        chest["Magic Item"] = roll_magic_items(tier)
    if randint(1, 100) <= 40:  # 40% chance for mundane weapon
        chest["Weapon"] = random_from_list(mundane_weapons)
    if not chest:
        chest["Empty"] = "This chest is empty. (Unlucky!)"
    print("\n--- Chest Generated ---")
    for k, v in chest.items():
        print(f"{k}: {v}")

def generate_event():
    print("\n--- Event Generated ---")
    print(random_from_list(events))

# --- Shop Generator (new) ---
def format_price(gp):
    return f"{gp} gp"

def generate_shop():
    shop_keys = list(SHOP_TYPES.keys())
    print("\nChoose shop type:")
    for i, s in enumerate(shop_keys, 1):
        print(f"{i}. {s}")
    print(f"{len(shop_keys)+1}. Random")
    while True:
        try:
            choice = int(input(f"Shop (1-{len(shop_keys)+1}): "))
            if 1 <= choice <= len(shop_keys)+1:
                break
        except ValueError:
            pass
        print("Invalid input.")
    if choice == len(shop_keys)+1:
        shop_type = random_from_list(shop_keys)
    else:
        shop_type = shop_keys[choice - 1]

    shop_info = SHOP_TYPES[shop_type]
    possible_items = shop_info["items"]
    low, high = shop_info["price_range"]

    # choose a number of items to stock
    stock_count = randint(5, min(12, len(possible_items)))
    picked_indices = set()
    inventory = []
    while len(inventory) < stock_count:
        idx = randint(0, len(possible_items) - 1)
        if idx in picked_indices:
            continue
        picked_indices.add(idx)
        item = possible_items[idx]
        base_price = randint(low, high)
        # small random modifier for flavor
        price = max(1, int(base_price * (0.8 + randint(0, 40) / 100.0)))
        inventory.append((item, price))

    print(f"\n--- {shop_type} Inventory ---")
    for item, price in inventory:
        print(f"{item} - {format_price(price)}")

def main_menu():
    while True:
        print("\nWhat would you like to generate?")
        print("1. NPC")
        print("2. Chest")
        print("3. Event")
        print("4. Shop")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")
        if choice == "1":
            npc = generate_npc()
            print_npc(npc)
        elif choice == "2":
            generate_chest()
        elif choice == "3":
            generate_event()
        elif choice == "4":
            generate_shop()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    print("D&D 5e NPC, Chest, Event and Shop Generator")
    main_menu()