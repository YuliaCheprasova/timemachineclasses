import datetime
class person():
    def wish(self):
        print('Я хочу отправить (напишите кого или что) ')
        who = input()
        return who
    def place(self, who):
        print('Хочу отправить ', who, ' в (напишите любую точку мира) ')
        where = input()
        return where
    def time(self, who, where):
        while (1):
            print(
                'Хочу отправить ', who,' в ', where, ' в (напишите в какой день какого года вы хотите его (её) отправить в формате год-месяц-дата, например, 2028-06-09) ')
            when = input()
            when = datetime.datetime.strptime(when, '%Y-%m-%d')
            when = when.date()
            now = datetime.datetime.now()
            now = now.date()
            tdelta = when - now
            tdelta = tdelta.days
            if tdelta <= 0:
                print(
                    "Скорее всего вы ввели прошедшую дату, обращаем ваше внимание на то, что машина может перемещать объекты только в будущее! Попробуйте снова ")
            else:
                return tdelta
class time_machine():
    def request(self, who, where, tdelta):
        print('Отправляю ', who, ' в ', where, ' на ', str(tdelta), ' дней вперед')
    def result(self):
        print('Отправление произошло успешно')

def __main__():
    a = person()
    b = time_machine()
    who = a.wish()
    where = a.place(who)
    when = a.time(who, where)
    b.request(who, where, when)
    b.result()
