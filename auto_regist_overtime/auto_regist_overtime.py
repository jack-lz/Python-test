#coding=utf-8
#!/usr/bin/python
#Filename:auto_regist_overtime.py

import urllib, urllib2
import cookielib
from bs4 import BeautifulSoup
import MySQLdb
import time
from datetime import datetime
import os
import warnings
import xlwt
import getpass
from OpenerCreator import OpenerCreator

#定义地址
login_URL = "http://oa-center/Programs/login/login.aspx"
overtime_URL = "http://oa-center/Programs/KQ/EmployeeRequestOvertime.aspx"


#定义登录所需要用的信息，如用户名、密码等，详见下图，使用urllib进行编码
header = {'Host': 'oa-center',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Connection': 'keep-alive'}




#获取考勤记录
def KaoQinQuery(timeSelect):
    kaoqin_URL = "http://oa-center/Programs/KQ/EmployeeInfoStatistic.aspx"
    kaoqinHTML = myopener.open(kaoqin_URL).read()
    soup = BeautifulSoup(kaoqinHTML)
    __VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
    __EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value'] 

    KaoQin_data = urllib.urlencode({
                    "__EVENTTARGET":"",
                    "__EVENTARGUMENT":"",
                    "__LASTFOCUS":"",
                    "__VIEWSTATE":__VIEWSTATE,
                    "__VIEWSTATEGENERATOR":"D274DF31",
                    "__EVENTVALIDATION":__EVENTVALIDATION,
                    "InfoSelect":"RadioButtonPUNCH_CARD_INFO",
                    "btnSearch":"查询",
                    "TimeSelect":timeSelect})
    request = urllib2.Request(kaoqin_URL, KaoQin_data)              #还可以将headers也添加进去
    kaoqinResp = myopener.open(request).read() #对象调用read()方法，返回的是html页面，也就是有html标签的纯文本 
    return kaoqinResp

# HTML提取出table保存到MYAQL
def HTMLSaveToMySQL(RespHTML, timeSelect):
    # 默认的是utf8(也有可能是gbk，看安装的版本)。
    conn = MySQLdb.connect(host='localhost', user=name, passwd=password, charset="utf8")
    # 建立cursor. 
    cur = conn.cursor()

    try :
        #执行SQL语句，建立数据库，表;
        cur.execute("""create database if not exists KaoQin""" )
        cur.execute("""use KaoQin""" )
        if 'RadioButtonTHIS_MONTH' == timeSelect :
            cur.execute("""show tables""")
            tablelist = cur.fetchall()
            if ('THIS_Month_TABLE',) not in tablelist :
                cur.execute("""create table THIS_Month_TABLE(
                            date DATE primary key,
                            week varchar(20),
                            card_count INT,
                            attendance TIME, 
                            departure TIME,
                            late_min INT,
                            leave_early_min INT, 
                            absenteeism_hour INT,
                            reason varchar(20) NULL
                             )""")
            cur.execute("""truncate table THIS_Month_TABLE""" )
            
        elif 'RadioButtonPREV_MONTH' == timeSelect :
            cur.execute("""show tables""")
            tablelist = cur.fetchall()
            if ('PREV_Month_TABLE',) not in tablelist :
                cur.execute("""create table PREV_Month_TABLE(
                            date DATE primary key,
                            week varchar(20),
                            card_count INT,
                            attendance TIME, 
                            departure TIME,
                            late_min INT,
                            leave_early_min INT, 
                            absenteeism_hour INT,
                            reason varchar(20) NULL
                             )""")
            cur.execute("""truncate table PREV_Month_TABLE""" )
           
        soup = BeautifulSoup(RespHTML)
        print "\n\n===========================================考勤记录=============================================="
        print "%12s | %5s | %8s | %8s | %8s | %10s | %10s | %10s | %10s |"\
            % ("日期", "星期", "刷卡次数", "出勤时间", "离勤时间", "迟到(分钟)", "早退(分钟)", "矿工(小时)", "事由")
        for table in soup.findAll('table'):
            for tr in table.findAll('tr'): 
                if None != tr.find('td') :
                    trlist = []
                    for td in tr.findAll('td'):
                        text = td.text.encode("utf-8")      
                        trlist.append(text.strip("\n"))
                    trtuple = tuple(trlist)
                    print "%10s | %5s | %8s | %8s | %8s | %10s | %10s | %10s | %8s |" % trtuple
                    if 'RadioButtonTHIS_MONTH' == timeSelect :
                        sql = """INSERT INTO THIS_Month_TABLE(
                                date, week, card_count, attendance, 
                                departure, late_min, leave_early_min, 
                                absenteeism_hour, reason) 
                                VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%trtuple
                    elif 'RadioButtonPREV_MONTH' == timeSelect :
                        sql = """INSERT INTO PREV_Month_TABLE(
                                date, week, card_count, attendance, 
                                departure, late_min, leave_early_min, 
                                absenteeism_hour, reason) 
                                VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%trtuple
                                       
                    cur.execute(sql)
                    # 与查询不同的是，执行完delete,insert,update这些语句后必须执行下面的命令才能成功更新数据库
                    conn.commit()
            break
    except Exception as e:
           print e
           conn.rollback()#回滚事务 


    # 一如既往的，用完了之后记得关闭cursor，然后关闭链接
    cur.close()
    conn.close()


def get_day_type(query):
    """  
    @query a single date: string eg."20160404" 
    @return day_type: 0 workday -1 holiday 
    20161001:2 20161002:2 20161003:2 20161004:1  
    """  
    url = 'http://api.goseek.cn/Tools/holiday?date=' + query   
    req = urllib2.Request(url)  
    resp = urllib2.urlopen(req).read() #使用默认的opener去请求
    soup = BeautifulSoup(resp)
    p = soup.find('p')
    day_type = eval(p.text)['data']  # "0"workday, "1"leave, "2"holiday
    if day_type == 0:  
        return 0  
    else:  
        return -1  


# 申请加班
def RegistOverTime(reason, start_date, start_time, end_date, end_time) :
    overtime_URL = "http://oa-center/Programs/KQ/EmployeeRequestOvertime.aspx"

    #添加明细
    overtimeHTML = myopener.open(overtime_URL).read()
    soup = BeautifulSoup(overtimeHTML)
    __VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
    __EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value'] 

    overtime_data = urllib.urlencode({
        "__LASTFOCUS":"",
        "__VIEWSTATE":__VIEWSTATE,
        "__VIEWSTATEGENERATOR":"067ECFDF",
        "__EVENTTARGET":"",
        "__EVENTARGUMENT":"",
        "__EVENTVALIDATION":__EVENTVALIDATION,
        "TextBoxREASON":reason,
        "TextBoxDATE_FROM":start_date,
        "DropDownListTIME_FROM":start_time,
        "TextBoxDATE_TO":end_date,
        "DropDownListTIME_TO":end_time,
        "btnAddLine":"添加明细"})
    request = urllib2.Request(overtime_URL, overtime_data)              #还可以将headers也添加进去
    overtime_Resp = myopener.open(request).read() #对象调用read()方法，返回的是html页面，也就是有html标签的纯文本 


    # 提交申请
    registHTML = myopener.open(overtime_URL).read()
    soup = BeautifulSoup(registHTML)
    __VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
    __EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value'] 

    regist_data = urllib.urlencode({
        "__VIEWSTATE":__VIEWSTATE,
        "__VIEWSTATEGENERATOR":"067ECFDF",
        "__EVENTVALIDATION":__EVENTVALIDATION,
        "TextBoxDATE_FROM":start_date,
        "DropDownListTIME_FROM":start_time,
        "TextBoxDATE_TO":end_date,
        "DropDownListTIME_TO":end_time,
        "btnPost":"提交"})
    request = urllib2.Request(overtime_URL, regist_data)              #还可以将headers也添加进去
    regist_Resp = myopener.open(request).read() #对象调用read()方法，返回的是html页面，也就是有html标签的纯文本 


#从SQL取出数据填写加班申请
def registFromSQL(timeSelect) :
    # 获取已经申请的加班记录
    record = QueryRegistedRecord()
    print "\n\n=================================================已申请记录===================================================="
    print '目前最近一次已申请的加班记录是：%s 的！\n'% record
    last_record = record.replace('-','')
    regist_result = False
    today = datetime.now()

    # excel file set
    global excel_name
    if 'RadioButtonTHIS_MONTH' == timeSelect :
        excel_name = today.strftime('%m') + "月加班申请结果_" + today.strftime('%Y-%m-%d_%H-%M-%S') + ".xls" 
    else:
        if int(today.strftime('%m')) == 1 :
            excel_name = "12" + "月加班申请结果_" + today.strftime('%Y-%m-%d_%H-%M-%S') + ".xls" 
        else :
            excel_name = str(int(today.strftime('%m'))-1) + "月加班申请结果_" + today.strftime('%Y-%m-%d_%H-%M-%S') + ".xls"         
    style_title = xlwt.easyxf('font: name Times New Roman, bold on',num_format_str='#,##0.00')
    style_context = xlwt.easyxf('font: name Times New Roman',num_format_str='#,##0.00')
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('加班申请记录')
    title = ("序号", "起始日期", "终止日期", "起始时间", "终止时间", "加班事由")

    for i in range(6) :      
       ws.write(0, i, title[i])

    conn = MySQLdb.connect(host='localhost', user=name, passwd=password,charset="utf8")
    # 建立cursor. 
    cur = conn.cursor()
    try :
        cur.execute("""use KaoQin""" )
        print "\n================================================本次申请记录==================================================="
        if 'RadioButtonTHIS_MONTH' == timeSelect :
            cur.execute("""select * from THIS_Month_TABLE""");
            kaoQinTable = cur.fetchall()
            num = 1
            for row in kaoQinTable :
                date = row[0].strftime('%Y%m%d')
                if date == today.strftime('%Y%m%d') :  # 去掉今天的
                    continue
                if (str(row[3]) == "0:00:00") and (str(row[4]) == "0:00:00"):
                    continue  
                dayType = get_day_type(date)    # 0 workday -1 holiday
                if 0 == dayType : 
                    iTime = int(str(row[4]).replace(':', '')) 
                    if (iTime > 184500) or (iTime <= 53000) :                     
                        if int(date) <= int(last_record) :   # 去掉已经申请的
                            print '=== %s 申请记录已经存在！无需再申请！'% date 
                            continue

                        reason = QueryOvertimeReason(row[0])
                        start_date = row[0].strftime('%Y-%m-%d')
                        end_date = row[0].strftime('%Y-%m-%d')
                        start_time = "18:30"
                        end_time = Rounding_leave(str(row[4]))
                        regist_response = Registovertime(reason, start_date, start_time, end_date, end_time)

                        submit_reason = regist_response.find(id = 'Table_LEAVE_TYPE').find('tr').find('input')['value'].strip("\n").encode('utf-8')
                        submit_timelist = regist_response.find(id = 'Table_3').find(id = 'GridViewLINE').findAll('tr')[1].findAll('td')
                        submit_startDate = submit_timelist[0].text.encode('utf-8').strip("\n")
                        submit_endDate = submit_timelist[1].text.encode('utf-8').strip("\n")
                        submit_startTime = submit_timelist[2].text.encode('utf-8').strip("\n")
                        submit_endTime = submit_timelist[3].text.encode('utf-8').strip("\n")
                        submit_tuple = (num, submit_startDate, submit_endDate, submit_startTime ,submit_endTime, submit_reason)
                        print "%2d、起始日期:%5s  终止日期:%5s  起始时间:%5s  终止时间:%5s  加班事由:%s"%submit_tuple               
                        for i in range(6) :
                            ws.write(num, i, submit_tuple[i])
                        num += 1
                    elif iTime > 053000 and iTime < 90000 : 
                        raw_input("""存在一个超过5点30的通宵加班！请自己向公司申请！\n
                                     请点击任意建继续:""")
                else :
                    come_time = int(str(row[3]).replace(':', '')) 
                    leave_time = int(str(row[4]).replace(':', '')) 
                    if (come_time >= 90000) :
                        if (leave_time >= 90000) or (leave_time <= 53000) :                          
                            if int(date) <= int(last_record) :   # 去掉已经申请的
                                print '=== %s 申请记录已经存在！无需再申请！'% date 
                                continue

                            reason = QueryOvertimeReason(row[0])
                            start_date = row[0].strftime('%Y-%m-%d')
                            end_date = row[0].strftime('%Y-%m-%d')
                            start_time = Rounding_come(str(row[3]))
                            end_time = Rounding_leave(str(row[4]))
                            regist_response = Registovertime(reason, start_date, start_time, end_date, end_time)
                        
                            submit_reason = regist_response.find(id = 'Table_LEAVE_TYPE').find('tr').find('input')['value'].strip("\n").encode('utf-8')
                            submit_timelist = regist_response.find(id = 'Table_3').find(id = 'GridViewLINE').findAll('tr')[1].findAll('td')
                            submit_startDate = submit_timelist[0].text.encode('utf-8').strip("\n")
                            submit_endDate = submit_timelist[1].text.encode('utf-8').strip("\n")
                            submit_startTime = submit_timelist[2].text.encode('utf-8').strip("\n")
                            submit_endTime = submit_timelist[3].text.encode('utf-8').strip("\n")
                            submit_tuple = (num, submit_startDate, submit_endDate, submit_startTime ,submit_endTime, submit_reason)
                            print "%2d、起始日期:%5s  终止日期:%5s  起始时间:%5s  终止时间:%5s  加班事由:%s"%submit_tuple               
                            for i in range(6) :
                                ws.write(num, i, submit_tuple[i])
                            num += 1
                        elif leave_time > 053000 and leave_time < 90000 : 
                            raw_input("""存在一个超过5点30的通宵加班！请自己向公司申请！\n
                                     请点击任意建继续:""")                     
        elif 'RadioButtonPREV_MONTH' == timeSelect :
            cur.execute("select * from PREV_Month_TABLE");
            kaoQinTable = cur.fetchall()
            num = 1
            for row in kaoQinTable :
                date = row[0].strftime('%Y%m%d')
                if date == today.strftime('%Y%m%d') :  # 去掉今天的
                    continue
                if (str(row[3]) == "0:00:00") and (str(row[4]) == "0:00:00"):
                    continue
                dayType = get_day_type(date)    # 0 workday -1 holiday
                if 0 == dayType :   
                    iTime = int(str(row[4]).replace(':', '')) 
                    if (iTime > 184500) or (iTime <= 53000) : 
                        if int(date) <= int(last_record) :   # 去掉已经申请的
                            print '=== %s 申请记录已经存在！无需再申请！' % date
                            continue

                        reason = QueryOvertimeReason(row[0])
                        start_date = row[0].strftime('%Y-%m-%d')
                        end_date = row[0].strftime('%Y-%m-%d')
                        start_time = "18:30"
                        end_time = Rounding_leave(str(row[4]))   
                        regist_response = Registovertime(reason, start_date, start_time, end_date, end_time)
                        
                        submit_reason = regist_response.find(id = 'Table_LEAVE_TYPE').find('tr').find('input')['value'].strip("\n").encode('utf-8')
                        submit_timelist = regist_response.find(id = 'Table_3').find(id = 'GridViewLINE').findAll('tr')[1].findAll('td')
                        submit_startDate = submit_timelist[0].text.encode('utf-8').strip("\n")
                        submit_endDate = submit_timelist[1].text.encode('utf-8').strip("\n")
                        submit_startTime = submit_timelist[2].text.encode('utf-8').strip("\n")
                        submit_endTime = submit_timelist[3].text.encode('utf-8').strip("\n")
                        submit_tuple = (num, submit_startDate, submit_endDate, submit_startTime ,submit_endTime, submit_reason)
                        print "%d、起始日期:%5s  终止日期:%5s  起始时间:%5s  终止时间:%5s  加班事由:%s"%submit_tuple               
                        for i in range(6) :
                            ws.write(num, i, submit_tuple[i])
                        num += 1
                    elif iTime > 053000 and iTime < 90000 : 
                        raw_input("""存在一个超过5点30的通宵加班！请自己向公司申请！\n
                                     请点击任意建继续:""")
                else :
                    come_time = int(str(row[3]).replace(':', '')) 
                    leave_time = int(str(row[4]).replace(':', '')) 
                    if (come_time >= 90000) :
                        if (leave_time >= 90000) or (leave_time <= 53000) :
                            if int(date) <= int(last_record) :   # 去掉已经申请的
                                print '=== %s 申请记录已经存在！无需再申请！' % date
                                continue
                            reason = QueryOvertimeReason(row[0])
                            start_date = row[0].strftime('%Y-%m-%d')
                            end_date = row[0].strftime('%Y-%m-%d')
                            start_time = Rounding_come(str(row[3]))
                            end_time = Rounding_leave(str(row[4]))
                            regist_response = Registovertime(reason, start_date, start_time, end_date, end_time)
                        
                            submit_reason = regist_response.find(id = 'Table_LEAVE_TYPE').find('tr').find('input')['value'].strip("\n").encode('utf-8')
                            submit_timelist = regist_response.find(id = 'Table_3').find(id = 'GridViewLINE').findAll('tr')[1].findAll('td')
                            submit_startDate = submit_timelist[0].text.encode('utf-8').strip("\n")
                            submit_endDate = submit_timelist[1].text.encode('utf-8').strip("\n")
                            submit_startTime = submit_timelist[2].text.encode('utf-8').strip("\n")
                            submit_endTime = submit_timelist[3].text.encode('utf-8').strip("\n")
                            submit_tuple = (num, submit_startDate, submit_endDate, submit_startTime ,submit_endTime, submit_reason)
                            print "%d、起始日期:%5s  终止日期:%5s  起始时间:%5s  终止时间:%5s  加班事由:%s"%submit_tuple               
                            for i in range(6) :
                                ws.write(num, i, submit_tuple[i])
                            num += 1
                        elif leave_time > 053000 and leave_time < 90000 : 
                            raw_input("""存在一个超过5点30的通宵加班！请自己向公司申请！\n
                                     请点击任意建继续:""") 
        wb.save(excel_name)
        regist_result = True
    except Exception as e:
        print e
        conn.rollback()#回滚事务 

    # 一如既往的，用完了之后记得关闭cursor，然后关闭链接
    cur.close()
    conn.close()
    return regist_result        


def Rounding_leave(time) :
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])
    if minute > 0 and minute <= 30 :
        minute = 30
    elif minute >30 :
        minute = 0
        hour +=1
        
    end_time = "%(hour)02d:%(minute)02d" % {'hour':hour, 'minute':minute}
    return end_time

