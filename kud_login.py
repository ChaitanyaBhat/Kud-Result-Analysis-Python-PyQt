from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, Dialog):
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
        self.usernameLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.informationLabel = QtWidgets.QLabel(Dialog)
        self.usernameEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordEdit = QtWidgets.QLineEdit(Dialog)
        self.submitButton = QtWidgets.QPushButton(Dialog)
             
        self.collegeLabel.setGeometry(QtCore.QRect(320,70,800,50))
        self.usernameLabel.setGeometry(QtCore.QRect(400,200,150,30))
        self.passwordLabel.setGeometry(QtCore.QRect(400,250,150,30))
        self.informationLabel.setGeometry(QtCore.QRect(550,160,400,20))
        self.usernameEdit.setGeometry(QtCore.QRect(550,200,250,30))
        self.passwordEdit.setGeometry(QtCore.QRect(550,250,250,30))
        self.submitButton.setGeometry(QtCore.QRect(520,350,100,30))

        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        font = QtGui.QFont()
        font.setPointSize(13)

        self.usernameEdit.setFont(font)
        self.passwordEdit.setFont(font)
        self.submitButton.setFont(font)
        
        font.setPointSize(12)
        self.informationLabel.setFont(font)
        
        self.collegeLabel.setFont(QtGui.QFont("Times",16,QtGui.QFont.Bold))
        self.collegeLabel.setStyleSheet("color: rgb(20,10,100)")
        self.usernameLabel.setFont(QtGui.QFont("Times",16,QtGui.QFont.Bold))
        self.usernameLabel.setStyleSheet("color: rgb(2, 67, 83)")
        self.passwordLabel.setFont(QtGui.QFont("Times",16,QtGui.QFont.Bold))
        self.passwordLabel.setStyleSheet("color: rgb(2, 67, 83)")
        self.informationLabel.setStyleSheet("color: rgb(200,10,10)")

        self.collegeLabel.setObjectName("college")
        self.usernameLabel.setObjectName('username_label')
        self.passwordLabel.setObjectName('password_label')
        self.informationLabel.setObjectName('information')
        self.usernameEdit.setObjectName("username")
        self.passwordEdit.setObjectName("password")
        self.submitButton.setObjectName('submit')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self,Dialog):
        _translator = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translator("Dialog","BCA Vth Semester Result Analysis 2019-20"))
        Dialog.setWindowIcon(QtGui.QIcon('global_college.jpg'))
        
        self.collegeLabel.setText(_translator('Dialog','GLOBAL COLLEGE OF MANAGEMENT, IT & COMMERCE'))
        self.usernameLabel.setText(_translator("Dialog","User Name:"))
        self.passwordLabel.setText(_translator('Dialog','Password:'))
        self.submitButton.setText(_translator('Dialog','Submit'))

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_LoginWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
