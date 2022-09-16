from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PATH="D:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://www.linkedin.com")

username = driver.find_element(By.CLASS_NAME,'input__input')

username.send_keys('')
password = driver.find_element(By.ID,'session_password')
password.send_keys('') 
log_in_button = driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button') 
log_in_button.click()
searchbar=driver.find_element(By.CLASS_NAME,'search-global-typeahead__input')
searchbar.click()
searchbar=driver.find_element(By.CLASS_NAME,'search-global-typeahead__input')
searchbar.send_keys("adrian javascript developer")
searchbar=driver.find_element(By.CLASS_NAME,'search-global-typeahead__input')
searchbar.send_keys(Keys.ENTER)
sleep(2)
clickprofile= driver.find_elements(By.CLASS_NAME,"reusable-search__result-container ")
sleep(2)
clickprofile[0].click()
sleep(2)
clickActivity=driver.find_element(By.CLASS_NAME,"pvs-navigation__text")
clickActivity.click()
sleep(2)
findButton=driver.find_element(By.XPATH,"//*[@aria-label='Posts']")
findButton.click()
sleep(2)
selectAllposts=driver.find_element(By.CLASS_NAME,"scaffold-finite-scroll__content")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
sleep(1)



print(selectAllposts.text)
