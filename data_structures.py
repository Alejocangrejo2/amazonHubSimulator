from collections import deque


# --------- QUEUE (Orders) ---------
class OrderQueue:
    def __init__(self):
        self.queue = deque()

    def add_order(self, order):
        self.queue.append(order)

    def process_order(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0


# --------- STACK (Truck - LIFO) ---------
class Truck:
    def __init__(self):
        self.stack = []

    def load_package(self, package):
        self.stack.append(package)

    def unload_package(self):
        if self.stack:
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


# --------- ARRAY -------------------
class Inventory:
    def __init__(self, rows=3, columns=3):
        self.shelves = [[None for _ in range(columns)] for _ in range(rows)]

    def store_product(self, row, column, product):
        if self.shelves[row][column] is None:
            self.shelves[row][column] = product
            return True
        return False

    def find_product(self, product_name):
        for i in range(len(self.shelves)):
            for j in range(len(self.shelves[i])):
                if self.shelves[i][j] == product_name:
                    return (i, j)
        return None

    def display_inventory(self):
        for row in self.shelves:
            print(row)