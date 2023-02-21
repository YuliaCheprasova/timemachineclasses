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
        print('Хочу отправить ', who, ' в ', where, ' в (напишите в какой год хотите его отправить) ')
        when = input()
        return when
class time_machine():
    def request(self, who, where, when):
        print('Отправляю ', who, ' в ', where, ' в ', when, ' год')
    def result(self):
        print('Отправление произошло успешно')