def Rounding_come(time) :
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])
    if minute > 0 and minute <= 30 :
        minute = 0
    elif minute >30 :
        minute = 30
    come_time = "%(hour)02d:%(minute)02d" % {'hour':hour, 'minute':minute}
    return come_time

def QueryOvertimeReason(date):
    # taskNote_showURL = "http://172.26.181.54/showcalendar.asp"
    # taskNote_finishURL = "http://172.26.181.54/showfinishstatus.asp"
    # taskNote_data = urllib.urlencode({
    #     "startDay":date})
    # myopener2 = urllib2.build_opener()
    # urllib2.install_opener
    # show_request = urllib2.Request(taskNote_showURL, taskNote_data)
    # show_response = myopener2.open(show_request).read()
    # sliptStr = show_response.split('刘振</FONT>')[-1].split('刘虎</FONT>')[0]
    # show_soup = BeautifulSoup(sliptStr)
    # alist = show_soup.findAll('a')
    # if alist :
    #     return alist[0].text.encode('utf-8')
    # else :
    #     input_reason = raw_input("没有找到%s的加班事由，请现在补充超过三个字的加班理由:"%date)
    #     while True :
    #         if len(input_reason) >= 10:
    #             break
    #         else :
    #             input_reason = raw_input("输入长度少于三，请重新输入:")
    #     return input_reason
    input_reason = "17Cy_NZ問題総点検検討_TSL_Gbook_Bug" #raw_input("没有找到%s的加班事由，请现在补充超过三个字的加班理由:"%date)
    while True :
        if len(input_reason) >= 10:
            break
        else :
            input_reason = raw_input("输入长度少于三，请重新输入:")
    time.sleep(2)
    return input_reason


