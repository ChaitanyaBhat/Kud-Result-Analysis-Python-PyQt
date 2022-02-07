from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys
import pandas as pd 
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush, QFont

df = pd.read_excel('kud_result5.xlsx',sheet_name = 'sheet2')

percentage = []
for i in range(5):
    percentage.append(str(df["Percentage"][i]))

class PieChart(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("BCA Vth Semester Result Analysis 2019-20")
        self.setWindowIcon(QIcon('global_college.jpg'))
        self.setFixedSize(1300,700)
        self.create_piechart()
        
    def create_piechart(self):
        series = QPieSeries()
        for i in range(5):
            series.append(percentage[i]+"%", df["Percentage"][i])
                
        for i in range(5):
            slice = series.slices()[i]
            slice.setLabelVisible(True)
        
        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("GRADE REPORT USING PIE CHART")
        
        chart.legend().setAlignment(Qt.AlignRight)
        
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
 
        self.setCentralWidget(chartview)

        width = self.width()
        height = self.height()

        self.legendLabel = QLabel('Python', self)
        self.legendLabel.setPixmap(QPixmap("legend.png"))
        self.legendLabel.resize(200,200)
        self.legendLabel.move(width-200, height-450)

        self.backButton = QPushButton('Back', self)
        self.backButton.clicked.connect(self.close)
        self.backButton.resize(130,30)
        self.backButton.move(width-720, height-50)

        self.show()

if __name__ == "__main__": 
    App = QApplication(sys.argv)
    pie_chart = PieChart()
    sys.exit(App.exec_())

