class Calisan:
    #pass
    parayi_arttir = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullName(self):
        return '{} {}'.format(self.first,self.last)

    def zamYap(self):
        self.pay = self.pay * self.parayi_arttir

    @classmethod
    def set_raise_amt(cls,amount):
        cls.parayi_arttir = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split("-")
        return cls(first,last,pay)

    @staticmethod
    def is_workDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



c1 = Calisan("First","Last",1000)
#c2 = Calisan()

c1.set_raise_amt(1.9)

print(c1);#print(c2)

c1.adi = "furkan"
c1.soyadi = "kubilay"
c1.mail = "furkankubilay81@hotmail.com"
c1.telefon = "0553 326 .. .."

print(c1.adi);print(c1.soyadi);print(c1.mail);print(c1.telefon)

print(c1.fullName())

#print(Calisan.fullName(c1))

print(c1.__dict__)

yC = Calisan.from_string("f-k-1000")
print(yC.__dict__)

import datetime
my_date = datetime.date(1995,6,18)
print(Calisan.is_workDay(my_date))
print(my_date.strftime("%A"))