def QueryRegistedRecord():
    Record_URL = 'http://oa-center/Programs/KQ/EmployeeRequestOvertime.aspx'
    soup = BeautifulSoup(myopener.open(Record_URL).read())
    __VIEWSTATE = soup.find(id = "__VIEWSTATE")['value']
    __EVENTVALIDATION = soup.find(id = "__EVENTVALIDATION")['value'] 

    record_data1 = urllib.urlencode({
        "__VIEWSTATE":__VIEWSTATE,
        "__VIEWSTATEGENERATOR":"067ECFDF",
        "__EVENTVALIDATION":__EVENTVALIDATION,
        "TextBoxREASON":"",
        "btnQuery":"记录查找",
        "TextBoxDATE_FROM":"2017-08-01",
        "DropDownListTIME_FROM":"18:30",
        "TextBoxDATE_TO":"2017-09-30",
        "DropDownListTIME_TO":"20:00"})
    soup1 = BeautifulSoup(myopener.open(Record_URL, record_data1).read())
    __VIEWSTATE1 = soup1.find(id = "__VIEWSTATE")['value']
    __EVENTVALIDATION1 = soup1.find(id = "__EVENTVALIDATION")['value'] 

    Record_data2 = urllib.urlencode({
        "__LASTFOCUS":"",
        "__VIEWSTATE":__VIEWSTATE1,
        "__VIEWSTATEGENERATOR":"067ECFDF",
        "__EVENTTARGET":"",
        "__EVENTARGUMENT":"",
        "__EVENTVALIDATION":__EVENTVALIDATION1,
        "TextBoxMANAGE_ID_SEARCH":"",
        "RecordSelect":"RadioButtonALL",
        "TextBoxDATE_FROM_SEARCH":"",
        "TextBoxDATE_TO_SEARCH":"",
        "TextBoxREASON":"",
        "btnQuery":"记录查找"
        })
    Record_soup2 = BeautifulSoup(myopener.open(Record_URL, Record_data2).read())
    return Record_soup2.findAll('table')[-1].findAll('td')[1].text.encode('utf-8').replace("\n", '')




