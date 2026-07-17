import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from random import randint, choice, sample
from dataclasses import dataclass, asdict

# --- Data Tables ---
male_names = [
    "Arin", "Baldur", "Cedric", "Dain", "Eldon", "Fendrel", "Garrick", "Harlan",
    "Jasper", "Korin", "Luthor", "Merric", "Nestor", "Orin", "Pavel", "Quentin",
    "Rogar", "Soren", "Theren", "Ulric", "Varric", "Wulfe", "Xander", "Yorick", "Zane"
]
female_names = [
    "Ayla", "Brina", "Celia", "Dara", "Elora", "Fira", "Gwen", "Helena",
    "Isolde", "Jessa", "Kara", "Lira", "Mira", "Nimue", "Ophelia", "Petra",
    "Quilla", "Rina", "Selene", "Tessa", "Una", "Vera", "Wyn", "Xanthe", "Yara", "Zara"
]
races = [
    "Human", "Elf", "Dwarf", "Halfling", "Tiefling", "Dragonborn", "Gnome", "Half-Orc",
    "Half-Elf", "Aasimar", "Genasi", "Firbolg", "Goblin", "Tabaxi", "Triton", "Kenku", "Lizardfolk"
]
alignments = [
    "Lawful Good", "Neutral Good", "Chaotic Good",
    "Lawful Neutral", "True Neutral", "Chaotic Neutral",
    "Lawful Evil", "Neutral Evil", "Chaotic Evil"
]
classes = [
    "Fighter", "Wizard", "Rogue", "Cleric", "Ranger", "Paladin", "Bard", "Monk",
    "Druid", "Sorcerer", "Warlock", "Barbarian", "Artificer"
]
backgrounds = [
    "Acolyte", "Criminal", "Folk Hero", "Noble", "Sage", "Soldier", "Urchin",
    "Hermit", "Outlander", "Charlatan", "Entertainer", "Guild Artisan", "Sailor"
]
environments = ["Forest", "Dungeon", "Urban", "Plains", "Swamp", "Mountain", "Desert"]
quirks = [
    "Always humming", "Afraid of heights", "Collects shiny rocks", "Speaks in rhyme",
    "Laughs at inappropriate times", "Obsessed with cleanliness", "Talks to animals",
    "Never lies", "Constantly doodling", "Has a lucky coin", "Hates rain", "Loves riddles",
    "Writes poetry", "Sleeps with eyes open", "Always hungry", "Fears magic"
]
npc_features = [
    "Has a glowing tattoo", "Wears a mysterious amulet", "Missing an eye", "Speaks with an accent",
    "Has a pet mouse", "Wears a cloak that changes color", "Has a mechanical arm", "Always accompanied by ravens",
    "Carries a cursed book", "Has a scar shaped like a star", "Eyes change color with mood", "Laughs in their sleep",
    "Smells faintly of roses", "Shadow moves independently", "Voice echoes oddly", "Wears a holy symbol of a forgotten god",
    "Has a magical birthmark", "Wears armor made of bones", "Has a tiny familiar", "Wears a mask in public"
]
monsters = {
    "Forest": [
        "Goblin", "Wolf", "Bandit", "Sprite", "Owlbear", "Treant", "Dryad", "Giant Spider", "Dire Wolf", "Centaur"
    ],
    "Dungeon": [
        "Skeleton", "Zombie", "Gelatinous Cube", "Mimic", "Cultist", "Ghoul", "Wight", "Beholder", "Carrion Crawler", "Shadow"
    ],
    "Urban": [
        "Thug", "Spy", "Guard", "Pickpocket", "Drunkard", "Assassin", "Noble", "Bugbear", "Wererat", "Mage"
    ],
    "Plains": [
        "Gnoll", "Lion", "Bandit", "Giant Eagle", "Ankheg", "Aarakocra", "Pegasus", "Bulette", "Hobgoblin"
    ],
    "Swamp": [
        "Lizardfolk", "Giant Frog", "Will-o'-Wisp", "Crocodile", "Black Dragon Wyrmling", "Bullywug", "Giant Toad", "Hydra"
    ],
    "Mountain": [
        "Orc", "Griffon", "Stone Giant", "Hobgoblin", "Wyvern", "Harpy", "Giant Goat", "Roc", "Gargoyle"
    ],
    "Desert": [
        "Jackalwere", "Scorpion", "Bandit", "Mummy", "Giant Lizard", "Yuan-ti Pureblood", "Lamia", "Brass Dragon Wyrmling"
    ]
}
events = [
    "A merchant offers a mysterious item.",
    "A sudden storm rolls in.",
    "A lost child asks for help.",
    "A hidden trap is triggered.",
    "A rival adventuring party appears.",
    "A magical anomaly distorts reality.",
    "A local festival is underway.",
    "A noble seeks bodyguards for a secret mission.",
    "A monster flees from something scarier.",
    "A wizard is testing a new spell nearby.",
    "A traveling circus arrives in town.",
    "A haunted house is discovered.",
    "A treasure map is found.",
    "A portal opens to another plane.",
    "A local hero is accused of a crime.",
    "A dragon is spotted overhead.",
    "A mysterious illness spreads.",
    "A prophecy is revealed.",
    "A bard challenges the party to a contest.",
    "A ghost asks for help to finish unfinished business."
]
magic_items_common = ["Potion of Healing", "Spell Scroll (Cantrip)", "Bag of Tricks", "Driftglobe"]
magic_items_uncommon = ["Potion of Invisibility", "Ring of Protection", "Wand of Magic Missiles"]
magic_items_rare = ["Sword of Sharpness", "Staff of Power", "Amulet of Health"]
mundane_items = ["Rope (50ft)", "Lantern", "Gemstone", "Shield", "Ring", "Map", "Lockpick Set"]

