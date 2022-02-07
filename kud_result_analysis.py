import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from PyQt5.QtGui import QIcon
from kud_login import *
from kud_select_result import *
from kud_student_result import *
from kud_subject_report import *
from kud_grade_report import *
from kud_top10_stds import *
from kud_pieChart import *
# from kud_pie_chart import *

class StudentResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.select = StudentResult()
        self.select.setupUi()
        self.select.backButton.clicked.connect(self.selection)

    def selection(self):
            self.close()
            self.ui = SelectionWindow()
            
class SubjectReportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.select = SubjectReport()
        self.select.setupUi()
        self.select.backButton.clicked.connect(self.selection)

    def selection(self):
        self.close()
        self.ui = SelectionWindow()

class GradeReportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.select = GradeReport()
        self.select.setupUi()
        self.select.backButton.clicked.connect(self.selection)

    def selection(self):
        self.close()
        self.ui = SelectionWindow()

class Top10StdsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.select = Top10Stds()
        self.select.setupUi()
        self.select.backButton.clicked.connect(self.selection)

    def selection(self):
        self.close()
        self.ui = SelectionWindow()

class PieChartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.select = PieChart()
        self.select.backButton.clicked.connect(self.selection)

    def selection(self):
        self.close()
        self.ui = SelectionWindow()

class SelectionWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.select = SelectionScreen()
        self.select.setupUi(self)
        self.show()
        self.select.studentButton.clicked.connect(self.student_result)
        self.select.subjectButton.clicked.connect(self.subject_report)
        self.select.gradeButton.clicked.connect(self.grade_report)
        self.select.top10Button.clicked.connect(self.top10_stds)
        self.select.chartButton.clicked.connect(self.pie_chart)

    def student_result(self):
        self.close()
        self.ui = StudentResultWindow()

    def subject_report(self):
        self.close()
        self.ui = SubjectReportWindow()

    def grade_report(self):
        self.close()
        self.ui = GradeReportWindow()

    def top10_stds(self):
        self.close()
        self.ui = Top10StdsWindow()

    def pie_chart(self):
        self.close()
        self.ui = PieChartWindow() 

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.login = Ui_LoginWindow()
        self.login.setupUi(self)
        self.show()
        self.login.submitButton.clicked.connect(self.validate)

    def validate(self):
        username = self.login.usernameEdit.text()
        password = self.login.passwordEdit.text()

        if username == "" or password == "":
            self.login.informationLabel.setText("User name and/or password required")
        elif username == "globalcollege" and password == "global":
            self.login.informationLabel.setText("Logged in successfully")
            self.selection()
        else:
            self.login.informationLabel.setText("Invalid user name and/or password")
            
    def selection(self):
        self.close()
        self.ui = SelectionWindow()

def main():
    app = QApplication(sys.argv)
    interact = LoginWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

