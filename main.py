from mobs import mob


if(__name__=="__main__"):
    choice=0
    while(choice!=3):
        print('''
            1. Admin
            2. Buyer
            3. Exit
        ''')
        choice=int(input("Enter choice: "))
        if(choice==1):
            choice=0
            while(choice!=6):
                print('''
                    1. Add New Mobile 
                    2. Show all Mobiles
                    3. Search for mobile
                    4. Delete mobile
                    5. Edit mobile
                    6. Exit
                ''')
                choice=int(input("\nEnter your choice: "))
                if(choice==1):
                    phid=int(input("enter ph id: "))
                    phname=input("Enter phone name: ")
                    price=float(input("Enter price: "))
                    m1=mob(phid,phname,price) 
                    mob.addMob(m1)  
                elif(choice==2):
                    print("ID     Mobile Model     Price")
                    mob.showAllMobs()
                elif(choice==3):
                    phid=int(input("Enter ph id you want to search: "))
                    mob.searchMob(phid)        
                elif(choice==4):
                    phid=int(input("Enter ph id you want to delete: "))
                    mob.deleteMob(phid)
                elif(choice==5):
                    phid=int(input("Enter phid you want to edit: "))
                    mob.editMob(phid)        
        elif(choice==2):
            choice=0
            while(choice!=5):
                print('''
                1. Show all Mobiles 
                2. Search for mobile by id
                3. Search for mobile by name
                4. Buy mobile
                5. Exit
                ''')
                choice=int(input("\nEnter your choice: "))
                if(choice==1):
                    mob.showAllMobs()
                elif(choice==2):
                    phid=int(input("Enter ph id you want to search"))
                    mob.searchMob(phid)
                elif(choice==3):
                    phname=input("Enter ph name you want to search")
                    mob.showMob1(phname)
                elif(choice==4):
                    #quantity=int(input("Enter quantity of mob you want"))
                    #for i in quantity:
                    quant=int(input("Enter quant you want to buy"))
                    mob.buyphone(quant)
