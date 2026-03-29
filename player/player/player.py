class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.status = "Healthy"
        self.has_passphrase = False

    def add_item(self, item):
        self.inventory.append(item)
        print(f"[ITEM ADDED]: {item}")
