# -*- coding: utf-8 -*-
"""
Created on Wed May 6 2:08:52 2020

@author: Pavel
"""

# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
#       Basketball Teams Data
#
#       FIRST VERSION  March  25, 2020
#       THIS VERSION   May 14, 2020
#       LAST RUN       May 14, 2020
#
#       LAST REVISOR   Zacharuk
#
#       This scrapes all data from basketball-reference.com that is needed and some extra that is not needed.
# ---------------------------------------------------------------------------

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
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base") 


print("I am in the webpage")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for Miscellaneous Stats in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team;Age;W;L;PW;PL;MOV;SOS;SRS;ORtg;DRtg;NRtg;Pace;FTr;3PAr;TS%;eFG%;TOV%;ORB%;FT/FGA;eFG%;TOV%;DRB%;FT/FGA;Arena;Attend.;Attend./G')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Miscellaneous_Stats.csv","a")
    stats.write(content + "\n")
    if year == 2020:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            try:
                Arena          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
                print(Arena)
            except:
                Arena = ""
            try:
                Attendance          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
                print(Attendance)
            except:
                Attendance = ""
            try:                                                                       
                Attendance_per_game          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
                print(Attendance_per_game)
            except:
                Attendance_per_game = ""
            time.sleep(1)         
            
            stats.write(str(Player) + ";" + str(Pos) + ";" + str(Age) + ";" + str(Team) + ";" + str(Games) + ";" +	str(MP)+ ";" + str(PER) + ";" + str(TS) + ";" + str(PAr_3) + ";" + str(FTr) + ";" + str(ORB) + ";" + str(DRB) + ";" + str(TRB) + ";" + str(AST) + ";" + str(STL) + ";" + str(BLK) + ";" + str(TOV) + ";" + str(USG) + ";" + str(OTK) + ";" + str(OWS) + ";" + str(DWS) + ";" + str(WS) + ";" + str(WS48) + ";" + str(PTS) + ";" + str(Arena) + ";" + str(Attendance) + ";" + str(Attendance_per_game) +"\n")
    else:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            try:
                Arena          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
                print(Arena)
            except:
                Arena = ""
            try:
                Attendance          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
                print(Attendance)
            except:
                Attendance = ""
            try:
                Attendance_per_game          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
                print(Attendance_per_game)
            except:
                Attendance_per_game = ""
            time.sleep(1)         
            
            stats.write(str(Player) + ";" + str(Pos) + ";" + str(Age) + ";" + str(Team) + ";" + str(Games) + ";" +	str(MP)+ ";" + str(PER) + ";" + str(TS) + ";" + str(PAr_3) + ";" + str(FTr) + ";" + str(ORB) + ";" + str(DRB) + ";" + str(TRB) + ";" + str(AST) + ";" + str(STL) + ";" + str(BLK) + ";" + str(TOV) + ";" + str(USG) + ";" + str(OTK) + ";" + str(OWS) + ";" + str(DWS) + ";" + str(WS) + ";" + str(WS48) + ";" + str(PTS) + ";" + str(Arena) + ";" + str(Attendance) + ";" + str(Attendance_per_game) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - VII finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for teams in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020_standings.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team,Overall,Place_Home,Place_Road,Conference_E,Conference_W,Division_A,Division_C,Division_SE,Division_NW,Division_P,Division_SW,All_Star_Pre,All_Star_Post,Margin_u_3,Margin_a_10,Oct,Nov,Dec,Jan,Feb,Mar')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Expanding_Standings.csv","a")
    stats.write(content + "\n")
    for row in range(1,31):
        print(str(row))
        time.sleep(3)
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            DEC          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
            print(DEC)
        except:
            DEC = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        time.sleep(1)         
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(DEC) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) +"\n")
    print('done ' + str(row))
    time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - I finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for opponents in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team,G,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Opponent_Per_Game_Stats.csv","a")
    stats.write(content + "," + "\n")
    if year == 2020:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
    else:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - II finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for opponents in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team,G,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Opponent_Stats.csv","a")
    stats.write(content + "," + "\n")
    if year == 2020:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
    else:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - IV finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for opponent_per_100_poss_stats in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team,G,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Opponent_Per_100_Poss_Stats.csv","a")
    stats.write(content + "," + "\n")
    if year == 2020:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
    else:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[10]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - VI finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for Opponent Shooting in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team,G,MP,FG%,Dist.,2P%_FGA,FGA_dist_0-3,FGA_dist_3-10,FGA_dist_10-16,FGA_dist_16-3pt,FGA_dist_3P,2P%_FG,FG_dist_0-3,FG_dist_3-10,FG_dist_10-16,FG_dist_16-3pt,FG_dist_3P,2PFG_Ast%,2PFG_Dunks_FGA%,2PFG_Dunks_Md,2PFG_Layups_FGA%,2PFG_Layups_Md,3PFG_Ast%,3PFG_Corner_%3PA,3PFG_Corner_3P%')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Opponent_Shooting.csv","a")
    stats.write(content + "," + "\n")
    if year == 2020:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            try:
                Arena          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
                print(Arena)
            except:
                Arena = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) + "," + str(Arena) +"\n")
    else:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            try:
                Arena          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[14]/div[3]/div[2]/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
                print(Arena)
            except:
                Arena = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) + "," + str(Arena) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - IX finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020_per_poss.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Player,Pos,Age,Team,Games,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS,,ORtg,DRtg')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Players_Per_100poss_Stats.csv","a")
    stats.write(content + "," + "\n")
    for row in range(1,780):
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
            OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
            print(OTK)
        except:
            OTK = ""
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
            RTD          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
            print(RTD)
        except:
            RTD = ""
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
        try:
            ORtg          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[29]").get_attribute('innerHTML')).text)
            print(ORtg)
        except:
            ORtg = ""
        try:
            DRtg          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[30]").get_attribute('innerHTML')).text)
            print(DRtg)
        except:
            DRtg = ""
        try:
            GS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[31]").get_attribute('innerHTML')).text)
            print(GS)
        except:
            GS = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(RTD) + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) + "," + str(ORtg) + "," + str(DRtg) + "," + str(GS) + "\n")
        
        print('done ' + str(row))
        time.sleep(0)
        
    stats.close()
    try:
        next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    except:
        try:
            next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a[1]")
        except:
            pass
    next_year.click()
    year = year-1
