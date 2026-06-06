#initiate class
class employee:
    #special/magic/dunder method - contructor
    def __init__(self):
        print("Started executing the attributes/data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("attributes/data have been initialized")
    
    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

#creating an object or instance of the class
sam=employee()

# print(sam.id)

# sam.travel("Kerela")

print(type(sam))