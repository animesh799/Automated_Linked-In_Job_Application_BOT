#MAKE SURE TO UPLOAD YOUR RESUME ON LINKED IN BEFORE RUNNING THE CODE  Settings & Privacy -> Job Seeking Preferences -> Job Application Settings

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# YOUR CHROME DRIVER PATH
CHROME_DRIVER_PATH = "C:\Developement\chromedriver.exe"
Email = input('Enter your Linked-In Email:')
Password = input('Enter your Password:')
PhoneNumber = input('Enter your Contact No.:')
JOBROLE = input("Enter preferred Job Role:")
driver = webdriver.Chrome(service_log_path=CHROME_DRIVER_PATH)

driver.get(
    f"https://www.linkedin.com/jobs/search/?currentJobId=3351752276&f_AL=true&geoId=102713980&keywords={JOBROLE}&"
    f"location=India&refresh=true")
driver.maximize_window()

time.sleep(4)

# Sign in process
SignIn = driver.find_element(By.LINK_TEXT, "Sign in")
SignIn.click()
time.sleep(4)
Email_box = driver.find_element(By.ID, "username")
Password_box = driver.find_element(By.ID, "password")
Submit_but = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

Email_box.send_keys(Email)
Password_box.send_keys(Password)
Submit_but.click()
time.sleep(3)

Job_list = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
# Extracting the list of Jobs from the UL element
for job in Job_list:
    job.click()
    time.sleep(2)
    # Finding Apply button
    try:
        Apply_but = driver.find_element(By.XPATH, "//*[@id='main']/div/section[2]/div/div[2]/div[1]/div/div[1]/div/"
                                                  "div[1]/""div[1]/div[3]/div/div/div")
        Apply_but.click()
        time.sleep(2)
        PhoneNumber_input = driver.find_element(By.CSS_SELECTOR, "input.fb-single-line-text__input")
        Next_btn = driver.find_element(By.CSS_SELECTOR, "footer button")

        # checking the application is multi-step or not
        if Next_btn.get_attribute("aria-label") == 'Continue to next step':
            Cancel_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button')
            Cancel_btn.click()
            time.sleep(2)
            Discard_but = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/button[1]')
            Discard_but.click()
            print("Complex application,skipped")
            continue

        # Submitting the application
        else:
            # filling contact if phone number is empty
            if PhoneNumber_input.text == '':
                PhoneNumber_input.send_keys(PhoneNumber)
                time.sleep(2)
            Next_btn.click()
            print("Application Submitted")

        # Clossing the popup once the application is submitted
        time.sleep(2)
        CloseButton = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button')
        CloseButton.click()
        time.sleep(2)

    except NoSuchElementException:
        print("No application button,skipped")
        continue

time.sleep(5)
driver.quit()
