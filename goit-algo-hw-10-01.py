import pulp

# Ініціалізація моделі
model = pulp.LpProblem("MaximizeOutput", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту Лимонад
B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # Кількість продукту Фруктовий сік

# Функція цілі (Максимізація прибутку)
model += A + B, "Profit"

# Додавання обмежень
model += 2 * A + 1 * B <= 100  # Обмеження для Води
model += A <= 50  # Обмеження для Цукру
model += A <= 30  # Обмеження для Лимонного соку
model += 2 * B <= 40  # Обмеження для Фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти Лимонаду:", A.varValue)
print("Виробляти Фруктового соку:", B.varValue)
