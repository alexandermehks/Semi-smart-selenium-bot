from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import sqlite3
from datetime import date

dbConnection = "PATH TO DB"

def index():
    PATH = "PATH TO CHROMEDRIVER"
    driver = webdriver.Chrome(PATH)
    searchList = ["12,3M"]
    try:
        driver.get("https://jobb.blocket.se")
        driver.maximize_window()
        driver.find_element_by_id("accept-ufti").click()
        driver.find_element_by_id("whatinput").send_keys("Data, it")

        driver.find_element_by_id("whereinput").click()
        driver.find_element_by_xpath("//div[@data-value='ks=regions.11']").click()
        driver.find_element_by_id("search-button").click()

        #Fethching first element on each page.
        #index_element = driver.find_element_by_id("1").click()
        #index_job_description = driver.find_element_by_id("job-description")
        #match = []
        #for search_argument in searchList:
            #if search_argument in index_job_description.text:
                #match.append(search_argument)
        #print("Matches found!", match)
        #driver.execute_script("window.history.go(-1)")
    except:
        print("Error in runtime 1")
        driver.quit()


    date_today = date.today()
    searchList = ["carbon", "Systemutvecklare till Handelsbanken, Stockholm", "Data", "you", "what", "we", "here", "work", "frameworks", "Hög lön","junior"]
    db_connection = sqlite3.connect(dbConnection)
    connection = db_connection.cursor();
    try:
        last_page = driver.find_element_by_xpath("//div[@class ='ui buttons fluid']/a/i[@class='small chevron right icon no-margin']")
        while last_page:
            for current_post in range(1,14):
                element = driver.find_element_by_id(str(current_post)).click()
                element_job_description = driver.find_element_by_id("job-description")
                element_job_title = driver.find_element_by_xpath("//div[@class='ui ten wide column no-padding']/h2[@class='ui header title h1 even-less-padding-bottom']")
                for search_argument in searchList:
                    if search_argument in element_job_description.text or search_argument in element_job_title.text:
                        try:
                            current_url = str(driver.current_url)
                            connection.execute("INSERT INTO Link (URL,DATE,ARGUMENT) values (?,?,?)",(current_url,date_today,search_argument))
                            db_connection.commit()
                        except:
                            print("Duplicate in DB, not adding.")
                driver.execute_script("window.history.go(-1)")
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(0.5)
            pagination = driver.find_elements_by_xpath("//a[@class='ui basic secondary button']")
            if pagination[4]:
                pagination[4].click()
            else:
                print("Success!", match)
                driver.quit()
            #TODO Add if statement to check if driver.current_url == last
            if not last_page:
                driver.quit()
            #iteration()
    except:
        print("Error in runtime 2")





