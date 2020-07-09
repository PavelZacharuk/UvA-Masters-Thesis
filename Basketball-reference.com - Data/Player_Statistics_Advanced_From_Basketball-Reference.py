# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:32:52 2020

@author: Pavel
"""

# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
#       Basketball Players Data
#
#       FIRST VERSION  March  19, 2020
#       THIS VERSION   May 6, 2020
#       LAST RUN       May 6, 2020
#
#       LAST REVISOR   Zacharuk
#
#       This scrapes information about Players Statistics during Regular Season in NBA. 
# ---------------------------------------------------------------------------

# =============================================================================
###############################################################################################
####                               PLAN OF THE PROCEDURE                                   ####
####        1. Import libraries                                                            ####
####        2. Open Chrome driver and go to the page                                       ####
####        3. Open page                                                                   ####
#####       4. Get everybody                                                               ####
####_______________________________________________________________________________________####
###############################################################################################

###############################################################################################
####        1. Import libraries                                                            ####
###############################################################################################
import time
import math
import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui  import Select
from selenium.webdriver.chrome.options import Options
from unidecode import unidecode
from pathlib import Path
from bs4 import BeautifulSoup
from math import ceil
#from interval import interval, inf, imath
import in_place
import shutil
import pandas as pd
import pyautogui


###############################################################################################
####        2. Open Chrome driver and go to the page                                       ####
###############################################################################################

print ("here")

options = webdriver.ChromeOptions() 
driver   = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver', options=options)
driver.get("https://www.basketball-reference.com/leagues/NBA_2020_advanced.html") 


print("I am in the webpage")


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2020")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2020_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2019-20_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,650):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - I finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2019")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2019_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2018-19_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,735):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - II finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2018")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2018_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2017-18_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,691):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - III finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2017")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2017_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2016-17_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,620):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - IV finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2016")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2016_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2015-16_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,602):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - V finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2015")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2015_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2014-15_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,676):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - VI finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2014")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2014_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2013-14_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,636):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - VII finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2013")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2013_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2012-13_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,597):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - VIII finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2012")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2012_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2011-12_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,575):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - IX finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2011")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2011_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2010-11_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,648):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - X finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2010")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2010_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2009-10_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,601):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - XI finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2009")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2009_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2008-09_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,605):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - XII finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2008")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2008_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2007-08_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,618):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - XIII finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2007")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2007_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Admin\Desktop\Pavel\UvA\Thesis\Data\Basketball-reference.com\2006-07_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,539):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - XIV finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2006")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2006_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Admin\Desktop\Pavel\UvA\Thesis\Data\Basketball-reference.com\2005-06_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,586):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - XV finished")
stats.close()


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2005")
#        driver.implicitly_wait(5)
driver.get("https://www.basketball-reference.com/leagues/NBA_2005_advanced.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)
################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

stats = open(r"C:\Users\Pavel\Desktop\UvA\Thesis\Data\Basketball-reference.com\2004-05_Player_Stats_Advanced.csv","a")
content = ('Player,Pos,Age,Team,Games,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%, ,OWS,DWS,WS,WS/48, ,OBPM,DBPM,BPM,VORP')

stats.write(content + "," + "\n")

###expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]/td[2]/span").click
##time.sleep(1)
##expand       = driver.find_element_by_xpath("/html/body/div/div[2]/div/main/article/div/div/div/div/div/div/div/div/div[3]/div/div/div/table/tbody/tr["+ str(row) +"]")
##expand.click()                                
##print("expanded")        
##time.sleep(2)    

for row in range(1,609):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + " " + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + " " + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) +"\n")
        
        print('done ' + str(row))
        time.sleep(0)

print("check - XVI finished")
stats.close()