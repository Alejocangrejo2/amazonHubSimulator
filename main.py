from simulator import LogisticsSimulator


def main():
    system = LogisticsSimulator()

    while True:
        print("\n--- SIMULADOR AMAZON HUB ---")
        print("1. Crear pedido")
        print("2. Procesar pedidos")
        print("3. Despachar camión")
        print("4. Mostrar inventario")
        print("5. Salir")

        option = input("Seleccione opción: ")

        if option == "1":
            customer = input("Nombre del cliente: ")
            product = input("Producto: ")
            system.receive_order(customer, product)

        elif option == "2":
            system.process_orders()

        elif option == "3":
            system.dispatch_truck()

        elif option == "4":
            system.inventory.display_inventory()

        elif option == "5":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()