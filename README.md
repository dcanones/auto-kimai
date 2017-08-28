# Introduction

AutoKimai is a tiny Python script that automatically charge project hours in [Kimai Time Tracker](http://www.kimai.org/). Kimai is a free and open source widely used TT.

# Usage

If you want to use AutoKimai, just import the class in autokimai.py and tune it yourself or modify the example.py file and run it. Here is an example script using AutoKimai:

````python
from autokimai import AutoKimai
import datetime

url = 'your_kimai_base_url'
user = 'your_kimai_username'
password = 'your_kimai_password'
project = 'project_name'
task = 'task_name'
holidays = ['06/06/2017',
            '13/04/2017',
            '01/05/2017',
            '15/08/2017',
            '12/10/2017',
            '01/11/2017',
            '08/12/2017',
            '25/12/2017',
            '14/08/2017',
            '28/02/2017',
            '30/05/2017',
            '15/06/2017',
            '18/04/2017',
            '31/05/2017']

bot = AutoKimai(user=user,
                password=password,
                project=project,
                task=task,
                start_date='21/03/2017',
                end_date=datetime.datetime.strftime(datetime.datetime.today(),'%d/%m/%Y'),
                holidays=holidays,
                test=False,
                url='http://145.81.201.195/kimai/')

if __name__ == "__main__":
    bot.run()
````

Parameters you have to specify to the class while instantiating are:

| Parameter | Description | Example |
| ------------- | ------------- | ----- |
| `user`      | Kimai username, a string | `'username'` |
| `password`  | Kimai password, a string | `'password'` |
| `project`   | The project you are going to charge hours. A substring enough specific to generate one single result while filtering | `'PROJECT MAYHEM'` |
| `task` | The task you are going to charge hours. A substring enough specific to generate one single result while filtering the form | `'Recruit new members'` |
| `start_date` | A string representing the date to start charging hours from, formatted as `%d/%m/%Y` | `21/03/2017` |
| `end_date` | A string representing the date to stop charging hours from, formatted as  `%d/%m/%Y` | `26/03/2017` |
| `holidays` | A list of strings (dates formatted as `%d/%m/%Y`) representing holidays. Make sure you includes your days off, national holidays and more | `['06/06/2017', '13/04/2017', '01/05/2017']` |
| `test` | A boolean indicating if you are making tests. If `True`the script will click Cancel button instead of OK, so no real time will be added | `True` |
| `url` | A string representing your base Kimai URL | `http://145.81.201.195/kimai/` | 