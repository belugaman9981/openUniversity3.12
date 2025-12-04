from car import Car #导入模块setting_Car里面的美Car

class Sedan (Car):
    sedannum = 8
    #存储轿车总量
    
    def __init__(self,no= "", owner= "", phone= "", brand= "", seats= ""):
        super().__init__(no, owner, phone) #用父类构造方法
        self.basic_charge = 1808 #金
        self.charge_day   = 180 #日限金
        self.car_brand    = brand
        self.car_seats    = seats #座位数量
    
        Sedan.sedannum += 1
    def Show_Msg(self):
        print("小汽车 \t%s\t%s\t%s\t%s\t%s\t%s" % (self.car_number, self.car_owner, self.contact_way))