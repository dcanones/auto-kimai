from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import platform
import time

class AutoKimai():

    login_url = 'index.php?a=logout'
    if platform.system() == 'Linux':
        driver = webdriver.Chrome(executable_path='drivers/chromedriver')
    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    else:
        raise OSError('Can not detect a valid operating system')
    driver.implicitly_wait(10)

    def __init__(self,
                 user,
                 password,
                 url,
                 start_date=None,
                 end_date=None,
                 project=None,
                 task=None,
                 holidays = [],
                 test=True):

        self.user = user
        self.password = password
        self.start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
        self.end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y')
        self.project = project
        self.task = task
        self.holidays = []
        for date in holidays:
            self.holidays.append(datetime.datetime.strptime(date, '%d/%m/%Y'))
        self.test = test
        self.base_url = url

    def login(self):
        self.driver.get(self.base_url + self.login_url)
        user_elem = self.driver.find_element_by_name('name')
        user_elem.send_keys(self.user)
        password_elem = self.driver.find_element_by_name('password')
        password_elem.send_keys(self.password)
        login_elem = self.driver.find_element_by_tag_name('button')
        login_elem.send_keys(Keys.RETURN)

    def add_entry(self, date_day):
        add_elem = self.driver.find_element_by_xpath('//*[@id="zef_head"]/div/a')
        add_elem.click()
        time.sleep(1.5)
        project_form = self.driver.find_element_by_id('add_edit_zef_pct_ID')
        for option in project_form.find_elements_by_tag_name('option'):
            if self.project in option.text:
                option.click()
        time.sleep(1.5)
        task_form = self.driver.find_element_by_id('add_edit_zef_evt_ID')
        for option in task_form.find_elements_by_tag_name('option'):
            if self.task in option.text:
                option.click()
        day_start = self.driver.find_element_by_id('edit_in_day')
        day_end = self.driver.find_element_by_id('edit_out_day')
        string_date = date_day.strftime('%d.%m.%Y')
        time.sleep(1)
        day_start.click()
        day_start.send_keys(Keys.ESCAPE)
        day_start.send_keys(string_date)
        day_start.send_keys(Keys.TAB)
        day_end.send_keys(Keys.ESCAPE)
        day_end.send_keys(string_date)
        time_start = self.driver.find_element_by_id('edit_in_time')
        time_end = self.driver.find_element_by_id('edit_out_time')
        time.sleep(.5)
        time_start.click()
        time_start.send_keys('09:00')
        time_start.send_keys(Keys.TAB)
        time_end.send_keys('17:00')
        if self.test:
            ok = self.driver.find_element_by_xpath('//*[@id="formbuttons"]/input[1]')
        else:
            ok = self.driver.find_element_by_xpath('//*[@id="formbuttons"]/input[2]')
        ok.click()

    def run(self):
        date = self.start_date
        self.login()
        while date < self.end_date:
            if date.weekday() not in [5, 6] and date not in self.holidays:
                self.add_entry(date)
            date += datetime.timedelta(days=1)
        self.driver.close()
