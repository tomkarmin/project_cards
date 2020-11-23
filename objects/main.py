from objects.animal import *
animal1=Animal()
animal1.__str__()
action=int(input('\n1=eat\n2=play\n3=rest\n0=game over\nchoose what to do: '))
while action==1 or action==2 or action==3 or action==0:
    if action==0:
        break
    elif action==1:
        food=int(input('how much food'))
        animal1.eat(food)
        action = int(input('\n1=eat\n2=play\n3=rest\n0=game over\nchoose what to do: '))
    elif action==2:
        play_time = int(input('how much play time'))
        animal1.play(play_time)
        action = int(input('\n1=eat\n2=play\n3=rest\n0=game over\nchoose what to do: '))
    elif action==3:
        rest_time = int(input('how much rest'))
        animal1.rest(rest_time)
        action = int(input('\n1=eat\n2=play\n3=rest\n0=game over\nchoose what to do: '))


