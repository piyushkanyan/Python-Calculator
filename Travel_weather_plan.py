distance_mi = int(input("Enter the travel distance (in miles): "))
if distance_mi == 0:
    print("The distance cannot be zero")
    distance_mi = int(input("Enter the travel distance (in miles): "))
elif distance_mi < 0:
    print("The distance cannot be negative")
    distance_mi = int(input("Enter the travel distance (in miles): "))
elif distance_mi > 200:
    print("The maximum distance allowed is 200 miles")
    distance_mi = int(input("Enter the travel distance (in miles): "))
else:
    print("You good to go")

is_raining = (input("Is it raining? (yes or no): ")).strip().lower()
has_bike = (input("Do you have a bike? (yes or no): ")).strip().lower()
has_car = (input("Do you have a car? (yes or no): ")).strip().lower()
has_ride_share_app = (
    (input("Do you have access to ride-sharing app? (yes or no): ")).strip().lower()
)
is_public = input("Is public transport available? (yes or no): ").lower().strip()


if distance_mi <= 1 and is_raining == "no":
    print("Walk")
    walk_speed = 3
    travel_time = (distance_mi / walk_speed) * 60
    print(f"Average walking speed: {walk_speed} mph")
    print(f"The estimated travel time is: {travel_time:.0f} minutes")
    print(f"Estimated cost is: 0")
elif distance_mi <= 5 and has_bike == "yes" and is_raining == "no":
    print("Ride your bike")
    bike_speed = 25
    bike_travel_price = distance_mi * 3
    travel_time = (distance_mi / bike_speed) * 60
    print(f"Average bike speed: {bike_speed} mph")
    print(f"The estimated travel time is: {travel_time:.0f} minutes")
    print(f"The estimated cost is {bike_travel_price}")
elif distance_mi > 5 and has_car == "yes":
    print("Drive your car")
    car_speed = 45
    car_travel_price = distance_mi * 15
    travel_time = (distance_mi / car_speed) * 60
    print(f"Average car speed: {car_speed} mph")
    print(f"The Estimated travel time is: {travel_time:.0f} minutes")
    print(f"The estimated cost is {car_travel_price}")
elif has_car == "no" and has_ride_share_app == "yes":
    print("Book a ride-sharing app")
    ride_share_speed = 40
    ride_share_travel_price = distance_mi * 25
    travel_time = (distance_mi / ride_share_speed) * 60
    print(f"Average Taxi speed: {ride_share_speed} mph")
    print(f"The estimated travel time is: {travel_time:.0f} minutes")
    print(f"The estimated cost is {ride_share_travel_price}")
elif has_ride_share_app == "no" and has_car == "no" and has_bike == "no":
    print("Use public transportation")
    public_speed = 50
    public_travel_price = distance_mi * 6
    travel_time = (distance_mi / public_speed) * 60
    print(f"Average public transport vechile speed: {public_speed} mph")
    print(f"The estimated travel time is: {travel_time:.0f} minutes")
    print(f"The estimated cost is {public_travel_price}")
else:
    print("Error")

print("=================================")
print("      Smart Travel Planner       ")
print("=================================")

print(f"The total distance is: {distance_mi}")
print(f"Is it raining: {is_raining}")
print(f"Have bike: {has_bike}")
print(f"have ride sharing app: {has_ride_share_app}")
print(f"have car: {has_car}")
print(f"Is public transport vechile available: {is_public}")
