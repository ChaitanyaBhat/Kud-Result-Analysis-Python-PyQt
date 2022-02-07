import mechanize
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

register_numbers = ["17u10609","17u10614","17u10619","17u10621","17u10630","17u10631","17u10633",
                    "17u10636","17u10638","17u10639","17u10640","17u10644","17u10680","17u10681",
                    "17u10683","17u10687","17u10692","17u10698","17u10699","17u10701","17u10713"]

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
    
    sbj1_split_marks = (t2_rows[0].findAll("td")[3].string + t2_rows[0].findAll("td")[4].string).split()
    sbj2_split_marks = (t2_rows[1].findAll("td")[3].string + t2_rows[1].findAll("td")[4].string).split()
    sbj3_split_marks = (t2_rows[2].findAll("td")[3].string + t2_rows[2].findAll("td")[4].string).split()
    sbj4_split_marks = (t2_rows[3].findAll("td")[3].string + t2_rows[3].findAll("td")[4].string).split()
    sbj5_split_marks = (t2_rows[4].findAll("td")[3].string + t2_rows[4].findAll("td")[4].string).split()
    sbj6_split_marks = (t2_rows[5].findAll("td")[3].string + t2_rows[5].findAll("td")[4].string).split()
    sbj7_split_marks = (t2_rows[6].findAll("td")[3].string + t2_rows[6].findAll("td")[4].string).split()
    
    sbj1_total_marks = int(sbj1_split_marks[1]) + int(sbj1_split_marks[2])
    sbj2_total_marks = int(sbj2_split_marks[1]) + int(sbj2_split_marks[2])
    sbj3_total_marks = int(sbj3_split_marks[1]) + int(sbj3_split_marks[2])
    sbj4_total_marks = int(sbj4_split_marks[1]) + int(sbj4_split_marks[2])
    sbj5_total_marks = int(sbj5_split_marks[1]) + int(sbj5_split_marks[2])
    sbj6_total_marks = int(sbj6_split_marks[1]) + int(sbj6_split_marks[2])
    sbj7_total_marks = int(sbj7_split_marks[1]) + int(sbj7_split_marks[2])
   
    # one_result['OPERATING SYSTEMS  E21'] = sbj1_split_marks[1] +' + '+  sbj1_split_marks[2] + ' = ' + str(sbj1_total_marks)
    # one_result['INTERNET PROGRAMMING  E22'] = sbj2_split_marks[1] +' + '+  sbj2_split_marks[2] + ' = ' + str(sbj2_total_marks)
    # one_result['DATABASE MANAGEMENT SYSTEM  E23'] = sbj3_split_marks[1] +' + '+  sbj3_split_marks[2] + ' = ' + str(sbj3_total_marks)
    # one_result['SOFTWARE ENGINEERING  E24'] = sbj4_split_marks[1] +' + '+  sbj4_split_marks[2] + ' = ' + str(sbj4_total_marks)
    # one_result['OPERATION RESEARCH  E25'] = sbj5_split_marks[1] +' + '+  sbj5_split_marks[2] + ' = ' + str(sbj5_total_marks)
    # one_result['COMPUTER LAB - I  E31'] = sbj6_split_marks[1] +' + '+  sbj6_split_marks[2] + ' = ' + str(sbj6_total_marks)
    # one_result['COMPUTER LAB - II  E32'] = sbj7_split_marks[1] +' + '+  sbj7_split_marks[2] + ' = ' + str(sbj7_total_marks)
    
    one_result['OPERATING SYSTEMS  E21'] = sbj1_split_marks[0]+ sbj1_split_marks[1]+ " + IA:"+ sbj1_split_marks[2]+ ' = ' + str(sbj1_total_marks)
    one_result['INTERNET PROGRAMMING  E22'] = sbj2_split_marks[0]+ sbj2_split_marks[1]+ " + IA:"+ sbj2_split_marks[2]+ ' = ' + str(sbj2_total_marks)
    one_result['DATABASE MANAGEMENT SYSTEM  E23'] = sbj3_split_marks[0]+ sbj3_split_marks[1]+ " + IA:"+ sbj3_split_marks[2]+ ' = ' + str(sbj3_total_marks)
    one_result['SOFTWARE ENGINEERING  E24'] = sbj4_split_marks[0]+ sbj4_split_marks[1]+ " + IA:"+ sbj4_split_marks[2]+ ' = ' + str(sbj4_total_marks)
    one_result['OPERATION RESEARCH  E25'] = sbj5_split_marks[0]+ sbj5_split_marks[1]+ " + IA:"+ sbj5_split_marks[2]+ ' = ' + str(sbj5_total_marks)
    one_result['COMPUTER LAB - I  E31'] = sbj6_split_marks[0]+ sbj6_split_marks[1]+ " + IA:"+ sbj6_split_marks[2]+ ' = ' + str(sbj6_total_marks)
    one_result['COMPUTER LAB - II  E32'] = sbj7_split_marks[0]+ sbj7_split_marks[1]+ " + IA:"+ sbj7_split_marks[2]+ ' = ' + str(sbj7_total_marks)
    
    t2_result = table2.findAll("tr")[7:11]
    one_result["Marks Obtained"] = t2_result[0].findAll("td")[1].string
    one_result["Result"] = t2_result[2].findAll("td")[1].string
    one_result["Percentage"] = round((((int(t2_result[0].findAll("td")[1].string))/700)*100), 2)
    
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
        'OPERATION RESEARCH  E25','COMPUTER LAB - I  E31','COMPUTER LAB - II  E32','Marks Obtained','Result',"Percentage"])
    df_result.index.name = 'Sl. No.'
    df_result = df_result[['Seat No.', 'Name', 'OPERATING SYSTEMS  E21', 'INTERNET PROGRAMMING  E22',
        'DATABASE MANAGEMENT SYSTEM  E23', 'SOFTWARE ENGINEERING  E24', 
        'OPERATION RESEARCH  E25', 'COMPUTER LAB - I  E31',
        'COMPUTER LAB - II  E32', 'Marks Obtained', 'Result', 'Percentage']]
    
    print(f'\n {df_result}')
    return results, df_result

