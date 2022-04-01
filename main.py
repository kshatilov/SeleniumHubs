import sys

from selenium import webdriver, common
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(link):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('use-fake-device-for-media-stream')
    chrome_options.add_argument('use-fake-ui-for-media-stream')
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(link)

    # enter room
    button_sequence = ["Join Room", "Accept", "Enter Room"]

    for button_text in button_sequence:
        success = False
        while not success:
            WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
            buttons_list = driver.find_elements(By.TAG_NAME, "button")

            for button in buttons_list:
                try:
                    if button.text == button_text:
                        button.click()
                        print(button_text + " is clicked")
                        success = True
                        break
                except common.exceptions.StaleElementReferenceException:
                    print("Detected loading issue")
                    break

    # walk around
    WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.CLASS_NAME, "a-canvas")))
    print("Entered room")

    while True:
        driver.execute_script("document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'w'}))")
        driver.execute_script("document.dispatchEvent(new KeyboardEvent('keyup', {'key': 'w'}))")
        driver.execute_script("document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'q'}))")
        driver.execute_script("document.dispatchEvent(new KeyboardEvent('keyup', {'key': 'q'}))")


if __name__ == '__main__':
    link = sys.argv[1]
    print("Visiting " + link)
    main(link)
