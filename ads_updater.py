from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import schedule
import time


# Perform login (replace with your login credentials)
username = 'your_username'
password = 'your_password'

# Function to update the ads
def update_ads():
    try: 
        # Initialize the web driver (make sure you have the appropriate webdriver installed)
        browser = webdriver.Firefox()
        
        # Open wg-gesucht.de
        browser.get('https://www.wg-gesucht.de')

        # Accept Cookies
        browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/span[2]/a').click()

        # click "Mein Account"
        browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/nav[1]/div[3]/div/a').click()

        # Fill in Login-Data and click Login
        wait = WebDriverWait(browser, 10)  # 10 seconds timeout
        input_username = wait.until(EC.element_to_be_clickable((By.ID, 'login_email_username')))
        input_username.send_keys(username)

        input_password = wait.until(EC.element_to_be_clickable((By.ID, 'login_password')))
        input_password.send_keys(password)

        login_submit = browser.find_element(By.ID, 'login_submit')
        login_submit.click()

        # ads online
        ads = [6552512, 6659241] # update numbers to your adds

        for element in ads:
            browser.get(f'https://www.wg-gesucht.de/angebot-bearbeiten.html?action=update_offer&offer_id={element}')
            update_submit = browser.find_element(By.ID, 'update_offer')
            time.sleep(0.5)
            update_submit.click()

        # Logout
        my_account_button = browser.find_element(By.LINK_TEXT, 'Mein Konto')
        # Scroll the "Mein Konto" button into view using JavaScript
        browser.execute_script("arguments[0].scrollIntoView(true);", my_account_button)
        
        actions = ActionChains(browser)
        actions.move_to_element(my_account_button).perform()
        time.sleep(0.5)
        logout_button = browser.find_element(By.CLASS_NAME, 'logout_button')
        logout_button.click()

    finally:
        # Close the web driver
        browser.quit()

if __name__ == '__main__':
    update_ads()

"""
# Schedule the ad update to occur every day at a specific time
schedule.every().day.at('12:00').do(update_ads)  # Update time as needed

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
"""
