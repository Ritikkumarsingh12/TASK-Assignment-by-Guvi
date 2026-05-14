from selenium import webdriver

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)

def after_scenario(context, scenario):
    context.driver.quit()