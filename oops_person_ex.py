class person:
    def __init__(self,person_name,person_age):
        self.pn=person_name
        self.pa=person_age
    def myfun(self):
        print("His name",self.pn,"and age",self.pa,"is performing his own task.")
    def myfun1(self):
        print(self.pn,"celebrating his birthday he turnes",self.pa,"years old!")
    abhijit=person("Abhijit",26)
    print(abhijit)
    abhijit.myfun()
    mrunal=person("Mrunal",26)
    mrunal.myfun1()
