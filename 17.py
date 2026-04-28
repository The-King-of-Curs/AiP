class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, klass):
        self.restaurant_name =  restaurant_name
        self.cuisine_type = cuisine_type
        self.klass = klass
    
    def was_fur_klass(self):
        print(f'этот рессторан класса {self.klass}')
        
    def describe_restaurant(self):
        print(f'\nназвание ресторана {self.restaurant_name}, кухня: {self.cuisine_type}')
        
    def open_restaurant(self):
        self.open = True 
        print(f'ресторан {self.restaurant_name} открыт')
            
    def clous_restaurant(self):
        self.open = False
        print(f'ресторан {self.restaurant_name} заблокирован ркн')
    
    def proverka(self):
        if self.open:
            print("Мы работаем, ркн одумался заходите! (шутка)")
        else:
            print("Извините, откроемся когда ркн задумается")


class Arbeitr(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, klass, arbeiter):
        super().__init__(restaurant_name, cuisine_type, klass)
        self.arbeiter = arbeiter
    
    def arbeit_true(self):
        self.arbeitet = True
        print(f'рабу {self.arbeiter} выдали задание')
    
    def arbeit_false(self):
        self.arbeitet = False
        print(f'рабу {self.arbeiter} нужно выдать задание')
    
    def prufung(self):
        if self.arbeitet:
            print(f'восё хорошо раб {self.arbeiter} выполняет работу')
        else:
            print(f'раб {self.arbeiter} бездельничеет нужно отобрать у него миска рис')


class Eiscafe(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, klass, adderss, arbeitszeit):
        super().__init__(restaurant_name, cuisine_type, klass)
        self.flavors = []
        self.address = adderss
        self.arbeitszeit = arbeitszeit
        self.eissort = {}
    
    def addresse(self):
        print(f'китай размести кафе по адресу: {self.address}')
    
    
    def arbei(self):
        print(f'китай сказал роботать по такому графику: {self.arbeitszeit}')    
    
        
    def eisgeschmak(self):
        print('сорт мороженого:')
        for geschmak in self.flavors:
            print(geschmak)
    
    def add_eisgeschmak(self, geschmak):
        if geschmak not in self.flavors:
            self.flavors.append(geschmak)
            print(f'вкус {geschmak} китай стал продавать')
        else:
            print(f'{geschmak} китай уже продаёт')
    
    def r_eisgeschmak(self, geschmak):
        if geschmak not in self.flavors:
            print(f'вкус {geschmak} китай не продавал')
        else:
            self.flavors.remove(geschmak)
            print(f'китай разочерован во вкусе {geschmak}')
    
    def auf_Lager(self, geschmak):
        if geschmak in self.flavors:
            print(f'китай не перестаёт выпускать вкус {geschmak}')
        else:
            print(f'китай не может делать что то в убыток партии, например как мороженое со вкусом {geschmak}')
    
    def add_eissort(self, sort, geschmak = ['ваниль']):
        if sort not in self.eissort:
            self.eissort[sort] = [geschmak]
        
        elif sort in self.eissort and geschmak not in self.eissort[sort]:
            self.eissort[sort].append(geschmak)
        
        else:
            print(f'такой вкус и тип мороженного китай любезно производит')
           
'''        
newRestaurant1 = Arbeitr('существует', 'вкусная', 'тутуру', 'тузик')
newRestaurant1.describe_restaurant()
newRestaurant1.clous_restaurant()
newRestaurant1.proverka()
newRestaurant1.was_fur_klass()
newRestaurant1.arbeit_true()
newRestaurant1.prufung()
newRestaurant1.arbeit_false()
newRestaurant1.proverka()

newRestaurant2 = Arbeitr('китай', 'рис', 'острый еда', 'ким пин тяо')
newRestaurant2.describe_restaurant()
newRestaurant2.clous_restaurant()
newRestaurant2.proverka()
newRestaurant2.was_fur_klass()
newRestaurant2.arbeit_true()
newRestaurant2.prufung()
newRestaurant2.arbeit_false()
newRestaurant2.proverka()

newRestaurant3 = Arbeitr('комунизм', 'общее', 'красный', 'народ')
newRestaurant3.describe_restaurant()
newRestaurant3.clous_restaurant()
newRestaurant3.proverka()
newRestaurant3.was_fur_klass()
newRestaurant3.arbeit_true()
newRestaurant3.prufung()
newRestaurant3.arbeit_false()
newRestaurant3.proverka()

newRestaurant4 = Arbeitr('партия', 'гордится', 'лудший', 'промолчим')
newRestaurant4.describe_restaurant()
newRestaurant4.clous_restaurant()
newRestaurant4.proverka()
newRestaurant4.was_fur_klass()
newRestaurant4.arbeit_true()
newRestaurant4.prufung()
newRestaurant4.arbeit_false()
newRestaurant4.proverka()
'''
myEiscafe = Eiscafe('китай мороженое', 'холодный кухня', 'китай', 'рядом', 'когда китай захочет')
myEiscafe.describe_restaurant()
myEiscafe.clous_restaurant()
myEiscafe.proverka()
myEiscafe.was_fur_klass()
myEiscafe.addresse()
myEiscafe.arbei()
myEiscafe.add_eisgeschmak('вкусный')
myEiscafe.add_eisgeschmak('вкусный 2')
myEiscafe.r_eisgeschmak('вкусный 2')
myEiscafe.auf_Lager('вкусный')
myEiscafe.add_eissort('на пвлка')
myEiscafe.eisgeschmak()
myEiscafe.proverka()