class Student:
    def __init__(self):
        self.name=input("type the name:")
        self.id=int(input('type id: '))
        self.grade_dic={}

    def __str__(self):
        return print(f'student name: {self.name}\tstudent id: {self.id}')

    def add_garde(self,subj,grade):
        self.grade_dic[subj]=grade

    def calc_factor(self,subj,factor):
        self.grade_dic[subj]=((self.grade_dic[subj])/100)*factor


    def avg(self):
        avrage=sum(self.grade_dic.values())/len(self.grade_dic.values())
        return print(avrage)