print("check - I finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2018_per_minute.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Player,Pos,Age,Team,Games,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Players_Per_36mins_Stats.csv","a")
    stats.write(content + "," + "\n")
    for row in range(1,780):
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
            OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
            print(OTK)
        except:
            OTK = ""
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
            RTD          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
            print(RTD)
        except:
            RTD = ""
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
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(RTD) + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) + "\n")
        
        print('done ' + str(row))
        time.sleep(0)
        
    stats.close()
    try:
        next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    except:
        try:
            next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a[1]")
        except:
            pass
    next_year.click()
    year = year-1
print("check - II finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020_per_game.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Player,Pos,Age,Team,Games,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Players_Per_Game.csv","a")
    stats.write(content + "," + "\n")
    for row in range(1,780):
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
            OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
            print(OTK)
        except:
            OTK = ""
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
            RTD          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
            print(RTD)
        except:
            RTD = ""
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
        try:
            idk          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[29]").get_attribute('innerHTML')).text)
            print(idk)
        except:
            idk = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(RTD) + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) + "," + str(idk) + "\n")
        
        print('done ' + str(row))
        time.sleep(0)
        
    stats.close()
    try:
        next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    except:
        try:
            next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a[1]")
        except:
            pass
    next_year.click()
    year = year-1
