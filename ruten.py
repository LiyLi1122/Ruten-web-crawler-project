from selenium import webdriver
import time
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("露天手機殼查詢")
window.geometry("800x650")
title = tk.Label(window, text = "請選擇手機廠商")
title.place(x = 230, y = 80)

def getData():
    url = "https://www.ruten.com.tw/"
    options = webdriver.ChromeOptions() 
    options.add_argument("--headless")
    web = webdriver.Chrome(chrome_options=options)
    web.get(url)
    box.bind("<<ComboboxSelected>>") #指定內容
    boxContent = box.get()
    entryContent = entry.get()

    web.find_element_by_css_selector("div.rt-lightbox>button").click()
    web.find_element_by_name("q").send_keys(boxContent+" "+entryContent)
    web.find_element_by_css_selector("#searchFormSubmit").click()
    

    
    time.sleep(0.5)
    data_list = []
    a = 1
    times = 0
    while a < 2:
        tmp = web.find_elements_by_css_selector(" div.block_C >div#ProdGridContainer h5.prod_name>a")
        price = web.find_elements_by_css_selector("#ProdGridContainer  div.prod_info>div.price_box.about")
        for i in range(len(tmp)):
            times += 1
            data_list.append({'name':tmp[i].text, 'price':price[i].text, 'link':tmp[i].get_attribute('href')})
        web.find_element_by_css_selector("li.next > a").click()
        #休息1秒才爬得到資料 
        time.sleep(1) 
        a+=1
        times = times
    web.quit()
    for i in data_list:
        info.insert("insert", f"名稱：{i['name']}　\n價錢： {i['price']}元　\n網址：{i['link']}")
        info.insert("end", "\n\n")
  
def dataDelete():
    info.delete("1.0","end")
  
def commandExit():
    window.destroy()    
  

   
values = ["Apple", "htc", "Samsung"]
box = ttk.Combobox(window, values = values, state = "readonly")
box.current(0)
box.place(x = 320, y = 80)

entryLabel = tk.Label(window, text = "輸入搜尋字" )
entryLabel.place(x = 250, y = 110)

entry = tk.Entry(window) 
entry.place(x = 320, y = 110)

btnSubmit = tk.Button(window, text = "搜尋", command = getData, width = 10)
btnSubmit.place(x = 480, y = 145) 

btnDelete = tk.Button(window, text = "清除", command = dataDelete, width = 10)
btnDelete.place(x = 380, y = 145) 

btnExit = tk.Button(window, text = "離開", command = commandExit, width = 10)
btnExit.place(x = 280, y = 145) 

info = tk.Text(window, width = 100, height = 32)
info.place(x = 40, y = 180) 


window.mainloop()












