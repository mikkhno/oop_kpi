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


class BasedTicket:
    def __init__(self, price, ttype='Normal'):
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
                print(tt[item])
        date = info[1].split(ds)
        print(date, sep='/')
        time = info[2].split(ts)
        print(time, sep=':')


    def __str__(self):
        self.sgen()
        self.sn_reader(self.ser_num)
        return f'SN:{self.ser_num}\nTicket:{self.ttype}\nPrice:{self.price}'


class AdvancedDiscount(BasedTicket):
    def __init__(self, price, ttype):
        super().__init__(price, ttype)
        self.price = 0.6 * self.price
        self.ttype = 'Advanced'


class StudentDiscount(BasedTicket):
    def __init__(self, price, ttype):
        super().__init__(price, ttype)
        self.price = 0.5 * self.price
        self.ttype = 'Student'


class LateTicket(BasedTicket):
    def __init__(self, price, ttype):
        super().__init__(price, ttype)
        self.price = 1.1 * self.price
        self.ttype = 'Late'


ticket = AdvancedDiscount(60, 'Normal')
print(ticket)