monster_stats = {
    "Goblin":      {"HP": 7, "AC": 15, "Attack": "+4 (Scimitar, 1d6+2)", "Type": "Humanoid"},
    "Wolf":        {"HP": 11, "AC": 13, "Attack": "+4 (Bite, 2d4+2)", "Type": "Beast"},
    "Bandit":      {"HP": 11, "AC": 12, "Attack": "+3 (Scimitar, 1d6+1)", "Type": "Humanoid"},
    "Sprite":      {"HP": 2, "AC": 15, "Attack": "+6 (Shortbow, 1d6+6)", "Type": "Fey"},
    "Owlbear":     {"HP": 59, "AC": 13, "Attack": "+7 (Multiattack, 1d10+5/2d8+5)", "Type": "Monstrosity"},
    "Skeleton":    {"HP": 13, "AC": 13, "Attack": "+4 (Shortsword, 1d6+2)", "Type": "Undead"},
    "Zombie":      {"HP": 22, "AC": 8, "Attack": "+3 (Slam, 1d6+1)", "Type": "Undead"},
    "Gelatinous Cube": {"HP": 84, "AC": 6, "Attack": "+4 (Pseudopod, 3d6+2)", "Type": "Ooze"},
    "Mimic":       {"HP": 58, "AC": 12, "Attack": "+5 (Bite, 1d8+3)", "Type": "Monstrosity"},
    "Cultist":     {"HP": 9, "AC": 12, "Attack": "+3 (Scimitar, 1d6+1)", "Type": "Humanoid"},
    "Thug":        {"HP": 32, "AC": 11, "Attack": "+4 (Mace, 1d6+2)", "Type": "Humanoid"},
    "Spy":         {"HP": 27, "AC": 12, "Attack": "+4 (Shortsword, 1d6+2)", "Type": "Humanoid"},
    "Guard":       {"HP": 11, "AC": 16, "Attack": "+3 (Spear, 1d6+1)", "Type": "Humanoid"},
    "Pickpocket":  {"HP": 8, "AC": 12, "Attack": "+2 (Dagger, 1d4+2)", "Type": "Humanoid"},
    "Drunkard":    {"HP": 6, "AC": 10, "Attack": "+1 (Unarmed, 1d4)", "Type": "Humanoid"},
    "Gnoll":       {"HP": 22, "AC": 15, "Attack": "+4 (Spear, 1d8+2)", "Type": "Humanoid"},
    "Lion":        {"HP": 26, "AC": 12, "Attack": "+5 (Bite, 1d8+3)", "Type": "Beast"},
    "Giant Eagle": {"HP": 26, "AC": 13, "Attack": "+5 (Talons, 2d6+3)", "Type": "Beast"},
    "Lizardfolk":  {"HP": 22, "AC": 15, "Attack": "+4 (Bite, 1d8+2)", "Type": "Humanoid"},
    "Giant Frog":  {"HP": 18, "AC": 11, "Attack": "+3 (Bite, 1d6+1)", "Type": "Beast"},
    "Will-o'-Wisp":{"HP": 22, "AC": 19, "Attack": "+4 (Shock, 2d8)", "Type": "Undead"},
    "Crocodile":   {"HP": 19, "AC": 12, "Attack": "+4 (Bite, 1d10+2)", "Type": "Beast"},
    "Orc":         {"HP": 15, "AC": 13, "Attack": "+5 (Greataxe, 1d12+3)", "Type": "Humanoid"},
    "Griffon":     {"HP": 59, "AC": 12, "Attack": "+6 (Multiattack, 2d8+4/2d6+4)", "Type": "Monstrosity"},
    "Stone Giant": {"HP": 126, "AC": 17, "Attack": "+9 (Rock, 7d6+6)", "Type": "Giant"},
    "Hobgoblin":   {"HP": 11, "AC": 18, "Attack": "+3 (Longsword, 1d8+1)", "Type": "Humanoid"},
    "Jackalwere":  {"HP": 18, "AC": 12, "Attack": "+2 (Bite, 1d4+2)", "Type": "Shapechanger"},
    "Scorpion":    {"HP": 7, "AC": 11, "Attack": "+2 (Sting, 1d6+2)", "Type": "Beast"},
    "Mummy":       {"HP": 58, "AC": 11, "Attack": "+5 (Rotting Fist, 2d6+3)", "Type": "Undead"},
    # Add more as needed
}

