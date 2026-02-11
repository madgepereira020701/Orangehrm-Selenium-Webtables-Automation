from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException
import time 

from datetime import datetime 
from driver_setup import driver 
wait = WebDriverWait(driver,10)


navbar = {'home':(By.CSS_SELECTOR,'#navbarExample > ul > li.nav-item.active > a'),
'contact':(By.CSS_SELECTOR, '#navbarExample > ul > li:nth-child(2) > a'),
'about us':(By.CSS_SELECTOR, '#navbarExample > ul > li:nth-child(3) > a'),
'cart':(By.ID,'cartur'),
'login':(By.ID,'login2'),
'sign up':(By.ID,'signin2')}
    

def register(creds):
    reg_user_loc = (By.ID,'sign-username')
    reg_pswd_loc = (By.ID,'sign-password')
    reg_submit_loc = (By.CSS_SELECTOR,'#signInModal > div > div > div.modal-footer > button.btn.btn-primary')

    wait.until(EC.element_to_be_clickable(navbar['sign up'])).click()
    username = wait.until(EC.visibility_of_element_located(reg_user_loc))
    username.clear()
    username.send_keys(creds['username'])
    password = wait.until(EC.visibility_of_element_located(reg_pswd_loc))
    password.clear()
    password.send_keys(creds['password'])

    register_btn = wait.until(EC.element_to_be_clickable(reg_submit_loc))
    register_btn.click()
    alert = wait.until(EC.alert_is_present())
    alertMsg =  alert.text
    alert.accept()
    if alertMsg == 'This user already exist.':
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#signInModal > div > div > div.modal-footer > button.btn.btn-secondary'))).click()
    login(creds)


def login(creds):
    log_user_loc = (By.ID,'loginusername')
    log_pswd_loc = (By.ID,'loginpassword')
    log_submit_loc = (By.CSS_SELECTOR,'#logInModal > div > div > div.modal-footer > button.btn.btn-primary')

    wait.until(EC.element_to_be_clickable(navbar['login'])).click()
    username = wait.until(EC.visibility_of_element_located(log_user_loc))
    username.clear()
    username.send_keys(creds['username'])
    password = wait.until(EC.visibility_of_element_located(log_pswd_loc))
    password.clear()
    password.send_keys(creds['password'])

    login_btn = wait.until(EC.element_to_be_clickable(log_submit_loc))
    login_btn.click()

def prodDesc():
    moreInfoID = (By.ID,'more-information')
    descXPATH = (By.XPATH,"//*[@id='more-information']/p")
    wait.until(EC.presence_of_element_located(moreInfoID))
    productDesc = wait.until(EC.presence_of_element_located((descXPATH)))
    productDesc = productDesc.text.strip()
    return productDesc
    # WebDriverWait(driver,2).until(
    # EC.presence_of_element_located((By.ID, "more-information")))
    # product_desc=driver.find_element(By.XPATH,"//*[@id='more-information']/p")
    # product_desc=product_desc.text.strip()
    # print("product desc ",product_desc)
    

def addToCart(prodCat, prodName, descFlag=0):
    prodCategories = {
        'Laptops':(By.LINK_TEXT,'Laptops'),
        'Monitors':(By.LINK_TEXT,'Monitors')
    }

    prodNames = {
        'Sony vaio i5':(By.LINK_TEXT,'Sony vaio i5'),
        'ASUS Full HD':(By.LINK_TEXT,'ASUS Full HD'),
        'MacBook Pro':(By.LINK_TEXT,'MacBook Pro'),
        'Dell i7 8gb':(By.LINK_TEXT,'Dell i7 8gb')
    }

    addToCartButton = (By.CSS_SELECTOR,'#tbodyid > div.row > div > a')
    nextButton = (By.ID,'next2')

    # Click cart > category
    wait.until(EC.visibility_of_element_located(navbar['home'])).click()
    wait.until(EC.visibility_of_element_located(prodCategories[prodCat])).click()
    
    while True:
        try:
            # Click product > addtocart > alertaccept
            wait.until(EC.visibility_of_element_located(prodNames[prodName])).click()
            try:
                try:
                    if(descFlag == 1):
                        print(f'Product Description: {prodDesc()}')
                except Exception as e:
                    print('product desc error ',e)
                wait.until(EC.visibility_of_element_located(addToCartButton)).click()
                alert = wait.until(EC.alert_is_present())
                alert.accept()
                break
            except Exception as e:
                print('Product found, error is',e)
        
        except TimeoutException:
            try:
                # Click next
                wait.until(EC.visibility_of_element_located(nextButton)).click()
            except TimeoutException:
                # product not found since next button cannot be found
                print("product not found")
                break

