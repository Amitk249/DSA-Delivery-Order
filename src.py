class DeliveryOrderAssigner:
    def __init__(self, priority_location, express_orders):
        """
        Initialize the assigner with priority order location and express orders.
        :param priority_location: Tuple representing the priority order's (x, y) coordinates.
        :param express_orders: List of tuples representing the (x, y) coordinates of express orders.
        """
        self.priority_location = priority_location
        self.express_orders = express_orders

    def squared_distance(self, x1, y1, x2, y2):
        """
        Calculate and return the squared Euclidean distance between two points.
        :param x1, y1: Coordinates of the first point.
        :param x2, y2: Coordinates of the second point.
        :return: Squared distance between the two points.
        """
        return (x2 - x1) ** 2 + (y2 - y1) ** 2

    def find_closest_express_orders(self):
        """
        Find and return the two closest express orders to the priority location.
        :return: A list of the two closest express orders (tuples of coordinates).
        """
        px, py = self.priority_location
        distances = []

        for order in self.express_orders:
            ex, ey = order
            dist = self.squared_distance(px, py, ex, ey)
            distances.append((dist, order))

        # Sort by distance and get the two closest orders
        distances.sort()
        closest_orders = [order for _, order in distances[:2]] # [(5,(1,2)), (5,(5,3)), (18,(1,2)), (18,(7,8))]

        return closest_orders

# Example usage
if __name__ == "__main__":
    # Priority order location
    priority_location = (4, 5)
    
    # Express orders locations
    express_orders = [(5, 3), (1, 2), (7, 8), (2, 4)]
    
    # Create an instance of DeliveryOrderAssigner
    assigner = DeliveryOrderAssigner(priority_location, express_orders)
    
    # Find the two closest express orders
    closest_orders = assigner.find_closest_express_orders()
    
    # Output the closest orders
    print("The two closest express orders are:", closest_orders)
    # Expected Output: [(5, 3), (2, 4)]