def Registovertime(reason, start_date, start_time, end_date, end_time) :
    regist_URL = "http://oa-center/Programs/KQ/EmployeeRequestOvertime.aspx"
    soup = BeautifulSoup(myopener.open(regist_URL).read())
    __VIEWSTATE = soup.find(id = "__VIEWSTATE")['value']
    __EVENTVALIDATION = soup.find(id = "__EVENTVALIDATION")['value'] 

    detail_data = urllib.urlencode({
        "__VIEWSTATE":__VIEWSTATE,
        "__VIEWSTATEGENERATOR":"067ECFDF",
        "__EVENTVALIDATION":__EVENTVALIDATION,
        "TextBoxREASON":reason,
        "TextBoxDATE_FROM":start_date,
        "DropDownListTIME_FROM":start_time,
        "TextBoxDATE_TO":end_date,
        "DropDownListTIME_TO":end_time,
        "btnAddLine":"添加明细"})
    detail_soup = BeautifulSoup(myopener.open(regist_URL, detail_data).read())
    __VIEWSTATE = detail_soup.find(id = "__VIEWSTATE")['value']
    __EVENTVALIDATION = detail_soup.find(id = "__EVENTVALIDATION")['value'] 

    submit_data = urllib.urlencode({
        "__VIEWSTATE":__VIEWSTATE,
        "__VIEWSTATEGENERATOR":"067ECFDF",
        "__EVENTVALIDATION":__EVENTVALIDATION,
        "TextBoxDATE_FROM":start_date,
        "DropDownListTIME_FROM":start_time,
        "TextBoxDATE_TO":end_date,
        "DropDownListTIME_TO":end_time,
        "btnPost":"提交"})
    submit_resp = myopener.open(regist_URL, submit_data).read()
    submit_soup = BeautifulSoup(submit_resp)
    return submit_soup

