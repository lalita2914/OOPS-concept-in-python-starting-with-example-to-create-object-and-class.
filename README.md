# OOPS-concept-in-python-starting-with-example-to-create-object-and-class.
 class cellphone:
    def __init__(self,cellphone_name,cellphone_color):
        self.cn=cellphone_name
        self.cc=cellphone_color
    def switchon(self):
        print("The",self.cn,"with",self.cc,"color is switchon itself!")
    def switchoff(self):
        print("The",self.cn,"with",self.cc,"color is switchoff itself!")
    def restart(self):
        print("The",self.cn,"with",self.cc,"color is restart itself!")
    android_cellphone=cellphone("samsung","black")
        print(android_cellphone)
    android_cellphone.switchon()
     iphone_cellphone=cellphone("iphone","white")
     iphone_cellphone.switchoff()
     basic_cellphone=cellphone("tata","blue")
     basic_cellphone.restart()
     