def grade_table(results,total_stds):
    total_marks = []
    pass_ = fail = 0
    for dictionary in results:
        if dictionary['Result'] == 'PASS':
            pass_+=1
            total_marks.append(int(dictionary['Marks Obtained']))
        elif dictionary['Result'] == 'FAIL':
            fail+=1
    distinction = first_class = second_class = pass_class = 0
    for mark in total_marks:
        percentage = (mark/700)*100
        if percentage >= 70:
            distinction += 1
        elif percentage >= 60:
            first_class += 1
        elif percentage >= 50:
            second_class += 1
        elif percentage >= 40:
            pass_class += 1
    
    pass_percentage = []
    num_of_stds = [distinction, first_class, second_class, pass_class, fail]
    for stds in num_of_stds:
        pass_percentage.append(round(((stds/total_stds)*100), 2))

    grade = ['Distinction', 'First Class', 'Second Class', 'Pass Class', 'Fail']
    grade_dict = {"Result":grade, "Number of Students":num_of_stds, "Percentage":pass_percentage}
    df_grade = pd.DataFrame(grade_dict, index = range(1,6))
    df_grade.index.name = 'Sl. No.'
    df_grade = df_grade[['Result','Number of Students','Percentage']]
    
    print(df_grade)    
    return df_grade

def each_sbj_result(sbj_results,total_stds):
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
    
    subject = ['OPERATING SYSTEMS',  'INTERNET PROGRAMMING', 'DATABASE MANAGEMENT SYSTEMS', 'SOFTWARE ENGINEERING', 
                'OPERATION RESEARCH', 'COMPUTER LAB - I', 'COMPUTER LAB - II']
    sbj_fail = []
    for i in range(len(sbj_pass)):
        sbj_fail.append((total_stds-sbj_pass[i]))
    sbj_total = []
    for i in range(len(sbj_pass)):
        sbj_total.append((sbj_pass[i]+sbj_fail[i]))
    
    pass_percentage = []
    for stds in sbj_pass:
        pass_percentage.append(round(((stds/total_stds)*100), 2))

    sbj_report_dict = {"Subject":subject, "Pass":sbj_pass, "Fail":sbj_fail, "Total":sbj_total, "Pass Percentage":pass_percentage}
    df_sbj_report = pd.DataFrame(data = sbj_report_dict, index = range(1,8))
    df_sbj_report.index.name = 'Sl. No.'
    df_sbj_report = df_sbj_report[['Subject', 'Pass', 'Fail', 'Total', 'Pass Percentage']]

    print(df_sbj_report)
    return df_sbj_report

def top_10_stds(results):
    top_10 = []
    top_stds = []
    keys = ['Seat No.','Name','Marks Obtained',"Percentage"]
    for dic in results:
        top_stds.append({x:dic[x] for x in keys}) 
    top_stds.sort(key=lambda x:x['Percentage'], reverse=True)
    for i in range(10):
        top_10.append(top_stds[i])
    df_top10 = pd.DataFrame(top_10, index=range(1,11))
    df_top10.index.name = 'Sl. No.'
    df_top10 = df_top10[['Seat No.', 'Name', 'Marks Obtained', 'Percentage']]
    
    print(df_top10)
    return df_top10
    

def df_into_excel(df_result,df_grade,df_sbj_report,df_top10):
    with pd.ExcelWriter("kud_result5.xlsx") as writer:
        df_result.to_excel(writer,sheet_name = 'sheet1')
        df_grade.to_excel(writer,sheet_name = 'sheet2')
        df_sbj_report.to_excel(writer,sheet_name = 'sheet3')
        df_top10.to_excel(writer,sheet_name = 'sheet4')

def result_chart(df):
    grade = ['Distinction', 'First Class', 'Second Class', 'Pass Class', 'Fail']
    plot = df.plot.pie(y="Percentage", labels=grade, figsize=(8, 6), startangle=45, 
                        autopct='%0.2f%%',wedgeprops   = { 'linewidth' : 0.5, 'edgecolor' : "black" })
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
                
def result_sheet(register_numbers):
    print ("\nData submitted\nYour results are being fetched...")

    ip = register_numbers
    total_stds = len(ip)

    results = []
    sbj_results = []

    br = get_web_page()
    for i in range(len(ip)):
        soup = get_page_data(br,ip,i)
        results,sbj_results = get_results(soup,results,sbj_results)
    
    results, df1 = result_table(results,ip)
    df2 = grade_table(results,total_stds)
    df3 = each_sbj_result(sbj_results,total_stds)
    df4 = top_10_stds(results)

    df_into_excel(df1,df2,df3,df4)
    print('\nYour results are in the file "kud_result5.xlsx"\n')

    result_chart(df2)


if __name__ == "__main__":
    result_sheet(register_numbers)
