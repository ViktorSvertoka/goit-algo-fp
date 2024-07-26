# Покрокова інструкція виконання фінального проєкту

## Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

- написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
- розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
- написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

## Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

![Screenshoot](./assets/image_1.png)

## Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

## Завдання 4. Візуалізація піраміди

Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.

```python
import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
def **init**(self, key, color="skyblue"):
self.left = None
self.right = None
self.val = key
self.color = color # Додатковий аргумент для зберігання кольору вузла
self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
if node is not None:
graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
if node.left:
graph.add_edge(node.id, node.left.id)
l = x - 1 / 2 ** layer
pos[node.left.id] = (l, y - 1)
l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
if node.right:
graph.add_edge(node.id, node.right.id)
r = x + 1 / 2 ** layer
pos[node.right.id] = (r, y - 1)
r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
return graph

def draw_tree(tree_root):
tree = nx.DiGraph()
pos = {tree_root.id: (0, 0)}
tree = add_edges(tree, tree_root, pos)

colors = [node[1]['color'] for node in tree.nodes(data=True)]
labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

plt.figure(figsize=(8, 5))
nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
plt.show()

# Створення дерева

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева

draw_tree(root)
```

![Screenshoot](./assets/image_2.png)

Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.

> [!NOTE]
>
> 👉🏻 Примітка. Суть завдання полягає у створенні дерева із купи.

## Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад `#1296F0`). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

> [!NOTE]
>
> 👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію

## Завдання 6. Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

```python
items = {
"pizza": {"cost": 50, "calories": 300},
"hamburger": {"cost": 40, "calories": 250},
"hot-dog": {"cost": 30, "calories": 200},
"pepsi": {"cost": 10, "calories": 100},
"cola": {"cost": 15, "calories": 220},
"potato": {"cost": 25, "calories": 350}
}
```

Розробіть функцію `greedy_algorithm` жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію `dynamic_programming`, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

## Завдання 7. Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

![Screenshoot](./assets/image_3.png)

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

## Підготовка та завантаження фінального проєкту

1. Створіть публічний репозиторій `goit-algo-fp`.
2. Виконайте завдання та відправте його у свій репозиторій.
3. Завантажте робочі файли на свій комп’ютер та прикріпіть їх у `LMS` у форматі `zip`. Назва архіву повинна бути у форматі `ФП_ПІБ`.
4. Прикріпіть посилання на репозиторій `goit-algo-fp` та відправте на перевірку.

## Формат здачі

Прикріплені файли репозиторію у форматі `zip` з назвою `ФП_ПІБ`.
Посилання на репозиторій.

## Критерії прийняття фiнального проєкту

### Завдання 1:

- Реалізовано функцію реверсування однозв'язного списку, яка змінює посилання між вузлами. Код виконується.

- Програмно реалізовано алгоритм сортування (функцію) для однозв'язного списку. Код виконується.

- Реалізовано функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список. Код виконується.

### Завдання 2:

- Код виконується. Програма візуалізує фрактал “дерево Піфагора”.

- Користувач має можливість вказати рівень рекурсії.

### Завдання 3:

- Програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху у графі з використанням бінарної купи (піраміди).

- У межах реалізації завдання створено граф, використано піраміду для оптимізації вибору вершин та виконано обчислення найкоротших шляхів від початкової вершини до всіх інших.

### Завдання 4:

- Код виконується. Функція візуалізує бінарну купу.

### Завдання 5:

- Програмно реалізовано алгоритми DFS і BFS для візуалізації обходу дерева в глибину та в ширину. Використано стек та чергу.

- Кольори вузлів змінюються від темних до світлих відтінків залежно від порядку обходу.

### Завдання 6:

- Програмно реалізовано функцію, яка використовує принцип жадібного алгоритму. Код виконується і повертає назви страв, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

- Програмно реалізовано функцію, яка використовує принцип динамічного

програмування. Код виконується і повертає оптимальний набір страв для максимізації калорійності при заданому бюджеті.

### Завдання 7:

- Програмно реалізовано алгоритм для моделювання кидання двох ігрових кубиків і побудови таблиці сум та їх імовірностей за допомогою методу Монте-Карло.

- Код виконується та імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, підраховує, скільки разів кожна можлива сума з’являється у процесі симуляції, і визначає ймовірність кожної можливої суми.

- Створено таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

- Зроблено висновки щодо правильності розрахунків шляхом порівняння отриманих за допомогою методу Монте-Карло результатів та результатів аналітичних розрахунків. Висновки оформлено у вигляді файлу 'readme.md' фінального завдання.

### Формат оцінювання:

- Оцінка від 0 до 100.
- Завдання 1 оцінюється в 15 балів.
- Завдання 2 оцінюється в 15 балів.
- Завдання 3 оцінюється в 10 балів.
- Завдання 4 оцінюється в 15 балів.
- Завдання 5 оцінюється в 15 балів.
- Завдання 6 оцінюється в 15 балів.
- Завдання 7 оцінюється в 15 балів.

---

## Завдання 1 - висновки:

1. **Реверсування списку:**

   - Функція `reverse_linked_list` змінює посилання між вузлами списку таким чином, що останній вузол стає першим, передостанній — другим і так далі.
   - Реалізація функції реверсування є правильною, посилання між вузлами змінюються коректно.

2. **Сортування вставками:**

   - Алгоритм сортування вставками поступово бере елементи з початкового списку і вставляє їх у правильному порядку в новий відсортований список.
   - Алгоритм сортування вставками працює коректно для однозв'язних списків, впорядковуючи елементи у зростаючому порядку.

3. **Об'єднання двох відсортованих списків:**

   - Функція `merge_sorted_lists` об'єднує два відсортовані списки, створюючи новий відсортований список шляхом порівняння та злиття елементів обох списків.
   - Функція злиття двох відсортованих списків коректно об'єднує їх в один відсортований список.

