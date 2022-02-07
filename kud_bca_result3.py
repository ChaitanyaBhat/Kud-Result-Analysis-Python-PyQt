# University number (trail purpose): 17u10698
import pandas as pd
import mechanize
from bs4 import BeautifulSoup

register_numbers = ['17u10690','17u10691','17u10692','17u10693','17u10697','17u10698','17u10699']

def get_web_page():
    br = mechanize.Browser()
    br.addheaders = [('User-agent','Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]
    br.set_handle_robots(False)

    br.open('http://www.kud.ac.in/kud_results.aspx?key=UG')
    return br
    
def get_page_data(br,ip,i):    
    br.select_form(nr=0)
    br['cbo_course'] = ["23"]
    br['txt_reg_num'] = ip[i]

    response = br.submit()
    html = response.read()
    soup = BeautifulSoup(html,"lxml")
    return soup

def get_results(soup,results,sbj_results):
    one_result = {}
    sbj_result = {}

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

    results.append(one_result)
    
    sbj_result['OPERATING SYSTEMS'] = t2_rows[0].findAll("td")[5].string
    sbj_result['INTERNET PROGRAMMING'] = t2_rows[1].findAll("td")[5].string
    sbj_result['DATABASE MANAGEMENT SYSTEM'] = t2_rows[2].findAll("td")[5].string 
    sbj_result['SOFTWARE ENGINEERING'] = t2_rows[3].findAll("td")[5].string
    sbj_result['OPERATION RESEARCH'] = t2_rows[4].findAll("td")[5].string
    sbj_result['COMPUTER LAB - I'] = t2_rows[5].findAll("td")[5].string
    sbj_result['COMPUTER LAB - II'] = t2_rows[6].findAll("td")[5].string
    
    sbj_results.append(sbj_result)
    
    return results, sbj_results

def result_table(results,ip):
    df_result = pd.DataFrame(results,index = range(1,len(ip)+1),columns = ['Seat No.','Name','OPERATING SYSTEMS  E21',
        'INTERNET PROGRAMMING  E22','DATABASE MANAGEMENT SYSTEM  E23','SOFTWARE ENGINEERING  E24',
        'OPERATION RESEARCH  E25','COMPUTER LAB - I  E31','COMPUTER LAB - II  E32','Total Marks','Result'])
    print(f'\n {df_result}')
    # df_result.to_excel('kud_result.xlsx')
    return results, df_result

def grade_table(results):
    total_marks = []
    pass_ = fail = 0
    # counting total pass, fail & appending total marks of all students:
    for dictionary in results:
        if dictionary['Result'] == 'PASS':
            pass_+=1
            total_marks.append(int(dictionary['Total Marks']))
        elif dictionary['Result'] == 'FAIL':
            fail+=1
    # percentage calculation:
    distinction = first_class = second_class = pass_class = 0
    for mark in total_marks:
        percentage = (mark/700)*100
        if percentage >= 80:
            distinction += 1
        elif percentage >= 70:
            first_class += 1
        elif percentage >= 60:
            second_class += 1
        elif percentage >= 50:
            pass_class += 1
    
    num_of_stds = [pass_, distinction, first_class, second_class, pass_class, fail]
    grade = ['Total Pass', 'Distinction', 'First Class', 'Second Class', 'Pass Class', 'Fail']
    grade_dict = {"Result":grade, "Number of Students":num_of_stds}
    df_grade = pd.DataFrame(grade_dict, index = range(1,7))
    print(df_grade)
    
    return df_grade

def each_sbj_result(sbj_results):
    sbj1_pass = sbj2_pass = sbj3_pass = sbj4_pass = sbj5_pass = sbj6_pass = sbj7_pass = 0
    for dictionary3 in sbj_results:
        if dictionary3['OPERATING SYSTEMS'] == '\xa0\xa0PASS':sbj1_pass += 1
        if dictionary3['INTERNET PROGRAMMING'] == '\xa0\xa0PASS':sbj2_pass += 1
        if dictionary3['DATABASE MANAGEMENT SYSTEM'] == '\xa0\xa0PASS':sbj3_pass += 1
        if dictionary3['SOFTWARE ENGINEERING'] == '\xa0\xa0PASS':sbj4_pass += 1
        if dictionary3['OPERATION RESEARCH'] == '\xa0\xa0PASS':sbj5_pass += 1
        if dictionary3['COMPUTER LAB - I'] == '\xa0\xa0PASS':sbj6_pass += 1
        if dictionary3['COMPUTER LAB - II'] == '\xa0\xa0PASS':sbj7_pass += 1
    
    sbj_pass = [sbj1_pass,sbj2_pass,sbj3_pass,sbj4_pass,sbj5_pass,sbj6_pass,sbj7_pass]
    return sbj_pass

def df_into_excel(df_result,df_grade,sbj_pass):
    subject = ['OPERATING SYSTEMS',  'INTERNET PROGRAMMING', 'DATABASE MANAGEMENT SYSTEMS', 'SOFTWARE ENGINEERING', 
                'OPERATION RESEARCH', 'COMPUTER LAB - I', 'COMPUTER LAB - II']
    sbj_fail = []
    for i in range(7):
        sbj_fail.append((7-sbj_pass[i]))
    sbj_total = []
    for i in range(7):
        sbj_total.append((sbj_pass[i]+sbj_fail[i]))
    
    sbj_report_dict = {"Subject":subject, "Pass":sbj_pass, "Fail":sbj_fail, "Total":sbj_total}
    df_sbj_report = pd.DataFrame(data = sbj_report_dict, index = range(1,8))
    print(df_sbj_report)

    with pd.ExcelWriter("kud_result3.xlsx") as writer:
        df_result.to_excel(writer,sheet_name = 'sheet1')
        df_grade.to_excel(writer,sheet_name = 'sheet2')
        df_sbj_report.to_excel(writer,sheet_name = 'sheet3')
                
def result_sheet(register_numbers):
    print ("\nData submitted\nYour results are being fetched...")

    ip = register_numbers

    results = []
    sbj_results = []

    br = get_web_page()
    for i in range(len(ip)):
        soup = get_page_data(br,ip,i)
        results,sbj_results = get_results(soup,results,sbj_results)
    
    results, df1 = result_table(results,ip)
    df2 = grade_table(results)
    sbj_pass = each_sbj_result(sbj_results)

    df_into_excel(df1,df2,sbj_pass)
    print('\nYour results are in the file "kud_result3.xlsx"\n')


if __name__ == "__main__":
    result_sheet(register_numbers)
