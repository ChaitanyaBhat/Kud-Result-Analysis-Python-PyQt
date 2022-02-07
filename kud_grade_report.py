import sys
import pandas as pd 
from PyQt5.QtCore import QAbstractTableModel, Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QHeaderView,
                            QVBoxLayout, QHBoxLayout, QLabel, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush, QFont

df = pd.read_excel('kud_result5.xlsx',sheet_name = 'sheet2')
df = df[['Sl. No.','Result','Number of Students','Percentage']]

class GradeReportTable(QAbstractTableModel):
    def __init__(self,data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent = None):
        return self._data.shape[0]

    def columnCount(self, parent = None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(),index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class GradeReport(QWidget):
    def __init__(self):
        super(GradeReport,self).__init__()

    def setupUi(self):
        self.subject_report_table_model = GradeReportTable(df)
        self.view = QTableView()
        self.view.setModel(self.subject_report_table_model)
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.view.setMaximumSize(364,173)
        
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
        self.headingLabel = QLabel('Grade Wise Report')
        self.logoLabel.setPixmap(QPixmap("kud2.jpg"))
        self.backButton = QPushButton("Back")
        self.emptyLabel = QLabel("")
        
        self.logoLabel.setAlignment(Qt.AlignCenter)
        self.collegeLabel.setAlignment(Qt.AlignTop)
        self.headingLabel.setAlignment(Qt.AlignCenter)

        self.collegeLabel.setFont(QFont("Times",16,QFont.Bold))
        self.collegeLabel.setStyleSheet("color: rgb(20,10,100)")

        self.headingLabel.setFont(QFont("Times",20,QFont.Bold,True))
        self.headingLabel.setStyleSheet("color: rgb(2, 67, 83)")

        self.backButton.setMaximumSize(130,30)
        self.backButton.clicked.connect(self.close)
        
        self.vLayout = QVBoxLayout()
        self.h_tableLayout = QHBoxLayout()
        self.hLayout = QHBoxLayout()
        self.v_emptyLayout1 = QVBoxLayout()
        self.v_emptyLayout2 = QVBoxLayout()
        self.v_emptyLayout3 = QVBoxLayout()

        self.vLayout.addWidget(self.logoLabel)
        self.vLayout.addWidget(self.collegeLabel)
        self.vLayout.addWidget(self.headingLabel)
        self.h_tableLayout.addWidget(self.view)
        self.hLayout.addWidget(self.backButton)
        self.v_emptyLayout1.addWidget(self.emptyLabel)
        self.v_emptyLayout2.addWidget(self.emptyLabel)
        self.v_emptyLayout3.addWidget(self.emptyLabel)

        self.vLayout.addLayout(self.h_tableLayout)
        self.vLayout.addLayout(self.hLayout)
        self.vLayout.addLayout(self.v_emptyLayout1)
        self.vLayout.addLayout(self.v_emptyLayout2)
        self.vLayout.addLayout(self.v_emptyLayout3)

        self.vLayout.setAlignment(Qt.AlignCenter)
        self.vLayout.setSpacing(20)
        self.setLayout(self.vLayout)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    grade = GradeReport()
    grade.setupUi()
    grade.show()
    sys.exit(app.exec_())
