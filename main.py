from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome import options
import random
import threading
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

global lowLimit,topLimit
def getUDD():
    f = open("venv/config.txt", "r")
    str = f.read()
    str = str.replace("userdatadir = ",'')
    return str

def setUDD():
    setUDDWindow = Tk()
    frameUDD = ttk.Frame(setUDDWindow)
    frameUDD.grid()
    setUDDWindow.title("Set User Data Directory")
    setUDDWindow.geometry("400x200")
    global userDataPath
    ttk.Label(frameUDD, text="Enter User Data Directory").grid(column=0, row=0)
    userDataPath = Entry(frameUDD)
    userDataPath.grid(column=0,row=1)
    def applySettings():
        f = open("venv/config.txt", "w")
        f.write("userdatadir = " + userDataPath.get())

    ttk.Button(frameUDD,text="Apply",command=applySettings).grid(column=0,row=2)


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
opt.add_argument(f"user-data-dir={getUDD()}")
driver = webdriver.Chrome(options=opt)
wait = WebDriverWait(driver, 10)
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

        if thirdPacks.text == "CLASSIC PACKS":
            thirdPacks.click()
        else:
            fourthPacks = driver.find_element('xpath',
                                              '/html/body/main/section/section/div[2]/div/div[1]/div/button[4]')

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
    maxPrice = int(secondTopLimit.get()) + 1
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


                    time.sleep(0.2)
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

                time.sleep(0.2)
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

                time.sleep(0.2)

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


def spamBronzeUpgrade():
    sbcSection = driver.find_element('xpath','/html/body/main/section/nav/button[6]')
    sbcSection.click()
    time.sleep(0.2)
    buttonGroup = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div[1]/div')
    buttonsList = buttonGroup.find_elements('xpath','*')

    for button in buttonsList:
        if button.text == "UPGRADES":
            button.click()

    sbcHub = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div[2]/div[2]')
    sbcList = sbcHub.find_elements('xpath','*')
    while True:
        for i in range(1,len(sbcList)):
            time.sleep(0.2)
            sbcName = driver.find_element('xpath',f"/html/body/main/section/section/div[2]/div/div[2]/div[2]/div[{i}]/div[1]/div[1]/h1")
            if sbcName.text == "ULTIMATE BRONZE UPGRADE":
                sbcDiv = driver.find_element('xpath',f'/html/body/main/section/section/div[2]/div/div[2]/div[2]/div[{i}]')
                sbcDiv.click()
                break

        time.sleep(1)
        useSquadBuilder = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div/section/div/button[2]')
        useSquadBuilder.click()

        qualityFilter = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[3]')
        time.sleep(0.5)
        if qualityFilter.text.lower() != "bronze":
            print('not bronze !')
            qualityFilter.click()
            bronzeSelection = driver.find_element('xpath',
                                                  '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[3]/div/ul/li[2]')
            bronzeSelection.click()
        else:
            pass

        rarityFilter = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[4]')
        rarityFilter.click()

        common = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[4]/div/ul/li[2]')
        common.click()

        buildButton = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[3]/button[2]')
        buildButton.click()

        playersInSBC = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/div/div[2]/div[1]')
        playerList = playersInSBC.find_elements('xpath','*')

        for i in range(1,12):
            print("x")
            playerSlot = driver.find_element('xpath',f"/html/body/main/section/section/div[2]/div/div/div/div[2]/div[1]/div[{i}]/div[3]")
            time.sleep(0.8)

            if playerSlot.get_attribute("class") == "small player item ut-item-loading empty droppable":
                playerSlot.click()
                time.sleep(0.2)
                addPlayerButton = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/button[3]')
                addPlayerButton.click()
                time.sleep(0.2)
                clearPosition = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[5]/div/div/button')
                clearPosition.click()
                time.sleep(0.2)
                playerQuality = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]')
                playerQuality.click()
                time.sleep(0.2)
                bronzeQualityPlayer = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]/div/ul/li[2]')
                bronzeQualityPlayer.click()
                time.sleep(0.2)
                playerRarity = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[4]')
                playerRarity.click()
                time.sleep(0.2)
                playerRarityCommon = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[4]/div/ul/li[2]')
                playerRarityCommon.click()
                time.sleep(0.2)
                searchClub = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[3]/button[2]')
                searchClub.click()
                time.sleep(0.5)
                addPlayerToSBC = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[3]/ul/li[1]/button')
                addPlayerToSBC.click()
                time.sleep(0.2)

        time.sleep(1)
        submitButton = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/div/div[2]/button[2]')
        submitButton.click()
        time.sleep(1)

        claimReward = driver.find_element('xpath','/html/body/div[4]/div/footer/button')
        claimReward.click()
        time.sleep(0.2)

        claimSecond = driver.find_element('xpath','/html/body/div[4]/div/footer/button')
        claimSecond.click()
        time.sleep(0.2)

