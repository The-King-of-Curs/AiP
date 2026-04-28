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