monster_xp = {
    "Goblin": 50, "Wolf": 50, "Bandit": 25, "Sprite": 10, "Owlbear": 700,
    "Skeleton": 50, "Zombie": 50, "Gelatinous Cube": 450, "Mimic": 450, "Cultist": 25,
    "Thug": 100, "Spy": 200, "Guard": 25, "Pickpocket": 25, "Drunkard": 10,
    "Gnoll": 100, "Lion": 100, "Giant Eagle": 200, "Lizardfolk": 100, "Giant Frog": 50,
    "Will-o'-Wisp": 450, "Crocodile": 50, "Orc": 100, "Griffon": 700, "Stone Giant": 2900,
    "Hobgoblin": 100, "Jackalwere": 200, "Scorpion": 10, "Mummy": 700,
    # Add more as needed
}

# --- Dataclasses ---
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

@dataclass
class Chest:
    Level: str
    Copper: int
    Silver: int
    Electrum: int
    Gold: int
    Platinum: int
    Items: list

@dataclass
class Encounter:
    Environment: str
    Difficulty: str
    Monsters: list
    Event: str

# --- Generators ---
def generate_npc(gender=None, lawful=None, min_age=16, max_age=80):
    gender = gender if gender in ["Male", "Female"] else choice(["Male", "Female"])
    name = choice(male_names if gender == "Male" else female_names)
    race = choice(races)
    cls = choice(classes)
    age = randint(min_age, max_age)
    alignment = choice([a for a in alignments if (lawful is None or a.startswith("Lawful") == lawful)])
    lawful_val = alignment.startswith("Lawful")
    background = choice(backgrounds)
    quirk = choice(quirks)
    feature = choice(npc_features)
    stats = {stat: randint(3, 18) for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]}
    return NPC(name, gender, race, cls, age, alignment, lawful_val, background, quirk, feature, **stats)