def listTransferList():
    transfersButton= driver.find_element('xpath','/html/body/main/section/nav/button[3]')
    transfersButton.click()
    transferList = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/div[3]')
    transferList.click()
    try:
        relistAll = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/div/section[2]/header/button')
        time.sleep(0.3)
        relistAll.click()
        confirm = driver.find_element('xpath','/html/body/div[4]/section/div/div/button[2]')
        confirm.click()
    except:
        pass

    notListedPlayers = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/div/section[3]/ul')
    playersList = notListedPlayers.find_elements('xpath','*')
    for i in range(1,len(playersList)+1):
        time.sleep(1)
        player = driver.find_element('xpath',f"/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li[1]")
        player.click()
        time.sleep(0.5)
        comparePrice = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[3]/button[9]')
        comparePrice.click()
        time.sleep(0.2)
        listings = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/section/div[2]/ul')
        time.sleep(0.2)
        listingsList = listings.find_elements('xpath','*')
        time.sleep(1)
        playerName = driver.find_element('xpath',f"/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li[{i}]/div/div[1]/div[2]")
        print(playerName.text)
        lowestPrice = int(driver.find_element('xpath',
                                              f'/html/body/main/section/section/div[2]/div/div/section/div[2]/section/div[2]/ul/li[1]/div/div[2]/div[3]/span[2]').text.replace(
            ',', ''))
        for j in range(1,len(listingsList)+1):


            time.sleep(0.4)
            listingPrice = driver.find_element('xpath',f'/html/body/main/section/section/div[2]/div/div/section/div[2]/section/div[2]/ul/li[{j}]/div/div[2]/div[3]/span[2]')




            if listingPrice.text.find(',') != -1:
                currentPrice = int(listingPrice.text.replace(',', ''))

            else:
                currentPrice = int(listingPrice.text)



            if currentPrice < lowestPrice:
                lowestPrice = currentPrice

        print("Lowest Price: " + str(lowestPrice))
        goBack = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[1]/button')
        goBack.click()
        time.sleep(0.2)
        listOnMarket = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/div[1]/button')
        listOnMarket.click()
        time.sleep(0.5)
        buyNowField = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[2]/input')
        time.sleep(0.1)

        buyNowField.send_keys(0)
        time.sleep(0.1)
        buyNowField.send_keys(lowestPrice)
        time.sleep(0.2)


        startPriceField = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/input')
        time.sleep(0.1)

        startPriceField.send_keys(0)
        time.sleep(0.2)
        startPriceField.send_keys(lowestPrice-200)
        sendItToMarket = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/div[2]/button')
        time.sleep(0.2)

        lowerBuyNow = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[2]/button[1]')
        lowerBuyNow.click()
        time.sleep(0.2)
        sendItToMarket.click()



