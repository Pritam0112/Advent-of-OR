import pandas as pd
from main import read_problem_instance, build_model, solve_model  # Import functions from main.py


def perform_sensitivity_analysis():
    # Define the problem instance file path
    problem_instance_fn = "instance.txt"

    # Read problem data from the file
    num_cities, num_connections, max_budget, connections_df = read_problem_instance(problem_instance_fn)

    start_city = 1  # Madrid
    end_city = 100  # Copenhagen

    # Example: List of prohibited cities for analysis
    prohibited_cities = [None, 2, 37, 41]  # Can include multiple cities to test

    for prohibited_city in prohibited_cities:
        print(f"Running model with prohibited city: {prohibited_city}")

        # Build the model with the current prohibited city
        model, edges, x = build_model(start_city, end_city, prohibited_city, max_budget, connections_df)

        # Solve the model
        solve_model(model, edges, x, connections_df)
        print('*'*100)

if __name__ == "__main__":
    perform_sensitivity_analysis()
