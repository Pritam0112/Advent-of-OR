## Now it's time to deliver! 🚚


Remember all the orders we received yesterday at the warehouse?

Well... We need to deliver them.

The main problem is that we made a sub-contract for that and there's only one vehicle available... For 443 places to go! 😱

We’ve noticed that going from location A to location B might be different from going from B to A 🔄🚦.

So we need to figure out the best possible path to minimize ⏱️ delivery times.

Can you help me solve this problem? 🧩

Here you can find an instance of this problem.


## **Traveling Salesman Problem**

The mathematical model for the Traveling Salesman Problem (TSP) can be expressed as follows:

#### **1. Problem Statement**
The goal is to find the shortest route to visit all cities exactly once and return to the starting city.



#### **2. Sets and Indices**
- $N = \{1, 2, \dots, n\}$: Set of cities (nodes).
- $i, j \in N$: Indices for cities.


#### **3. Parameters**
- $c_{ij}$: Cost or distance of traveling from city $i$ to city $j$.



#### **4. Decision Variables**
- $x_{ij}$: Binary variable indicating whether the route travels directly from city $i$ to city $j$:
- 
          : 1, if the route includes traveling from i to j.
          : 0, otherwise.



#### **5. Objective Function**
Minimize the total travel cost:

$\text{Minimize } Z = \sum_{i \in N} \sum_{j \in N, j \neq i} c_{ij} x_{ij}.$



#### **6. Constraints**
1. **Each city must be visited exactly once:**
   - Outgoing route constraint:

      $$\sum_{j \in N, j \neq i} x_{ij} = 1, \quad \forall i \in N.$$
   - Incoming route constraint:
    
      $$\sum_{i \in N, i \neq j} x_{ij} = 1, \quad \forall j \in N.$$

2. **Subtour elimination (Lazy Constraints):**
   - Subtours are dynamically eliminated using lazy constraints:

     $$\sum_{i \in S} \sum_{j \in S, i \neq j} x_{ij} \leq |S| - 1, \quad \forall S \subset N, 2 \leq |S| < n.$$
     - Here, $S$ is a subset of cities forming a subtour.
     - This constraint ensures that no subset of cities $S$ forms a disconnected cycle.

3. **Binary decision variables:**
   $x_{ij} \in \{0, 1\}, \quad \forall i, j \in N.$



**Other subtour elimination constraint**

Miller-Tucker-Zemlin formulation:

$u_i - u_j + n x_{ij} \leq n - 1, \quad \forall i, j \in N, i \neq j.$
   - $u_i$ : Continuous variable used to eliminate subtours, representing the relative position of city 𝑖 in the tour.
   - it ensures that cities are ordered in a single connected tour, avoiding subtours.
---
Day 12 Optimal solution:

| Case | Approach | Total Travel Cost | Time Taken |
| ---- | -------- | ----------------- | ---------- |
| 1    | Gurobi (lazy constraint) | 2720.0 | 11.56 seconds |
| 2    | Google OR Tools | 2763 | 13.83 seconds |
| 3    | Hybrid (Google OR Tools and Gurobi) | 2720.0 | 17.55 seconds (including 2.70 seconds for Gurobi) |


