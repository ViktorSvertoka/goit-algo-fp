# Реалізація однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Функція реверсування однозв'язного списку
def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


# Алгоритм сортування однозв'язного списку (сортування вставками)
def sorted_insert(sorted_list, new_node):
    if not sorted_list.head or sorted_list.head.data >= new_node.data:
        new_node.next = sorted_list.head
        sorted_list.head = new_node
    else:
        current = sorted_list.head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node


def insertion_sort(linked_list):
    sorted_list = LinkedList()
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = None
        sorted_insert(sorted_list, current)
        current = next_node
    linked_list.head = sorted_list.head


# Функція, що об'єднує два відсортовані однозв'язні списки
def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1:
        tail.next = current1
    if current2:
        tail.next = current2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


# Створення першого списку
list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(4)
list1.append(2)

print("Перший список:")
list1.print_list()

# Реверсування першого списку
reverse_linked_list(list1)
print("Реверсований перший список:")
list1.print_list()

# Сортування першого списку
insertion_sort(list1)
print("Відсортований перший список:")
list1.print_list()

# Створення другого списку
list2 = LinkedList()
list2.append(7)
list2.append(5)
list2.append(6)

print("Другий список:")
list2.print_list()

# Сортування другого списку
insertion_sort(list2)
print("Відсортований другий список:")
list2.print_list()

# Об'єднання двох відсортованих списків
merged_list = merge_sorted_lists(list1, list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
