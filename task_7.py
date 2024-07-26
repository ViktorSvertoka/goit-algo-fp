import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Словник для підрахунку кількостей кожної можливої суми
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1

    # Обчислення ймовірностей
    probabilities = {key: value / num_rolls for key, value in sum_counts.items()}
    return probabilities


def plot_probabilities(probabilities):
    # Графік ймовірностей
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, color="skyblue")
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.xticks(sums)
    plt.grid(axis="y")
    plt.show()


def main():
    num_rolls = 100000  # Кількість імітацій
    probabilities = simulate_dice_rolls(num_rolls)
    print("Ймовірності кожної суми:", probabilities)
    plot_probabilities(probabilities)


if __name__ == "__main__":
    main()
