class Vehicle:

    def __init__(self,type,model,year,weight):
        self.type=type
        self.model=model
        self.year=year
        self.weight=weight
    
    def set_maximum_mileage(self):
        pass

    def set_towing_capacity(self):
        pass

class Car(Vehicle):
    def set_maximum_mileage(self):
        return 300000
    
    def set_towing_capacity(self):
        towing_capacity=''
        if self.weight in [1.0,2.5]:
            towing_capacity='500 kg'
        elif self.weight in [2.5,3.5]:
            towing_capacity='1 ton' 
        else:
            towing_capacity="Towing capacity is not possible"
        return towing_capacity

class Motocycle(Vehicle):
    def set_maximum_mileage(self):

        return 150000
    
    def set_towing_capacity(self):
        towing_capacity='A motocycle cannot tow another vehicles '
        return towing_capacity

class Truck(Vehicle):
    def set_maximum_mileage(self):
        return 1000000
    
    def set_towing_capacity(self):
        towing_capacity=''
        if self.weight in [30,45]:
            towing_capacity='15 tons'
        elif self.weight in [45,60]:
            towing_capacity='30 tons' 
        else:
            towing_capacity="Towing capacity is not possible"
        return towing_capacity
    

car_instance = Car(type="Hyundai", model="Tucson", year=2023, weight=2)
motorcycle_instance = Motocycle(type="Kawasaki", model="Ninja", year=2023, weight=0.5)
truck_instance = Truck(type="Scania", model="R450", year=2023, weight=40)


car_mileage = car_instance.set_maximum_mileage()
car_towing_capacity = car_instance.set_towing_capacity()

motorcycle_mileage = motorcycle_instance.set_maximum_mileage()
motorcycle_towing_capacity = motorcycle_instance.set_towing_capacity()

truck_mileage = truck_instance.set_maximum_mileage()
truck_towing_capacity = truck_instance.set_towing_capacity()

print(f"Car mileage: {car_mileage}")
print(f"Car towing capacity: {car_towing_capacity}")

print(f"Motorcycle mileage: {motorcycle_mileage}")
print(f"Motorcycle towing capacity: {motorcycle_towing_capacity}")

print(f"Truck mileage: {truck_mileage}")
print(f"Truck towing capacity: {truck_towing_capacity}")