print("check - III finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for players in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2018_totals.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2018
content = ('Player,Pos,Age,Team,Games,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Players_Totals.csv","a")
    stats.write(content + "," + "\n")
    for row in range(1,780):
        print(str(row))
        time.sleep(3)                                                             
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:                      
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:                                                                                           
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
            print(OTK)
        except:
            OTK = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(WS48)
        except:
            WS48 = ""
        try:
            RTD          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
            print(RTD)
        except:
            RTD = ""
        try:
            OBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(OBPM)
        except:
            OBPM = ""
        try:
            DBPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(DBPM)
        except:
            DBPM = ""
        try:
            BPM          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(BPM)
        except:
            BPM = ""
        try:
            VORP          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(VORP)
        except:
            VORP = ""
        try:
            idk          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/table/tbody/tr["+ str(row) +"]/td[29]").get_attribute('innerHTML')).text)
            print(idk)
        except:
            idk = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(RTD) + "," + str(OBPM) + "," + str(DBPM) + "," + str(BPM) + "," + str(VORP) + "," + str(idk) + "\n")
        
        print('done ' + str(row))
        time.sleep(0)
        
    stats.close()
    try:
        next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    except:
        try:
            next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a[1]")
        except:
            pass
    next_year.click()
    year = year-1
print("check - IV finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for teams in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team,G,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Team_Per_Game_Stats.csv","a")
    stats.write(content + "," + "\n")
    if year == 2020:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
    else:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:                                                                         
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - I finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for teams in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team,G,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Team_Stats.csv","a")
    stats.write(content + "," + "\n")
    if year == 2020:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
    else:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[7]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - III finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for team_per_100_poss_stats in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2010.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2010
content = ('Team,G,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Team_Per_100_Poss_Stats.csv","a")
    stats.write(content + "," + "\n")
    if year == 2020:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[8]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
    else:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - V finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for Team Shooting in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team,G,MP,FG%,Dist.,2P%_FGA,FGA_dist_0-3,FGA_dist_3-10,FGA_dist_10-16,FGA_dist_16-3pt,FGA_dist_3P,2P%_FG,FG_dist_0-3,FG_dist_3-10,FG_dist_10-16,FG_dist_16-3pt,FG_dist_3P,2PFG_Ast%,2PFG_Dunks_FGA%,2PFG_Dunks_Md,2PFG_Layups_FGA%,2PFG_Layups_Md,3PFG_Ast%,3PFG_Dunks_FGA%,3PFG_Dunks_Md,3PFG_Layups_FGA%,3PFG_Layups_Md')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Team_Shooting.csv","a")
    stats.write(content + "," + "\n")
    if year == 2020:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:                                                                      
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            try:
                Arena          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
                print(Arena)
            except:
                Arena = ""
            try:
                Attendance          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
                print(Attendance)
            except:
                Attendance = ""
            try:
                Attendance_per_game          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[12]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
                print(Attendance_per_game)
            except:
                Attendance_per_game = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) + "," + str(Arena) + "," + str(Attendance) + "," + str(Attendance_per_game) +"\n")
    else:
        for row in range(1,31):
            print(str(row))
            time.sleep(3)
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                TS = ""  
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
            try:
                AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(AST)
            except:
                AST = ""
            try:
                STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
                print(STL)
            except:
                STL = ""
            try:
                BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
                print(BLK)
            except:
                BLK = ""
            try:
                TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
                print(TOV)
            except:
                TOV = ""
            try:
                USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
                print(USG)
            except:
                USG = ""
            try:
                OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
                print(OTK)
            except:
                OTK = ""
            try:
                OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
                print(OWS)
            except:
                OWS = ""
            try:
                DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
                print(DWS)
            except:
                DWS = ""
            try:
                WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
                print(WS)
            except:
                WS = ""
            try:
                WS48          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
                print(WS48)
            except:
                WS48 = ""
            try:
                PTS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
                print(PTS)
            except:
                PTS = ""
            try:
                Arena          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
                print(Arena)
            except:
                Arena = ""
            try:
                Attendance          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
                print(Attendance)
            except:
                Attendance = ""
            try:
                Attendance_per_game          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[13]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
                print(Attendance_per_game)
            except:
                Attendance_per_game = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(WS48) + "," + str(PTS) + "," + str(Arena) + "," + str(Attendance) + "," + str(Attendance_per_game) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - VIII finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for teams in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020_standings.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Team,ATL,BOS,BRK,CHI,CHO,CLE,DAL,DEN,DET,GSW,GOU,IND,LAC,LAL,MEM,MIA,MIL,MIN,NOP,NYK,OKC,ORL,PHI,PHO,POR,SAC,SAS,TOR,UTA,WAS')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Teams_vs_Teams.csv","a")
    stats.write(content + "," + "\n")
    for row in range(1,31):
        print(str(row))
        time.sleep(3)
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            STL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(STL)
        except:
            STL = ""
        try:
            BLK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[16]").get_attribute('innerHTML')).text)
            print(BLK)
        except:
            BLK = ""
        try:
            TOV          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[17]").get_attribute('innerHTML')).text)
            print(TOV)
        except:
            TOV = ""
        try:
            USG          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[18]").get_attribute('innerHTML')).text)
            print(USG)
        except:
            USG = ""
        try:
            OTK          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[19]").get_attribute('innerHTML')).text)
            print(OTK)
        except:
            OTK = ""
        try:
            OWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[20]").get_attribute('innerHTML')).text)
            print(OWS)
        except:
            OWS = ""
        try:
            DWS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[21]").get_attribute('innerHTML')).text)
            print(DWS)
        except:
            DWS = ""
        try:
            WS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[22]").get_attribute('innerHTML')).text)
            print(WS)
        except:
            WS = ""
        try:
            ORL          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[23]").get_attribute('innerHTML')).text)
            print(ORL)
        except:
            ORL = ""
        try:
            PHI          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[24]").get_attribute('innerHTML')).text)
            print(PHI)
        except:
            PHI = ""
        try:
            PHO          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[25]").get_attribute('innerHTML')).text)
            print(PHO)
        except:
            PHO = ""
        try:
            POR          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[26]").get_attribute('innerHTML')).text)
            print(POR)
        except:
            POR = ""
        try:
            SAC          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[27]").get_attribute('innerHTML')).text)
            print(SAC)
        except:
            SAC = ""
        try:
            SAS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[28]").get_attribute('innerHTML')).text)
            print(SAS)
        except:
            SAS = ""
        try:
            TOR          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[29]").get_attribute('innerHTML')).text)
            print(TOR)
        except:
            TOR = ""
        try:
            UTA          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[30]").get_attribute('innerHTML')).text)
            print(UTA)
        except:
            UTA = ""
        try:
            WAS          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[3]/div/table/tbody/tr["+ str(row) +"]/td[31]").get_attribute('innerHTML')).text)
            print(WAS)
        except:
            WAS = ""
        time.sleep(1)         
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(STL) + "," + str(BLK) + "," + str(TOV) + "," + str(USG) + "," + str(OTK) + "," + str(OWS) + "," + str(DWS) + "," + str(WS) + "," + str(ORL) + "," + str(PHI) + "," + str(PHO) + "," + str(POR) + "," + str(SAC) + "," + str(SAS) + "," + str(TOR) + "," + str(UTA) + "," + str(WAS) +"\n")
    print('done ' + str(row))
    time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - II finished")