warnings.filterwarnings('ignore') #忽略warnings

#获取myopener
MyopenerCreator = OpenerCreator(header)
myopener = MyopenerCreator.MakeMyOpener()
loginPageHTML = myopener.open(login_URL).read()   #为了获取到__VIEWSTATE 和 __EVENTVALIDATION先访问该地址一次
soup = BeautifulSoup(loginPageHTML)    
__VIEWSTATE = soup.find(id="__VIEWSTATE")['value'] 
__EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value'] 

while True :
    print "\n=================================================系统登录======================================================"
    login_username = raw_input("请输入您的工号：")
    login_password = getpass.getpass("请输入OA系统的密码：")


    login_data = urllib.urlencode({
                '__VIEWSTATE': __VIEWSTATE,
                '__VIEWSTATEGENERATOR': 'e19c8057',
                '__EVENTVALIDATION': __EVENTVALIDATION,
                'tbUserName': login_username,
                'tbPassword': login_password,
                'btnLogin': '确定'})
    response = myopener.open(login_URL,login_data).read() #此处的open方法同urllib2的urlopen方法，也可以传入request
    loginSoup = BeautifulSoup(response)

    if None == loginSoup.find('table'):
        break
    else :
        print '登录失败!'


print "\n\n=================================================数据库登录===================================================="
print("请确保你启动了本地Mysql数据库管理软件!")
name = raw_input("请输入数据库登录名：")
password = getpass.getpass("请输入数据库登录密码：")


