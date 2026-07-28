class Ticket:
    source="Hyd"
    dest="Goa"
    total=0
    def __init__(self,name,age,email,phone_no):
        self.name=name
        self.age=age
        self.email=email
        self.phone_no=phone_no
        Ticket.total+=1
t1=Ticket("Harsha",24,"harsha@gmail.com",9128374655)
print(Ticket.total)