import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import random

random.seed(42)

# Визначення функції та межі інтегрування
def f(x):
    return (x + 1)*(x - 1)*(x - 2) + 1.5

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = (x + 1)*(x - 1)*(x - 2) + 1.5 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

x2 = lambda x: (x + 1)*(x - 1)*(x - 2) + 1.5
Si, _ = integrate.quad(x2, 0, 2)

# Розміри прямокутника
a = 2  # ширина прямокутника
b = 4  # висота прямокутника

def is_inside(x, y):
    """Перевіряє, чи знаходиться точка (x, y) під кривою функції."""
    return y <= f(x)

# Генерація випадкових точок
points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]

# Відбір точок, що знаходяться під кривою
inside_points = [point for point in points if is_inside(point[0], point[1])]

# Кількість усіх точок та точок під кривою
N = len(points)
M = len(inside_points)

Sm = (M / N) * (a * b)  # Площа за методом Монте-Карло

# Виведення результатів
print(f"Кількість точок під кривою: {M}, загальна кількість точок: {N}")
print(f"Площа, обчислена за допомогою бібліотеки SciPy: {Si}, площа за методом Монте-Карло: {Sm}")