# DSA-Delivery-Order

## Overview

The `DeliveryOrderAssigner` class is designed to find the two closest express orders to a given priority order location using squared Euclidean distance. This class is useful in scenarios where a priority order must be fulfilled quickly, and the closest available resources (express orders) need to be identified.

## Features

- **Squared Distance Calculation:** Efficiently computes squared Euclidean distance to avoid unnecessary floating-point operations.
- **Closest Orders Selection:** Identifies and returns the two closest express orders based on the computed distances.
  
## How to Use

1. **Initialize the Class:**
   - Create an instance of the `DeliveryOrderAssigner` class by passing the priority order's location and a list of express orders' locations.
   - Example:
     ```python
     priority_location = (4, 5)
     express_orders = [(5, 3), (1, 2), (7, 8), (2, 4)]
     assigner = DeliveryOrderAssigner(priority_location, express_orders)
     ```

2. **Find Closest Orders:**
   - Call the `find_closest_express_orders` method on the instance to get the two closest express orders.
   - Example:
     ```python
     closest_orders = assigner.find_closest_express_orders()
     print("The two closest express orders are:", closest_orders)
     ```
  
3. **Output:**
   - The method will return a list of tuples representing the coordinates of the two closest express orders.
   - Expected Output:
     ```python
     [(5, 3), (2, 4)]
     ```

## Example

```python
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
```

---

### What's Implemented

- **Distance Calculation:** The class calculates the squared distance between the priority order and each express order.
- **Closest Orders Identification:** The method `find_closest_express_orders` identifies the two express orders closest to the priority location and returns them.

