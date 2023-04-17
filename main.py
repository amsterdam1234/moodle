from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from twilio.rest import Client


if __name__ == '__main__':

    # set up options to run the browser in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # set up twilo
    account_sid = 'AC41f909b1afde584e85bbe759f0281a45'
    auth_token = '20282b717ddd9b1bda43debc3eb22e29'
    client = Client(account_sid, auth_token)

    # heart beat
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="run is started",
        to='whatsapp:+972544784039'
    )

    # create a new Chrome browser instance
    driver = webdriver.Chrome(options=chrome_options)

    # navigate to the Moodle login page
    driver.get("https://moodle.bgu.ac.il/moodle/login/index.php")

    # find the username input field and enter your username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("omeramst")

    # find the password input field and enter your password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Kmalabdalla98!")

    # submit the login form
    submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

    # wait for the page to load
    wait = WebDriverWait(driver, 10)

    # find the new upcoming events
    events = driver.find_elements(By.CLASS_NAME, "event")

    # print the event details for each event
    for event in events:
        event_text = event.text
        with open("venv/assigments.txt", "r") as f:
            if event_text in f.read():
                print(event_text, "already exists in ASSIGNMENTS.txt")
            else:
                with open("venv/assigments.txt", "a") as f:
                    f.write(event_text + "\n")
                print(event_text, "added to ASSIGNMENTS.txt")
                message = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=event_text,
                    to='whatsapp:+972544784039'
                )

    # close the browser
    driver.quit()

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="run is finished",
        to='whatsapp:+972544784039'
    )


