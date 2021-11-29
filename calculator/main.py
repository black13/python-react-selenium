#assumes python3.
from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Edge(executable_path=r'./edgedriver/msedgedriver.exe')
    driver.get("http://localhost:3000/calculator")
    elem = driver.find_element_by_name("q")

if __name__ == "__main__":
    main()