def generate_chest(level):
    # Coin logic based on chest level
    coins = {
        "Common":  (randint(10, 100), randint(5, 50), randint(0, 10), randint(0, 10), randint(0, 1)),
        "Uncommon":(randint(50, 200), randint(20, 100), randint(5, 30), randint(10, 50), randint(0, 3)),
        "Rare":    (randint(100, 500), randint(50, 200), randint(10, 50), randint(50, 200), randint(1, 10)),
        "Very Rare":(randint(200, 1000), randint(100, 500), randint(20, 100), randint(100, 500), randint(5, 20))
    }
    c, s, e, g, p = coins[level]
    # Items logic
    items = []
    if level == "Common":
        items += sample(mundane_items, k=randint(1, 2))
        if randint(1, 4) == 1: items.append(choice(magic_items_common))
    elif level == "Uncommon":
        items += sample(mundane_items, k=randint(2, 3))
        items += sample(magic_items_common, k=randint(1, 2))
        if randint(1, 3) == 1: items.append(choice(magic_items_uncommon))
    elif level == "Rare":
        items += sample(mundane_items, k=randint(2, 4))
        items += sample(magic_items_uncommon, k=randint(1, 2))
        if randint(1, 2) == 1: items.append(choice(magic_items_rare))
    else: # Very Rare
        items += sample(mundane_items, k=randint(3, 5))
        items += sample(magic_items_uncommon, k=randint(2, 3))
        items += sample(magic_items_rare, k=randint(1, 2))
    return Chest(level, c, s, e, g, p, items)

def generate_encounter(env, difficulty, party_level):
    # XP budgets from DMG p.56 for 4 PCs
    xp_budgets = {
        "Easy":  [25, 50, 75, 125, 250, 300, 350, 450, 550, 600, 800, 1000, 1100, 1250, 1400, 1600, 1800, 2000, 2200, 2400],
        "Medium":[50, 100, 150, 250, 500, 600, 750, 900, 1100, 1200, 1600, 2000, 2200, 2500, 2800, 3200, 3600, 4000, 4400, 4800],
        "Hard":  [75, 150, 225, 375, 750, 900, 1100, 1400, 1700, 1900, 2400, 3000, 3300, 3800, 4300, 4800, 5400, 6000, 6600, 7200],
        "Deadly":[100, 200, 400, 500, 1100, 1400, 1700, 2100, 2400, 2800, 3200, 4000, 4400, 5000, 5700, 6400, 7200, 8000, 8800, 9600]
    }
    party_level = max(1, min(20, int(party_level)))
    xp_budget = xp_budgets[difficulty][party_level-1]
    monsters_list = monsters.get(env, monsters["Forest"])
    chosen = []
    total_xp = 0
    tries = 0
    # Try to fill the XP budget with monsters, but don't go over 8 monsters
    while total_xp < xp_budget and tries < 100:
        m = choice(monsters_list)
        xp = monster_xp.get(m, 50)
        if total_xp + xp > xp_budget or len(chosen) >= 8:
            break
        chosen.append(m)
        total_xp += xp
        tries += 1
    event = choice(events)
    return Encounter(env, difficulty, chosen, event)

def ability_modifier(score):
    return (score - 10) // 2

# --- UI Functions ---
def npc_generate_ui():
    gender = npc_gender_var.get()
    lawful = None if npc_lawful_var.get() == "Any" else (npc_lawful_var.get() == "Lawful")
    min_age = int(npc_min_age.get())
    max_age = int(npc_max_age.get())
    npc = generate_npc(gender if gender != "Any" else None, lawful, min_age, max_age)
    output_npc.config(state="normal")
    output_npc.delete(1.0, tk.END)
    for k, v in asdict(npc).items():
        if k in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            mod = ability_modifier(v)
            output_npc.insert(tk.END, f"{k}: {v} ({mod:+d})\n")
        else:
            output_npc.insert(tk.END, f"{k}: {v}\n")
    output_npc.config(state="disabled")

