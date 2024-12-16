# **Day 2**

### **🌍 Problem Description**

My friend VictORia and I are planning a road trip. 🚗🗽
We want to drive from Madrid to Copenhagen, and we've seen there are a lot of ways to do it.
Most probably, even if we wanted to go through Budapest, we cannot go that path. 🏦
We have a limited budget for fuel of 73€ 💶, and we want to get the shortest possible way. 📍

Can you help me solve this problem? ✨

-------------------------------------

### **🔖 Objectives**

The goal of this problem is to determine the shortest possible route 🔎 for a road trip from Madrid (city index 1) to Copenhagen (city index 100) while adhering to the following constraints:

- **⛽ Fuel Budget Constraint:** The total fuel cost of the chosen route must not exceed 73 euros.
- **❌ Avoiding Prohibited City:** The route must not pass through Budapest.
- **🛣️ Path Feasibility:** The route must start at Madrid, end at Copenhagen, and ensure a continuous path.

### **Sets and Indices**
- $C$ : Set of cities (nodes in the graph).
- $E$: Set of connections (edges in the graph) between cities $(i, j)$.

### **Parameters**
- $d_{ij}$: Distance between city $i$ and city $j$, $(i, j) \in E$.
- $f_{ij}$: Fuel cost for traveling from city $i$ to city $j$, $(i, j) \in E$.
- $B$: Maximum fuel budget in euros.
- $S$: Starting city (Madrid, city 1).
- $T$: Ending city (Copenhagen, city 100).
- $K$: Prohibited city (Budapest).

---


### **Decision Variables**
- $x_{ij} \in \{0, 1\} :$
  - $x_{ij} = 1$ : if the route from city $i$ to city $j$ is selected.
  - $x_{ij} = 0$ : otherwise.


### **Objective**
Minimize the total distance traveled:

$$\text{Minimize } \sum_{(i, j) \in E} d_{ij} \cdot x_{ij}$$
### **Constraints**
### **1. Flow Conservation (Starting Point)**  
 
At the starting point (Madrid), exactly one route must leave the city. This ensures that we begin our journey from Madrid.  

$$\sum_{j: (S, j) \in E} x_{S\ j} = 1$$
### **2. Flow Conservation (Ending Point)**  

At the ending point (Copenhagen), exactly one route must enter the city. This ensures that we end our journey at Copenhagen.

$$\sum_{i: (i, T) \in E} x_{i\ T} = 1$$
### **3. Flow Conservation (Intermediate Cities)**  

For each intermediate city (except for the starting and ending cities), the number of incoming routes must be equal to the number of outgoing routes. This ensures that we do not leave any city without entering another city and vice versa.  

$$\sum_{i: (i, k) \in E} x_{ik} = \sum_{j: (k, j) \in E} x_{kj}, \quad \forall k \in C \setminus \{1, 100\}$$
### **4. Fuel Budget Constraint**  
  
The total fuel cost of the selected route must not exceed the given fuel budget  B = 73 euros. This ensures that the chosen route remains within the budget.

$$\sum_{(i, j) \in E} f_{ij} \cdot x_{ij} \leq 73$$
### **5. Avoiding Budapest**  
The route must avoid passing through Budapest. No route can enter or leave Budapest. This ensures that the selected route does not go through the prohibited city.

$$\sum_{i: (i, K) \in E} x_{i\ K} + \sum_{j: (K, j) \in E} x_{K\ j} = 0$$
### **6. Binary Decision Variables**  

Each decision variable $x_{ij}$ must be binary, indicating whether the route from city $i$ to city $j$ is selected (1) or not (0). This ensures that the route selection is binary.  

$$x_{ij} \in \{0, 1\}, \quad \forall (i, j) \in E$$


---

# Day 2 Files

Here are the files for the problem:

- [Data: instance.txt](instance.txt)
- [Model: main.py](main.py)
- [Sensitivity Analysis: sensitivity_analysis.py](sensitivity_analysis.py)
- [Solution: solution.txt](solution.txt)

