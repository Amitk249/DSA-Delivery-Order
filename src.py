def find_closest_express_orders(priority_location, express_orders):
    # Define a function to calculate squared distance
    def squared_distance(x1, y1, x2, y2):
        return (x2 - x1) ** 2 + (y2 - y1) ** 2

    # Extract priority order location
    px, py = priority_location # priority order - (4,5)

    # Calculate squared distances for all express orders
    
    # We have created an empty list 
    distances = []
    #  for order in ex_ord {eg : [(5,3),(1,2)...]}
    for order in express_orders:
        # it check in the loop 
        ex, ey = order
        # calculate the distance priority order and express_order
        dist = squared_distance(px, py, ex, ey)
        # all th calculates distance appended 
        distances.append((dist, order))

    # Sort by distance and get the two closest orders
    distances.sort()
    # calculate the closest distances 
    closest_orders = [order for _, order in distances[:2]]
    
    return closest_orders

# Example usage
# This are the cordinates of the priority orders
    
priority_location = (4, 5)
# this are the cordinates of the express orders 
express_orders = [(5, 3), (1, 2), (7, 8), (2, 4)]
closest_orders = find_closest_express_orders(priority_location, express_orders)
print(closest_orders)  # Output: [(5, 3), (1, 2)]
