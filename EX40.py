class student():
    def __init__(self, firstname, lastname, studentnumber, course):
        self.firstname = firstname
        self.lastname = lastname
        self.studentnumber = studentnumber
        self.course = course
    def printDetails(self):
        print("Firstname = ", self.firstname)
        print("Lastname = ", self.lastname)
        print("Student number = ", self.studentnumber)
        print("Course = ", self.course)
    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def getStudentnumber(self):
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
    def main():
        geudet = Student("Geudet", "Popa", 3344, "IT")
        geudet.printDetails()
        anewstring = geudet.getFirstname() + " is studying the course" + geudet.getCourse()
        print(anewstring)

        geudet.setFirstname("Mircea")
        geudet.setLastname("Popa")
        geudet.setStudentnumber("3345")
        geudet.printDetails()

        anewstring = geudet.getFirstname() + "is studying the course" + geudet.getCourse()
        print(anewstring)
