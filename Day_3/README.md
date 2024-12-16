# **DAy 3**

## **Task Assignment Problem** 📋💼

Hey, ORville here 👋

I'm a logistics manager overseeing the allocation of tasks to employees in our company, **FurnitORe**. We have 100 tasks and 100 employees. However, the cost of assigning each task to an employee varies, and we need to minimize the total cost 💸.[post](https://www.linkedin.com/posts/borjamenendezmoreno_operationsresearch-activity-7269618917482909696-qJ_2?utm_source=share&utm_medium=member_desktop)

## Problem Description 🧑‍💼
In this problem, we aim to assign **n tasks** to **n employees** such that:
1. Each task is assigned to exactly one employee. 🎯
2. Each employee is assigned to exactly one task. 👥
3. The total cost of the assignment is minimized. 💰

### Mathematical Formulation 📊

#### Sets and Parameters 📝
1. **Sets:**
   - $T$: Set of tasks, $T = \{1, 2, \dots, n\}$.
   - $E$: Set of employees, $E = \{1, 2, \dots, n\}$.

2. **Parameters:**
   - $c_{ij}$: The cost of assigning task $i$ to employee $j$, where $i \in T$, $j \in E$.

#### Decision Variables ⚙️
- $x_{ij}$: A binary decision variable, where 1, if task $i$ is assigned to employee $j$. 0, otherwise.

#### Objective Function 🎯
The goal is to minimize the total cost of assignment:

$$\text{Minimize } Z = \sum_{i \in T} \sum_{j \in E} c_{ij} \cdot x_{ij}.$$

#### Constraints 📏
1. **Each task must be assigned to exactly one employee:**
   
$$\sum_{j \in E} x_{ij} = 1, \quad \forall i \in T.$$

2. **Each employee must be assigned to exactly one task:**
   
$$\sum_{i \in T} x_{ij} = 1, \quad \forall j \in E.$$

3. **Binary nature of decision variables:**
   
$$x_{ij} \in \{0, 1\}, \quad \forall i \in T, \forall j \in E.$$

## Solution 💻

[Solution: Solution.txt](Solution.txt)