#选择功能
while True :
    fun_select = raw_input("""
\n==================================================功能选择=====================================================
0: 退出程序
1: 本月加班申请
2：上月加班申请

选择你需要执行的操作: """)
    if '' != fun_select:
        break 

if 0 == int(fun_select):
    os._exit(0)
elif 1 == int(fun_select) :
    kaoqinRespHTML = KaoQinQuery('RadioButtonTHIS_MONTH')
    HTMLSaveToMySQL(kaoqinRespHTML, 'RadioButtonTHIS_MONTH')
    registResult = registFromSQL('RadioButtonTHIS_MONTH')
    if registResult :
        print "\n\n==================================================处理完成====================================================="
        print "本次申请详细记录保存当前目录，文件名为：%s\n\n" % excel_name
    else:
        print "执行过程中出现错误或该日期已经不能申请加班，请查询！"
elif 2 == int(fun_select) :
    kaoqinRespHTML = KaoQinQuery('RadioButtonPREV_MONTH')
    HTMLSaveToMySQL(kaoqinRespHTML, 'RadioButtonPREV_MONTH')
    registResult =  registFromSQL('RadioButtonPREV_MONTH') 
    if registResult :
        print "\n\n==================================================处理完成====================================================="
        print "本次申请详细记录保存在当前目录，文件名为：%s\n\n" % excel_name
    else:
        print "执行过程中出现错误或该日期已经不能申请加班，请查询！"
else :
    print '功能选择错误，请重新启动!'
    os._exit()














