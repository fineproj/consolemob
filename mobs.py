class mob:
    def __init__(self,phid,phname,price):
        self.phid=phid
        self.phname=phname
        self.price=price

    def __str__(self):
        return str(self.phid)+"     "+self.phname+"     "+str(self.price)
        print("\n")

    def  addMob(p):
        with open("mob.txt","a") as fp:
            fp.write(str(p))
            fp.write("\n")

    def showAllMobs():
        try:
            with open("mob.txt","r") as fp:
                data=fp.read()
                print(data)
        except FileNotFoundError:
            print("File not present")

    def searchMob(phid):
        try:
            with open("mob.txt","r") as fp:
                for line in fp:
                    line=line.strip()
                    result=line.find(str(phid),0,4)
                    if(result!=-1):
                        print("Name: ",line)
                        break
                else:
                    print("Record not found")

        except FileNotFoundError:
            print("File not present")

    def deleteMob(phid):
        allMob=[]
        found=False
        try:
            with open("mob.txt","r") as fp:
                for line in fp:
                    line=line.strip()
                    result=line.find(str(phid),0,4)
                    if(result!=-1):
                        found=True
                else:
                    allMob.append(line)
        except FileNotFoundError:
            print("File not present")
        else:
            print(allMob)

        if(found):
            with open("mob.txt","w") as fp:
                for m in allMob:
                    fp.write(m)
                    fp.write("\n")
        else:
            print("Record not present")

    def editMob(phid):
        allMob=[]

        found=False
        try:
            with open("mob.txt","r") as fp:
                for line in fp:
                    line = line.strip()
                    result=line.find(str(phid),0,4)
                    if(result!=-1):
                        found=True
                        #changes
                        m=line.split(",") #returns list

                        ans=input("Do you wish to change name?(y/n)")
                        if(ans=="y"):
                            m[1]=input("Enter the new name")
                        ans=input("Do you wish to change price?(y/n)")
                        if(ans=="y"):
                            m[2]=input("enter new price")

                        line=",".join(m)
                    allMob.append(line)
        except FileNotFoundError:
            print("File not present")

        if(found):
            with open("mob,txt","w") as fp:
                for a in allMob:
                    fp.write(a)
                    fp.write("\n")
        else:
            print("Record not present")

    def showMob1(phname):
        try:
            with open("mob.txt","r") as fp:
                for line in fp:
                    line=line.strip()
                    result=line.find(str(phname))
                    if(result!=-1):
                        print("Mob found: ",line)
                        break
                else:
                    print("Mob not found")
        
        except FileNotFoundError:
            print("File not present")

    def buyphone(quant):
        allMob=[]
        total=0
        #found=False
        try:
            with open("mob.txt","r") as fp:
                for i in range(1,quant):
                    if(i>quant):
                        break
                    else:
                        phid=int(input("Enter mobile id"))
                        quantity=int(input("Enter quantity of this model: "))
                        for line in fp:
                            line =line.strip()
                            result=line.find(str(phid),0,4)
                            if(result!=-1):
                                #found=True
                                m=line.split(",")
                                total+=float(m[2])*quantity
                                abc=m[1]
                                allMob.append(abc)
                                continue
                            else:
                                print("Mobile not available")
                print("     Bill       ")
                print("Mobile Name: ",allMob)
                print("Quantity: ",quant)
                print("Total: ",total)   

        except FileNotFoundError:
            print("File not present")