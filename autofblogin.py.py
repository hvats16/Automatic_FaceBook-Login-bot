user_id = input("Enter you email or phone number: ")
user_password = input("Enter your password: ")
print(user_id)
print(user_password)

from selenium import webdriver
browser = webdriver.Chrome("C:\\Users\\Harshit\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get("https://www.facebook.com/")

email_element = browser.find_element_by_id("email")
email_element.send_keys(user_id)

password_elemnt = browser.find_element_by_id("pass")
password_elemnt.send_keys(user_password)

login_facebook = browser.find_element_by_id("u_0_b")
login_facebook.click()
