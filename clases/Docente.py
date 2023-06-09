from User import User
from Dept import Dept

class Account(User):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.__depts = []

    def addDept(self, dept):
        self.__depts.append(dept)

    def createDept(self):
        deptName = input("Insert the dept name: ")
        deptType = input("Insert the dept type: ")
        objdept = Dept(deptName, deptType)
        self.__depts.append(objdept)

    def getDept(self):
        return self.__depts
