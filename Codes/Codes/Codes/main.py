from manage import RentManage
from car    import Car
from truck  import Truck
from sedan  import Sedan

def checkCarNumber(carNum):
    pattern1 = re.compile(u'[\u4e00-\u9fa5]?')
    pattern2 = re.compile(u'[A-Z]+')
    pattern3 = re.compile(u'[0-9]+')
        
    match1 = pattern1.search(carNum)
    match2 = pattern2.search(carNum)
    match3 = pattern3.search(carNum)
        
    if match1 and match2 and match3:
        return True
        
    else:
        return False
     
            
def checkContactWay(ContactWay):
    pattern = re.compile(u'1[3|4|5|7|8]\d{9}$')
    match = pattern.search(ContactWay)
        
    if match:
        return True
        
    else:
        return False           
                                                               

if __name__ == '__main__':
    rentmanage = RentManage()
    
    while True:
        rentmanage.menu()
        choice = input("请输入: ")
        
        if choice == "1":
            car_number  = input("车牌号: ")
            
            if checkCarNumber(car_number):
                car_owner   = input("车主姓名: ")
                contact_way = input("车主联系方式: ")
            
                if checkContactWay(contact_way):
                    while True:
                        car_model   = input("请选择车型: \n1.家用汽车\n2.巴士\n3.货车\n" )
                    
                        if car_model == "1":
                            car_brand = input("品牌: ")
                            car_seats = input("座位数: ")
                            newsedan  = Sedan (car_number, car_owner, contact_way, car_brand, car_seats)
                            rentmanage.Add(newsedan) # 添加1辆轿车
                    
                        elif choice == "2": #查询
                            rentmanage.search_By_Number()
                    
                        elif choice == "3": #显示
                            rentmanage.show_Cars()
                        
                        elif choice == "4": #修改
                            rentmanage.change_Carinfo()
                    
                        elif choice == "5": #删除
                            rentmanage.delete_car() #676767676767