def chest_generate_ui():
    level = chest_level_var.get()
    chest = generate_chest(level)
    output_chest.config(state="normal")
    output_chest.delete(1.0, tk.END)
    output_chest.insert(tk.END, f"Chest Level: {chest.Level}\n")
    output_chest.insert(tk.END, f"Copper: {chest.Copper}\nSilver: {chest.Silver}\nElectrum: {chest.Electrum}\nGold: {chest.Gold}\nPlatinum: {chest.Platinum}\n")
    output_chest.insert(tk.END, "Items:\n")
    for item in chest.Items:
        output_chest.insert(tk.END, f"- {item}\n")
    output_chest.config(state="disabled")

def encounter_generate_ui():
    env = encounter_env_var.get()
    diff = encounter_diff_var.get()
    party_level = encounter_party_level_var.get()
    enc = generate_encounter(env, diff, party_level)
    output_encounter.config(state="normal")
    output_encounter.delete(1.0, tk.END)
    output_encounter.insert(tk.END, f"Environment: {enc.Environment}\nDifficulty: {enc.Difficulty}\nParty Level: {party_level}\n")
    output_encounter.insert(tk.END, f"Event: {enc.Event}\n")
    for m in enc.Monsters:
        stats = monster_stats.get(m, {
            "HP": randint(8, 30),
            "AC": randint(10, 16),
            "Attack": "+2 (Attack, 1d6+2)",
            "Type": "Unknown"
        })
        stat_items = list(stats.items())
        output_encounter.insert(tk.END, f"{m}\n")
        for i, (stat_name, stat_value) in enumerate(stat_items):
            prefix = "├──" if i < len(stat_items) - 1 else "└──"
            output_encounter.insert(tk.END, f"{prefix} {stat_name}: {stat_value}\n")
    output_encounter.config(state="disabled")

def export_to_txt(text_widget, title):
    content = text_widget.get(1.0, tk.END).strip()
    if not content:
        messagebox.showinfo("Export", "Nothing to export!")
        return
    fname = f"{title}_export.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    messagebox.showinfo("Export", f"Exported to {fname}")

def copy_to_clipboard(text_widget):
    content = text_widget.get(1.0, tk.END).strip()
    if not content:
        messagebox.showinfo("Copy", "Nothing to copy!")
        return
    root.clipboard_clear()
    root.clipboard_append(content)
    messagebox.showinfo("Copy", "Copied to clipboard!")

# --- UI Setup ---
root = tk.Tk()
root.title("")  # Remove window text
root.geometry("560x500")
root.resizable(True, True)

notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- NPC Tab ---
npc_tab = ttk.Frame(notebook)
notebook.add(npc_tab, text="NPC Generator")

npc_gender_var = tk.StringVar(value="Any")
npc_lawful_var = tk.StringVar(value="Any")
npc_min_age = tk.StringVar(value="16")
npc_max_age = tk.StringVar(value="80")

npc_filters = ttk.LabelFrame(npc_tab, text="Filters", padding=10)
npc_filters.grid(row=0, column=0, sticky="ew", padx=8, pady=8)

ttk.Label(npc_filters, text="Gender:").grid(row=0, column=0, sticky="w", padx=4)
ttk.OptionMenu(npc_filters, npc_gender_var, "Any", "Any", "Male", "Female").grid(row=0, column=1, sticky="w", padx=4)

ttk.Label(npc_filters, text="Lawful:").grid(row=0, column=2, sticky="w", padx=4)
ttk.OptionMenu(npc_filters, npc_lawful_var, "Any", "Any", "Lawful", "Chaotic").grid(row=0, column=3, sticky="w", padx=4)

ttk.Label(npc_filters, text="Age:").grid(row=0, column=4, sticky="w", padx=4)
ttk.Entry(npc_filters, textvariable=npc_min_age, width=5).grid(row=0, column=5, padx=2)
ttk.Label(npc_filters, text="-").grid(row=0, column=6)
ttk.Entry(npc_filters, textvariable=npc_max_age, width=5).grid(row=0, column=7, padx=2)

