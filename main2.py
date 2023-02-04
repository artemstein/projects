import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 20
        self.progress = 3
        self.money = 150
        self.alive = True


    def to_study(self):
        print('Time to study!')
        self.gladness -= 5
        self.progress += 0.5
        self.money -= 30

    def to_chill(self):
        print('Take a chill...')
        self.gladness += 2.5
        self.progress -= 0.2
        self.money -= 30

    def to_sleep(self):
        print('Time to sleep...')
        self.gladness += 5.5
        self.money -= 30

    def to_work(self):
        print('Time to work!')
        self.progress += 0.1
        self.money += 50

    def is_alive(self):
        if self.progress < 0.3:
            print('Kicked out...')
            self.alive = False

        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False

        elif self.progress >= 50:
            print('Passed exams')
            self.alive = False

        elif self.gladness >= 100:
            print('Have a good mood!')
            self.progress += 5

        elif self.money >= 1000:
            print('Time for tutor!')
            self.progress += 5
            self.money -= 700

        elif self.money <= 50:
            print('Need to work now!!!')
            self.money += 100
            self.gladness -= 7
            self.progress -= 1.5

        elif self.progress <= 1:
            print('Need to study now!!!')
            self.gladness -= 5
            self.progress += 3


    def day_info(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {round(self.progress, 2)}')
        print(f'Money - {self.money}')

    def live(self, day):
        day = 'Day ' + str(day) + ' of ' + self.name + ' life'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_sleep()
        else:
            self.to_work()

        self.day_info()
        self.is_alive()

artem = Student('Artem')
for day in range(1, 366):
    if artem.alive == False:
        break
    artem.live(day)
