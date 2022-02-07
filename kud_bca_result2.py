# University number (trail purpose): 17u10698
import pandas as pd
import mechanize
from bs4 import BeautifulSoup

# register number of students whose results are to be fetched
register_numbers = ['17u10697','17u10698','17u10699']

def get_web_page():
    # browsing the kud result page 
    print("\nData submitted\n")
    br = mechanize.Browser()
    br.addheaders = [('User-agent','Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]
    br.set_handle_robots(False)
    br.open('http://www.kud.ac.in/kud_results.aspx?key=UG')
    print ("Results are being fetched...\n")
    return br
    
def get_page_data(br,ip,i): 
    # getting the result page content of each student     
    br.select_form(nr=0)
    br['cbo_course'] = ["23"]
    br['txt_reg_num'] = ip[i]
    response = br.submit()
    html = response.read()
    soup = BeautifulSoup(html,"lxml")
    return soup

def get_results(soup,results):
    # parsing the 2 result-table contents of each student 
    one_result = {}
    
    table1 = soup.findAll('table',{"width":"570"})[0]
    table2 = soup.findAll('table',{"width":"570"})[1]
    
    t1_rows = table1.findAll("tr")[1:3]
    one_result['Seat No.']=t1_rows[0].findAll("td")[1].string
    one_result['Name']=t1_rows[1].findAll("td")[1].string
    
    t2_rows = table2.findAll("tr")[:7]
    one_result['OPERATING SYSTEMS  E21'] = t2_rows[0].findAll("td")[3].string+" + IA:"+t2_rows[0].findAll("td")[4].string
    one_result['INTERNET PROGRAMMING  E22'] = t2_rows[1].findAll("td")[3].string+" + IA:"+t2_rows[1].findAll("td")[4].string
    one_result['DATABASE MANAGEMENT SYSTEM  E23'] = t2_rows[2].findAll("td")[3].string+" + IA:"+t2_rows[2].findAll("td")[4].string
    one_result['SOFTWARE ENGINEERING  E24'] = t2_rows[3].findAll("td")[3].string+" + IA:"+t2_rows[3].findAll("td")[4].string
    one_result['OPERATION RESEARCH  E25'] = t2_rows[4].findAll("td")[3].string+" + IA:"+t2_rows[4].findAll("td")[4].string
    one_result['COMPUTER LAB - I  E31'] = t2_rows[5].findAll("td")[3].string+" + IA:"+t2_rows[5].findAll("td")[4].string
    one_result['COMPUTER LAB - II  E32'] = t2_rows[6].findAll("td")[3].string+" + IA:"+t2_rows[6].findAll("td")[4].string

    t2_result = table2.findAll("tr")[7:11]
    one_result["Total Marks"] = t2_result[0].findAll("td")[1].string
    one_result["Result"] = t2_result[2].findAll("td")[1].string
    # print(one_result)

    results.append(one_result)
    return results

def result_table(results,ip):
    # exporting fetched result of all students into spreadsheet
    df = pd.DataFrame(results,index = range(1,len(ip)+1),columns = ['Seat No.','Name','OPERATING SYSTEMS  E21',
        'INTERNET PROGRAMMING  E22','DATABASE MANAGEMENT SYSTEM  E23','SOFTWARE ENGINEERING  E24',
        'OPERATION RESEARCH  E25','COMPUTER LAB - I  E31','COMPUTER LAB - II  E32','Total Marks','Result'])
    # print(f'\n {df}')
    df.to_excel('kud_result2.xlsx')
    print('\nYour results are in the file "kud_result2.xlsx"\n')

def result_sheet(register_numbers):
    results = []
    one_result = {}
    ip = register_numbers

    br = get_web_page()
    
    # looping through all the register numbers
    for i in range(len(ip)):
        soup = get_page_data(br,ip,i)
        results = get_results(soup,results)
    
    result_table(results,ip)

if __name__ == "__main__":
    result_sheet(register_numbers)
