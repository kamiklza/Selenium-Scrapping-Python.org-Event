from selenium import webdriver

chrome_driver_path = "/Users/Kamiklza/PycharmProjects/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

event_list = driver.find_elements_by_css_selector(".shrubbery .menu li a")

for even in event_list:
    print(even.text)

driver.quit()
