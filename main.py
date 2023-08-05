from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome import options
import random
import threading
import time

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
opt.add_argument(r"user-data-dir=C:\Users\agkam\AppData\Local\Google\Chrome\User Data\Profile")
driver = webdriver.Chrome(options=opt)
def openBrowser():

    driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")






def loopBronze():
    while True:
        randomWait = random.randint(5,15)/10

        storeButton = driver.find_element('xpath','/html/body/main/section/nav/button[4]')
        storeButton.click()
        time.sleep(randomWait)
        packsButton = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/div[2]')
        packsButton.click()
        time.sleep(randomWait)

        thirdPacks = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div[1]/div/button[3]')
        fourthPacks = driver.find_element('xpath', '/html/body/main/section/section/div[2]/div/div[1]/div/button[4]')

        if thirdPacks.text == "CLASSIC PACKS":
            thirdPacks.click()
        else:
            fourthPacks.click()
        time.sleep(randomWait)
        open750Coins = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div[3]/div[2]/div[3]/button')
        open750Coins.click()
        confirmButton = driver.find_element('xpath','/html/body/div[4]/section/div/div/button[1]')
        confirmButton.click()
        ##THE PACK IS OPENED##
        time.sleep(8)

        for i in range(12):

            try:
                redeemCoins = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]')
                if redeemCoins.is_displayed():
                    redeemCoins.click()
                    continue
            except:
                pass

            try:
                playerBioField = driver.find_element("xpath",'/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[1]')


                if playerBioField.is_displayed():
                    sendToClub = driver.find_element("xpath",
                                                     "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[6]")
                    if sendToClub.text !="Swap Duplicate Item from Club" :
                        sendToClub.click()
                    else:
                        sendToTransfer = driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]")
                        sendToTransfer.click()

                else:
                    quickSell = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[10]')
                    quickSell.click()

                    qsConfirm = driver.find_element("xpath","/html/body/div[4]/section/div/div/button[1]")
                    qsConfirm.click()
                time.sleep(randomWait)
            except:
                pass



def main():
    root = Tk()

    frame = ttk.Frame(root)
    frame.grid()
    root.title("FUT G")
    root.geometry("200x500")

    ttk.Label(frame, text="FUT G").grid(column=0,row=0)
    ttk.Button(frame,text="Open Web App",command=openBrowser).grid(column=0,row=1)
    ttk.Button(frame, text="Unlimited Bronze Pack", command=loopBronze).grid(column=0, row=2)

    root.mainloop()





main()