## Завдання 2 - висновки:

1. **Правильність реалізації:**

   - Програма коректно реалізує рекурсивний алгоритм для малювання `дерева Піфагора`.
   - Використання `math.cos(math.radians(angle))` для скорочення довжини гілок забезпечує стабільне скорочення і запобігає накопиченню помилок.

2. **Гнучкість:**

   - Користувач має можливість вказати рівень рекурсії, що дозволяє контролювати деталізацію та складність фрактала.

3. **Візуалізація:**

   - Програма успішно візуалізує фрактал `"дерево Піфагора"` з будь-яким рівнем рекурсії, забезпечуючи наочність та чіткість малюнка.

## Завдання 3 - висновки:

1. **Правильність реалізації:**

   - Алгоритм Дейкстри коректно реалізований з використанням бінарної купи `(heapq)`.
   - Відстані обчислюються правильно, і алгоритм ефективно знаходить найкоротші шляхи у зваженому графі.

2. **Гнучкість:**

   - Граф можна легко змінити, додавши або видаливши вершини і ребра.

3. **Ефективність:**

   - Використання бінарної купи оптимізує вибір вершин, зменшуючи час виконання алгоритму порівняно з наївною реалізацією.

## Завдання 4 - висновки:

1. **Візуалізація бінарної купи**:

   - Функція для візуалізації бінарної купи успішно реалізована.
   - Відображення дерева показує коректну структуру бінарної купи.

2. **Коректність виконання програми**:
   - Програма правильно відображає вузли та їхні зв'язки, використовуючи бібліотеку `networkx`.
   - Всі тестові приклади демонструють правильність роботи функції візуалізації.

## Завдання 5 - висновки:

1. **Алгоритми DFS та BFS:**

   - Реалізовані алгоритми обходу в глибину `(DFS)` та в ширину `(BFS)` коректно працюють, використовуючи стек та чергу відповідно.

2. **Кольорове відображення порядку обходу:**

   - Вузли дерева забарвлюються у відтінки від темних до світлих, залежно від порядку обходу, що робить процес обходу більш наочним.

3. **Візуалізація процесу обходу:**

   - Кожен крок обходу дерева відображається на графіку, що дозволяє відстежувати послідовність відвідування вузлів та забезпечує наочність алгоритмів.

## Завдання 6 - висновки:

1. **Жадібний алгоритм:**

   - Функція `greedy_algorithm()` вибирає страви з максимальним співвідношенням калорій до вартості в межах бюджету.
   - Обчислює співвідношення калорій до вартості для кожної страви.
   - Сортує страви за цим співвідношенням і вибирає страви, поки дозволяє бюджет.
   - Жадібний алгоритм ефективно вибирає страви для максимізації співвідношення калорій до вартості.

2. **Динамічне програмування:**

   - Функція `dynamic_programming()` обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
   - Створює таблицю для зберігання максимальної калорійності для кожного можливого бюджету.
   - Для кожної страви оновлює таблицю на основі поточного бюджету.
   - Визначає оптимальний набір страв для максимізації калорійності при заданому бюджеті.
   - Динамічне програмування дає оптимальне рішення для максимізації калорійності при заданому бюджеті.

## Завдання 7 - висновки:

### Порівняння ймовірностей кидання двох кубиків

У цій таблиці представлені ймовірності для кожної суми, отримані за допомогою методу Монте-Карло, а також аналітичні розрахунки ймовірностей. Вказано також відхилення між обчисленими ймовірностями.

| Сума | Ймовірність (Метод Монте-Карло) | Ймовірність (Аналітична) | Відхилення (%) |
| ---- | ------------------------------- | ------------------------ | -------------- |
| 2    | 2.81%                           | 2.78%                    | +0.03%         |
| 3    | 5.62%                           | 5.56%                    | +0.06%         |
| 4    | 8.38%                           | 8.33%                    | +0.05%         |
| 5    | 11.14%                          | 11.11%                   | +0.03%         |
| 6    | 13.85%                          | 13.89%                   | -0.04%         |
| 7    | 16.73%                          | 16.67%                   | +0.06%         |
| 8    | 13.85%                          | 13.89%                   | -0.04%         |
| 9    | 10.93%                          | 11.11%                   | -0.18%         |
| 10   | 8.42%                           | 8.33%                    | +0.09%         |
| 11   | 5.52%                           | 5.56%                    | -0.04%         |
| 12   | 2.76%                           | 2.78%                    | -0.02%         |

### Аналіз Результатів

1. **Точність Монте-Карло**:

   - Відхилення між ймовірностями, отриманими за допомогою методу Монте-Карло, та аналітичними розрахунками є незначним. Відхилення варіюється від -0.18% до +0.18%, що свідчить про точність методу Монте-Карло при великій кількості симуляцій.

2. **Відповідність**:

   - Результати методу Монте-Карло в основному відповідають аналітичним розрахункам, з незначними відхиленнями. Це підтверджує правильність симуляцій і те, що використані симуляції були достатньо великі, щоб наблизитися до аналітичних результатів.

3. **Природа Відхилень**:
   - Незначні відхилення можуть бути зумовлені випадковим характером симуляцій, і вони є нормальною частиною використання методу Монте-Карло. Більше симуляцій могли б зменшити ці відхилення, проте з практичної точки зору результати вже досить близькі до аналітичних значень.

### Висновок

Отримані результати за допомогою методу Монте-Карло дуже близькі до аналітичних значень, що підтверджує ефективність і точність симуляцій при достатньо великій кількості ітерацій. Це демонструє, що метод Монте-Карло може бути надійним інструментом для оцінки ймовірностей у випадкових процесах, таких як кидання кубиків.