Teams = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets','Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks','Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets','Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies','Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans','New York Knickerbockers','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers','Phoenix Suns','Portland Trailblazers','Sacramento Kings','San Antonio Spurs','Toronto Raptors','Utah Jazz','Washington Wizards']
Teams[25]


###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for teams in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2007
content = ('Date,Start(ET), ,Score,Home_or_Away(@),Opponent,Win/Loss,OT,Points_Team,Points_Opponent,Win,Loss,Streak,Notes')

i = 1
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
team_sort = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div[2]/table/thead/tr/th[2]")
team_sort.click()
next_team = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div[2]/table/tbody/tr[16]/td[1]")
next_team.click()
try:
    more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
    more_dropdown.click()
except:
    try:
       more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
       more_dropdown.click()
    except:
        try:
            more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
            more_dropdown.click()
        except:
            try:
                more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                more_dropdown.click()
            except:
                try:
                    more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                    more_dropdown.click()
                except:
                    try:
                        more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                        more_dropdown.click()
                    except:
                        try:
                            more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                            more_dropdown.click()
                        except:
                            try:
                                more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                more_dropdown.click()
                            except:
                                try:
                                    more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                    more_dropdown.click()
                                except:
                                    try:
                                        more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                        more_dropdown.click()
                                    except:
                                        try:
                                           more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                           more_dropdown.click()
                                        except:
                                            try:
                                                more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                                more_dropdown.click()
                                            except:
                                                try:
                                                    more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                                    more_dropdown.click()
                                                except:
                                                    try:
                                                        more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                                        more_dropdown.click()
                                                    except:
                                                        try:
                                                            more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                                            more_dropdown.click()
                                                        except:
                                                            try:
                                                                more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                                                more_dropdown.click()
                                                            except:
                                                                more_dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/a")
                                                                more_dropdown.click()
try:
    schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
    schedule_result.click()
except:
    try:
        schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
        schedule_result.click()
    except:
        try:
            schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
            schedule_result.click()
        except:
            try:
                schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                schedule_result.click()
            except:
                try:
                    schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                    schedule_result.click()
                except:
                    try:
                        schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                        schedule_result.click()
                    except:
                        try:
                            schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                            schedule_result.click()
                        except:
                            try:
                                schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                                schedule_result.click()
                            except:
                                try:
                                    schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                                    schedule_result.click()
                                except:
                                    try:
                                        schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                                        schedule_result.click()
                                    except:
                                        try:
                                            schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                                            schedule_result.click()
                                        except:
                                            try:
                                                schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                                                schedule_result.click()
                                            except:
                                                try:
                                                    schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                                                    schedule_result.click()
                                                except:
                                                    try:
                                                        schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                                                        schedule_result.click()
                                                    except:
                                                            schedule_result = driver.find_element_by_xpath("/html/body/div[2]/div[4]/ul/li[6]/div/ul/li[2]/a")
                                                            schedule_result.click()
                                    
