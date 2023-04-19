class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh'):
          self.firstname = firstname
          self.lastname = lastname
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

class PersonAccount(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh'):
      self.incomes = dict()
      self.expenses = dict()
      self.properties = dict()
      super().__init__(firstname, lastname)

    def total_income(self):
      return sum(self.incomes.values())
    
    def total_expense(self):
      return sum(self.expenses.values())
    
    def account_info(self):
      return f'Ingresos: {self.incomes} \nEgresos: {self.expenses} \nPropiedades:{self.properties}'
    
    def add_income(self,concepto,monto):
       self.incomes[concepto]  = monto
      
    def add_expense(self,concepto,monto):
      self.expenses[concepto]  = monto

    def add_properties(self,concepto,monto):
       self.properties[concepto]  = monto  

    def account_balance(self):
      return self.total_income() - self.total_expense()
    
p3 = PersonAccount('Luis', 'Villagomez')
p4 = PersonAccount('Adriana', 'Villagomez')

print(p3.person_info())
print(p4.person_info())



p3.add_income('Ventas',100)
p3.add_income('Propinas',50)
p3.add_income('Devoluciones',700)   

p3.add_expense('Agua',60)
p3.add_expense('Renta',150)
p3.add_expense('Luz',70)   

p3.add_properties('Casa',600)
p3.add_properties('Bodega',1500)
p3.add_properties('Coche',700)  

print(p3.account_info())
print(p3.total_income())
print(p3.total_expense())
print(p3.account_balance())    

print(p4.total_income())
print(p4.total_expense())
print(p4.account_balance())