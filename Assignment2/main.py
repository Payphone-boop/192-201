from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "EV1234", 75)
motorbike = Motorbike("Honda", "Click", "MB5678", 125)

# Create a renter
renter = Renter("John", 12345)

print("=== Vehicles ===")
print(car)
print(electric_car)
print(motorbike)

# Rent a vehicle
print("\n=== Rent Vehicle ===")
car.rent()
print(car)

# Return the vehicle
print("\n=== Return Vehicle ===")
car.return_vehicle()
print(car)

# Show renter information
print("\n=== Renter ===")
print("Name:", renter.name)
print("License:", renter.license_no)
print("Rented vehicles:", renter.rented)

# Test invalid renter name
print("\n=== Invalid Renter Tests ===")

try:
    bad_renter = Renter("", 12345)
except ValueError as e:
    print("Caught ValueError:", e)

# Test invalid license number
try:
    bad_renter = Renter("Alice", 0)
except ValueError as e:
    print("Caught ValueError:", e)

# Test changing invalid values
try:
    renter.name = ""
except ValueError as e:
    print("Caught ValueError:", e)

try:
    renter.license_no = -10
except ValueError as e:
    print("Caught ValueError:", e)

# Polymorphism
print("\n=== Polymorphism ===")

vehicles = [car, electric_car, motorbike]

for vehicle in vehicles:
    print(vehicle)
