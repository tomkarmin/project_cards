class Animal:
    def __init__(self):
        self.hung_level=5.00
        0<=self.hung_level<=10
        self.eng_level=5.00
        0<=self.eng_level<=10
        self.animal_name=input('choose your animal name:')
    def __str__(self):
     return print(f' the animal name is: {self.animal_name} hunger level :{self.hung_level} energy level :{self.eng_level}')


    def eat(self,food):
        d_hunger=food//50

        self.hung_level-=d_hunger
        if self.hung_level<0:
            self.hung_level=0

            print(f'{self.animal_name} is no longer hungery')
        d_eng=food//100
        self.eng_level-=d_eng
        if self.eng_level<0:
            self.eng_level=0
        return (self.__str__())

    def play(self,play_time):
        p_level=play_time//10
        self.hung_level+=2*(p_level)
        self.eng_level-=2*(p_level)
        if self.eng_level<0:
            self.eng_level=0
            print('game over')
        if self.hung_level>10:
            self.hung_level=10
        return (self.__str__())
    def rest(self,rest_time):
        u_eng=rest_time//20
        u_hung=rest_time//30
        self.hung_level+=u_hung
        self.eng_level+=u_eng
        if self.eng_level>=10:
            self.eng_level=10
            print(f'{self.animal_name} is dine resting and want to play again')
        elif self.hung_level>10:
            self.hung_level=10
            print(f'{self.animal_name} is hungey and want to eat')
        return (self.__str__())


