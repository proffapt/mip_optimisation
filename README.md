# MIP Optimisation

This is the code repository for the final project submitted for OR LAB, Industrial & Systems Engineering, IIT KGP.<br>
Here we have presented a POC method to optimise the menu of our mess using the Mixed Integer Programming model.<br>
It also gives multiple solutions based on the deviation specified from the Optimal Solution.<br>
Following example of Input and it's corresponding Output demonstrates what it is supposed to do.

#### Input
|parameter|value|
|---|---|
|age|25|
|gender|M|
|budget_up|250|
|budget_low|100|

The final model for this example is store in `demo_model.lp`.

#### Output
```graphql
>> Using python 3
Enter your age: 25
Enter your gender (M/F): M
Enter your budget's upper limit: 250
Enter your budget's lower limit: 100
Set parameter Username
Academic license - for non-commercial use only - expires 2023-12-31

Optimal Solution
Food_Item_12: 2.10 servings
Food_Item_29: 0.73 servings
Food_Item_46: 7.90 servings
Food_Item_53: 3.00 servings
Food_Item_60: 0.36 servings
Food_Item_87: 4.00 servings
Food_Item_95: 0.82 servings
Total Cost: $228.16


Other Solution #2
Food_Item_36: 4.91 servings
Food_Item_39: 0.53 servings
Food_Item_46: 19.61 servings
Food_Item_59: 3.06 servings
Food_Item_68: 0.31 servings
Total Cost: $250.00


Other Solution #3
Food_Item_8: 1.00 servings
Food_Item_36: 5.44 servings
Food_Item_46: 21.20 servings
Food_Item_59: 2.48 servings
Total Cost: $238.36


Other Solution #4
Food_Item_36: 2.05 servings
Food_Item_39: 3.52 servings
Food_Item_46: 5.74 servings
Food_Item_59: 2.01 servings
Food_Item_69: 1.00 servings
Total Cost: $246.03


Other Solution #5
Food_Item_8: 1.00 servings
Food_Item_14: 1.00 servings
Food_Item_36: 5.53 servings
Food_Item_46: 14.81 servings
Food_Item_59: 1.94 servings
Total Cost: $198.68


Other Solution #6
Food_Item_36: 5.44 servings
Food_Item_46: 21.03 servings
Food_Item_59: 3.04 servings
Food_Item_68: 0.12 servings
Food_Item_82: 1.00 servings
Total Cost: $249.92


Other Solution #7
Food_Item_4: 1.00 servings
Food_Item_8: 1.00 servings
Food_Item_14: 1.00 servings
Food_Item_36: 4.39 servings
Food_Item_46: 10.26 servings
Food_Item_59: 1.41 servings
Total Cost: $155.14


Other Solution #8
Food_Item_11: 4.00 servings
Food_Item_12: 0.44 servings
Food_Item_14: 1.00 servings
Food_Item_39: 2.88 servings
Food_Item_46: 3.50 servings
Food_Item_59: 0.20 servings
Food_Item_69: 1.00 servings
Food_Item_73: 0.16 servings
Total Cost: $250.00


Other Solution #9
Food_Item_8: 1.00 servings
Food_Item_36: 5.55 servings
Food_Item_46: 14.00 servings
Food_Item_57: 1.00 servings
Food_Item_59: 2.21 servings
Total Cost: $186.10


Other Solution #10
Food_Item_11: 5.00 servings
Food_Item_12: 0.34 servings
Food_Item_14: 1.00 servings
Food_Item_27: 0.14 servings
Food_Item_39: 2.60 servings
Food_Item_46: 4.34 servings
Food_Item_59: 0.44 servings
Food_Item_69: 1.00 servings
Total Cost: $250.00
```
