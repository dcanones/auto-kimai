from autokimai import AutoKimai
import datetime

url = 'your_kimai_base_url'
user = 'your_user'
password = 'your_password'
project = 'your_project'
task = 'your_task'
holidays = ['06/06/2017',
            '13/04/2017',
            '01/05/2017',
            '15/08/2017',
            '12/10/2017',
            '01/11/2017',
            '08/12/2017',
            '25/12/2017',
            '30/05/2017',
            '15/06/2017',
            '18/04/2017',
            '31/05/2017']

bot = AutoKimai(user=user,
                password=password,
                project=project,
                task=task,
                start_date='25/08/2017',
                end_date='26/08/2017',
                holidays=holidays,
                test=False,
                url='http://199.99.999.199/kimai/')

if __name__ == "__main__":
    bot.run()
