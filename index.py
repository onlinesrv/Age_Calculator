import urllib.request as urllib2
from PyQt5.QtWidgets import QMessageBox,QMainWindow
import sys,requests
from PyQt5.uic import loadUiType , loadUi
from PyQt5 import QtWidgets 
from PyQt5.QtCore import QTime,QDate, QTimer,QUrl
from datetime import datetime
from bs4 import BeautifulSoup as bs
from PyQt5.QtGui import QDesktopServices


from main import Ui_MainWindow




class MainApp(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.culc_btn.clicked.connect(self.chek_inputs)
        self.exit_btn.clicked.connect(self.close_me)
        self.add_time.stateChanged.connect(self.chek_time)
        self.contactus.clicked.connect(self.open_link)

        self.birthday.setInputMask("99-99-9999")
        self.birthtime.setInputMask("99:99")

    

    
    def uodate_age(self):
        
        
        self.m_sec = int(self.age_i_s.text())
        self.m_min = int(self.age_i_m.text())
        self.m_hour = int(self.age_i_h.text())
        self.m_day = int(self.age_i_d.text())
        self.m_month = int(self.age_i_mo.text())
        self.m_year = int(self.age_i_y.text())
      
       
        tt = QTimer(self)
        tt.timeout.connect(self.contunu_number)
        tt.start(1000)

    def contunu_number(self):
        self.m_sec +=1
        self.age_i_s.setText(str(self.m_sec))
        self.age_s.setText(str(int(self.age_s.text()) + 1))

        if self.m_sec >= 59:
            self.m_sec = 0
            self.m_min +=1
            self.age_i_m. setText(str(self.m_min))
            self.age_m.setText(str(int(self.age_m.text()) + 1))
            

           
            if self.m_min >= 59:
                self.m_min = 0
                self.m_hour +=1
                self.age_i_h. setText(str(self.m_hour))
                self.age_h.setText(str(int(self.age_h.text()) + 1))

                if self.m_hour >= 23:
                    self.m_hour = 0
                    self.m_day +=1
                    self.age_i_d.setText(str(self.m_day))
                    self.age_d.setText(str(int(self.age_d.text()) + 1))
                   
                    if self.m_day >= 29:
                        self.m_day = 0
                        self.m_month +=1
                        self.age_i_mo.setText(str(self.m_month))
                        self.age_m2.setText(str(int(self.age_m2.text()) + 1))
                        
                        if self.m_month >= 11:
                            self.m_month = 0
                            self.m_year +=1
                            self.age_i_y.setText(str(self.m_year))
                            self.age_y.setText(str(int(self.age_y.text()) + 1))










    


        


   



    def chek_inputs(self):
        if len(self.birthday.text()) != len(self.birthday.inputMask()):
            QMessageBox.warning(self,"خطـأ","الرجاء إدخال  تاريخ الميلاد بالكامل")
        else:
            self.birth_date_dd = int((self.birthday.text().split('-'))[0])
            self.birth_date_mm = int((self.birthday.text().split('-'))[1])
            self.birth_date_yy = int((self.birthday.text().split('-'))[2])
            if self.birth_date_dd > 31 or self.birth_date_mm > 12 or self.birth_date_yy > 2023 or self.birth_date_dd < 1 or self.birth_date_mm < 1 or self.birth_date_yy < 1:
                QMessageBox.warning(self,"خطـأ","الرجاء إدخال  تاريخ الميلاد صحيح")
            else:
                if self.birthtime.isEnabled():
                    if len(self.birthtime.text()) != len(self.birthtime.inputMask()):
                        QMessageBox.warning(self,"خطـأ","الرجاء إدخال  وقت الميلاد بالكامل")
                    else: 
                        self.birth_time_hh = int((self.birthtime.text().split(':'))[0])
                        self.birth_time_mm = int((self.birthtime.text().split(':'))[1])
                        self.birth_time_ss = 0
                        if self.birth_time_hh > 23 or self.birth_time_mm > 59 : 
                            QMessageBox.warning(self,"خطـأ","الرجاء إدخال  وقت الميلاد صحيح")
                        else:
                            
                            birth_day = self.birthday.text()
                            birth_time = f"{self.birthtime.text()}:00"
                            age = self.calculate_age(birth_day,birth_time)
                            self.show_age(age)
                            
                else:
                    self.birthtime.setText("00:00")
                    self.birth_time_hh = 0
                    self.birth_time_mm = 0
                    self.birth_time_ss = 0

                    birth_day = self.birthday.text()
                    birth_time = f"{self.birthtime.text()}:00"
                    age = self.calculate_age(birth_day,birth_time)
                    self.show_age(age)

                    


    




    def calculate_age(self,birth_date, birth_time):

        
        # Parse the birth date and time
        birth_datetime = datetime.strptime(birth_date + " " + birth_time, "%d-%m-%Y %H:%M:%S")


        # Get the current date and time
        current_date,current_time = self.get_date_time_now()
        
        self.current_datetime = datetime.strptime(current_date + " " + current_time, "%d-%m-%Y %H:%M:%S")
      




        # Calculate the difference between the two dates
        age_timedelta = self.current_datetime - birth_datetime

        # Extract the age components
        years = age_timedelta.days // 365
        months = (age_timedelta.days % 365) // 30
        days = (age_timedelta.days % 365) % 30
        hours = age_timedelta.seconds // 3600
        minutes = (age_timedelta.seconds % 3600) // 60
        seconds = (age_timedelta.seconds % 3600) % 60

        # Convert the age to years
        age_years = age_timedelta.days // 365

        # Convert the age to months
        age_months = age_years * 12

        # Convert the age to weeks
        age_weeks = age_timedelta.days // 7

        # Convert the age to days
        age_days = age_timedelta.days


        # Convert the age to hours
        age_hours = int(age_timedelta.total_seconds() // 3600)

        # Convert the age to minutes
        age_minutes = int(age_timedelta.total_seconds() // 60)

        # Convert the age to seconds
        age_seconds = int(age_timedelta.total_seconds())

        self.age = {
        "years": years,
        "months": months,
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "age_years": age_years,
        "age_months": age_months,
        "age_weeks": age_weeks,
        "age_days": age_days,
        "age_hours": age_hours,
        "age_minutes": age_minutes,
        "age_seconds": age_seconds
        
       }
        
       
        return self.age
    

    def show_age(self,age):


        self.age_i_y.setText(str(age["years"]))
        self.age_i_mo.setText(str(age["months"]))
        self.age_i_d.setText(str(age["days"]))
        self.age_i_h.setText(str(age["hours"]))
        self.age_i_m.setText(str(age["minutes"]))
        self.age_i_s.setText(str(age["seconds"]))
        self.age_y.setText(str(age["age_years"])) 
        self.age_m2.setText(str(age["age_months"])) 
        self.age_d.setText(str(age["age_days"])) 
        self.age_h.setText(str(age["age_hours"])) 
        self.age_m.setText(str(age["age_minutes"])) 
        self.age_s.setText(str(age["age_seconds"])) 



        self.uodate_age()
       
    
    def get_age_soconds(self):
        yy=int(self.age_i_y.text())
        mo=int(self.age_i_mo.text())
        dd=int(self.age_i_d.text())
        hh=int(self.age_i_h.text())
        mm=int(self.age_i_m.text())
        ss=int(self.age_i_s.text())
        total_ss = ss + (mm *60) + (hh*3600) +(dd*86400) +(mo*2629746) +(yy*31556952)
        print(total_ss)



        

        



    def get_date_time_now(self):
        #get current date and time 
        conn = self.test_connection()
        if conn:
            self.comment.setText(' يتم الإعتماد على الوقت الخاص بمنطقتكم عن على الأنترنت')
            date,time = self.get_date_time_online()

            
        else:
            self.comment.setText('يتم الإعتماد على الوقت في الجهاز')
            date,time = self.get_date_time_offline()
        

        return(date,time)
    
    def chek_time(self,state):
        if state == 2:
            self.birthtime.setEnabled(True)
        else:
            self.birthtime.setEnabled(False)

    def test_connection(self):
        try:
            urllib2.urlopen('https://www.google.com/',timeout=1)
            return True
        except urllib2.URLError as err:
        
            return False
    
    def get_date_time_online(self):
        #DATE
        r1 = requests.get('https://www.calendardate.com/todays.htm')
        soup = bs(r1.text,'html.parser')
        today = soup.find_all(id="tprg")[6].getText().strip()#.replace(' ','').replace('-','')
        parsed_date = datetime.strptime(today, "%Y-%m-%d")
        n_today = parsed_date.strftime("%d-%m-%Y")
        
        #TIME
        r2 = requests.get('https://www.thetimenow.com')
        soup = bs(r2.text,'html.parser')
       
        time = (soup.find(id="main_time").text).strip()

        return(n_today,time)

    def get_date_time_offline(self):
        #DATE
        today  = QDate.currentDate().toString("dd-MM-yyyy")
        of_n_year = int(((today.split('-'))[0]).strip())
        of_n_month = int(((today.split('-'))[1]).strip())
        of_n_day = int(((today.split('-'))[2]).strip())

        #TIME
        now_time = QTime.currentTime().toString("HH:mm:ss")
        of_n_hh = now_time.split(":")[0]
        of_n_mm =now_time.split(":")[1]
        of_n_ss = now_time.split(":")[2]

        return(today,now_time)

    def close_me(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("هل تريد الخروج من البرنامج؟")
        msg.setWindowTitle(" تأكيد الخروج")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # change the button texts to "OK" and "Cancel"
        msg.button(QMessageBox.Yes).setText("نعم")
        msg.button(QMessageBox.No).setText("لا")
        msg.setDefaultButton(QMessageBox.No)
        response = msg.exec_()
        if response == QMessageBox.Yes:
            self.close()
            


    def open_link(self):
        QDesktopServices.openUrl(QUrl("https://www.facebook.com/pythonprog"))















app = QtWidgets.QApplication(sys.argv)
mainWindow = MainApp()
mainWindow.show()
sys.exit(app.exec())
