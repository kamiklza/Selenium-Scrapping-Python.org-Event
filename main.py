from selenium import webdriver

chrome_driver_path = "/Users/Kamiklza/PycharmProjects/chromedriver"
desktop_driver_path = "C:/Users/user/PycharmProjects/chromedriver.exe"

driver = webdriver.Chrome(executable_path=desktop_driver_path.encode())

driver.get("https://www.python.org/")

event_time = driver.find_elements_by_css_selector(".medium-widget.event-widget.last .menu time")
event_list = driver.find_elements_by_css_selector(".medium-widget.event-widget.last .menu li a")


events = {n: {"time": event_time[n].text, "name": event_list[n].text} for n in range(len(event_time))}
print(events)

# #-------Official Answer to Create the List---------#
# events = {}
# for n in range(len(event_time)):
#     events[n] = {
#         "time" : event_time[n].text,
#         "name" : event_list[n].text
#     }
# print(events)

#----------------------------------------------------#


driver.quit()

