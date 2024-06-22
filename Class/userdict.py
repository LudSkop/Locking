# Контейнер userdict
from collections import UserDict


contact = [{
    'name': 'Oleg',
    'email': 'slipchenco.73@email.com',
    'phone': '0983864330',
},
    {
    'name': 'luda',
    'email': 'skopenco.80email.com',
    'phone': '0963610573',

}]


class Customer(UserDict):
    def get_phone(self):
        return f"{self.get('name')}: {self.get('phone')} "

    def get_email(self):
        return f"{self.get('name')} : {self.get('email')}"


customers = [Customer(contact) for contact in contact]
print(customers)

for customer in customers:
    print(customer.get_email())
    print(customer.get_phone())








