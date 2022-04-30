class Order: 
    def __init__(self, name): 
        self.customer = 0 
        self.name = name 
    def order(self, price):
        self.customer += price 
        return self.customer

class extraOrder(Order): 
    def order(self, price): 
        self.customer += price 
        return str(self.customer) + '원' 

extraCustomer = extraOrder('영희') 

print(extraCustomer.order(1000))

