class Student():
    def __init__(self, firstname, lastname, studentnumber, course):
        self.firstname = firstname
        self.lastname = lastname
        self.studentnumber = studentnumber
        self.course = course
    def printDetails(self):
        print("Firstname = ", self.firstname)
        print("Lastname = ", self.lastname)
        print("Studentnumber = ", self.studentnumber)
        print("Course = ", self.course)
    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def getStdentnumber(self):
        return self.studentnumber
    def getCourse(self):
        return self.course
    def setFirstname(self, firstnameinput):
        self.firstname = firstnameinput
    def setLastname(self, lastnameinput):
        self.lastname = lastnameinput
    def setStudentnumber(self, studentnumberinput):
        self.studentnumber = studentnumberinput
    def setCourse(self, courseinput):
        self.course = courseinput

student1 = Student("Geudet" , "Popa" , 3344, "IT")
student1.printDetails()

student2 = Student("Mircea" , "Popa" , 3345, "IT")
student2.printDetails()