driver.get("https://www.basketball-reference.com/teams/SAC/2007_games.html")
year = 2007

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_" + str(Teams[i]) + "_Regular_Season_Results.csv","a")
    stats.write(content + "," + "\n")
    for row in range(1,87):
        print(str(row))
        time.sleep(3)
        try:                                                                       
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
            print (Player)
        except:
            try:
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print(Player)
            except:
                Player = ""
        try:
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)
        except:
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)     
            except:
                Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                MP = ""
        try:
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                    TS = ""   
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                TRB = ""
        try:
            Notes          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(Notes)
        except:
            try:
                Notes          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(Notes)
            except:
                Notes = ""
        time.sleep(1)         
        
        stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(Notes) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - III finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for teams in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content_per_game = ('Name,Age,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS/G')

for i in range(0,30):
    driver.get("https://www.basketball-reference.com/leagues/NBA_2020.html#all_team-stats-base")
    team_sort = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div[2]/table/thead/tr/th[2]")
    team_sort.click()
    next_team = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[6]/div[3]/div[2]/table/tbody/tr["+ str(i+1) +"]/td[1]")
    next_team.click()
                                            
    year = 2020
    
    while year > 2004:  
        stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_" + str(Teams[i]) + "_Regular_Season_Player_Stats_Per_Game.csv","a")
        stats.write(content + "," + "\n")
        for row in range(1,87):
            print(str(row))
            time.sleep(3)
            try:                                                                       
                Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                print (Player)
            except:
                try:
                    Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1]").get_attribute('innerHTML')).text)
                    print(Player)
                except:
                    Player = ""
            try:
                Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                print (Pos)
            except:
                try:
                    Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
                    print (Pos)
                except:
                    Pos = ""
            try:
                Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                print (Age)
            except:
                try:
                    Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
                    print (Age)
                except:
                    Age = ""
            try:
                Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                print(Team) 
            except:
                try:
                    Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
                    print(Team) 
                except:
                    Team = ""                                        
            try:
                Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                print(Games)
            except:
                try:
                    Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
                    print(Games)     
                except:
                    Games = ""                                                      
            try:
                MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                print(MP)
            except:
                try:
                    MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
                    print(MP)
                except:
                    MP = ""
            try:
                PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                print(PER)
            except:
                try:
                    PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
                    print(PER)
                except:
                    PER = ""
            try:
                TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                print(TS)
            except:
                try:
                    TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
                    print(TS)
                except:
                        TS = ""   
            try:
                PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                print(PAr_3)
            except:
                try:
                    PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
                    print(PAr_3)
                except:
                    PAr_3 = ""   
            try:
                FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                print(FTr)
            except:
                try:
                    FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
                    print(FTr)
                except:
                    FTr = "" 
            try:
                ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                print(ORB)
            except:
                try:
                    ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
                    print(ORB)
                except:
                    ORB = ""
            try:
                DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                print(DRB)
            except:
                try:
                    DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
                    print(DRB)
                except:
                    DRB = ""
            try:
                TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                print(TRB)
            except:
                try:
                    TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
                    print(TRB)
                except:
                    TRB = ""
            try:
                Notes          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                print(Notes)
            except:
                try:
                    Notes          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
                    print(Notes)
                except:
                    Notes = ""
            time.sleep(1)         
            
            stats.write(str(Player) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(Notes) +"\n")
            print('done ' + str(row))
            time.sleep(0)
        stats.close()
        next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
        next_year.click()
        year = year-1
print("check - III finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for schedule in playoff in 2019")
driver.get("https://www.basketball-reference.com/playoffs/NBA_2019_games.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2019
content = ('Date;Start(ET);Visitor/Neutral;PTS;Home/Neutral;PTS;;;Attend.;Notes')
driver.get("https://www.basketball-reference.com/playoffs/NBA_2019_games.html")         

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_" + "_Play_Off_Schedule.csv","a")
    stats.write(content + ";" + "\n")
    for row in range(1,87):
        print(str(row))
        time.sleep(3)
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/th/a").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2]/a ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:                                   
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4]/a").get_attribute('innerHTML')).text)   
            print(Games)
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""   
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        time.sleep(1)         
        
        stats.write(str(Player) + ";" + str(Pos) + ";" + str(Age) + ";" + str(Team) + ";" + str(Games) + ";" +	str(MP)+ ";" + str(PER) + ";" + str(TS) + ";" + str(PAr_3) + ";" + str(FTr) +"\n")
        print('done ' + str(row))
        time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - IV finished")

