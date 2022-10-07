from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'')  # ADD geckodriver path here before testing
browser.get('http://localhost:8000')

assert 'Django' in browser.title