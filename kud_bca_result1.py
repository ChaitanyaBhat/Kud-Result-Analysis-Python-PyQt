# University number (trail purpose): 17u10698
import pandas as pd
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.addheaders = [('User-agent','Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]
br.set_handle_robots(False)

br.open('http://www.kud.ac.in/kud_results.aspx?key=UG')
br.select_form(nr=0)

ip=input("Enter the university seat number\n")
br['cbo_course'] = ["23"]
br['txt_reg_num'] = ip
print ("\nData submitted\nYour results are being fetched...")

response = br.submit()
html = response.read()
soup = BeautifulSoup(html,"lxml")

table1 = soup.findAll('table',{"width":"570"})[0]
table2 = soup.findAll('table',{"width":"570"})[1]

t1_rows = table1.findAll("tr")[1:3]
data1 = []
for t1_data in t1_rows:
    data1.append(t1_data.findAll("td")[1])
seat_no = data1[0].string 
name = data1[1].string

t2_rows = table2.findAll("tr")[:7]
subject = []; ext_marks = []; ia_marks = []; result = []
for t2_data in t2_rows:
    subject.append(t2_data.findAll("td")[0])
    ext_marks.append(t2_data.findAll("td")[3]) 
    ia_marks.append(t2_data.findAll("td")[4]) 
    result.append(t2_data.findAll("td")[5]) 

t2_result = table2.findAll("tr")[7:11]
data2 =[]
for data in t2_result:
    data2.append(data.findAll("td")[1])
marks_obtained = data2[0].string
total_marks = data2[1].string
final_result = data2[2].string


dic ={"":[seat_no,name,
            ext_marks[0].string+" + IA:"+ia_marks[0].string,ext_marks[1].string+" + IA:"+ia_marks[1].string,
            ext_marks[2].string+" + IA:"+ia_marks[2].string,ext_marks[3].string+" + IA:"+ia_marks[3].string,
            ext_marks[4].string+" + IA:"+ia_marks[4].string,ext_marks[5].string+" + IA:"+ia_marks[5].string,
            ext_marks[6].string+" + IA:"+ia_marks[6].string,total_marks,final_result]}
df = pd.DataFrame(dic, index = ["Seat No.","Candidate Name",subject[0].string,subject[1].string,subject[2].string,
                                subject[3].string,subject[4].string,subject[5].string,subject[6].string,"Total Marks","Result"])
print(f'\n {df}')
