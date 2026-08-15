def print_trip_summary(destination, days, budget, travel_style, hotel_cost, transport_cost,food_cost, miscellaneous_cost):
    print("===================")
    print("KelanaAI")
    print("===================")
    print(f"Destination: {destination}")
    print(f"days: {days}")
    print(f"budget: {budget}")
    print(f"travel style: {travel_style}")
    print(f"hotel cost: {hotel_cost}")
    print(f"transportation cost: {transport_cost}")
    print(f"food cost: {food_cost}")
    print(f"miscellaneous cost: {miscellaneous_cost}")
    total = hotel_cost + transport_cost + food_cost + miscellaneous_cost
    print(f"total cost: {total}")
    if total > budget:
        print("BUDGET EXCEEDED")

destination = input("destination: " )
days = int(input("days: "))
budget = float(input("budget: "))
travel_style = input("travel style: ")
hotel_cost = float(input("hotel cost: "))
transport_cost = float(input("transport cost: "))
food_cost = float(input("food cost: "))
miscellaneous_cost = float(input("miscellaneous cost: "))

result = print_trip_summary(destination, days, budget, travel_style, hotel_cost, transport_cost,food_cost, miscellaneous_cost)