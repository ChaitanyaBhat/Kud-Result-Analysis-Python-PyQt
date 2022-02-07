from PyQt5 import QtCore, QtGui, QtWidgets

class SelectionScreen(object):
    def __init__(self):
        self.setupUi
        
    def setupUi(self,Dialog):
        Dialog.setObjectName("Dialog")
        screen_width = 1500; screen_height = 800
        Dialog.resize(screen_width,screen_height)

        self.img =QtWidgets.QLabel(Dialog)
        
        self.img.setObjectName("image")
        self.img.setPixmap(QtGui.QPixmap("blue.jpg"))

        self.img2 =QtWidgets.QLabel(Dialog)
        self.img2.setGeometry(QtCore.QRect(430,-10,500,100))
        self.img2.setObjectName("image2")
        self.img2.setPixmap(QtGui.QPixmap("kud2.jpg"))

        self.collegeLabel = QtWidgets.QLabel(Dialog)
        self.selectLabel = QtWidgets.QLabel(Dialog)
        self.studentButton = QtWidgets.QPushButton(Dialog) 
        self.subjectButton = QtWidgets.QPushButton(Dialog) 
        self.gradeButton = QtWidgets.QPushButton(Dialog)
        self.top10Button = QtWidgets.QPushButton(Dialog)
        self.chartButton = QtWidgets.QPushButton(Dialog)

        self.collegeLabel.setGeometry(QtCore.QRect(320,70,800,50))
        self.selectLabel.setGeometry(QtCore.QRect(400,120,800,50))
        self.studentButton.setGeometry(QtCore.QRect(400,200,400,50))
        self.subjectButton.setGeometry(QtCore.QRect(400,300,400,50))
        self.gradeButton.setGeometry(QtCore.QRect(400,400,400,50))
        self.top10Button.setGeometry(QtCore.QRect(400,500,400,50))
        self.chartButton.setGeometry(QtCore.QRect(400,600,400,50))

        self.collegeLabel.setFont(QtGui.QFont("Times",16,QtGui.QFont.Bold))
        self.collegeLabel.setStyleSheet("color: rgb(20,10,100)")

        self.selectLabel.setFont(QtGui.QFont("Times",20,QtGui.QFont.Bold,True))
        self.selectLabel.setStyleSheet("color: rgb(2, 67, 83)")

        font = QtGui.QFont()
        font.setPointSize(16)

        self.studentButton.setFont(font)
        self.subjectButton.setFont(font)
        self.gradeButton.setFont(font)
        self.top10Button.setFont(font)
        self.chartButton.setFont(font)

        self.collegeLabel.setObjectName("college")
        self.selectLabel.setObjectName("select")
        self.studentButton.setObjectName('student')
        self.subjectButton.setObjectName('subject')
        self.gradeButton.setObjectName('grade')
        self.top10Button.setObjectName('top 10')
        self.chartButton.setObjectName('chart')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog","BCA Vth Semester Result Analysis 2019-20"))
        Dialog.setWindowIcon(QtGui.QIcon('global_college.jpg'))

        self.collegeLabel.setText(_translate('Dialog','GLOBAL COLLEGE OF MANAGEMENT, IT & COMMERCE'))
        self.selectLabel.setText(_translate('Dialog','Click on the option which you want:'))
        self.studentButton.setText(_translate("Dialog","Each Student Result"))
        self.subjectButton.setText(_translate("Dialog","Subject Wise Report"))
        self.gradeButton.setText(_translate("Dialog","Grade Wise Report"))
        self.top10Button.setText(_translate("Dialog","Top Ten Students"))
        self.chartButton.setText(_translate("Dialog","Result chart"))

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SelectionScreen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
