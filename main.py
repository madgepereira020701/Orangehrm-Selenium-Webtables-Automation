from driver_setup import driver 
import methods as m 
import time

# 1. Visit https://opensource-demo.orangehrmlive.com/
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
driver.get(url)
driver.maximize_window()
time.sleep(5)

# 2. Log in using the following credentials: Username: Admin Password: admin123
# 3. Verify that login is successful by checking the Dashboard page is displayed
creds = {'username':'Admin','password':'admin123'}
m.login(creds)
time.sleep(5)