from datetime import date
from datetime import datetime

# time separator
ts = 'X'

# date separator
ds = 'D'

# data separator
s = 'F'

# ticket type
tt = ['Normal', 'Advanced', 'Student', 'Late']

price = 100

class NormalTicket:
    def __init__(self, price, ttype):
        self.ser_num = None
        self.price = price
        self.ttype = ttype

    def sgen(self):
        now = datetime.now()
        current_time = now.strftime("%HX%MX%S")
        today = date.today()
        d1 = today.strftime("%dD%mD%Y")
        sn = f'{self.ttype[0]}F{d1}F{current_time}'
        self.ser_num = sn

    def sn_reader(self, sn):
        info = sn.split(s)
        for item in range(len(tt)):
            if info[0] == tt[item][:1]:
                print("Ticket type:", tt[item])

        date = info[1].split(ds)
        print("Purchase date:")
        for i in range(len(date)):
            print(date[i], end="/")
        print()

        time = info[2].split(ts)
        print("Purchase time:")
        for i in range(len(time)):
            print(time[i], end=':')
        print()


    def __str__(self):
        self.sgen()
        self.sn_reader(self.ser_num)
        return f'SerialNumber:{self.ser_num}\nPrice:{self.price}'


class AdvancedTicket(NormalTicket):
    def __init__(self, price, ttype):
        super().__init__(price, ttype)
        self.price = 0.6 * self.price
        self.ttype = 'Advanced'


class StudentTicket(NormalTicket):
    def __init__(self, price, ttype):
        super().__init__(price, ttype)
        self.price = 0.5 * self.price
        self.ttype = 'Student'


class LateTicket(NormalTicket):
    def __init__(self, price, ttype):
        super().__init__(price, ttype)
        self.price = 1.1 * self.price
        self.ttype = 'Late'


choice = int(input("Which ticket do you want to buy?\n1 - Normal  2 - Advanced  3 - Student  4 - Late\n"))
match choice:
    case 1:
        ticket = NormalTicket(price,'Normal')
    case 2:
        ticket = AdvancedTicket(price,'Normal')
    case 3:
        ticket = StudentTicket(price,'Normal')
    case 4:
        ticket = LateTicket(price,'Normal')
    case _:
        print('Your choice has not been recognised.')

print("Take your ticket and enjoy the IT-event!")
print(ticket)



