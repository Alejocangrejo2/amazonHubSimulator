import tkinter as tk
from tkinter import ttk, messagebox
from simulator import LogisticsSimulator


class LogisticsGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Amazon Hub")
        self.root.geometry("1100x700")
        self.root.configure(bg="#eef2f3")

        self.system = LogisticsSimulator()

        # ===============================
        # VARIABLES
        # ===============================

        self.name_var = tk.StringVar()
        self.product_var = tk.StringVar()
        self.city_var = tk.StringVar()
        self.origin_var = tk.StringVar(value="Medellín")

        # ===============================
        # TITLE
        # ===============================

        title = tk.Label(
            root,
            text="Amazon Hub",
            font=("Arial", 20, "bold"),
            bg="#eef2f3"
        )
        title.pack(pady=15)

        # ===============================
        # MAIN CONTAINER
        # ===============================

        main_frame = tk.Frame(root, bg="#eef2f3")
        main_frame.pack(fill="both", expand=True, padx=20)

        left_frame = tk.Frame(main_frame, bg="#eef2f3")
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = tk.Frame(main_frame, bg="#eef2f3")
        right_frame.pack(side="right", fill="both", expand=True)

        # ===============================
        # ORDER FRAME
        # ===============================

        order_frame = tk.LabelFrame(left_frame, text="Nuevo Pedido", padx=10, pady=10)
        order_frame.pack(fill="x", pady=10)

        tk.Label(order_frame, text="Nombre Cliente:").grid(row=0, column=0, sticky="w")
        tk.Entry(order_frame, textvariable=self.name_var, width=20).grid(row=0, column=1)

        tk.Label(order_frame, text="Producto:").grid(row=0, column=2, sticky="w", padx=10)

        ttk.Combobox(
            order_frame,
            textvariable=self.product_var,
            values=[
                "Laptop", "Tablet", "Celular",
                "Monitor", "Teclado", "Mouse",
                "Impresora", "Router", "Audífonos"
            ],
            state="readonly",
            width=18
        ).grid(row=0, column=3)

        tk.Label(order_frame, text="Ciudad Destino:").grid(row=1, column=0, sticky="w")

        ttk.Combobox(
            order_frame,
            textvariable=self.city_var,
            values=["Medellín", "Cali", "Pasto"],
            state="readonly",
            width=18
        ).grid(row=1, column=1)

        tk.Button(
            order_frame,
            text="Agregar Pedido",
            command=self.add_order,
            bg="#4CAF50",
            fg="white"
        ).grid(row=1, column=3, pady=10)

        # ===============================
        # INVENTORY (ARRAY 3x3 VISUAL)
        # ===============================

        inventory_frame = tk.LabelFrame(left_frame, text="Inventario", padx=10, pady=10)
        inventory_frame.pack(fill="x", pady=10)

        for i in range(3):
            for j in range(3):
                product = self.system.inventory.shelves[i][j]
                label = tk.Label(
                    inventory_frame,
                    text=product if product else "-",
                    width=15,
                    height=3,
                    relief="solid",
                    bg="#caf5e3"
                )
                label.grid(row=i, column=j, padx=5, pady=5)

        # ===============================
        # ORDER LIST (QUEUE + LOGS)
        # ===============================

        list_frame = tk.LabelFrame(right_frame, text="Pedidos y Logs del Sistema", padx=10, pady=10)
        list_frame.pack(fill="both", expand=True, pady=10)

        self.order_listbox = tk.Listbox(list_frame, font=("Consolas", 10))
        self.order_listbox.pack(fill="both", expand=True)

        # ===============================
        # DISPATCH FRAME
        # ===============================

        dispatch_frame = tk.LabelFrame(root, text="Despacho de Camión", padx=10, pady=10)
        dispatch_frame.pack(fill="x", padx=20, pady=15)

        tk.Label(dispatch_frame, text="Ciudad de Origen:").pack(side="left", padx=5)

        ttk.Combobox(
            dispatch_frame,
            textvariable=self.origin_var,
            values=["Medellín", "Cali", "Pasto"],
            state="readonly",
            width=15
        ).pack(side="left", padx=5)

        tk.Button(
            dispatch_frame,
            text="Procesar Pedidos",
            command=self.process_orders,
            bg="#8ECCFF",
            fg="white"
        ).pack(side="left", padx=15)

        tk.Button(
            dispatch_frame,
            text="Despachar Camión",
            command=self.dispatch_truck,
            bg="#ff0000",
            fg="white"
        ).pack(side="left")

    # ===============================
    # METHODS
    # ===============================

    def add_order(self):
        name = self.name_var.get()
        product = self.product_var.get()
        city = self.city_var.get()

        if not name or not product or not city:
            messagebox.showwarning("Error", "Completa todos los campos")
            return

        message = self.system.receive_order(name, product, city)
        self.order_listbox.insert(tk.END, message)

        self.name_var.set("")
        self.product_var.set("")
        self.city_var.set("")

    def process_orders(self):
        messages = self.system.process_orders()
        self.order_listbox.insert(tk.END, "---- PROCESANDO ----")
        for msg in messages:
            self.order_listbox.insert(tk.END, msg)

    def dispatch_truck(self):
        origin = self.origin_var.get()
        messages = self.system.dispatch_truck(origin)

        self.order_listbox.insert(tk.END, "---- DESPACHO ----")
        for msg in messages:
            self.order_listbox.insert(tk.END, msg)


# ===============================
# MAIN
# ===============================

if __name__ == "__main__":
    root = tk.Tk()
    app = LogisticsGUI(root)
    root.mainloop()