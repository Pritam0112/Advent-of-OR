# **Day 5**  
## 🚛 **Best Locations** 📍  

Hi, **FlORence ici** 👋  

I'm a manager of **AmazOR** that wants to find the best possible locations for our warehouses while deciding how to allocate our client demands to these warehouses.  

Our warehouses can only handle a limited amount of demand, but we need to ensure that **all client demands are met**.  

While opening a new facility, we have some **fixed costs**, and we also take into account the **cost of allocating the demand** of each client to each warehouse.  

Of course, we want to **minimize our costs** here...  

Can you help me solve this problem? 🔍  

---

## 🧮 **The Warehouse Optimization Problem**  

### **📌 Sets and Indices**  
- $i \in I$: **Set of clients**. 👥  
- \$j \in J$: **Set of warehouses**. 🏭  

---

### **📊 Parameters**  
- $F_j$: **Fixed cost** for opening warehouse $j$. 💰  
- $Q_j$: **Capacity** of warehouse $j$. 📦  
- $d_i$: **Demand** of client $i$. 🎯  
- $c_{ij}$: **Transportation cost** for satisfying the demand of client $i$ from warehouse $j$. 🚚  

---

### **📈 Decision Variables**  
- $x_j$: Binary variable indicating whether warehouse $j$ is open or not. 🏢  
- $y_{ij}$: Continuous variable representing the quantity allocated from warehouse $j$ to client $i$. 📊  

---

### 🎯 **Objective Function**  
Minimize the **total cost**, which includes:  
1. **Fixed costs** of opening warehouses.  
2. **Transportation costs** to satisfy client demands.  

$$
\text{Minimize } Z = \sum_{j \in J} F_j x_j + \sum_{i \in I} \sum_{j \in J} c_{ij} y_{ij}
$$  

---

### ⚖️ **Constraints**  

1. **✅ Client Demand Satisfaction**  
The total demand of each client \( i \) must be fully satisfied by the open warehouses:  

$$
\sum_{j \in J} y_{ij} = d_i \quad \forall i \in I
$$  

2. **📦 Warehouse Capacity**  
The total allocation to a warehouse \( j \) cannot exceed its capacity if the warehouse is open:  

$$
\sum_{i \in I} y_{ij} \leq Q_j x_j \quad \forall j \in J
$$  

3. **🚫 No Allocation to Closed Warehouses**  
Allocation \( y_{ij} \) can only happen if warehouse \( j \) is open:  

$$
y_{ij} \leq Q_j x_j \quad \forall i \in I, j \in J
$$  

4. **🔢 Binary Condition for Warehouses**  

$$
x_j \in \{0, 1\} \quad \forall j \in J
$$  

---

[📁 Solution: Solution.txt](Solution.txt)  
