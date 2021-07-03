from time import sleep
import pyautogui as auto
import schedule, webbrowser

link = "Link"

time = "hr:min" 

def join():
    webbrowser.open_new_tab('https://' + link)
    sleep(7)
    #auto.hotkey('ctrl', 'd')
    #auto.hotkey('ctrl', 'e')
    auto.hotkey('command', 'd')
    auto.hotkey('command', 'e')                        
    auto.click(1034, 569)

schedule.every().day.at(time).do(join)

while 1 :
     schedule.run_pending()
     time.sleep(1)