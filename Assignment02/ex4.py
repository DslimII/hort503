#variable for number of cars
cars = 100
#variable for space_in_a_car
space_in_a_car = 4.0
#variable for drivers
drivers = 30
#variable for passengers
passengers = 90
#variable and calculation for cars_not_driven
cars_not_driven = cars - drivers
#variable for drivers
cars_driven = drivers
#variable and calculation for car_pool_capacity
car_pool_capacity = cars_driven * space_in_a_car
#variable and calculation for average_passenger_per_car
average_passenger_per_car = passengers / cars_driven

print("There are" , cars, "cars available.")
print("There are only" , drivers, "drivers available.")
print("There will be" , cars_not_driven , "empty cars today.")
print("We can transport" , car_pool_capacity , "people today.")
print("We have" , passengers , "to carpool today.")
print("We need to put about" , average_passenger_per_car , " in each car.")
