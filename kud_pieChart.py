import sys
import pandas as pd 
from PyQt5.QtCore import QAbstractTableModel, Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QHeaderView,
                            QVBoxLayout, QHBoxLayout, QLabel, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush, QFont

class PieChart(QWidget):
    def __init__(self):
        super(PieChart,self).__init__()
        self.setupUi()

    def setupUi(self):      
        self.setGeometry(0,0,1400,700)
        self.setWindowTitle("BCA Vth Semester Result Analysis 2019-20")
        self.setWindowIcon(QIcon('global_college.jpg'))

        #self.backgroundImg = QImage("pie_chart.png")
        self.backgroundImg = QImage("blue.jpg")
        self.setImage = self.backgroundImg.scaled(QSize(1400,700))                
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.setImage))                        
        self.setPalette(palette)
        
        self.collegeLabel = QLabel('GLOBAL COLLEGE OF MANAGEMENT, IT & COMMERCE')
        self.backButton = QPushButton("Back")
        
        self.collegeLabel.setAlignment(Qt.AlignCenter)

        self.collegeLabel.setFont(QFont("Times",12,QFont.Bold))
        self.collegeLabel.setStyleSheet("color: rgb(20,10,100)")

        self.backButton.setMaximumSize(130,30)
        self.backButton.clicked.connect(self.close)
        
        self.vLayout = QVBoxLayout()
        self.h_tableLayout = QHBoxLayout()
        self.hLayout = QHBoxLayout()
      
        self.vLayout.addWidget(self.collegeLabel)
   #changes  
        self.piechartImg = QLabel('')   
        self.piechartImg.setPixmap(QPixmap("Figure_1.png"))
        self.piechartImg.setAlignment(Qt.AlignCenter)
        self.vLayout.addWidget(self.piechartImg)
#end
        self.hLayout.addWidget(self.backButton)
        
        self.vLayout.addStretch(1)
        self.vLayout.addLayout(self.h_tableLayout)
        self.vLayout.addLayout(self.hLayout)
        
        self.vLayout.setAlignment(Qt.AlignCenter)
        self.vLayout.setSpacing(20)
        self.setLayout(self.vLayout)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    chart = PieChart()
    chart.setupUi()
    chart.show()
    sys.exit(app.exec_())
