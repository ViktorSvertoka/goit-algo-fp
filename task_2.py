import turtle
import math


# Функція для малювання гілки
def draw_tree(branch_length, angle, level):
    if level > 0:
        # Малюємо основну гілку
        turtle.forward(branch_length)

        # Малюємо праву гілку
        turtle.right(angle)
        draw_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

        # Повертаємося до основної гілки
        turtle.left(2 * angle)
        draw_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

        # Повертаємося до вихідного положення
        turtle.right(angle)
        turtle.backward(branch_length)


# Основна функція
def main():
    # Запитуємо у користувача рівень рекурсії
    level = int(input("Введіть рівень рекурсії: "))

    # Налаштовуємо екран turtle
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Налаштовуємо черепашку
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -screen.window_height() // 2)
    turtle.pendown()
    turtle.speed(0)

    # Малюємо дерево
    draw_tree(100, 30, level)

    # Завершуємо малювання
    turtle.done()


# Виконання основної функції
if __name__ == "__main__":
    main()
