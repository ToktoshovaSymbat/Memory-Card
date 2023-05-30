#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QLabel, QButtonGroup 
from random import shuffle ,randint
class Question():
    def __init__(self,question,right_ansver,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_ansver
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([]) 

window = QWidget() 
window.setWindowTitle("Memory Card")
window.resize(400,400)

btn_Ok = QPushButton("Ответить")  
lb_Question = QLabel("Самый сложный вопрос в галактике!")  
  
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("Вариант 1") 
rbtn_2 = QRadioButton("Вариант 2") 
rbtn_3 = QRadioButton("Вариант 3") 
rbtn_4 = QRadioButton("Вариант 4") 
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1) 
RadioGroup.addButton(rbtn_2) 
RadioGroup.addButton(rbtn_3) 
RadioGroup.addButton(rbtn_4) 
 
layout_ans_hor = QHBoxLayout() 
layout_ans_ver1 = QVBoxLayout()  
layout_ans_ver2 = QVBoxLayout()  
layout_ans_ver1.addWidget(rbtn_1) 
layout_ans_ver1.addWidget(rbtn_2) 
layout_ans_ver2.addWidget(rbtn_3) 
layout_ans_ver2.addWidget(rbtn_4) 
 
layout_ans_hor.addLayout(layout_ans_ver1) 
layout_ans_hor.addLayout(layout_ans_ver2) 
 
 
 
RadioGroupBox.setLayout(layout_ans_hor) 
 
AnsGroupBox = QGroupBox("Результат теста") 
lb_Result = QLabel("прав ты или нет?") 
lb_Correct = QLabel("ответ будет тут!") 
  
layout_res = QVBoxLayout() 
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | 
Qt.AlignTop)) 
 
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter,stretch=1) 
AnsGroupBox.setLayout(layout_res) 
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | 
Qt.AlignVCenter)) 
 
layout_line3.addStretch(1) 
layout_line2.addWidget(RadioGroupBox) 
layout_line2.addWidget(AnsGroupBox) 
 
AnsGroupBox.hide() 
layout_line3.addWidget(btn_Ok, stretch=2)
layout_line3.addStretch(1) 
 
 
layout_card = QVBoxLayout() 
 
layout_card.addStretch(1) 
layout_card.addLayout(layout_line1) 
layout_card.addStretch(1) 
 
layout_card.addLayout(layout_line2, stretch=8) 
 
layout_card.addStretch(1) 
layout_card.addLayout(layout_line3) 
layout_card.addStretch(1) 
 
def show_result(): 
    RadioGroupBox.hide() 
    AnsGroupBox.show() 
    btn_Ok.setText("Следующий вопрос") 
 
def show_question(): 
    RadioGroupBox.show() 
    AnsGroupBox.hide() 
    btn_Ok.setText("Ответить")  
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False) 
    rbtn_2.setChecked(False) 
    rbtn_3.setChecked(False) 
    rbtn_4.setChecked(False) 
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
     shuffle(answers)
     answers[0].setText(q.right_answer)
     answers[1].setText(q.wrong1)
     answers[2].setText(q.wrong2)
     answers[3].setText(q.wrong3)
     lb_Question.setText(q.question)
     lb_Correct.setText(q.right_answer)
     show_question()

def show_corect(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_corect('Правильно!')
        window.score +=1
        print('Стаститика\n-Всего вопросов:',window.total,'\nПравильных ответов:',window.score)
        print('Рейтинг:',(window.score/len(question_list)*100))
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_corect('Неправильно!')
        print('Стаститика\n-Всего вопросов:',window.total,'\nПравильных ответов:',window.score)
        print('Рейтинг:',(window.score/window.total*100))


def next_question():
    #window.cur_question = window.cur_question +1
    #if window.cur_question >= len(question_list):
        #window.cur_question = 0
    cur_question = randint(0,len(question_list) - 1)
    window.total +=1
    q = question_list[cur_question]
    ask(q)

def check_OK():
    if btn_Ok.text() =='Ответить':
        check_answer()
    else:
        next_question()

question_list = []

q1 = Question('Сколько солнечных лучей на флаге Кыргзстана','40','41','50','360')
q2 = Question('В какой стране нету своей армии?','Монако','Бразилия','Англия','Чили')
q3 = Question('Сколько воин была после ВОВ?','248','20','100','49')
q4 = Question('Национальный музыкальный  ударный нструмент Грузии?','Диплипито','Мандалина','Гитара','Арфа')
q5 = Question('Что из переччисленного не является чудесом света?','Храм Василия Блаженого','Тадж-Махал','Колос Родосский','Амазонка')
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)


#window.cur_question = -1
window.total = 0
window.score = 0
 
next_question()
 
window.setLayout(layout_card) 
btn_Ok.clicked.connect(check_OK) 
window.show() 
app.exec()