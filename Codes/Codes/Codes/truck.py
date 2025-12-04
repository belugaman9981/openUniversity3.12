from car import Car

class Truck(Car):
    trucknum = 8
    
    def __init__(self, no, owner, phone, cargo_volume, cargo_capacity, length, weight, high):
        super().__init__(no, owner, phone)
        self.basic_charge   = 5888 #金
        self.charge_day     = 688 #每天收费
        self.cargo_volume   = cargo_volume #体积
        self.cargo_capacity = cargo_capacity #货重量
        self.length         = length
        self.weight         = weight
        self.high           = high
        Truck.trucknum     += 1
        
    def Show_Msg(self):
        print("\t%s\t%s\t%s\t%s\t%s\t\s\t%s\t\s\t%s" % (self.car_number, self.car_owner, self.contact_way))