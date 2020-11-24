
class Course:
    def __init__(self,course,id,prof,subj,max):
        self.course_name=course
        self.course_id=id
        self.stud_list=[]
        self.subj_dic = {}
        self.subj_dic[prof]=subj
        self.max=max
    def __repr__(self):
        return print(f'course name: {self.course_name}\tcourse id: {self.course_id}\nprofesor and subject:{self.subj_dic}\nmaximum number of students:{self.max}')


    def add_student(self,student):
        self.stud_list.append(student)
        return self.stud_list

    def add_factor(self,subj,factor):
        for i in self.stud_list:
            i.calc_factor()

    def del_stud(self,id):
        lst_del:[]
        for i in self.stud_list:
            if i.id==id:
                lst_del.append(i)
        self.stud_list.remove(lst_del)



    def calc_avg(self):
        all_avg=0
        for i in self.stud_list:
         all_avg+=i.avg






