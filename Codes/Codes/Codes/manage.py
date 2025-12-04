import time

from car         import Car
from truck       import Truck
from sedan       import Sedan
from bus         import Bus


class RentManage:
    def __init__(self):
        self.car_list = []
        db = pymysql.connect("localhost", "root", "Cx198512", "carmanagasys")
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM tb_sedan")
        results = cursor.fetchall()
        
        for item in results:
            onesedan = Sedan(item[0], item[1], item[2], item[3], item[4])
            self.car_list.append(onesedan)
            
        cursor.execute("SELECT * FROM tb_bus")
        results = cursor.fetchall()
        
        for item in results:
            onebus = Bus(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            self.car_list.append(onebus)   
            
        cursor.execute("SELECT * FROM tb_truck")
        results = cursor.fetchall()
        
        for item in results:
            onetruck = Truck(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])
            self.car_list.append(onetruck)
            
        
    def menu(self):
        
        """# 显示系统功能信息"""
        
        print("""
            _______________________________
            |***欢迎进入蚂蚁租车管理系统***|
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                    (1) 添加车辆
                    (2) 查询车辆
                    (3) 显示车辆
                    (4) 修改车辆
                    (5) 删除车辆
                    (6) 出租车辆
                    (7) 归还车辆
                    (8) 退出系统
        """)
            
            
    def Add(self, newcar):
        for car in self.car_list:
            if car.car_number == newcar.car_number:
                print("该车辆已经存在, 重新输入!")
                return
            
            self.car_list.append(newcar)
            print("车牌号为%s的车入库成功!"% newcar.car_number)
            
            
    def show_Cars (self):#显示车辆
        if len(self.car_list) != 0:
            print("=================小=================")
            print("乍型\t车牌号\t\t车主\t电话\t\t品牌\t座位数\t是否出租")
            
            for car in self.car_list:
                if isinstance (car, Sedan):
                    car.Show_Msg()
                
            print("==================================")
            print("车型\t车牌号\t\t车主\t电话\t\t品牌\t载客量\t是否出租")
            
            for car in self.car_list:
                if isinstance(car, Bus):
                    car.Show_Msg()
                    
            print("=================货车================")
            print("车型\t车牌号\t\t车主\t电话\t\t载货体积\t载货重量\t\t宽\t高\t是否出租")
            
            for car in self.car_list:
                if isinstance (car, Truck):
                    car.Show_Msg()
                    
                    
    def search_By_Number(self):
        """# 按车牌号查询"""
        findcar_number = input("请输入您要查找的车牌号:")
        for car in self.car_list:
            if car.car_number == findcar_number:
                car.Show_Msg()
                break
            
        else:
            print("未找到车牌号为%s的车辆"%findcar_number)
            
    
    def change_Carinto(self):
        """# 修改车辆信息"""
        print("=================修改车辆登记信息=================")
        car_number = input("车牌号:")
        
        for car in self.car_list:
            if car.car_number == car_number:
                change = int(input("(修改信息的序号:\n1.车主\n2.联系方式\n输入你要修改的信息序号:"))
                
                if change == 1:
                    new_info = input("输入新的信息:")
                    car.car_owner = new_info
                    print("车主名修改成功")
                
                break
            
            elif change == 2:
                new_info = input("输入新的信息:")
                car.contact_way = new_info
                print("联系方式修改成功")
                
        else:
            print("未找到车牌号为%s的车辆"% car_number)
            
            
    def delete_car(self):
        """# 删除车辆信息"""
        print("=================删除车辆=================")
        car_number = input("车牌号:")
        
        for car in self.car_list:
            if car.car_number == car_number:
                self.car_list.remove(car) #刪除元素
                print("车牌号为%s的车辆成功删除" % car_number)
                
                
    def Rent(self):
        print("=================出租车辆=================")
        car_number = input("车牌号:" )
        
        for car in self.car_list:
            if car.car_number == car_number:
                car.date_rent = time.ctime() #出租时间
                car.rented = True
                #动态添加2个实例变量
                car.rentername = input("请输入租车人姓名:" )
                car.renterid = input("请输入租车人身份证号:" )
                print("=================租车合同=================")
                print("***租车人信息***")
                print("姓名: %s\t\t 身份证号:%s" % (car.rentername, car.renterid))
                print("***出租车辆信息***")
                car.Show_Msg()
                    
                    
    def Return(self):
        print("======================归还车辆=======================")
        car_number = input("车牌号:")
        for car in self.car_list:
            if  car.car_number == car_number:
                car.date_return = time.ctime() #归还时间
                car.rented = False
                #计算租车时间
                rent_time = time.mktime(time.strptime(car.date_return)) - time.mktime(time.strptime(car.date_rent))
                d         = rent_time // 86400 # 1天86400秒
                h         = (rent_time - d * 86400) // 3600
                m         = (rent_time - h * 3600)  // 60
                s         = rent_time  - h * 3600   - m * 60
                rent_time = "%d天%d时%d分%d秒" % (d, h, m, s)
                    
                    
    def Statistics(self):
        sedanRentedNum = 0
        truckRentedNum = 0
        busRentedNum   = 0
        
        for car in self.car_list:
            if isinstance(car, Car)   and car.rented == True:
                sedanRentedNum += 1
            
            if isinstance(car, Bus)   and car.rented == True:
                busRentedNum += 1
                 
            if isinstance(car, Truck) and car.rented == True:
                truckRentedNum += 1
                
        print("租车行共计车辆" + str(Car.car_count))
        
    
    def __del__(self):
        db     = pymysql.connect("localhost", "root", "Cx198512", "carmanagasys")
        cursor = db.cursor()
        sql    = "Delete from tb_sedan"
        cursor.execute(sql)
        sql    = "Delete from tb_bus"
        cursor.execute(sql)
        sql    = "Delete from tb_truck"
        cursor.execute(sql)
        
        for newcar in self.car_list:
            if isinstance(newcar, Sedan):
                addcar = (newcar.car_number, newcar.car_owner, newcar.contact_way, newcar.car_brand, newcar.car_seats, newcar.rented, newcar.basic_charge, newcar.charge_day, newcar.date_rent, newcar.date_return)
                cursor.execute("Insert into tb_sedan (car_number, car_owner, contact_way, car_brand, car_seats, rented, basic_charge, charge_day, date_rent, date_return) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", addcar)
                
        