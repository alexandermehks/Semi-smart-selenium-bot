import tkinter
from tkinter import *
from jobb import *

window = tkinter.Tk()

window.title("Job Searching")
window.geometry('300x150')

x = "Null"

def get_jobs():
    db_connection = sqlite3.connect(dbConnection)
    connection = db_connection.cursor()
    links = connection.execute("SELECT URL, DATE, SETT, ARGUMENT FROM Link")
    links = links.fetchall()
    return links
    db_connection.close()

def iterate_jobs():
    list = []
    jobs = get_jobs()
    for job in jobs:
        if job[2] == None:
            list.append(job)
        else:
            #print("All jobs iterated")
            pass
    return list

def click_function_get_job():
    list = iterate_jobs()
    counter = 0
    db_connection = sqlite3.connect(dbConnection)
    connection = db_connection.cursor()
    connection.execute("UPDATE Link SET SETT='JA' WHERE URL=(?)",(list[counter][0],))
    db_connection.commit()
    connection.close()
    counter += 1
    a = list[counter][0]
    x = list[counter][3]
    print(x)
    return list[counter] 

def open_driver():
    job = click_function_get_job()
    #PATH = "/usr/bin/chromedriver"
    #driver = webdriver.Chrome(PATH)
    driver = webdriver.Firefox()
    driver.get(job[0])
    return job

def exit():
    window.quit()

#Search Job button
#TODO add command to button (window, text="", command = "function")
btn_search_job = Button(window, text="search job", command = open_driver)
btn_search_job.place(x=50, y=25)


#Update Database button or run script.
#TODO add command
btn_update = Button(window, text="Update Jobs!", command = index)
btn_update.place(x=150, y=25)


#Exit button
btn_exit = Button(window, text="Exit", command = exit)
btn_exit.place(x=125, y=60)

#TODO Add triggered keyword
keyword = tkinter.Label(window, text=x)
keyword.place(x=10, y=100)

print(x)

window.mainloop()


