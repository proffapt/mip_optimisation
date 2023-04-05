import gurobipy as gp
import pandas as pd

# read data from Excel sheets
food_data = pd.read_excel('data.xlsx', sheet_name='Sheet1')
male_data = pd.read_excel('data.xlsx', sheet_name='Sheet2')
female_data = pd.read_excel('data.xlsx', sheet_name='Sheet3')

# get input from user
age = int(input('Enter your age: '))
gender = input('Enter your gender (M/F): ')
budget_up = float(input("Enter your budget's upper limit: "))
budget_low = float(input("Enter your budget's lower limit: "))

if budget_low > budget_up:
    print("Please go and take kindergarten Mathematics course again :)")
    exit(1)

# create optimization model
model = gp.Model('Nutrition Optimization')

# Deciding the type of variable, INTEGER or NON-INTEGER
types = []
for i in range(len(food_data)):
    if food_data.iloc[i, 7] == 'Y':
        types.append(gp.GRB.INTEGER)
    else:
        types.append(gp.GRB.CONTINUOUS)

# define decision x for each food item
foods = list(food_data['Food'])
x = model.addVars(foods, lb=0, ub=gp.GRB.INFINITY, vtype=types, name='servings')

# define the budget constraints
costs = dict(zip(foods, food_data['Cost']))
model.addConstr(gp.quicksum(costs[i] * x[i] for i in foods) <= budget_up)
model.addConstr(gp.quicksum(costs[i] * x[i] for i in foods) >= budget_low)

# find correct row from male_data or female_data based on age and gender
if gender == 'M':
    age_group_data = male_data[(male_data['Age Lower'] <= age) & (male_data['Age Upper'] >= age)]
elif gender == 'F':
    age_group_data = female_data[(female_data['Age Lower'] <= age) & (female_data['Age Upper'] >= age)]
else:
    print(f"Please use either M or F as input for gender ¯\\_(ツ)_/¯")
    exit(1)

# add constraints for nutrient intake
nutrients = ['Protein', 'Calories', 'Carbohydrates', 'Fat', 'Fiber']
for nutr in nutrients:
    lb = age_group_data[nutr + ' Lower'].values[0]
    ub = age_group_data[nutr + ' Upper'].values[0]
    amounts = dict(zip(foods, food_data[nutr]))
    model.addConstr(gp.quicksum(amounts[i] * x[i] for i in foods) >= lb)
    model.addConstr(gp.quicksum(amounts[i] * x[i] for i in foods) <= ub)

# Saving the model
model.write("model.lp")
# Silencing the gigantic output
model.setParam("OutputFlag", False)

# add solution pool
model.params.PoolSearchMode = 2 # exhaustively search for good solutions
model.params.PoolGap = 0.1 # set optimality gap tolerance to 50%
model.params.PoolSolutions = 10 # set maximum number of solutions to store in pool to 10
model.params.MIPFocus = 2 # emphasize it to find good feasible solutions

# solve optimization model
model.optimize()

# print optimal solution and other good solutions (if any)
if model.status == gp.GRB.OPTIMAL:
    # print solutions from the solution pool
    for j in range(model.SolCount):
        if j == 0:
            print('\nOptimal Solution')
        else:
            print(f'\nOther Solution #{j+1}')

        model.params.SolutionNumber = j
        total_cost = 0
        for i in foods:
            if x[i].Xn > 0.1:
                print(f'{i}: {x[i].Xn:.2f} servings')
                total_cost += x[i].Xn*costs[i]
        print(f'Total Cost: ${total_cost:.2f}\n')

else:
    print('No feasible solution found.')
