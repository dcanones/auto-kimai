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
                url='http://199.86.204.152/kimai/')

if __name__ == "__main__":
    bot.run()