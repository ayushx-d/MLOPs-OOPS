# #Simplle Inheritance

# ## Base class
# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# ##Derived class
# class Dog(Animal):
#     def __init__(self):
#         self.behaviour="friendly"

#     def speak1(self):
#         print(f"{self.name} barks. He is very {self.behaviour}")


# ## Create an instance of Animal
# # animal=Animal("Generic Animal")
# # animal.speak()

# ## Create an instance of Dog
# dog=Dog()
# dog.speak1()



# Super Keyword

# Super

# Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# # Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()  # Call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")

# # Create an instance of Dog
dog = Dog("Golden Retriever")
dog.speak()
# Output:
# Buddy makes a sound.
# Buddy barks. It is a Golden Retriever.