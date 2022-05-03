from concurrent.futures import thread
import random
import time
from selenium import webdriver

def range(limit):
    path = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/span/div/label["+str(getrand(1,limit))+"]/div[2]/div/div/div[3]/div"
    return path
def single(limit):
    return "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div["+str(getrand(1,limit))+"]/label/div/div[1]/div/div[3]/div"
def multiple(limit):
    return "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div["+str(getrand(1,limit))+"]/label/div/div[1]/div[2]"


def getrand(a,b):
    return random.randint(a,b)

for _ in range(0,10):
    url = "https://docs.google.com/forms/d/e/1FAIpQLScHRpVNbu5qYx7-a1IrD6aTSd_BvilCS_j5iB5Q0ZpSDtkiXw/viewform"
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # Q1
    q1 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/span/div/label["+str(getrand(1,3))+"]/div[2]/div/div/div[3]/div")
    print("Element",q1)
    q1.click()
    # Q2
    q2 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div["+str(getrand(1,4))+"]/label/div/div[1]/div/div[3]/div")
    q2.click()
    # Q3
    q3 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div["+str(getrand(1,2))+"]/label/div/div[1]/div/div[3]/div")
    q3.click()
    # Q4
    q4 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div["+str(getrand(1,2))+"]/label/div/div[1]/div/div[3]/div")
    q4.click()
    # Q5
    q5 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div["+str(getrand(1,3))+"]/label/div/div[1]/div/div[3]/div")
    q5.click()
    # Q6
    q6 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div["+str(getrand(1,5))+"]/label/div/div[1]/div[2]")
    q6.click()

    # /html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]
    # Q7
    q7 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div["+str(getrand(1,2))+"]/label/div/div[1]/div/div[3]/div")
    q7.click()
    # Q8
    # /html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div
    # "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label["+str(getrand(1,5))+"]/div[2]/div/div/div[3]/div"
    q8 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label["+str(getrand(1,5))+"]/div[2]/div/div/div[3]/div")
    q8.click()
    # Q9
    # /html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]
    q9 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div["+str(getrand(1,4))+"]/label/div/div[1]/div[2]")
    q9.click()
    # Q10
    q10 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div/span/div/div["+str(getrand(1,2))+"]/label/div/div[1]/div/div[3]/div")
    q10.click()
    btn = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div")
    btn.click()
    driver.close()
