from car import Car

class Bus (Car):
    busnum = 0 
    
    def __init__(self, no, owner, phone, brand, busload,):
        super().__init__(no, owner, phone)
        self.basic_charge = 3088 #金
        self.charge_day   = 508 #每天收费
        self.brand        = brand #牌
        self.busload      = busload #载客量
        Bus.busnum       += 1
        
    def Show_Msg(self):
        print("\t%s\t%s\t%s\t%s\t%s\t%s" % (self.car_number, self.car_owner, self.contact_way))
        
        
        
