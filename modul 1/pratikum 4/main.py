class Hero:
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    def siapa(self):
        return f"{self.name} memiliki power {self.power}"

    def healthUp(self, up):
        self.health += up
        
    def gethealth(self):
        return self.health
    
    # Method baru dengan parameter dan return value
    def serang(self, target):
        """Method untuk menyerang hero lain"""
        damage = max(0, self.power - target.armor)  # Damage dikurangi armor target
        target.health -= damage
        return f"{self.name} menyerang {target.name} dengan damage {damage}!"

hero1 = Hero("Sniper", 100, 10, 5)
hero2 = Hero("Axe", 200, 15, 0)

print(hero1.siapa())
hero1.armor = 10
print(f"Armor {hero1.name} = {hero1.armor}") 
print(f"Jumlah hero = {Hero.jumlah}")
hero1.healthUp(20)
print(f"Health {hero1.name} = {hero1.gethealth()}")
print(f"Health {hero2.name} = {hero2.gethealth()}")

# Demonstrasi method baru dengan parameter dan return value
print("\n=== METHOD BARU ===")
hasil_serang = hero1.serang(hero2)  # Memanggil method dengan parameter
print(hasil_serang)
print(f"Health {hero2.name} setelah diserang = {hero2.gethealth()}")