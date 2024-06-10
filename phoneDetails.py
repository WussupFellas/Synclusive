class Phone:
    def __init__(self, brand, model, capacity, used_capacity):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.used_capacity = used_capacity
    
    def storage(self):
        self.storage = (self.capacity - self.used_capacity)
        return self.storage

if __name__ == "__main__":
    phone = Phone("iPhone","15", 256, 100)
    storage = phone.storage()

print(f"Your {phone.brand} {phone.model}, with a total of {str(phone.capacity)} GB, is using {str(phone.used_capacity)} GB.")
print(f"You currently have {str(storage)} GB remaining.")