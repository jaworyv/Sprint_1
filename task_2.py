class Tester:

    def __init__(self, name):
        self.name = name
        self.deadline = True

    def work_hard(self, deadline):
        if deadline == True:
            print(self.name, 'Что ж, ещё часок поработаю!')
        elif deadline == False:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(True)   # 'tester_2 Что ж, ещё часок поработаю!'