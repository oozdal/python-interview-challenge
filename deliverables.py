
# You operate a delivery service with a company location. You have three clients, 
# each requesting a specific quantity of items and located at varying distances from your company.
# The company can only deliver items within a certain distance from its location, 
# and there's a maximum weight limit for deliveries.

# Here are the details:

#    Client 1 requests 5 bags of apples and is located 50 km away.
#    Client 2 requests 10 bags of oranges and is located 100 km away.
#    Client 3 requests 20 watermelons and is located 250 km away.
#    The company can only deliver within 100 km of its location.
#    The maximum weight the company can carry is 70 kg.

# Your task is to design a system to manage these delivery requests:

#    Create a class called Delivery that can store information about a client's request, 
#    including the client's name, requested item, quantity, and distance from the company's location.

#    Design another class called DeliverySchedule to handle scheduling deliveries. This class should be able to take all the requests and determine whether the company can fulfill them based on the maximum distance and weight constraints.

# Your program should output whether the company can deliver the requested items considering the maximum distance and weight constraints.

from typing import List

class Delivery:
    def __init__(self, client_name, items, distance, weight):
        self.client_name = client_name
        self.items = items
        self.distance = distance
        self.weight = weight

    def get_client_name(self):
        return self.client_name

    def get_items(self):
        return self.items

    def get_distance(self):
        return self.distance
    
    def get_weight(self):
        return self.weight


class Schedule:
    def __init__(self, max_distance = 100, max_weight = 80):
        self.max_distance = max_distance
        self.max_weight = max_weight

    def can_deliver(self, deliveries: List):
        deliverable_clients = []
        for delivery in deliveries:
            if delivery.get_distance() <= self.max_distance and delivery.get_weight() <= self.max_weight:
                deliverable_clients.append(delivery.get_client_name())
        return deliverable_clients
    
    
if __name__ == '__main__':
    # Testing
    delivery_client1 = Delivery("client1", "5 bags of apples", 50, 30)
    delivery_client2 = Delivery("client2", "10 bags of oranges", 100, 50)
    delivery_client3 = Delivery("client3", "20 watermelons", 250, 80)

    deliveries = [delivery_client1, delivery_client2, delivery_client3]

    schedule_service = Schedule()
    deliverable_clients = schedule_service.can_deliver(deliveries)
    print("Clients to whom the company can deliver some items:", deliverable_clients)