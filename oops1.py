


#intiate a class

class employee:

    def __init__(self):
        print("Started executing attributes/data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("attributes/data have been intiated")

    def travel(self,destination):
        print("This travel method was called manually")
        print(f'Employee is now travelling to {destination}')


sam =employee()

print(sam.salary)