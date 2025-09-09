# Smartphone base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self._storage = storage  

    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    def get_storage(self):
        return self._storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self._storage = new_storage
        else:
            print("❌ Storage must be positive!")

# Inherited class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  
        self.gpu = gpu

    def play_game(self, game):
        print(f"🎮 Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!")

# Testing
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "Adreno 740")

phone1.call("123-456-789")
print("📂 Storage:", phone1.get_storage())

phone2.call("987-654-321")
phone2.play_game("Call of Duty Mobile")
