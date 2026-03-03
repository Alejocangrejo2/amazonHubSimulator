from data_structures import OrderQueue, Truck, Inventory
from models import Order


class LogisticsSimulator:

    def __init__(self):
        self.order_queue = OrderQueue()
        self.truck = Truck()
        self.inventory = Inventory()

        # Posiciones geográficas (norte → sur)
        self.city_positions = {
            "Medellín": 0,
            "Cali": 1,
            "Pasto": 2
        }

        # Electronic products stored in warehouse (3x3 array)
        self.inventory.store_product(0, 0, "Laptop")
        self.inventory.store_product(0, 1, "Tablet")
        self.inventory.store_product(0, 2, "Celular")

        self.inventory.store_product(1, 0, "Monitor")
        self.inventory.store_product(1, 1, "Teclado")
        self.inventory.store_product(1, 2, "Mouse")

        self.inventory.store_product(2, 0, "Impresora")
        self.inventory.store_product(2, 1, "Router")
        self.inventory.store_product(2, 2, "Audífonos")

    # ===============================
    # ORDER MANAGEMENT
    # ===============================

    def receive_order(self, customer_name, product_name, city):
        order = Order(customer_name, product_name, city)
        self.order_queue.add_order(order)
        return f"Pedido recibido: {order}"

    # ===============================
    # PROCESS + LOAD TO TRUCK
    # ===============================

    def process_orders(self):
        temp_orders = []
        messages = []

        while not self.order_queue.is_empty():
            order = self.order_queue.process_order()
            position = self.inventory.find_product(order.product_name)

            if position:
                temp_orders.append(order)
            else:
                messages.append(f"Producto no disponible: {order.product_name}")

        # Se cargan sin ordenar (la optimización ahora es en el despacho)
        for order in temp_orders:
            self.truck.load_package(order)
            messages.append(f"Cargando: {order}")

        return messages

    # ===============================
    # SMART DISPATCH (OPTIMIZED ROUTE)
    # ===============================

    def dispatch_truck(self, origin_city):

        if not self.truck.stack:
            return ["No hay paquetes en el camión."]

        messages = []
        messages.append(f"Camión saliendo desde {origin_city}...")

        origin_position = self.city_positions[origin_city]

        packages = list(self.truck.stack)

        # Ordenar por cercanía geográfica (sin devolverse innecesariamente asi ahorrando tiempo entre pedidos)
        packages.sort(
            key=lambda order: abs(self.city_positions[order.city] - origin_position)
        )

        self.truck.stack.clear()

        for order in packages:
            messages.append(
                f"Entregado: {order.product_name} para {order.customer_name} ({order.city})"
            )

        return messages