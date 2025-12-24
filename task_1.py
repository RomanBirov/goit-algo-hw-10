import pulp

#  Створення моделі (максимізація)
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішення (кількість продуктів)
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція — максимізувати загальну кількість продукції
model += lemonade + fruit_juice, "Total_Production"

# Обмеження ресурсів
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit"
model += 1 * lemonade <= 50, "Sugar_Limit"
model += 1 * lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

# Розв'язання задачі
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Вивід результатів
print("Статус:", pulp.LpStatus[model.status])
print("Кількість лимонаду:", int(lemonade.varValue))
print("Кількість фруктового соку:", int(fruit_juice.varValue))
print("Загальна кількість продукції:", int(pulp.value(model.objective)))
