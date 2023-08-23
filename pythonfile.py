class flight():
    def __init__(self):
        self.fd={"AI161E90": ["BLR", "BOM", 5600], "BR161F91": ["BOM", "BBI", 6750], "AI161F99": ["BBI", "BLR", 8210], "VS171E20":["JLR", "BBI", 5500], "AS171G30": ["HYD", "JLR", 4400], "AI131F49": ["HYD", "BOM", 3499]}

    def opt1(self):
        x=input("Enter city for flight : ")
        for i in self.fd:
            if self.fd[i][1]==x:
                print(i, ":", self.fd[i])
    def opt2(self):
        x=input("Enter city for flight : ")
        for i in self.fd:
            if self.fd[i][0]==x:
                print(i, ":", self.fd[i])

    def opt3(self):
        x=input("Enter departure city for flight : ")
        y=input("Enter arrival city for flight : ")
        for i in self.fd:
            if self.fd[i][0]==x and self.fd[i][1]==y:
                print(i, ":", self.fd[i])
            



def main():
    obj1=flight()
    print("Choose an option : ")
    print("1. Flights for a particular city\n2. Flights from a city\n3. Flights between two given cities")
    n=int(input("Enter your choice(1/2/3) : "))
    if n==1:
        obj1.opt1()
    elif n==2:
        obj1.opt2()
    elif n==3:
        obj1.opt3()

main()