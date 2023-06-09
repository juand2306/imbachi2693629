from User import User
class Class(User):
    def __init__(self, name, id, className):
        super().__init__(name, id)
        self.__className = className
        self.__classes = []

    def addClass(self, classObj):
        self.__classes.append(classObj)

    def setClass(self):
        className = input("Enter the class name: ")
        objClass = Class(className)
        self.__classes.append(objClass)