class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent Constroctor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("last Name - "+self.last_name)
        print "Eye Color - "+self.eye_color


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self,last_name, eye_color)          #this initializes the inherited variables
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("last Name - "+self.last_name)
        print "Eye Color - "+self.eye_color
        print "Number of toys - "+str(self.number_of_toys)
        

billy_cyrus = Parent("Cyrus", "blue")
#billy_cyrus.show_info()

miley_cyrus = Child("Cyrus","Blue", 5)
miley_cyrus.show_info()
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
