class Person:
    def __init__(self, p_name, p_age , p_height):
        print("Constructing the person object")
        self._name=p_name
        self._age=p_age
        self._height=p_height
        self._public_prop="I am Public"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name=new_name

    def _del_(self):
        print("The garbage collector is automatically destroying the person object!")


person1 = Person("John", 18 , 24)

print ("The name of the person is :" + str(person1.name))
person1.name="Mark"

print ("The name of the person is :" + str(person1.name))

print("Public :" + str(person1._public_prop))