def spamSBC():
    sbcSection = driver.find_element('xpath', '/html/body/main/section/nav/button[6]')
    sbcSection.click()
    time.sleep(0.2)
    buttonGroup = driver.find_element('xpath', '/html/body/main/section/section/div[2]/div/div[1]/div')
    buttonsList = buttonGroup.find_elements('xpath', '*')



    for button in buttonsList:
        if button.text == "UPGRADES":
            button.click()

    sbcNameFromTTK = sbcName.get()
    wantedQuality = qualitySelect.get()
    print(wantedQuality)
    wantedRarity =raritySelect.get()
    print(wantedRarity)

    sbcHub = driver.find_element('xpath', '/html/body/main/section/section/div[2]/div/div[2]/div[2]')
    sbcList = sbcHub.find_elements('xpath', '*')
    while True:
        for i in range(1, len(sbcList)):
            time.sleep(0.2)
            sbcNameCurrent = driver.find_element('xpath',
                                          f"/html/body/main/section/section/div[2]/div/div[2]/div[2]/div[{i}]/div[1]/div[1]/h1")
            if sbcNameCurrent.text == sbcNameFromTTK:
                sbcDiv = driver.find_element('xpath',
                                             f'/html/body/main/section/section/div[2]/div/div[2]/div[2]/div[{i}]')
                sbcDiv.click()
                break

        time.sleep(1)
        useSquadBuilder = driver.find_element('xpath',
                                              '/html/body/main/section/section/div[2]/div/div/section/div/section/div/button[2]')
        useSquadBuilder.click()

        qualityFilter = driver.find_element('xpath',
                                            '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[3]')
        time.sleep(0.5)


        if qualityFilter.text.lower() != wantedQuality:

            qualityFilter.click()
            qualityGroup = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[3]/div/ul').find_elements('xpath','*')
            for i in range(1,6):
               quality = driver.find_element('xpath',f'/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[3]/div/ul/li[{i}]')
               if quality.text.lower() == wantedQuality:
                   quality.click()




        rarityFilter = driver.find_element('xpath',
                                           '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[4]')
        rarityFilter.click()

        if rarityFilter.text.lower() != wantedRarity:

            for i in range(1,4):
                time.sleep(0.2)
                rarity = driver.find_element('xpath',f'/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[4]/div/ul/li[{i}]')
                if rarity.text.lower() == wantedRarity:
                    rarity.click()
                    break

        else:
            rarityFilter.click()



        buildButton = driver.find_element('xpath',
                                          '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[3]/button[2]')
        buildButton.click()

        playersInSBC = driver.find_element('xpath', '/html/body/main/section/section/div[2]/div/div/div/div[2]/div[1]')
        playerList = playersInSBC.find_elements('xpath', '*')

        time.sleep(0.5)

        for i in range(1, 12):
            print("x")
            playerSlot = driver.find_element('xpath',
                                             f"/html/body/main/section/section/div[2]/div/div/div/div[2]/div[1]/div[{i}]/div[3]")
            time.sleep(0.3)

            if playerSlot.get_attribute("class") == "small player item ut-item-loading empty droppable":
                playerSlot.click()
                time.sleep(0.2)
                addPlayerButton = driver.find_element('xpath',
                                                      '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/button[3]')
                addPlayerButton.click()
                time.sleep(0.2)
                clearPosition = driver.find_element('xpath',
                                                    '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[5]/div/div/button')
                clearPosition.click()
                time.sleep(0.2)
                playerQuality = driver.find_element('xpath',
                                                    '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]')
                playerQuality.click()
                time.sleep(0.2)

                if wantedQuality == "bronze":
                    bronzeQualityPlayer = driver.find_element('xpath',
                                                          '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]/div/ul/li[2]')
                    bronzeQualityPlayer.click()
                elif wantedQuality == "silver":
                    silverQuality = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]/div/ul/li[3]')
                    silverQuality.click()
                elif wantedQuality == "gold":
                    goldQuality = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]/div/ul/li[4]')
                    goldQuality.click()

                time.sleep(0.2)


                playerRarity = driver.find_element('xpath',
                                                   '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[4]')
                playerRarity.click()
                time.sleep(0.2)

                if wantedRarity == "common":
                    playerRarityCommon = driver.find_element('xpath',
                                                             '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[4]/div/ul/li[2]')
                    playerRarityCommon.click()
                else:
                    playerRarityRare = driver.find_element('xpath','/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[4]/div/ul/li[3]')
                    playerRarityRare.click()

                time.sleep(0.2)
                searchClub = driver.find_element('xpath',
                                                 '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[3]/button[2]')
                searchClub.click()
                time.sleep(0.5)
                addPlayerToSBC = driver.find_element('xpath',
                                                     '/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[3]/ul/li[1]/button')
                addPlayerToSBC.click()
                time.sleep(0.2)

        time.sleep(1)
        submitButton = driver.find_element('xpath',
                                           '/html/body/main/section/section/div[2]/div/div/div/div[2]/button[2]')
        submitButton.click()
        time.sleep(1)

        claimReward = driver.find_element('xpath', '/html/body/div[4]/div/footer/button')
        claimReward.click()
        time.sleep(0.2)

        claimSecond = driver.find_element('xpath', '/html/body/div[4]/div/footer/button')
        claimSecond.click()
        time.sleep(0.2)







def main():
    root = Tk()

    frame = ttk.Frame(root)
    frame.grid()
    root.title("FUT G 2")
    root.geometry("700x700")

    menubar = Menu(root)
    root.config(menu=menubar)

    file_menu = Menu(menubar,tearoff=0)
    file_menu.add_command(label="Set User Data Dir",command=setUDD)
    menubar.add_cascade(
        label="File",
        menu=file_menu
    )

    ttk.Label(frame, text="FUT G 2").grid(column=0,row=0)
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

    ttk.Button(frame, text="Unlimited Bronze Upgrade", command=spamBronzeUpgrade).grid(column=1,row=1)

    ttk.Button(frame,text="List TL",command=listTransferList).grid(column=1,row=2)

    ttk.Label(frame,text="Spam SBC").grid(column=1,row=3)

    ttk.Label(frame,text="SBC Name").grid(column=1,row=4)

    global sbcName
    sbcName = Entry(frame)
    sbcName.grid(column=1,row=5)

    ttk.Label(frame,text="Quality").grid(column=1,row=6)

    variable = StringVar(root)
    variable.set("Select Quality")

    global qualitySelect
    qualitySelect = ttk.Combobox(root,textvariable=variable)
    qualitySelect['values'] = ('bronze','silver','gold')
    qualitySelect['state'] = 'readonly'
    qualitySelect.grid(row=7,column=1)

    ttk.Label(frame,text="Rarity").grid(column=1,row=8,)


    variable2 = StringVar(root)
    variable2.set("Select Rarity")
    global raritySelect
    raritySelect = ttk.Combobox(root,textvariable=variable2)
    raritySelect['values'] = ('common','rare')
    raritySelect['state'] = 'readonly'
    raritySelect.grid(column=1,row=9)


    ttk.Button(frame,text="Spam SBC",command=spamSBC).grid(column=1,row=10)

    root.mainloop()


main()