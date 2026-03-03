class Order:
    def __init__(self, customer_name, product_name, city):
        self.customer_name = customer_name
        self.product_name = product_name
        self.city = city

    def __str__(self):
        return f"{self.product_name} para {self.customer_name} ({self.city})"