class Nuke():
    explosion = 100
    casing = "Titanium"
    kg_uranium = 25
    location = "Your location according to Google (99.999989 percentage accuracy)"
    def __init__(self):
        print("i have ur ip address")
    def orderproperties(self):
        self.kg_uranium = int(input("(numbers only plz) How many kilograms of uranium do you want to have in your nuke? (Reccomended: 25 Kilograms)"))
        self.explosion = self.kg_uranium*4
        print(f"{self.explosion} Tons of TNT (Power of explosion)")
        self.location = input("Name of place you want to nuke")
    def finalorder(self):
        print(f"Power of explosion -> {self.explosion}, Kilograms of uranium -> {self.kg_uranium}, Location -> {self.location}")

nuke1 = Nuke()
nuke1.orderproperties()
nuke1.finalorder()
        
