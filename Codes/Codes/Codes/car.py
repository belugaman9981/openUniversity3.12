
class Car():
    car_count = 0 #类变量,可共享
    def __init__(self, car_number, car_owner, contact_way):
        self.car_number   = car_number # 车牌号
        self.car_owner    = car_owner # 车主姓名
        self.contact_way  = contact_way # 联系方式
        self.date_rent    = "" # 出租日期
        self.date_return  = "" # 归还日期
        self.rented       = False # 出租状态
        self.basic_charge = 0 # 押金
        self.charge_day   = 0; # 每日租金
        
    def Show_Msg(self):
        print("车牌号: %s\n车主: %s\n电话: %s"%(self.car_number, self.car_owner, self.contact_way))
        print("押金: %d\n日租金: %d\n出租日期: %s\n归还日期: %s\n出租状 态: %d\n" % (self.basic_charge, self.charge_day))
