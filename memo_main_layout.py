from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QTableWidget, QListView, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel, QSpinBox)
from memo_app import app
from memo_edit_layout import layout_form
from memo_card_layout import layout_card

app.setStyleSheet("""
        QWidget {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                  stop:0 #03045e, stop:1 #e0aaff);
                  color: white;            
        }
""")



list_questions = QListView()
wdgt_edit = QWidget()
wdgt_edit.setLayout(layout_form)
btn_add = QPushButton('Наступне питання')
btn_add.setStyleSheet("background-color: #003566")
btn_delete = QPushButton('Видалити питання')
btn_delete.setStyleSheet("background-color: #003566")
btn_start = QPushButton('Почати')
btn_start.setStyleSheet("background-color: #003566")
btn_theme_toggle = QPushButton('Біла/Темна Тема')
btn_theme_toggle.setStyleSheet("background-color: #003566")


main_col1 = QVBoxLayout()
main_col1.addWidget(list_questions)
main_col1.addWidget(btn_add)

main_col2 = QVBoxLayout()
main_col2.addWidget(wdgt_edit)
main_col2.addWidget(btn_delete)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start, stretch=2)
main_line2.addStretch(1)
main_line2.addWidget(btn_theme_toggle)

layout_main = QVBoxLayout()
layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)


