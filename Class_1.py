class person :
    count = 0
    def __init__(self,name,age,berthday,) -> None:
        self.name = name
        self.age = age
        self.berthday = berthday
    def get_name (self) :
        print('name is: %s' % self.name )
    def get_age (self) :
        print('age is: %s'% self.age)
    def get_berthday(self) :
        print('berthday is: %s' % self.berthday)
    def get_name_and_age(self) :
        print('name is: %s' % self.name ,'and age is: %i' % self.age)

mmdreza = person('mmdreza',20,1383)

mmdreza.get_name()
mmdreza.get_name_and_age()
mmdreza.get_berthday()

     





# name = 'habib heidari'
# print(name.split('h'))
# print(type(name))