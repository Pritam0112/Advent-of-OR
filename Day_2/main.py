import pandas as pd
from gurobipy import Model, GRB


def read_problem_instance(problem_instance_fn):
    """
    Reads a problem instance file for cities, connections, and fuel costs.

    Args:
        problem_instance_fn (str): The file path to the problem instance file.

    Returns:
        tuple: A tuple containing:
            - num_cities (int): Number of cities.
            - num_connections (int): Number of connections.
            - max_budget (int): Maximum fuel budget.
            - connections_df (DataFrame): A DataFrame with columns: First City, Second City, Distance, Fuel Cost.
    """
    with open(problem_instance_fn, "r") as f:
        first_line = True
        connections = []

        for line in f:
            # Skip empty lines or comments
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # Process the first line
            if first_line:
                num_cities, num_connections, max_budget = map(int, line.split())
                first_line = False
            else:
                # Parse connection data
                city1, city2, distance, fuel_cost = map(int, line.split())
                connections.append((city1, city2, distance, fuel_cost))

    # Create a DataFrame from the connections
    connections_df = pd.DataFrame(connections, columns=["First City", "Second City", "Distance", "Fuel Cost"])

    # Debugging output
    print(f"Number of cities: {num_cities}")
    print(f"Number of connections: {num_connections}")
    print(f"Max fuel budget: {max_budget} euros")
    print("Sample data:")
    print(connections_df.head())
    print('-'*100)

    return num_cities, num_connections, max_budget, connections_df


def build_model(start_city, end_city, prohibited_city, fuel_budget, connections_df):
    """
    Build the optimization model for the road trip problem.

    Args:
        start_city (int): The starting city index.
        end_city (int): The ending city index.
        prohibited_city (int): The prohibited city index (e.g., Budapest).
        fuel_budget (int): The fuel budget.
        connections_df (DataFrame): DataFrame containing the connections between cities.

    Returns:
        Model: The Gurobi model.
    """
    # Create the optimization model
    model = Model("RoadTrip")

    # Add variables
    edges = list(zip(connections_df["First City"], connections_df["Second City"]))
    distance = {(row["First City"], row["Second City"]): row["Distance"] for _, row in connections_df.iterrows()}
    fuel_cost = {(row["First City"], row["Second City"]): row["Fuel Cost"] for _, row in connections_df.iterrows()}

    # Decision variables (binary)
    x = model.addVars(edges, vtype=GRB.BINARY, name="x")

    # Objective Function: Minimize the total distance
    model.setObjective(x.prod(distance), GRB.MINIMIZE)

    # Constraints
    # At the starting point, exactly one route must leave the city.
    model.addConstr(sum(
        x[start_city, j] for j in connections_df.loc[connections_df["First City"] == start_city, "Second City"]) == 1,
                    "Start")

    # At the ending point, exactly one route must enter the city.
    model.addConstr(
        sum(x[i, end_city] for i in connections_df.loc[connections_df["Second City"] == end_city, "First City"]) == 1,
        "End")

    # Flow conservation for intermediate cities
    intermediate_cities = set(connections_df["First City"]).union(set(connections_df["Second City"]))
    intermediate_cities -= {start_city, end_city}
    for k in intermediate_cities:
        model.addConstr(
            sum(x[i, k] for i in connections_df.loc[connections_df["Second City"] == k, "First City"]) ==
            sum(x[k, j] for j in connections_df.loc[connections_df["First City"] == k, "Second City"]),
            f"Flow_{k}"
        )

    # Prohibit travel through the prohibited city (e.g., Budapest)
    if prohibited_city is not None:
        model.addConstr(
            sum(x[i, prohibited_city] for i in
                connections_df.loc[connections_df["Second City"] == prohibited_city, "First City"]) +
            sum(x[prohibited_city, j] for j in
                connections_df.loc[connections_df["First City"] == prohibited_city, "Second City"]) == 0,
            "Prohibit_City"
        )

    # Fuel budget constraint
    model.addConstr(x.prod(fuel_cost) <= fuel_budget, "FuelBudget")

    return model, edges, x


def solve_model(model, edges, x, connections_df):
    """
    Solves the model and prints the optimal route, its total distance, and fuel costs.

    Args:
        model (Model): The Gurobi model.
        edges (list): List of edges.
        x (dict): Gurobi decision variables.
        connections_df: Dataframe
    """
    # Optimize the model
    model.optimize()

    print('-'*100)
    # Display the solution if optimal
    if model.status == GRB.OPTIMAL:
        route = [1]  # Start from the starting city (Madrid)
        current_city = 1
        total_distance = 0
        total_cost = 0

        # Trace the route by following the decision variables
        while True:
            next_city = next((j for i, j in edges if i == current_city and x[i, j].x > 0.5), None)
            if not next_city: break
            route.append(next_city)

            # Get the distance and fuel cost directly from the DataFrame
            leg_info = connections_df[(connections_df["First City"] == current_city) &
                                      (connections_df["Second City"] == next_city)]
            if leg_info.empty:
                leg_info = connections_df[(connections_df["First City"] == next_city) &
                                          (connections_df["Second City"] == current_city)]

            # Assuming leg_info has only one row
            distance = leg_info["Distance"].values[0]
            cost = leg_info["Fuel Cost"].values[0]

            total_distance += distance  # Add distance of this leg
            total_cost += cost  # Add fuel cost of this leg
            current_city = next_city

        # Print the route in the format 1 -> 72 -> 53 -> 100
        print('The optimal Route: ')
        print(" -> ".join(map(str, route)))
        print(f"Total distance: {total_distance} km")
        print(f"Total fuel cost: {total_cost} euros")
    else:
        print("No feasible solution found.")

def __main__():

    # read data
    problem_instance_fn = "instance.txt"
    num_cities, num_connections, max_budget, connections_df = read_problem_instance(problem_instance_fn)

    start_city = 1  # Madrid
    end_city = 100  # Copenhagen
    prohibited_city = None
    fuel_budget = max_budget

    model, edges, x = build_model(start_city, end_city, prohibited_city, fuel_budget, connections_df)
    solve_model(model, edges, x, connections_df)

if __name__ == "__main__":
    __main__()