def checkCartRows():
    # # click cart 
    wait.until(EC.element_to_be_clickable(navbar['cart'])).click()
    time.sleep(3) # added due to timeoutexception being raised for the above statement 
    cartTable = driver.find_elements(By.CSS_SELECTOR, "tbody#tbodyid tr.success")
    return len(cartTable)


def purchaseFromCart(purchaseValues):
    placeOrderButton = (By.CSS_SELECTOR,'#page-wrapper > div > div.col-lg-1 > button')
    purchaseFields = {
        'name': (By.ID, 'name'),
        'country': (By.ID, 'country'),
        'city': (By.ID, 'city'),
        'card': (By.ID, 'card'),
        'month': (By.ID, 'month'),
        'year': (By.ID, 'year')
    }
    purchaseButton = (By.CSS_SELECTOR,'#orderModal > div > div > div.modal-footer > button.btn.btn-primary')
    okButton = (By.CSS_SELECTOR,'body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button')

    # click cart > purchaseButton 
    # wait.until(EC.visibility_of_element_located(navbar['cart'])).click()
    wait.until(EC.visibility_of_element_located(placeOrderButton)).click()
    
    # fill form 
    wait.until(EC.visibility_of_element_located(purchaseFields['name'])).send_keys(purchaseValues['name'])
    wait.until(EC.presence_of_element_located(purchaseFields['country'])).send_keys(purchaseValues['country'])
    wait.until(EC.presence_of_element_located(purchaseFields['city'])).send_keys(purchaseValues['city'])
    wait.until(EC.presence_of_element_located(purchaseFields['card'])).send_keys(purchaseValues['card'])
    wait.until(EC.presence_of_element_located(purchaseFields['month'])).send_keys(purchaseValues['month'])
    wait.until(EC.presence_of_element_located(purchaseFields['year'])).send_keys(purchaseValues['year'])



    # submit form 
    wait.until(EC.visibility_of_element_located(purchaseButton)).click()

    # ok button 
    wait.until(EC.visibility_of_element_located(okButton)).click()


def fillContactFormFile(filePath,contactData):
    con_email = (By.ID,'recipient-email')
    con_name = (By.ID,'recipient-name')
    con_msg = (By.ID,'message-text')
    con_submit = (By.CSS_SELECTOR,'#exampleModal > div > div > div.modal-footer > button.btn.btn-primary') 

    with open(filePath, 'a') as file:
        for row in contactData:
            # click contact
            wait.until(EC.visibility_of_element_located(navbar['contact'])).click()

            # fill form 
            wait.until(EC.visibility_of_element_located(con_email)).send_keys(row['Email'])
            wait.until(EC.visibility_of_element_located(con_name)).send_keys(row['Name'])
            wait.until(EC.visibility_of_element_located(con_msg)).send_keys(row['Message'])

            # click send 
            wait.until(EC.visibility_of_element_located(con_submit)).click()

            alert = wait.until(EC.alert_is_present())
            alert.accept()

            # append message to file 
            now = datetime.now()
            current_date = now.strftime("%d-%m-%y")
            current_time = now.strftime("%H:%M")
            message = f"\nToday\'s date: {current_date}\nCurrent time: {current_time}\nEmail: {row['Email']}\nName: {row['Name']}\nMessage: {row['Message']}\n--- \n"
            file.write(message)



def totalCartAmount():
    totalID = (By.ID,'totalp')
    wait.until(EC.visibility_of_element_located(navbar['cart'])).click()
    totalAmnt = wait.until(EC.visibility_of_element_located(totalID)).text
    return totalAmnt

def deleteFromCart(itemName):
    cartTable = driver.find_elements(By.CSS_SELECTOR, "tbody#tbodyid tr.success")
    for row in cartTable: 
        productName = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text 
        if productName == itemName:
            row.find_element(By.LINK_TEXT,'Delete').click()
            break