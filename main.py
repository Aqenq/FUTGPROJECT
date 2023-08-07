from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome import options
import random
import threading
import time

global lowLimit,topLimit

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

def snipeSearch():
    cheapestIndex = 0
    minPrice = int(lowLimit.get())
    startPrice = int(firstTopLimit.get())
    maxPrice = int(secondTopLimit.get())
    try:
        wantedRating = int(ratingSnipe.get())
    except:
        wantedRating = 0

    minPriceField = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input')
    maxPriceField = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')

    minPriceField.clear()
    maxPriceField.clear()

    minPriceField.send_keys(minPrice)
    maxPriceField.send_keys(startPrice)

    searchButton = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]')

    searchButton.click()

    bought = True
    lowestPrice = maxPrice

    currentPrice = int(startPrice)
    while bought:
        time.sleep(0.2)
        if 1==1:


            playerList = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section[1]/div/ul')

            playerCount = playerList.find_elements('xpath','*')
            print(len(playerCount))
            if len(playerCount) != 0:
                for i in range(1,len(playerCount)+1):


                    time.sleep(0.1)
                    price = driver.find_element('xpath',f'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{i}]/div/div[2]/div[3]/span[2]')

                    priceInt = int(price.text.replace(',',''))

                    playerRating = driver.find_element('xpath',f'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{i}]/div/div[1]/div[1]/div[5]/div[2]/div[1]')

                    playerName = driver.find_element('xpath',f'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{i}]/div/div[1]/div[2]')
                    print("Name: " + playerName.text + " Rating: " + playerRating.text + " Price: " + str(priceInt))


                    if priceInt < lowestPrice:
                        lowestPrice = priceInt
                        cheapestIndex = i
                        print(cheapestIndex)


                if lowestPrice < maxPrice:
                    if cheapestIndex != 1:
                        playerToBuy = driver.find_element('xpath',f'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{cheapestIndex}]')
                        playerToBuy.click()

                    if wantedRating == 0 or int(playerRating.text) == wantedRating:

                        buyNow = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]')
                        buyNow.click()
                        confirmBuy = driver.find_element('xpath','/html/body/div[4]/section/div/div/button[1]')
                        confirmBuy.click()
                        bought = False
                        print('Bought Player')
                        print(playerRating.text + " " + playerName.text + " " + str(priceInt))
                    else:
                        continue

            else:

                time.sleep(0.1)
                goBack = driver.find_element('xpath', '/html/body/main/section/section/div[1]/button[1]')
                goBack.click()
                if currentPrice > maxPrice:
                        #increaseButton = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/button[2]')
                        #increaseButton.click()
                        currentPrice = startPrice
                        minPrice += 501
                        minPriceField.clear()
                        minPriceField.send_keys(minPrice)
                        print("price limit exceeded")


                currentPrice = currentPrice + 501

                time.sleep(0.1)

                maxPriceField = driver.find_element('xpath',
                                                    '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')

                maxPriceField.clear()


                maxPriceField.send_keys(currentPrice)

                time.sleep(0.1)


                searchButton = driver.find_element('xpath',
                                                   '/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]')

                searchButton.click()
        #except:
         #   print("patladı")














def main():
    root = Tk()

    frame = ttk.Frame(root)
    frame.grid()
    root.title("FUT G")
    root.geometry("200x500")

    ttk.Label(frame, text="FUT G").grid(column=0,row=0)
    ttk.Button(frame,text="Open Web App",command=openBrowser).grid(column=0,row=1)
    ttk.Button(frame, text="Unlimited Bronze Pack", command=loopBronze).grid(column=0, row=2)

    ttk.Label(frame,text="Low Limit").grid(column=0,row=3)
    global lowLimit
    lowLimit = Entry(frame)
    lowLimit.grid(column=0,row=4)
    ttk.Label(frame,text="Start Top Limit").grid(column=0,row=5)
    global firstTopLimit
    firstTopLimit = Entry(frame)
    firstTopLimit.grid(column=0, row=6)
    ttk.Label(frame, text="Max Top Limit").grid(column=0, row=7)
    global secondTopLimit
    secondTopLimit = Entry(frame)
    secondTopLimit.grid(column=0,row=8)

    global ratingSnipe
    ttk.Label(frame, text="Rating (Optional)").grid(column=0, row=9)
    ratingSnipe = Entry(frame)
    ratingSnipe.grid(column=0,row=10)

    ttk.Button(frame, text="Snipe", command=snipeSearch).grid(column=0,row=11)

    root.mainloop()


main()