class Product:
    #attributes
    # Name = 'mazuri'
    # Price = 380.00
    # Amount = 100

    #Constructor
    def __init__(self,Name,Price,Amount):
        self.Name = Name
        self.Price = Price
        self.Amount = Amount


    #medthod
    def hello(self):
            print('Welcome to PetExo Shop')
    def Customername(self):
            print('ชื่อลูกค้า')
    def Moneyhave(self):
            print('จำนวนเงินของลูกค้า')
    def Nameproduct(self):
            print('ชื่อสินค้า')
    def Amountbuy(self):
            print('จำนวนที่ต้องการซื้อ')
    def Pricesell(self):
            print('ราคาสินค้าต่อชิ้น')

class Customer(Product):
    def __init__(self, FullName, Money,Name,Price,Amount):
        super().__init__(Name,Price,Amount)

        self.FullName = FullName
        self.Money = Money
    def calculate(self):
        self.total = self.Amount * self.Price
        self.Money -= self.total
        print(f'เหลือเงิน: {self.Money} บาท' )

###################################################################################################
#Instance
# product1 = Product('Mazuri',380.0,100.0)
# product1.hello()

# print(product1.Name)
# print(product1.Price)
# print(product1.Amount)

# print("============================================================")

# product2 = Product('Ganzhupro',239.0,100)
# product1.hello()

# print(product2.Name)
# print(product2.Price)
# print(product2.Amount)

# # print(type(product1))
# # print(type(product2))

print("============================================================")
Customer1 = Customer('Siripon',4800,'Mazuri',480,3)
Customer1.hello()
Customer1.Customername()
print(Customer1.FullName)
Customer1.Moneyhave()
print(Customer1.Money)
Customer1.Nameproduct()
print(Customer1.Name)
Customer1.Amountbuy()
print(Customer1.Amount)
Customer1.Pricesell()
print(Customer1.Price)

Customer1.calculate()

print("============================================================")
Customer2 = Customer('Weratu',4280,'Ganzhupro',380,3)
Customer2.hello()

Customer2.Customername()
print(Customer2.FullName)
Customer2.Moneyhave()
print(Customer2.Money)
Customer2.Nameproduct()
print(Customer2.Name)
Customer2.Amountbuy()
print(Customer2.Amount)
Customer2.Pricesell()
print(Customer2.Price)

Customer2.calculate()

print("============================================================")
Customer3 = Customer('Wareerat',4280,'Mazuri',480,5)
Customer3.hello()
Customer3.Customername
print(Customer3.FullName)

Customer3.Customername()
print(Customer3.FullName)
Customer3.Moneyhave()
print(Customer3.Money)
Customer3.Nameproduct()
print(Customer3.Name)
Customer3.Amountbuy()
print(Customer3.Amount)
Customer3.Pricesell()
print(Customer3.Price)

Customer3.calculate()
