from driver_setup import driver 
import methods as m 
import time

# 1. Visit https://www.demoblaze.com/index.html#
url = 'https://www.demoblaze.com/index.html#'
driver.get(url)
driver.maximize_window()
time.sleep(5)

# 2. Register yourself as a user (you can use random data).
creds = {'username':'USERD456','password':'FDFDFDpp00D456'}
m.register(creds)
time.sleep(5)

# 3. Add Sony vaio i5 to cart.
m.addToCart('Laptops', 'Sony vaio i5')
time.sleep(5)

# 4. Add ASUS Full HD to cart.
m.addToCart('Monitors', 'ASUS Full HD')
time.sleep(5)

# 5. Go to cart.
# 6. Check if cart has 2 products.
if m.checkCartRows()== 2:
    print('Cart has 2 products.')
else:
    print('Cart does not have 2 products.')
time.sleep(5)


# 7. Purchase the products in the cart
purchaseValues = {
    'name': creds['username'],
    'country': 'INDIA',
    'city': 'MARGAO',
    'card': '123456789',
    'month': 'AUGUST',
    'year': '2025',
}
m.purchaseFromCart(purchaseValues)
time.sleep(5)

# 8. Go to cart and verify that it is empty.
if m.checkCartRows() == 0:
    print('Cart is empty.')
else:
    print('Cart is not empty.')
time.sleep(5)

# 9. Make a purchase with the empty cart.
m.purchaseFromCart(purchaseValues)
time.sleep(5)

# 10. Create a contact.txt file.
filePath = 'contact.txt'
open(filePath, 'w').close() 
time.sleep(5)

# 11. Fill the contact form with the following data:
contactData = [
    {'Email':'ABC@example.com', 'Name':'ABC', 'Message':'Hi there. ABC here.'},
    {'Email':'XYZ@example.com', 'Name':'XYZ', 'Message':'Hi there. XYZ here.'},
    {'Email':'MNO@example.com', 'Name':'MNO', 'Message':'Hi there. MNO here.'},
    {'Email':'123@example.com', 'Name':'123', 'Message':'Hi there. 123 here.'}
]
time.sleep(5)

# 15. For each contact request, write the form details in contact.txt file in following format:
# 16. New Contact Request: 
# 17. Today’s date: <date> 
# Current time: <time>
# Email: <email>
# Name: <name>
# Message: <message>
# ---
m.fillContactFormFile(filePath,contactData)
time.sleep(5)


# 18. Go to laptops section.
# 19. Go to 2nd page.
# 20. Add MacBook Pro to the cart.
m.addToCart('Laptops', 'MacBook Pro')
time.sleep(5)

# 21. Add Dell i7 8gb to the cart.
# 22. Get product description of Dell i7 8gb.
m.addToCart('Laptops', 'Dell i7 8gb',1)
time.sleep(5)

# 23. Go to cart.
# 24. Get total amount.
print('Total Amount: ',m.totalCartAmount())
time.sleep(5)

# 25. Remove Dell i7 8gb from the cart.
m.deleteFromCart('Dell i7 8gb')
time.sleep(5)

# 26. Purchase the items from the cart.
m.purchaseFromCart(purchaseValues)
time.sleep(5)

driver.quit()