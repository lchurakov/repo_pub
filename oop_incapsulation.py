class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print("Очень интересный вопрос! Не знаю.")


class Student(Human):

    def ask_question(self, someone, question):
        print(someone.name, question)
        someone.answer_question(question)

        print()


class Mentor(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        else:
            super().answer_question(question)


class CodeReviewer(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)


class Curator(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        print('Держись, всё получится. Хочешь видео с котиками?')


class Friend(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        self.answer_question(question)


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу разрабом?')