###############################################################################################
####        3. Open page                                                                   ####
###############################################################################################

print ("I am getting information for coaches in 2020")
driver.get("https://www.basketball-reference.com/leagues/NBA_2020_coaches.html")
#pyautogui.hotkey('f5')
#driver.find_element_by_xpath("//*[@id='sfs_ContentBased']/div[1]/div/table/tbody/tr/td[2]/div/div/button").submit()
#driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span").click
#expand       = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[4]/div[1]/div/ul/li[5]/span")
#expand.click()
time.sleep(5)

################################################################################################
#####        4. Get everybody                                                               ####
################################################################################################

year = 2020
content = ('Coach,Team,,Seasons_w_Franch,Seasons_Overall,,Regular_Season_Current_Games,Regular_Season_Current_Wins,Regular_Season_Current_Loss,Regular_Season_w_Franchise_Games,Regular_Season_w_Franchise_Wins,Regular_Season_w_Franchise_Loss,Regular_Season_Career_Games,Regular_Season_Career_Wins,Regular_Season_Career_Loss,Regular_Season_Career_W%')

while year > 2004:  
    stats = open("C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\" + str(year-1) + "-" + str(year)[2:4] + "_Coach_Stats.csv","a")
    stats.write(content + "," + "\n")
    for row in range(1,50):
        print(str(row))
        time.sleep(3)
        try:
            Player         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/th").get_attribute('innerHTML')).text)
            print (Player)
        except:
            Player = ""
        try:
            Tm       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[1] ").get_attribute('innerHTML')).text)
            print (Tm)
        except:
            Tm = ""
        try:                                                                 
            Pos       = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[2] ").get_attribute('innerHTML')).text)
            print (Pos)
        except:
            Pos = ""
        try:
            Age         = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[3] ").get_attribute('innerHTML')).text)
            print (Age)
        except:
            Age = ""
        try:
            Team     = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[4] ").get_attribute('innerHTML')).text)            
            print(Team) 
        except:
            Team = ""                                        
        try:
            Games          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[5]").get_attribute('innerHTML')).text)   
            print(Games)     
        except:
            Games = ""                                                      
        try:
            MP        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[6]").get_attribute('innerHTML')).text)
            print(MP)
        except:
            MP = ""
        try:
            PER          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[7]").get_attribute('innerHTML')).text)
            print(PER)
        except:
            PER = ""
        try:
            TS        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[8]").get_attribute('innerHTML')).text)
            print(TS)
        except:
            TS = ""  
        try:
            PAr_3        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[9]").get_attribute('innerHTML')).text)
            print(PAr_3)
        except:
            PAr_3 = ""   
        try:
            FTr        = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[10]").get_attribute('innerHTML')).text)
            print(FTr)
        except:
            FTr = "" 
        try:
            ORB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[11]").get_attribute('innerHTML')).text)
            print(ORB)
        except:
            ORB = ""
        try:
            DRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[12]").get_attribute('innerHTML')).text)
            print(DRB)
        except:
            DRB = ""
        try:
            TRB          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[13]").get_attribute('innerHTML')).text)
            print(TRB)
        except:
            TRB = ""
        try:
            AST          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[14]").get_attribute('innerHTML')).text)
            print(AST)
        except:
            AST = ""
        try:
            WR          = unidecode(BeautifulSoup(driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr["+ str(row) +"]/td[15]").get_attribute('innerHTML')).text)
            print(WR)
        except:
            WR = ""
        time.sleep(1)         
        stats.write(str(Player) + "," + str(Tm) + "," + str(Pos) + "," + str(Age) + "," + str(Team) + "," + str(Games) + "," +	str(MP)+ "," + str(PER) + "," + str(TS) + "," + str(PAr_3) + "," + str(FTr) + "," + str(ORB) + "," + str(DRB) + "," + str(TRB) + "," + str(AST) + "," + str(WR) +"\n")
    print('done ' + str(row))
    time.sleep(0)
    stats.close()
    next_year = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/a")
    next_year.click()
    year = year-1
print("check - I finished")