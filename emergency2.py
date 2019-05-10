import selenium
import pyautogui
from selenium import webdriver
import random
import time
import sys


draft = ['This is a message if I go missing. I made a programing script thats set up on a timer and put it on a vps, if i dont reset it every few days then it sends out this message to certain emails. I have been getting calls that people are after me and that they want to shoot me... I know this is kinda random but yea im a little scared So Im just making this program and setting precatuions if anything happens then I believe that the people i listed below had something to do with it. Ryan Woodward (113 oxnard ave, oxnard ca. 7073448127), Ryans Parents/Girlfriend. 7072057005, ryans friends: Stieve(101 Gilway st. benicia ca. 7072082119), Taylor Robeiro, 203 eaton st. benicia ca 7079804599, koal wright (1701 lopes rd benicia). Just threw this together in case something happens to me but probably wont I know this sounds ridiculous but im taking this pretty serious and would like you to actually look into this if you guys receive this message, thanks. My name is William Mullin. live at 4908 mercier st. kansas city. mo.']

senders = ['whmiiiphoto@gmail.com',
           'sskskaskatskate@gmail.com',
           'whmiii404@gmail.com',
           'bmullin236@gmail.com'
           'wmullin404@gmail.com',
           'wmullin4042@gmail.com',
           'wmullin4043@gmail.com',
           'wmullin4044@gmail.com',
           'wmullin4045@gmail.com',
           'wmullin4046@gmail.com',
           'wmullin4047@gmail.com',
           'wmullin4048@gmail.com',
           'wmullin4049@gmail.com',
           'wmullin40410@gmail.com',
           'skrilliamphotography@gmail.com',
           'bmullin236@gmail.com']

passwords = ['SSKSK814whm54321',
            'SSKSK814whm321',
            'SSKSK814'
            'whm12345SSKSK85432',
            'iviheuhierouhgouh2q4o8',
            'SSKKS814',
            'qpiwugefipugpig1283 7qrt',
            'kuwregfiu1987239y89142f',
            'OIQGFOY8T124387FT89QY4',
            'SSKKS814',
            'SSKKS814',
            'SSKKS814',
            'SSKKS814',
            'SSKKS814',
            'wkleurgio7324g783qwarfq34eagtvrsrgdrdt',
            'worfipug2i43f7tq384grawg4fivgwri']


emails = ['whmiiiphoto@gmail.com',
          'whmiiiphoto@gmail.com',
          'whmiiiphoto@gmail.com',
          'whmiiiphoto@gmail.com',
          'whmiiiphoto@gmail.com',
          'whmiiiphoto@gmail.com',
          'whmiiiphoto@gmail.com',
          'whmiiiphoto@gmail.com']


while True:
    # time.sleep(259200) #3 days program fires
    counter = 0

    for i in range(15):
        driver = webdriver.Firefox()

        try:
            driver.implicitly_wait(25)
            driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        except:
            time.sleep(2)
            driver.refresh()
            driver.implicitly_wait(25)

        try:
            time.sleep(2)
            driver.implicitly_wait(25)
            email = driver.find_element_by_xpath('//*[@id="identifierId"]')
            email.send_keys(senders[counter])
            driver.implicitly_wait(25)
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content').click()
            driver.implicitly_wait(25)
        except:
            driver.refresh()
            driver.implicitly_wait(25)
            email = driver.find_element_by_xpath('//*[@id="identifierId"]')
            email.send_keys(senders[counter])

        try:
            time.sleep(2)
            driver.implicitly_wait(25)
            email = driver.find_element_by_xpath('//*[@id="identifierId"]')
            email.send_keys(senders[counter])
            driver.implicitly_wait(25)
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content').click()
            driver.implicitly_wait(25)
        except:
            pass

        try:
            time.sleep(3)
            pyautogui.press('enter')

        except:
            pass

        try:
            driver.implicitly_wait(25)
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input').click()
        except:
            pass

        try:
            time.sleep(3)
            pyautogui.typewrite(passwords[counter])
            pyautogui.press('enter')

        except:
            pass

        try:
            time.sleep(2)
            driver.implicitly_wait(25)
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div/div').click()
        except:
            pass

        try:
            driver.implicitly_wait(25)
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[4]/header/div[2]/div[4]/div[1]/div/div/div[2]/div/a[1]').click()
        except:
            pass

        try:
            time.sleep(4)
            pyautogui.typewrite(emails[counter])
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('tab')
        except:
            pass

        try:
            time.sleep(2)
            driver.implicitly_wait(25)
            subject = driver.find_element_by_xpath('//*[@id=":qr"]').click()
            time.sleep(2)
            pyautogui.typewrite('WILLIAM MULLIN MISSING REPORT.')
            time.sleep(1)
            subject = driver.find_element_by_xpath('//*[@id=":qr"]').click()
            time.sleep(1)
            pyautogui.typewrite('WILLIAM MULLIN MISSING REPORT.')
        except:
            pass

        try:
            time.sleep(2)
            driver.implicitly_wait(25)
            letter = driver.find_element_by_xpath('//*[@id=":rw"]').click()
            time.sleep(2)
            pyautogui.typewrite('{}'.format(draft))
        except:
            pass

        try:
            time.sleep(2)
            driver.implicitly_wait(25)
            driver.find_element_by_xpath('//*[@id=":qh"]').click()
        except:
            pass

        try:
            time.sleep(1)
            driver.implicitly_wait(25)
            driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div/div[2]/div/a/span').click()
        except:
            pass

        counter+=1
        time.sleep(1)
        driver.quit()
        time.sleep(3)
