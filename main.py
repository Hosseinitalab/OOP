class Car:
    def __init__(self, id):
        self._id = id
    
    @property
    def id(self):
        return self._id
    # @id.setter
    # def id(self, new_id):
    #     self._id = new_id

    

x = Car(0)  
print(x.id)
x.id = 5
print(x.id)
