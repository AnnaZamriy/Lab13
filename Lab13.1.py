class RIVER:
    def __init__(self, name, continent, length):
        self.name = name
        self.continent = continent
        self.length = length
    
    def change_name(self, name2):
        self.name = name2
    
    def change_length(self, new_length):
        self.length = new_length
    
    def __str__(self):
        return f"River: {self.name}, Continent: {self.continent}, Length: {self.length} km"

rivers = []

rivers.append(RIVER("Дніпро", "Європа", 2201))
rivers.append(RIVER("Міссісіпі", "Північна Америка", 3766))
rivers.append(RIVER("Горинь", "Європа", 659))

for river in rivers:
    print(river)

rivers[2].change_name("Горинь Велика")
rivers[2].change_length(2300)

for river in rivers:
    print(river)
