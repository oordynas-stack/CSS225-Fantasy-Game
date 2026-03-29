class Player:
    def __init__(self, name):
        self.name = name
        self.has_passphrase = False
        self.status = "Healthy"
        self.inventory = [] # Added this list

    def add_item(self, item):
        self.inventory.append(item)
        print(f"[ITEM ADDED]: {item}")