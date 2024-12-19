from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
QWidget, 
QPushButton, 
QHBoxLayout, 
QVBoxLayout, 
QLabel, 
QMessageBox,
QRadioButton, 
QGroupBox, 
QButtonGroup)
from time import sleep
from random import shuffle

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')
window.cur_question = -1
window.total = 0
window.score = 0
question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroup = QButtonGroup()
question_list = []


class Question():
    def __init__(self, questionText, correctAnswer, wrong1, wrong2, wrong3):
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.correctAnswer = correctAnswer
        self.questionText = questionText


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.correctAnswer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.questionText)
    labelCorrect.setText(q.correctAnswer)
    show_question()


def show_correct(result):
    checkAnsw.setText(result)
    show_result()


def show_question():
    AnsGroupBox.hide()
    question.show()
    RadioGroupBox.show()
    answ.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Статистика:\n -Всего вопросов:', window.total, '\n -Правильных ответов:', window.score)
        print('Рейтинг:', round(window.score / window.total * 100, 1), '%')
    elif (answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked()):
        show_correct('Неправильно')
        print('Рейтинг:', round(window.score / window.total * 100, 1), '%')


def next_question():
    window.cur_question += 1
    window.total += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)


def click_ok():
    if answ.text() == 'Ответить':
        check_answer()
    else:
        next_question()


def show_result():
    RadioGroupBox.hide()
    question.hide()
    AnsGroupBox.show()
    answ.setText('Следующий вопрос')


def start_test():
    if answ.text() == 'Ответить':
        show_result()
    else:
        show_question()


q1 = Question('Выбери перевод слова "переменная"', 'variable', 'variation', 'variant', 'changing')
q2 = Question('Сколько будет 2+2?', '4', '5', '3', '2')
q3 = Question('Какой национальности не существует?','Смурфы','Энцы', 'Чулымцы', 'Алеуты')
q4 = Question('Самый активный неметалл','F2','O2','N2','I2')
q5 = Question('Самый большой спутник Юпитера','Ганимед','Ио','Европа','Каллисто')
q6 = Question('Единственная планета названная в честь греческого бога', 'Уран', 'Марс', 'Венера', 'Сатурн')
q7 = Question('Температура абсолютного нуля','273','274','272','271')
q8 = Question('Самый сложный вопрос в мире!','Вариант 1','Вариант 2','Вариант 3','Вариант 4')


question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
shuffle(question_list)


v0_1 = QVBoxLayout()
v0 = QVBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
v3 = QVBoxLayout()


h1 = QHBoxLayout()
hspecial = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()


btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Чулымцы')
btn3 = QRadioButton('Смурфы')
btn4 = QRadioButton('Алеуты')

answers = [btn1, btn2, btn3, btn4]


RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)


answ = QPushButton('Ответить')
answ.clicked.connect(click_ok)


v0.addWidget(question)
v1.addWidget(btn1)
v1.addWidget(btn2)
v2.addWidget(btn3)
v2.addWidget(btn4)
h3.addStretch(1)
h3.addWidget(answ, stretch = 2)
h3.addStretch(1)


hspecial.addLayout(v1)
hspecial.addLayout(v2)


RadioGroupBox.setLayout(hspecial)
h2.addWidget(RadioGroupBox)
v0.addLayout(h2)
v0.addLayout(h3)


window.setLayout(v0)


AnsGroupBox = QGroupBox('Результаты теста')
checkAnsw = QLabel('Прав ты или нет?')
labelCorrect = QLabel('Ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(checkAnsw, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(labelCorrect, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
h2.addWidget(AnsGroupBox)
v0.addLayout(h2)


window.setLayout(v0)


next_question()


window.show()


AnsGroupBox.hide()


app.exec_()