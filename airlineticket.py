""" 
Airline Ticket Price Calculator
You’re building a tool to calculate the cost of various airplane tickets based on the airline, distance and seating class. Your tool must take in this information as a series of inputs (one ticket calculation per line of input) and produce a list of output costs.
Each airline contains its own cost requirements. Ultimately, the airline is only interested in two major components: the space (seating class) you take on the plane, and the distance you fly. You must generate ticket costs using this gathered data:
Airlines: United, Delta, Southwest, American
Operating Costs
 - Economy:  $0
 - Premium:  $0.10/mile up to a maximum of $25
 - Business: $50 + $0.25/mile
Per-Airline Prices
 - United charges $0.50/mile
   + OperatingCost

 - Delta charges $0.9/mile

 - Southwest charges $0.75/mile
   + OperatingCost
   + $0.10/mile for Premium seats

 - American charges the maximum of 2 * OperatingCost and $1/mile
Keep in mind that, while there are only four airlines listed above, your solution should be able to expand to dozens of individual airlines, whose ticket cost can be based on arbitrary functions of “Operating Costs”, miles, and/or seating class.
You can assume that the input will be provided as a list of strings and that there could be millions of lines of input. Each string will provide the Airline, Distance and Seating Class. Please review the examples
"""


def calulcate_operating_cost(seatingclass, miles):
    if seatingclass == "Economy":
        return 0
    elif seatingclass == "Premium":
        return min(0.10 * miles, 25)
    elif seatingclass == "Business":
        return 50 + (0.25 * miles)
    else:
        return "Invalid seating class"
    
def calculate_airline_cost(airline, seatingclass, miles):
    operating_cost = calulcate_operating_cost(seatingclass, miles)

    if airline == "United":
        travel_cost = 0.5 * miles + operating_cost
    elif airline == "Delta":
        travel_cost =  0.9 * miles + operating_cost
    elif airline == "Southwest":
        if seatingclass == "Premium":
            travel_cost = 0.75 * miles  + operating_cost +  0.10 * miles
        else:
            travel_cost = 0.75 * miles  + operating_cost
    elif airline == "American":
        travel_cost = max( 2 * operating_cost, 1 * miles )
    else:
        ValueError ("Airline is invalid")
    return travel_cost


# input_values = input("Enter airline, seating class, distance in comma seperated")

ticket_data = [
    "United,Economy,300",
    "Delta,Business,1500",
    "Southwest,Premium,200",
    "American,Economy,800"
]

for ticket_cost in ticket_data:
    airline, seatingclass, distance = ticket_cost.split(",")
    miles = int(distance)
    cost = calculate_airline_cost(airline, seatingclass, miles )
    print(
        f"Airline: {airline}\n", f"Seating class: {seatingclass}\n" , f"cost: {cost}\n"
        )
