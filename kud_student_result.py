import sys
import pandas as pd 
from PyQt5.QtCore import QAbstractTableModel, Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QHeaderView,
                            QVBoxLayout, QHBoxLayout, QLabel, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush, QFont

df = pd.read_excel('kud_result5.xlsx',sheet_name = 'sheet1')
df = df[['Sl. No.', 'Seat No.', 'Name', 'OPERATING SYSTEMS  E21', 'INTERNET PROGRAMMING  E22',
        'DATABASE MANAGEMENT SYSTEM  E23', 'SOFTWARE ENGINEERING  E24', 
        'OPERATION RESEARCH  E25', 'COMPUTER LAB - I  E31',
        'COMPUTER LAB - II  E32', 'Marks Obtained', 'Result', 'Percentage']]

class StudentResultTable(QAbstractTableModel):
    def __init__(self,data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent = None):
        return len(self._data.index)

    def columnCount(self, parent = None):
        return len(self._data.columns)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(),index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class StudentResult(QWidget):
    def __init__(self):
        super(StudentResult,self).__init__()
        self.setupUi

    def setupUi(self):
        self.subject_report_table_model = StudentResultTable(df)
        self.view = QTableView()
        self.view.setModel(self.subject_report_table_model)
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.view.setMaximumSize(1300,380)
        
        self.setGeometry(0,0,1400,700)
        self.setWindowTitle("BCA Vth Semester Result Analysis 2019-20")
        self.setWindowIcon(QIcon('global_college.jpg'))
        self.backgroundImg = QImage("blue.jpg")
        self.setImage = self.backgroundImg.scaled(QSize(1400,700))                  
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.setImage))                        
        self.setPalette(palette)
        
        self.logoLabel = QLabel('')
        self.collegeLabel = QLabel('GLOBAL COLLEGE OF MANAGEMENT, IT & COMMERCE')
        self.headingLabel = QLabel('Each Student Result')
        self.infoLabel = QLabel("Max. marks per subject = 100           Min. marks per subject = 40         Total marks = 700")
        self.logoLabel.setPixmap(QPixmap("kud2.jpg"))
        self.backButton = QPushButton("Back")
        
        self.logoLabel.setAlignment(Qt.AlignCenter)
        self.collegeLabel.setAlignment(Qt.AlignCenter)
        self.headingLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        
        self.collegeLabel.setFont(QFont("Times",16,QFont.Bold))
        self.collegeLabel.setStyleSheet("color: rgb(20,10,100)")

        self.headingLabel.setFont(QFont("Times",20,QFont.Bold,True))
        self.headingLabel.setStyleSheet("color: rgb(2, 67, 83)")

        self.infoLabel.setFont(QFont("Times",14))
        self.infoLabel.setStyleSheet("color: rgb(2, 67, 83)")
       
        self.backButton.setMaximumSize(130,30)
        self.backButton.clicked.connect(self.close)
        
        self.hLayout = QHBoxLayout()
        self.vLayout = QVBoxLayout()

        self.vLayout.addWidget(self.logoLabel)
        self.vLayout.addWidget(self.collegeLabel)
        self.vLayout.addWidget(self.headingLabel)
        self.vLayout.addWidget(self.infoLabel)
        self.vLayout.addWidget(self.view)
        self.hLayout.addWidget(self.backButton)

        self.vLayout.addLayout(self.hLayout)
        self.vLayout.setAlignment(Qt.AlignCenter)
        self.vLayout.setSpacing(20)
        self.setLayout(self.vLayout)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    result = StudentResult()
    result.setupUi()
    result.show()
    sys.exit(app.exec_())
