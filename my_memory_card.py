#подключение библиотек
from PyQt5.QtCore import Qt
from random import shuffle, choice
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
QLabel, QVBoxLayout, QWidget, QRadioButton, QGroupBox, QHBoxLayout,
QButtonGroup
)

#класс-шаблон для вопросов
class Question():
    def __init__(self, q, r_a, w_a1, w_a2, w_a3):
        self.questionn = q # вопрос
        self.right_answer = r_a # правильный ответ
        self.wrong_answer1 = w_a1 # неправильный ответ 1
        self.wrong_answer2 = w_a2 # неправильный ответ 2
        self.wrong_answer3 = w_a3 # неправильный ответ 3

#функции
def show_result(): #на труфолс
    RadioGroupBox.hide()
    Otvetbox.show()
    otvet.setText('Следщ вопрс')

def show_quchen(): #обратная отчистка окон
    Otvetbox.hide()
    RadioGroupBox.show()
    otvet.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def otvet_zapusk():
    if otvet.text() == 'Ответить':
        check_answer()
    else:
        next_question()


def ask(q: Question): #q должно быть из класса Question
    shuffle(buttons) #перемешать кнопки
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong_answer1) 
    buttons[2].setText(q.wrong_answer2) 
    buttons[3].setText(q.wrong_answer3) 
    question.setText(q.questionn)
    truee.setText(q.right_answer)
    window.total_question += 1
    show_quchen()

def check_answer(): #проверить правильный ответ
    if buttons[0].isChecked():
        trufalse.setText('Пральна')
        show_result()
        window.correct_answers += 1
        #рейтинг
        raiting = (window.correct_answers/window.total_question)*100
        print('Статистика')
        print('-Всего вопросов', window.total_question)
        print('-Правильных ответов', window.correct_answers)
        print('Рейтинг',raiting, '%')
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        trufalse.setText('Непральна')
        raiting = (window.correct_answers/window.total_question)*100
        print('Статистика')
        print('-Всего вопросов', window.total_question)
        print('-Правильных ответов', window.correct_answers)
        print('Рейтинг', raiting, '%')
        show_result()

def next_question(): #следщ вопрос
    random_question = choice(questions)
    ask(random_question)
#подключение главного окна
app = QApplication([])
window = QWidget()
window.correct_answers = 0 #правидбные ответы счетсик
window.total_question = 0 # кол-во вопрсов
window.setWindowTitle('Мемари кард')
window.resize(800,600) #размер окна


#создание вопроса
question = QLabel('Кто татар')


#создание кнопки ответить
otvet = QPushButton('Ответить')

#Создание группы 
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Олег')

rbtn_2 = QRadioButton('Вадим')

rbtn_3 = QRadioButton('Серега')

rbtn_4 = QRadioButton('Алтан')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#создание списка
buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(buttons)

#создание группы ответа
Otvetbox = QGroupBox('Результаты теста')
trufalse = QLabel('Правильно/неправильно')
truee = QLabel('Пральна')
Otvetbox.hide()

#создание линии главного окна
v_line = QVBoxLayout() #глав
h_line1 = QHBoxLayout() # второстепенные
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

#создание линии доп.окна Группы
h_line = QHBoxLayout() #глав
v_line1 = QVBoxLayout()#второстепенные
v_line2 = QVBoxLayout()

#прикрепление линий группы
v_line1.addWidget(rbtn_1, alignment= Qt.AlignCenter)
v_line1.addWidget(rbtn_2, alignment= Qt.AlignCenter)
v_line2.addWidget(rbtn_3, alignment= Qt.AlignCenter)
v_line2.addWidget(rbtn_4, alignment= Qt.AlignCenter)
h_line.addLayout(v_line1)
h_line.addLayout(v_line2)
RadioGroupBox.setLayout(h_line)

#прикрепление линиий группы ответа
ans_v_line = QVBoxLayout()
ans_v_line.addWidget(trufalse)
ans_v_line.addWidget(truee,  alignment= Qt.AlignCenter)
Otvetbox.setLayout(ans_v_line)

#прикрепление линий главного окна
h_line1.addWidget(question, alignment= Qt.AlignCenter)
h_line2.addWidget(RadioGroupBox)
h_line2.addWidget(Otvetbox)
h_line3.addStretch(1)
h_line3.addWidget(otvet,stretch=3)
h_line3.addStretch(1)
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

#взаимодействие
otvet.clicked.connect(otvet_zapusk)

#Множество вопросов
questions = []
questions.append(Question('Что все так хотят, но этого никогда нет?', #вопрос
                        'печенье', #правильный ответ
                        'сушки', #неправильный ответ
                        "доп.астракоины",#неправильный ответ
                        "стаканчики"))#неправильный ответ

questions.append(Question('Главный злодей в МГЧД?', #вопрос
                        'Птица', #правильный ответ
                        'Олег Волков', #неправильный ответ
                        "Сергей Разумовский",#неправильный ответ
                        "Игорь Гром"))#неправильный ответ

questions.append(Question('Главный герой в Гарри Поттере?', #вопрос
                        'Гарри Поттер', #правильный ответ
                        'Северус Снейп', #неправильный ответ
                        "Воландеморт",#неправильный ответ
                        "Губка боб"))#неправильный ответ

questions.append(Question('Брат мадары отдавший ему свой шаринган', #вопрос
                        'Изуна Учиха', #правильный ответ
                        'Саске Учиха', #неправильный ответ
                        "Какаши",#неправильный ответ
                        "Итачи Учиха"))#неправильный ответ

questions.append(Question('Из чего делается кетчунез?', #вопрос
                        'кетчуп и майонез', #правильный ответ
                        'кетчуп', #неправильный ответ
                        "майонез",#неправильный ответ
                        "васаби и горчица"))#неправильный ответ

questions.append(Question('Тот..чье имя нельзя называть?', #вопрос
                        'Воландеморт', #правильный ответ
                        'Пушкин', #неправильный ответ
                        "Дрейк",#неправильный ответ
                        "Том Редлл"))#неправильный ответ
questions.append(Question('Как зовут преподавателя?', #вопрос
                        'Мария', #правильный ответ
                        'Извините..', #неправильный ответ
                        "А можете подойти пж",#неправильный ответ
                        "Молния маквин"))#неправильный ответ
questions.append(Question('Какого цвета синий?', #вопрос
                        'синий', #правильный ответ
                        'сеорбуромалиновый', #неправильный ответ
                        "красноватый",#неправильный ответ
                        "белый"))#неправильный ответ                    
                        
                        
                                    

#ВЫВОД
window.setLayout(v_line)
next_question()
window.show()
app.exec_()