ttk.Button(npc_tab, text="Generate NPC", command=npc_generate_ui).grid(row=1, column=0, pady=8, sticky="ew", padx=8)
output_npc = scrolledtext.ScrolledText(npc_tab, width=62, height=15, font=('Consolas', 11))
output_npc.grid(row=2, column=0, padx=8, pady=8)
output_npc.config(state="disabled")
ttk.Button(npc_tab, text="Copy", command=lambda: copy_to_clipboard(output_npc)).grid(row=3, column=0, sticky="w", padx=8, pady=4)
ttk.Button(npc_tab, text="Export", command=lambda: export_to_txt(output_npc, "npc")).grid(row=3, column=0, sticky="e", padx=8, pady=4)

# --- Chest Tab ---
chest_tab = ttk.Frame(notebook)
notebook.add(chest_tab, text="Chest Generator")

chest_level_var = tk.StringVar(value="Common")
ttk.Label(chest_tab, text="Chest Level:").grid(row=0, column=0, sticky="w", padx=8, pady=8)
ttk.OptionMenu(chest_tab, chest_level_var, "Common", "Common", "Uncommon", "Rare", "Very Rare").grid(row=0, column=1, sticky="w", padx=8)
ttk.Button(chest_tab, text="Generate Chest", command=chest_generate_ui).grid(row=0, column=2, padx=8, pady=8)
output_chest = scrolledtext.ScrolledText(chest_tab, width=62, height=15, font=('Consolas', 11))
output_chest.grid(row=1, column=0, columnspan=3, padx=8, pady=8)
output_chest.config(state="disabled")
ttk.Button(chest_tab, text="Copy", command=lambda: copy_to_clipboard(output_chest)).grid(row=2, column=0, sticky="w", padx=8, pady=4)
ttk.Button(chest_tab, text="Export", command=lambda: export_to_txt(output_chest, "chest")).grid(row=2, column=2, sticky="e", padx=8, pady=4)

# --- Encounter Tab ---
encounter_tab = ttk.Frame(notebook)
notebook.add(encounter_tab, text="Encounter Generator")

encounter_env_var = tk.StringVar(value="Forest")
encounter_diff_var = tk.StringVar(value="Medium")
encounter_party_level_var = tk.StringVar(value="1")
encounter_filters = ttk.LabelFrame(encounter_tab, text="Filters", padding=10)
encounter_filters.grid(row=0, column=0, columnspan=5, sticky="ew", padx=8, pady=8)

ttk.Label(encounter_filters, text="Environment:").grid(row=0, column=0, sticky="w", padx=8)
ttk.OptionMenu(encounter_filters, encounter_env_var, "Forest", *environments).grid(row=0, column=1, sticky="w", padx=8)
ttk.Label(encounter_filters, text="Difficulty:").grid(row=0, column=2, sticky="w", padx=8)
ttk.OptionMenu(encounter_filters, encounter_diff_var, "Medium", "Easy", "Medium", "Hard").grid(row=0, column=3, sticky="w", padx=8)
ttk.Label(encounter_filters, text="Party Level:").grid(row=0, column=4, sticky="w", padx=8)
ttk.Entry(encounter_filters, textvariable=encounter_party_level_var, width=4).grid(row=0, column=5, padx=2)

ttk.Button(encounter_tab, text="Generate Encounter", command=encounter_generate_ui).grid(row=1, column=0, columnspan=5, pady=8, sticky="ew", padx=8)
output_encounter = scrolledtext.ScrolledText(encounter_tab, width=62, height=15, font=('Consolas', 11))
output_encounter.grid(row=2, column=0, columnspan=5, padx=8, pady=8)
output_encounter.config(state="disabled")
ttk.Button(encounter_tab, text="Copy", command=lambda: copy_to_clipboard(output_encounter)).grid(row=3, column=0, sticky="w", padx=8, pady=4)
ttk.Button(encounter_tab, text="Export", command=lambda: export_to_txt(output_encounter, "encounter")).grid(row=3, column=4, sticky="e", padx=8, pady=4)

root.mainloop()
