# -*- coding: utf-8 -*-
"""
Created on Mon May 25 00:17:23 2020

@author: Pavel Zacharuk
"""

# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------------------------------------------------------
#       Basketball Teams Data
#
#       FIRST VERSION  May  25, 2020
#       THIS VERSION   July 7, 2020
#       LAST RUN       July 9, 2020
#
#       LAST REVISOR   Zacharuk
#
#       This loads all data and manages all tables into easier to work with form. 
#       Then further defines the models for regression and analyzes the results.
#       This code also creates our own features, for further detail please see the thesis that is connected with this code.
# -------------------------------------------------------------------------------------------------------------------------------

# Load packages
import os
import pandas as pd
import numpy as np
from io import StringIO
import re
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from math import cos, sin, atan
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from statsmodels.tools.tools import add_constant

import keras
import tensorflow
import itertools
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model
from tensorflow.keras import losses
from tensorflow.keras import optimizers
from tensorflow.keras import backend
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from keras.wrappers.scikit_learn import KerasClassifier
import pydot
import graphviz


# Create dictionary with dictionaries where we later save all the dataframes and create list of files in our directory
dicts = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
list_of_files = ['Coach_Stats','Expanding_Standings','Individual_teams_Regular_Season_Standings','Miscellaneous Stats','Opponent Per Game Statistics','Opponent Statistics','Opponent_Per_100_Poss_Stats','Opponent_Shooting','Player statistics','Players_Per_36mins','Players_Per_100poss','Players_Per_Game','Players_Totals','Team Per Game Statistics','Team Statistics','Team_Per_100_Poss_Stats','Team_Shooting','Team_vs_Team','ZPlay_Off']

# Loop to load all data files
for i in range(0,19):
    directory = "C:\\Users\\Admin\\Desktop\\Pavel\\UvA\\Thesis\\Data\\Basketball-reference.com\\"+str(list_of_files[i])+"\\CSV"
    for root,dirs,files in os.walk(directory):
        os.chdir(directory)
        for file in files:
           if file.endswith(".csv"):
               if i == 2:
                   col_names = ["Date","Start(ET)"," ","Score","Home_or_Away(@)","Opponent","Win/Loss","OT","Points_Team","Points_Opponent","Win","Loss","Streak"]
                   for_pd = StringIO()
                   with open(file) as team_dat:
                       lines_to_edit = team_dat.readlines()
                       print(lines_to_edit[0], file=for_pd)
                       lines_to_edit = lines_to_edit[1:]
                       for line in lines_to_edit:
                           new_line = re.sub(r',', '/', line.rstrip(), count=2)
                           print (new_line, file=for_pd)
                       for_pd.seek(0)
                   dicts[i][file] = pd.read_csv(for_pd, names = col_names, index_col = False, skiprows = [0])
               elif i == 17:
                   col_names = ["Team","ATL","BOS","BRK","CHI","CHO","CLE","DAL","DEN","DET","GSW","GOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","NYK","OKC","ORL","PHI","PHO","POR","SAC","SAS","TOR","UTA","WAS"]
                   dicts[i][file] = pd.read_csv(file, names = col_names, skiprows = [0])
               elif (i == 3 or i == 18):
                   dicts[i][file] = pd.read_csv(file, sep = ';')
               elif i == 8:
                   dicts[i][file] = pd.read_csv(file, usecols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27])
               else:
                   dicts[i][file] = pd.read_csv(file)


# Remove rows with only NaN in all Dataframes
new_alist = []
for i,d in enumerate(dicts):                   #traverse the list
       temp = {} 
       for key,val in d.items():
           val = val.dropna(thresh=2,axis = 0)
           val = val.dropna(how = 'all',axis = 1)
           temp[key] = val
       new_alist.append(temp)                      #add the updated `dict`


# I want to see if Players Efficiency Rating (PER) per minute is lowering with age, it's not. I don't want to print this every time, so just run this piece the first time.
#for i,d in enumerate(dicts):
#    if i == 8:
#        for key,val in d.items():
#           plt.scatter(new_alist[i][key].iloc[:,2],new_alist[i][key].iloc[:,6]) 
#           plt.show()


# Now we will assign every player to the team (many players have more than one team that they played for) based on the highest games played for each team, the team he played most games in is going to be the team that the player is going to be assigned to, then the PER this PER is taken
Players_PER = []
for i,d in enumerate(dicts):                   #traverse the list
    if i == 8:       
        temp = {} 
        for key,val in d.items():
            names = new_alist[i][key].iloc[:,0].unique()
            df_temp = pd.DataFrame()
            for j in names:
                stats = new_alist[i][key].loc[(new_alist[i][key]["Player"]==j),:]
                stats = stats.loc[stats["Games"] == stats.iloc[:,4].max(),:]
                df_temp = df_temp.append(stats)
            df_temp.reset_index(drop = True)
            temp[key] = df_temp
        Players_PER.append(temp)                      #add the updated `dict`


# Now we will assign strength to each team, we take the sum of 8 highest PER of each team's players
Teams_PER = []
for i,d in enumerate(Players_PER):                   #traverse the list     
    temp = {} 
    for key,val in d.items():
        teams = Players_PER[i][key].iloc[:,3].unique()
        df_temp = pd.DataFrame()
        for j in teams:
            stats = Players_PER[i][key].loc[(Players_PER[i][key]["Team"]==j),:]
            stats = pd.DataFrame([(j,stats['PER'].nlargest(8).sum())],columns = ['Team','Team_PER'])
            df_temp = df_temp.append(stats)
        df_temp = df_temp.reset_index(drop = True)
        temp[key] = df_temp
    Teams_PER.append(temp)                      #add the updated `dict`
    
    
# Team Names Chronology : https://www.nba.com/celtics/history/nba-teams-chronology
Team_Names = {'Atlanta Hawks' : {'Atlanta Hawks','Atlanta Hawks*'},
              'Boston Celtics' : {'Boston Celtics','Boston Celtics*'},
              'Brooklyn Nets' : {'New Jersey Nets','Brooklyn Nets','New Jersey Nets*','Brooklyn Nets*'},
              'Charlotte Hornets':{'Charlotte Bobcats','Charlotte Hornets','Charlotte Bobcats*','Charlotte Hornets*'},
              'Chicago Bulls' : {'Chicago Bulls','Chicago Bulls*'},
              'Cleveland Cavaliers' : {'Cleveland Cavaliers','Cleveland Cavaliers*'},
              'Dallas Mavericks' : {'Dallas Mavericks','Dallas Mavericks*'},
              'Denver Nuggets' : {'Denver Nuggets','Denver Nuggets*'},
              'Detroit Pistons' : {'Detroit Pistons','Detroit Pistons*'},
              'Golden State Warriors' : {'Golden State Warriors','Golden State Warriors*'},
              'Houston Rockets' : {'Houston Rockets','Houston Rockets*'},
              'Indiana Pacers' : {'Indiana Pacers','Indiana Pacers*'},
              'Los Angeles Clippers' : {'Los Angeles Clippers','Los Angeles Clippers*'},
              'Los Angeles Lakers' : {'Los Angeles Lakers','Los Angeles Lakers*'},
              'Memphis Grizzlies' : {'Memphis Grizzlies','Memphis Grizzlies*'},
              'Miami Heat' : {'Miami Heat','Miami Heat*'},
              'Milwaukee Bucks' : {'Milwaukee Bucks','Milwaukee Bucks*'},
              'Minnesota Timberwolves' : {'Minnesota Timberwolves','Minnesota Timberwolves*'},
              'New Orleans Pelicans' : {'New Orleans Hornets','Oklahoma City Hornets','New Orleans Pelicans','New Orleans/Oklahoma City Hornets','New Orleans Hornets*','Oklahoma City Hornets*','New Orleans Pelicans*','New Orleans/Oklahoma City Hornets*'},
              'New York Knickerbockers' : {'New York Knickerbockers','New York Knickerbockers*','New York Knicks','New York Knicks*'},
              'Oklahoma City Thunder' : {'Seattle SuperSonics','Oklahoma City Thunder','Seattle SuperSonics*','Oklahoma City Thunder*'},
              'Orlando Magic' : {'Orlando Magic','Orlando Magic*'},
              'Philadelphia 76ers' : {'Philadelphia 76ers','Philadelphia 76ers*'},
              'Phoenix Suns' : {'Phoenix Suns','Phoenix Suns*'},
              'Portland Trailblazers' : {'Portland Trailblazers','Portland Trailblazers*','Portland Trail Blazers','Portland Trail Blazers*'},
              'Sacramento Kings':{'Sacramento Kings','Sacramento Kings*'},
              'San Antonio Spurs' : {'San Antonio Spurs','San Antonio Spurs*'},
              'Toronto Raptors' : {'Toronto Raptors','Toronto Raptors*'},
              'Utah Jazz' : {'Utah Jazz','Utah Jazz*'},
              'Washington Wizards' : {'Washington Wizards','Washington Wizards*'}}

Team_Shortened = {'Atlanta Hawks':['ATL'],
                  'Boston Celtics':['BOS'],
                  'Brooklyn Nets':['BRK','NJN'],
                  'Charlotte Hornets':['CHO','CHB','CHA'],
                  'Chicago Bulls':['CHI'],
                  'Cleveland Cavaliers':['CLE'],
                  'Dallas Mavericks':['DAL'],
                  'Denver Nuggets':['DEN'],
                  'Detroit Pistons':['DET'],
                  'Golden State Warriors':['GSW'],
                  'Houston Rockets':['HOU'],
                  'Indiana Pacers':['IND'],
                  'Los Angeles Clippers':['LAC'],
                  'Los Angeles Lakers':['LAL'],
                  'Memphis Grizzlies':['MEM'],
                  'Miami Heat':['MIA'],
                  'Milwaukee Bucks':['MIL'],
                  'Minnesota Timberwolves':['MIN'],
                  'New Orleans Pelicans':['NOP','NOH','NOK'],
                  'New York Knickerbockers':['NYK'],
                  'Oklahoma City Thunder':['OKC','SEA'],
                  'Orlando Magic':['ORL'],
                  'Philadelphia 76ers':['PHI'],
                  'Phoenix Suns':['PHO'],
                  'Portland Trailblazers':['POR'],
                  'Sacramento Kings':['SAC'],
                  'San Antonio Spurs':['SAS'],
                  'Toronto Raptors':['TOR'],
                  'Utah Jazz':['UTA'],
                  'Washington Wizards':['WAS']}

Team_Index = {'Atlanta Hawks':[0],
                  'Boston Celtics':[1],
                  'Brooklyn Nets':[2],
                  'Charlotte Hornets':[3],
                  'Chicago Bulls':[4],
                  'Cleveland Cavaliers':[5],
                  'Dallas Mavericks':[6],
                  'Denver Nuggets':[7],
                  'Detroit Pistons':[8],
                  'Golden State Warriors':[9],
                  'Houston Rockets':[10],
                  'Indiana Pacers':[11],
                  'Los Angeles Clippers':[12],
                  'Los Angeles Lakers':[13],
                  'Memphis Grizzlies':[14],
                  'Miami Heat':[15],
                  'Milwaukee Bucks':[16],
                  'Minnesota Timberwolves':[17],
                  'New Orleans Pelicans':[18],
                  'New York Knickerbockers':[19],
                  'Oklahoma City Thunder':[20],
                  'Orlando Magic':[21],
                  'Philadelphia 76ers':[22],
                  'Phoenix Suns':[23],
                  'Portland Trailblazers':[24],
                  'Sacramento Kings':[25],
                  'San Antonio Spurs':[26],
                  'Toronto Raptors':[27],
                  'Utah Jazz':[28],
                  'Washington Wizards':[29]}

# Here I create dataframe for each team with results of each team against their opponents during years 2004 to 2020
new_target = []
for i,d in enumerate(new_alist):                   #traverse the list
    if i == 2:   
        for k,v in Team_Names.items():
            temp = {}
            for key,val in d.items():
                if any(s in key for s in v):
                    try:
                        temp[k] = temp[k].append(val)
                    except KeyError:
                        temp[k] = val
                else:
                    pass
            new_target.append(temp)
            
# Put only new names of teams in the new_target
for i,d in enumerate(new_target):                   #traverse the list   
    for key,val in d.items():
        for r in range(len(val)):
            for k,v in Team_Names.items():
                if val.iloc[r,4] in v:
                    val.iloc[r,4] = k

# Here I create dataframe for play off schedule with results of each team against their opponents in play_offs during years 2004 to 2019
new_target_play_off = []
for i,d in enumerate(new_alist):                   #traverse the list
    if i == 18:   
        temp = {}
        for key,val in d.items():
            try:
                temp[key] = temp[key].append(val)
            except KeyError:
                temp[key] = val
        new_target_play_off.append(temp)
            
# Put only new names of teams in the new_target
for i,d in enumerate(new_target_play_off):                   #traverse the list   
    for key,val in d.items():
        for r in range(len(val)):
            for k,v in Team_Names.items():
                if val.iloc[r,2] in v:
                    val.iloc[r,2] = k
                if val.iloc[r,4] in v:
                    val.iloc[r,4] = k

# I create target variable, 1 for a win and 0 for loss
t = []
for i,d in enumerate(new_target):                   #traverse the list   
    for key,val in d.items():
        temp = {}
        dummies = val['Win/Loss']=='W'
        dummies = dummies * 1
        temp[key] = dummies
        t.append(temp)
        
t_play_off = []
for i,d in enumerate(new_target_play_off):                   #traverse the list   
    for key,val in d.items():
        temp = {}
        temp_df = pd.DataFrame(columns=['Dummy'])
        # First a dummy for the home win or loss and then visitor win or loss
        for r in range(len(val)):
            if (val.iloc[r,3] - val.iloc[r,5]) < 0:
                dummy = 1
                temp_df = temp_df.append({'Dummy':dummy},ignore_index=True)
            else:
                dummy = 0
                temp_df = temp_df.append({'Dummy':dummy},ignore_index=True)
        # visitor
        for r in range(len(val)):
            if (val.iloc[r,3] - val.iloc[r,5]) > 0:
                dummy = 1
                temp_df = temp_df.append({'Dummy':dummy},ignore_index=True)
            else:
                dummy = 0
                temp_df = temp_df.append({'Dummy':dummy},ignore_index=True)
        temp[key] = temp_df
        t_play_off.append(temp)

# Now I create independant variables x, with normalized variables
new_hyperparameters = []
for i,d in enumerate(new_alist):                   #traverse the list
    if i == 3:   
        for k,v in Team_Names.items():
            temp = {}                            # should have 16 rows all the time for every data frame
            for key,val in d.items():
                interesting_stats = val.loc[val.iloc[:,0].isin(v),:]
                wins = pd.Series(interesting_stats.iloc[:,2]/(interesting_stats.iloc[:,2]+interesting_stats.iloc[:,3]))
                wins = wins.rename('WR')
                interesting_stats = interesting_stats.join(wins)
                try:
                    temp[k] = temp[k].append(interesting_stats)
                except KeyError:
                    temp[k] = interesting_stats
            temp[k] = temp[k].reset_index(drop = True)
            temp[k] = temp[k].iloc[:,[1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,27]]
            # Now I rescale variables that are not percentage already
            temp[k].iloc[:,0] = preprocessing.scale(temp[k].iloc[:,0])
            temp[k].iloc[:,1] = preprocessing.scale(temp[k].iloc[:,1])
            temp[k].iloc[:,2] = preprocessing.scale(temp[k].iloc[:,2])
            temp[k].iloc[:,3] = preprocessing.scale(temp[k].iloc[:,3])
            temp[k].iloc[:,4] = preprocessing.scale(temp[k].iloc[:,4])
            temp[k].iloc[:,5] = preprocessing.scale(temp[k].iloc[:,5])
            temp[k].iloc[:,6] = preprocessing.scale(temp[k].iloc[:,6])
            temp[k].iloc[:,7] = preprocessing.scale(temp[k].iloc[:,7])
            temp[k].iloc[:,12] = temp[k].iloc[:,12]*0.01
            temp[k].iloc[:,13] = temp[k].iloc[:,13]*0.01
            temp[k].iloc[:,16] = temp[k].iloc[:,16]*0.01
            temp[k].iloc[:,17] = temp[k].iloc[:,17]*0.01
            new_hyperparameters.append(temp)

j=0
for i,d in enumerate(Teams_PER):                   #traverse the list  
    for k,v in Team_Names.items():
        temp = {}                                # should have 16 rows all the time for every data frame
        for s,f in Team_Shortened.items():
            if any(a in s for a in v):
                for key,val in d.items():
                    if len(f) == 1:
                        interesting_stats = val.loc[val.iloc[:,0] == f[0],:]
                    elif len(f) == 2:
                        if any(a == f[0] for a in val.iloc[:,0]):
                            interesting_stats = val.loc[val.iloc[:,0] == f[0],:]
                        elif any(a == f[1] for a in val.iloc[:,0]):
                            interesting_stats = val.loc[val.iloc[:,0] == f[1],:]
                    elif len(f) == 3:
                        if any(a == f[0] for a in val.iloc[:,0]):
                            interesting_stats = val.loc[val.iloc[:,0] == f[0],:]
                        elif any(a == f[1] for a in val.iloc[:,0]):
                            interesting_stats = val.loc[val.iloc[:,0] == f[1],:]
                        elif any(a == f[2] for a in val.iloc[:,0]):
                            interesting_stats = val.loc[val.iloc[:,0] == f[2],:]
                    try:
                        temp[k] = temp[k].append(interesting_stats)
                    except KeyError:
                        temp[k] = interesting_stats
        temp[k].columns = ['skip','Team_PER']
        temp[k] = temp[k].reset_index(drop = True)
        temp[k].iloc[:,1] = preprocessing.scale(temp[k].iloc[:,1])
        new_hyperparameters[j][k] = new_hyperparameters[j][k].join(temp[k].iloc[:,1])
        j = j+1


for i,d in enumerate(new_alist):                   #traverse the list  
    if i == 13:                                   # Get points made by the team per game
        j = 0
        for k,v in Team_Names.items():
            temp = {}                                # should have 16 rows all the time for every data frame
            for key,val in d.items():
                interesting_stats = val.loc[val.iloc[:,0].isin(v),:]
                try:
                    temp[k] = temp[k].append(interesting_stats)
                except KeyError:
                    temp[k] = interesting_stats
            temp[k] = temp[k].reset_index(drop = True)
            temp[k] = temp[k].iloc[:,[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]]
            # Now Scale all the variables that are not percentage
            temp[k].iloc[:,0] = preprocessing.scale(temp[k].iloc[:,0])
            temp[k].iloc[:,1] = preprocessing.scale(temp[k].iloc[:,1])
            temp[k].iloc[:,2] = preprocessing.scale(temp[k].iloc[:,2])
            temp[k].iloc[:,4] = preprocessing.scale(temp[k].iloc[:,4])
            temp[k].iloc[:,5] = preprocessing.scale(temp[k].iloc[:,5])
            temp[k].iloc[:,7] = preprocessing.scale(temp[k].iloc[:,7])
            temp[k].iloc[:,8] = preprocessing.scale(temp[k].iloc[:,8])
            temp[k].iloc[:,10] = preprocessing.scale(temp[k].iloc[:,10])
            temp[k].iloc[:,11] = preprocessing.scale(temp[k].iloc[:,11])
            temp[k].iloc[:,13] = preprocessing.scale(temp[k].iloc[:,13])
            temp[k].iloc[:,14] = preprocessing.scale(temp[k].iloc[:,14])
            temp[k].iloc[:,15] = preprocessing.scale(temp[k].iloc[:,15])
            temp[k].iloc[:,16] = preprocessing.scale(temp[k].iloc[:,16])
            temp[k].iloc[:,17] = preprocessing.scale(temp[k].iloc[:,17])
            temp[k].iloc[:,18] = preprocessing.scale(temp[k].iloc[:,18])
            temp[k].iloc[:,19] = preprocessing.scale(temp[k].iloc[:,19])
            temp[k].iloc[:,20] = preprocessing.scale(temp[k].iloc[:,20])
            temp[k].iloc[:,21] = preprocessing.scale(temp[k].iloc[:,21])
            new_hyperparameters[j][k] = new_hyperparameters[j][k].join(temp[k], rsuffix = '_Team')
            j = j+1
    elif i == 4:                                   # Get points made by the Opponent per game
        j = 0
        for k,v in Team_Names.items():
            temp = {}                                # should have 16 rows all the time for every data frame
            for key,val in d.items():
                interesting_stats = val.loc[val.iloc[:,0].isin(v),:]
                try:
                    temp[k] = temp[k].append(interesting_stats)
                except KeyError:
                    temp[k] = interesting_stats
            temp[k] = temp[k].reset_index(drop = True)
            temp[k] = temp[k].iloc[:,[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]]
            # Now Scale all the variables that are not percentage
            temp[k].iloc[:,0] = preprocessing.scale(temp[k].iloc[:,0])
            temp[k].iloc[:,1] = preprocessing.scale(temp[k].iloc[:,1])
            temp[k].iloc[:,2] = preprocessing.scale(temp[k].iloc[:,2])
            temp[k].iloc[:,4] = preprocessing.scale(temp[k].iloc[:,4])
            temp[k].iloc[:,5] = preprocessing.scale(temp[k].iloc[:,5])
            temp[k].iloc[:,7] = preprocessing.scale(temp[k].iloc[:,7])
            temp[k].iloc[:,8] = preprocessing.scale(temp[k].iloc[:,8])
            temp[k].iloc[:,10] = preprocessing.scale(temp[k].iloc[:,10])
            temp[k].iloc[:,11] = preprocessing.scale(temp[k].iloc[:,11])
            temp[k].iloc[:,13] = preprocessing.scale(temp[k].iloc[:,13])
            temp[k].iloc[:,14] = preprocessing.scale(temp[k].iloc[:,14])
            temp[k].iloc[:,15] = preprocessing.scale(temp[k].iloc[:,15])
            temp[k].iloc[:,16] = preprocessing.scale(temp[k].iloc[:,16])
            temp[k].iloc[:,17] = preprocessing.scale(temp[k].iloc[:,17])
            temp[k].iloc[:,18] = preprocessing.scale(temp[k].iloc[:,18])
            temp[k].iloc[:,19] = preprocessing.scale(temp[k].iloc[:,19])
            temp[k].iloc[:,20] = preprocessing.scale(temp[k].iloc[:,20])
            temp[k].iloc[:,21] = preprocessing.scale(temp[k].iloc[:,21])
            new_hyperparameters[j][k] = new_hyperparameters[j][k].join(temp[k], rsuffix = '_Opp')
            j = j+1
    elif i == 0:                                # Getting coach win loss ratio
        j = 0
        for k,v in Team_Shortened.items():
            temp = {}
            for key,val in d.items():
                if len(v) == 1:
                    coaches = val.loc[val.iloc[:,1] == v[0],:]                    
                elif len(v) == 2:
                    if any(a == v[0] for a in val.iloc[:,1]):
                        coaches = val.loc[val.iloc[:,1] == v[0],:]
                    elif any(a == v[1] for a in val.iloc[:,1]):
                        coaches = val.loc[val.iloc[:,1] == v[1],:]
                elif len(v) == 3:
                    if any(a == v[0] for a in val.iloc[:,1]):
                        coaches = val.loc[val.iloc[:,1] == v[0],:]
                    elif any(a == v[1] for a in val.iloc[:,1]):
                        coaches = val.loc[val.iloc[:,1] == v[1],:]
                    elif any(a == v[2] for a in val.iloc[:,1]):
                        coaches = val.loc[val.iloc[:,1] == v[2],:]
                weight = coaches.iloc[:,4]/coaches.iloc[:,4].sum()
                WL = coaches.iloc[:,-1]*weight
                WL = pd.Series(WL.sum())
                try:
                    temp[k] = temp[k].append(WL)
                except KeyError:
                    temp[k] = WL
            temp[k] = temp[k].reset_index(drop = True)
            temp[k] = temp[k].rename('Coach_WR')
            new_hyperparameters[j][k] = new_hyperparameters[j][k].join(temp[k])
            j = j+1


# Now I create independant variables x, with not normalized variables
#new_hyperparameters_un = []
#for i,d in enumerate(new_alist):                   #traverse the list
#    if i == 3:   
#        for k,v in Team_Names.items():
#            temp = {}                            # should have 16 rows all the time for every data frame
#            for key,val in d.items():
#                interesting_stats = val.loc[val.iloc[:,0].isin(v),:]
#                wins = pd.Series(interesting_stats.iloc[:,2]/interesting_stats.iloc[:,3])
#                wins = wins.rename('WR')
#                interesting_stats = interesting_stats.join(wins)
#                try:
#                    temp[k] = temp[k].append(interesting_stats)
#                except KeyError:
#                    temp[k] = interesting_stats
#            temp[k] = temp[k].reset_index(drop = True)
#            temp[k] = temp[k].iloc[:,[1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,27]]
#            temp[k].iloc[:,12] = temp[k].iloc[:,12]*0.01
#            temp[k].iloc[:,13] = temp[k].iloc[:,13]*0.01
#            temp[k].iloc[:,16] = temp[k].iloc[:,16]*0.01
#            temp[k].iloc[:,17] = temp[k].iloc[:,17]*0.01
#            new_hyperparameters_un.append(temp)

#j=0
#for i,d in enumerate(Teams_PER):                   #traverse the list  
#    for k,v in Team_Names.items():
#        temp = {}                                # should have 16 rows all the time for every data frame
#        for s,f in Team_Shortened.items():
#            if any(a in s for a in v):
#                for key,val in d.items():
#                    if len(f) == 1:
#                        interesting_stats = val.loc[val.iloc[:,0] == f[0],:]
#                    elif len(f) == 2:
#                        if any(a == f[0] for a in val.iloc[:,0]):
#                            interesting_stats = val.loc[val.iloc[:,0] == f[0],:]
#                        elif any(a == f[1] for a in val.iloc[:,0]):
#                            interesting_stats = val.loc[val.iloc[:,0] == f[1],:]
#                    elif len(f) == 3:
#                        if any(a == f[0] for a in val.iloc[:,0]):
#                            interesting_stats = val.loc[val.iloc[:,0] == f[0],:]
#                        elif any(a == f[1] for a in val.iloc[:,0]):
#                            interesting_stats = val.loc[val.iloc[:,0] == f[1],:]
#                        elif any(a == f[2] for a in val.iloc[:,0]):
#                            interesting_stats = val.loc[val.iloc[:,0] == f[2],:]
#                    try:
#                        temp[k] = temp[k].append(interesting_stats)
#                    except KeyError:
#                        temp[k] = interesting_stats
#        temp[k].columns = ['skip','Team_PER']
#        temp[k] = temp[k].reset_index(drop = True)
        #temp[k].iloc[:,1] = preprocessing.scale(temp[k].iloc[:,1])
#        new_hyperparameters_un[j][k] = new_hyperparameters_un[j][k].join(temp[k].iloc[:,1])
#        j = j+1


#for i,d in enumerate(new_alist):                   #traverse the list  
#    if i == 13:                                   # Get points made by the team per game
#        j = 0
#        for k,v in Team_Names.items():
#            temp = {}                                # should have 16 rows all the time for every data frame
#            for key,val in d.items():
#                interesting_stats = val.loc[val.iloc[:,0].isin(v),:]
#                try:
#                    temp[k] = temp[k].append(interesting_stats)
#                except KeyError:
#                    temp[k] = interesting_stats
#            temp[k] = temp[k].reset_index(drop = True)
#            temp[k] = temp[k].iloc[:,[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]]
#            new_hyperparameters_un[j][k] = new_hyperparameters_un[j][k].join(temp[k], rsuffix = '_Team')
#            j = j+1
#    elif i == 4:                                   # Get points made by the Opponent per game
#        j = 0
#        for k,v in Team_Names.items():
#            temp = {}                                # should have 16 rows all the time for every data frame
#            for key,val in d.items():
#                interesting_stats = val.loc[val.iloc[:,0].isin(v),:]
#                try:
#                    temp[k] = temp[k].append(interesting_stats)
#                except KeyError:
#                    temp[k] = interesting_stats
#            temp[k] = temp[k].reset_index(drop = True)
#            temp[k] = temp[k].iloc[:,[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]]
#            new_hyperparameters_un[j][k] = new_hyperparameters_un[j][k].join(temp[k], rsuffix = '_Opp')
#            j = j+1
#    elif i == 0:                                # Getting coach win loss ratio
#        j = 0
#        for k,v in Team_Shortened.items():
#            temp = {}
#            for key,val in d.items():
#                if len(v) == 1:
#                    coaches = val.loc[val.iloc[:,1] == v[0],:]                    
#                elif len(v) == 2:
#                    if any(a == v[0] for a in val.iloc[:,1]):
#                        coaches = val.loc[val.iloc[:,1] == v[0],:]
#                    elif any(a == v[1] for a in val.iloc[:,1]):
#                        coaches = val.loc[val.iloc[:,1] == v[1],:]
#                elif len(v) == 3:
#                    if any(a == v[0] for a in val.iloc[:,1]):
#                        coaches = val.loc[val.iloc[:,1] == v[0],:]
#                    elif any(a == v[1] for a in val.iloc[:,1]):
#                        coaches = val.loc[val.iloc[:,1] == v[1],:]
#                    elif any(a == v[2] for a in val.iloc[:,1]):
#                        coaches = val.loc[val.iloc[:,1] == v[2],:]
#                weight = coaches.iloc[:,4]/coaches.iloc[:,4].sum()
#                WL = coaches.iloc[:,-1]*weight
#                WL = pd.Series(WL.sum())
#                try:
#                    temp[k] = temp[k].append(WL)
#                except KeyError:
#                    temp[k] = WL
#            temp[k] = temp[k].reset_index(drop = True)
#            temp[k] = temp[k].rename('Coach_WR')
#            new_hyperparameters_un[j][k] = new_hyperparameters_un[j][k].join(temp[k])
#            j = j+1


# Now I would like to create a list of dictionaries for each team where I'd have dataframe with team and each possible opponent stats
new_x = []
for i,d in enumerate(new_hyperparameters):                   #traverse the list  
    for key,val in d.items():
        temp = {}                                # should have 16 rows all the time for every data frame
        for s,f in enumerate(new_hyperparameters):
            if s != i:
                for k,v in f.items():
                    team_vs_team = val.join(v, rsuffix = '_TeamsOpponent')
                    try:
                        temp[key+"_vs_"+k] = temp[key+"_vs_"+k].append(team_vs_team)
                    except KeyError:
                        temp[key+"_vs_"+k] = team_vs_team
        new_x.append(temp)
        
#new_x_un = []
#for i,d in enumerate(new_hyperparameters_un):                   #traverse the list  
#    for key,val in d.items():
#        temp = {}                                # should have 16 rows all the time for every data frame
#        for s,f in enumerate(new_hyperparameters_un):
#            if s != i:
#                for k,v in f.items():
#                    team_vs_team = val.join(v, rsuffix = '_TeamsOpponent')
#                    try:
#                        temp[key+"_vs_"+k] = temp[key+"_vs_"+k].append(team_vs_team)
#                    except KeyError:
#                        temp[key+"_vs_"+k] = team_vs_team
#        new_x_un.append(temp)



# Next I need to create X, so it has to have 1281 rows and 132 columns, there were 14 seasons that had 82 games, 1 with 66 (8th season) and last season has not been finished yet
x = []
for index,dicti in enumerate(new_target):                   #traverse the list  
    for i,d in enumerate(new_x):
        if i == index:
            for key,val in dicti.items():
                temp = {}
                for k,v in d.items():
                    for r in range(len(val)):
                        if (val.iloc[r,4] in k):
                            if r < 82:
                                season = 0
                            elif 81 < r < 82*2:
                                season = 1-1                                # one has to realize at this point that the data for predicting next regular season's results have to be done based on statistics from last season, therefore here we start deducting -1 and we will skip first 82 rows in each dataframe later and also in target variable
                            elif 82*2 -1 < r < 82*3:
                                season = 2-1
                            elif 82*3 -1 < r < 82*4:
                                season = 3-1
                            elif 82*4 -1 < r < 82*5:
                                season = 4-1
                            elif 82*5 -1 < r < 82*6:
                                season = 5-1
                            elif 82*6 -1 < r < 82*7:
                                season = 6-1
                            elif 82*7 -1 < r < 82*8 -16:
                                season = 7-1
                            elif 82*8 -1 -16 < r < 82*9 - 16:
                                season = 8-1
                            elif 82*9 -1 -16 < r < 82*10 - 16:
                                season = 9-1
                            elif 82*10 -1 -16 < r < 82*11 - 16:
                                season = 10-1
                            elif 82*11 -1 -16 < r < 82*12 - 16:
                                season = 11-1
                            elif 82*12 -1 -16 < r < 82*13 - 16:
                                season = 12-1
                            elif 82*13 -1 -16 < r < 82*14 - 16:
                                season = 13-1
                            elif 82*14 -1 -16 < r < 82*15 - 16:
                                season = 14-1
                            else:
                                season = 15-1
                               
                            row_vals = pd.DataFrame(v.iloc[season,:]).T
                            try:
                                temp[key] = temp[key].append(row_vals)
                            except KeyError:
                                temp[key] = row_vals
                x.append(temp)

# skipping first 82 rows in each x and target variable new_target
for index,dicti in enumerate(x): 
    for key,val in dicti.items():
        val = val.iloc[82:,:]
        x[index][key] = val

for index,dicti in enumerate(new_target): 
    for key,val in dicti.items():
        val = val.iloc[82:,:]
        new_target[index][key] = val

for index,dicti in enumerate(t): 
    for key,val in dicti.items():
        val = val.iloc[82:]
        t[index][key] = val
        
        
# Next I need to create X for play off, so it has to have around 186 rows and 132 columns
x_play_off = []
for index,dicti in enumerate(new_target_play_off):                   #traverse the list  
    for key,val in dicti.items(): 
        temp = {}
        for team in range(len(val)):
            for kk,vv in Team_Index.items():
                if kk == val.iloc[team,4]:
                    home_index = vv[0]
                    for i,d in enumerate(new_x):
                        if i == home_index:
                            for k,v in d.items():
                                if (val.iloc[team,2] in k):
                                    if ('2004-05' in key):
                                        season = 0
                                    elif ('2005-06' in key):
                                        season = 1
                                    elif ('2006-07' in key):
                                        season = 2
                                    elif ('2007-08' in key):
                                        season = 3
                                    elif ('2008-09' in key):
                                        season = 4
                                    elif ('2009-10' in key):
                                        season = 5
                                    elif ('2010-11' in key):
                                        season = 6
                                    elif ('2011-12' in key):
                                        season = 7
                                    elif ('2012-13' in key):
                                        season = 8
                                    elif ('2013-14' in key):
                                        season = 9
                                    elif ('2014-15' in key):
                                        season = 10
                                    elif ('2015-16' in key):
                                        season = 11
                                    elif ('2016-17' in key):
                                        season = 12
                                    elif ('2017-18' in key):
                                        season = 13
                                    elif ('2018-19' in key):
                                        season = 14
                                    else:
                                        season = 15
                                        
                                    row_vals = pd.DataFrame(v.iloc[season,:]).T
                                    try:
                                        temp[key] = temp[key].append(row_vals)
                                    except KeyError:
                                        temp[key] = row_vals
        for team in range(len(val)):
            for kk,vv in Team_Index.items():
                if kk == val.iloc[team,2]:
                    visitor_index = vv[0]
                    for i,d in enumerate(new_x):
                        if i == visitor_index:
                            for k,v in d.items():
                                if (val.iloc[team,4] in k):
                                    if ('2004-05' in key):
                                        season = 0
                                    elif ('2005-06' in key):
                                        season = 1
                                    elif ('2006-07' in key):
                                        season = 2
                                    elif ('2007-08' in key):
                                        season = 3
                                    elif ('2008-09' in key):
                                        season = 4
                                    elif ('2009-10' in key):
                                        season = 5
                                    elif ('2010-11' in key):
                                        season = 6
                                    elif ('2011-12' in key):
                                        season = 7
                                    elif ('2012-13' in key):
                                        season = 8
                                    elif ('2013-14' in key):
                                        season = 9
                                    elif ('2014-15' in key):
                                        season = 10
                                    elif ('2015-16' in key):
                                        season = 11
                                    elif ('2016-17' in key):
                                        season = 12
                                    elif ('2017-18' in key):
                                        season = 13
                                    elif ('2018-19' in key):
                                        season = 14
                                    else:
                                        season = 15
                               
                                    row_vals = pd.DataFrame(v.iloc[season,:]).T
                                    try:
                                        temp[key] = temp[key].append(row_vals)
                                    except KeyError:
                                        temp[key] = row_vals
        x_play_off.append(temp)
        
        
#x_un = []
#for index,dicti in enumerate(new_target):                   #traverse the list  
#    for i,d in enumerate(new_x_un):
#        if i == index:
#            for key,val in dicti.items():
#                temp = {}
#                for k,v in d.items():
#                    for r in range(len(val)):
#                        if (val.iloc[r,4] in k):
#                            if r < 82:
#                                season = 0
#                            elif 81 < r < 82*2:
#                                season = 1
#                            elif 82*2 -1 < r < 82*3:
#                                season = 2
#                            elif 82*3 -1 < r < 82*4:
#                                season = 3
#                            elif 82*4 -1 < r < 82*5:
#                                season = 4
#                            elif 82*5 -1 < r < 82*6:
#                                season = 5
#                            elif 82*6 -1 < r < 82*7:
#                                season = 6
#                            elif 82*7 -1 < r < 82*8 -16:
#                                season = 7
#                            elif 82*8 -1 -16 < r < 82*9 - 16:
#                                season = 8
#                            elif 82*9 -1 -16 < r < 82*10 - 16:
#                                season = 9
#                            elif 82*10 -1 -16 < r < 82*11 - 16:
#                                season = 10
#                            elif 82*11 -1 -16 < r < 82*12 - 16:
#                                season = 11
#                            elif 82*12 -1 -16 < r < 82*13 - 16:
#                                season = 12
#                            elif 82*13 -1 -16 < r < 82*14 - 16:
#                                season = 13
#                            elif 82*14 -1 -16 < r < 82*15 - 16:
#                                season = 14
#                            else:
#                                season = 15
#                               
#                            row_vals = pd.DataFrame(v.iloc[season,:]).T
#                            try:
#                                temp[key] = temp[key].append(row_vals)
#                            except KeyError:
#                                temp[key] = row_vals
#                x_un.append(temp)


# Now from an easy to look through dictionaries x and t, I'll create dataframes X and T with all the data connected together
X = pd.DataFrame()
for i,d in enumerate(x):
    for k,v in d.items():
        X = X.append(v)

X_play_off = pd.DataFrame()
for i,d in enumerate(x_play_off):
    for k,v in d.items():
        X_play_off = X_play_off.append(v)
        
# We add variable of home or away match
temp_pd = pd.DataFrame() 
for i,d in enumerate(new_target):                   #traverse the list for away or home match
    for key,val in d.items():
        dummies = val['Home_or_Away(@)']=='@'
        dummies = dummies * 1
        dummies = pd.DataFrame(dummies)
        temp_pd = temp_pd.append(dummies)
X = X.reset_index(drop = True)
temp_pd = temp_pd.reset_index(drop = True)
X = X.join(temp_pd)

# For play off the home or away variable has to be added before the connection, otherwise it would be harder
temp_pd = pd.DataFrame() 
for i,d in enumerate(new_target_play_off):                   #traverse the list for away or home match
    for key,val in d.items():
        dummies_1 = pd.DataFrame(np.ones(shape = (len(val),1)),columns=['Home_or_Away(@)'])
        dummies_0 = pd.DataFrame(np.zeros(shape = (len(val),1)),columns=['Home_or_Away(@)'])
        dummies = dummies_1.append(dummies_0)
        temp_pd = temp_pd.append(dummies)
X_play_off = X_play_off.reset_index(drop = True)
temp_pd = temp_pd.reset_index(drop = True)
X_play_off = X_play_off.join(temp_pd)

        

#X_un = pd.DataFrame()
#for i,d in enumerate(x_un):
#    for k,v in d.items():
#        X_un = X_un.append(v)

#temp_pd = pd.DataFrame() 
#for i,d in enumerate(new_target):                   #traverse the list for away or home match
#    for key,val in d.items():
#        dummies = val['Home_or_Away(@)']=='@'
#        dummies = dummies * 1
#        dummies = pd.DataFrame(dummies)
#        temp_pd = temp_pd.append(dummies)
#X_un = X_un.reset_index(drop = True)
#temp_pd = temp_pd.reset_index(drop = True)
#X_un = X_un.join(temp_pd)

T = pd.DataFrame()
for i,d in enumerate(t):
    for k,v in d.items():
        v = pd.DataFrame(v)
        T = T.append(v)

T_play_off = pd.DataFrame()
for i,d in enumerate(t_play_off):
    for k,v in d.items():
        v = pd.DataFrame(v)
        T_play_off = T_play_off.append(v)
#### Features without normalization later show that are not optimal and do not make sense to even test, recommended to skip that.


############################################################################################################################
########################################## Data Preprocessing ##############################################################
############################################################################################################################


# See if there is multicollinearity
Var_Corr = X.corr()
fig, ax = plt.subplots(figsize=(50,50))
sns.heatmap(Var_Corr, xticklabels=Var_Corr.columns, yticklabels=Var_Corr.columns, annot=True, linewidths=.5, ax=ax)

# Dropping features with too high correlations between features
X_drop = X.drop(['SRS', 'NRtg', 'Pace', 'FTr', '3PAr', 'TS%', 'eFG%', 'MP', 'FG', 'FGA', '3P', '3PA', '2P%', 'FT', 'FTA', 'TRB', 'PF', 'FG_Team', '3PA_Team', '2PA_Team','2P%_Team','FTA_Team', 'TRB_Team', 'SRS_TeamsOpponent', 'NRtg_TeamsOpponent', 'Pace_TeamsOpponent', 'FTr_TeamsOpponent', '3PAr_TeamsOpponent', 'TS%_TeamsOpponent', 'eFG%_TeamsOpponent', 'eFG%.1_TeamsOpponent', 'MP_TeamsOpponent', 'FG_TeamsOpponent', 'FGA_TeamsOpponent', '3P_TeamsOpponent', '3PA_TeamsOpponent', '2PA_TeamsOpponent', 'FT_TeamsOpponent', 'FTA_TeamsOpponent', 'TRB_TeamsOpponent', 'FG_Team_TeamsOpponent', '3PA_Team_TeamsOpponent', '2PA_Team_TeamsOpponent', 'FTA_Team_TeamsOpponent', 'TRB_Team_TeamsOpponent'], axis=1)
#X_un_drop = X_un.drop(['SRS', 'NRtg', 'Pace', 'FTr', '3PAr', 'TS%', 'eFG%', 'MP', 'FG', 'FGA', '3P', '3PA', '2P%', 'FT', 'FTA', 'TRB', 'PF', 'FG_Team', '3PA_Team', '2PA_Team','2P%_Team','FTA_Team', 'TRB_Team', 'SRS_TeamsOpponent', 'NRtg_TeamsOpponent', 'Pace_TeamsOpponent', 'FTr_TeamsOpponent', '3PAr_TeamsOpponent', 'TS%_TeamsOpponent', 'eFG%_TeamsOpponent', 'eFG%.1_TeamsOpponent', 'MP_TeamsOpponent', 'FG_TeamsOpponent', 'FGA_TeamsOpponent', '3P_TeamsOpponent', '3PA_TeamsOpponent', '2PA_TeamsOpponent', 'FT_TeamsOpponent', 'FTA_TeamsOpponent', 'TRB_TeamsOpponent', 'FG_Team_TeamsOpponent', '3PA_Team_TeamsOpponent', '2PA_Team_TeamsOpponent', 'FTA_Team_TeamsOpponent', 'TRB_Team_TeamsOpponent'], axis=1)
X_drop_play_off = X_play_off.drop(['SRS', 'NRtg', 'Pace', 'FTr', '3PAr', 'TS%', 'eFG%', 'MP', 'FG', 'FGA', '3P', '3PA', '2P%', 'FT', 'FTA', 'TRB', 'PF', 'FG_Team', '3PA_Team', '2PA_Team','2P%_Team','FTA_Team', 'TRB_Team', 'SRS_TeamsOpponent', 'NRtg_TeamsOpponent', 'Pace_TeamsOpponent', 'FTr_TeamsOpponent', '3PAr_TeamsOpponent', 'TS%_TeamsOpponent', 'eFG%_TeamsOpponent', 'eFG%.1_TeamsOpponent', 'MP_TeamsOpponent', 'FG_TeamsOpponent', 'FGA_TeamsOpponent', '3P_TeamsOpponent', '3PA_TeamsOpponent', '2PA_TeamsOpponent', 'FT_TeamsOpponent', 'FTA_TeamsOpponent', 'TRB_TeamsOpponent', 'FG_Team_TeamsOpponent', '3PA_Team_TeamsOpponent', '2PA_Team_TeamsOpponent', 'FTA_Team_TeamsOpponent', 'TRB_Team_TeamsOpponent'], axis=1)

# See if there is still multicollinearity
Var_Corr = X_drop.corr()
fig, ax = plt.subplots(figsize=(50,50))
sns.heatmap(Var_Corr, xticklabels=Var_Corr.columns, yticklabels=Var_Corr.columns, annot=True, linewidths=.5, ax=ax)
      
X = X.values
X_drop = X_drop.values
#X_un = X_un.values
#X_un_drop = X_un_drop.values
X_play_off = X_play_off.values
X_drop_play_off = X_drop_play_off.values
T = T.values.astype(float)
T_play_off = T_play_off.values.astype(float)

## Trying out PCA ##
# single value decomposition
U, s, Vh = np.linalg.svd(X, full_matrices=False)

eigvals = ((s**2) / (np.cumsum(s)[-1]))/10000

#plotting the principal components
fig = plt.figure(figsize=(8,5))
sing_vals = np.arange(133) + 1
plt.plot(sing_vals, eigvals, 'ro-', linewidth=2, color='b')
plt.title('Plot of Principle Components with Regular Season Features')
plt.xlabel('PC')

leg = plt.legend(['Eigenvalues from Single Value Decomposition'], borderpad=0.3, prop=matplotlib.font_manager.FontProperties(size='small'))
leg.get_frame().set_alpha(0.2)
plt.show()

#We want to choose number of principle components that describe 95% of variability
print(eigvals[:33].sum()/eigvals.sum()) # We therefore choose 33

# I will choose 33 Principal Components
Weights=Vh[:33,]
X_PCA = X@Weights.T

# With play off data
# single value decomposition
U_play_off, s_play_off, Vh_play_off = np.linalg.svd(X_play_off, full_matrices=False)

eigvals = ((s_play_off**2) / (np.cumsum(s_play_off)[-1]))/10000

#plotting the principal components
fig = plt.figure(figsize=(8,5))
sing_vals = np.arange(133) + 1
plt.plot(sing_vals, eigvals, 'ro-', linewidth=2, color='b')
plt.title('Plot of Principle Components with Play Off Features')
plt.xlabel('PC')

leg = plt.legend(['Eigenvalues from Single Value Decomposition'], borderpad=0.3, prop=matplotlib.font_manager.FontProperties(size='small'))
leg.get_frame().set_alpha(0.2)
plt.show()

#We want to choose number of principle components that describe 95% of variability
print(eigvals[:31].sum()/eigvals.sum()) # We therefore choose 31

# I will choose 31 Principal Components
Weights=Vh_play_off[:31,]
X_play_off_PCA = X_play_off@Weights.T


## Trying polynomial transformation after PCA
# Now I do polynomial transformation of the second order
poly = PolynomialFeatures(degree=2, include_bias=False)
X_Transf = poly.fit_transform(X_PCA)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_play_off_Transf = poly.fit_transform(X_play_off_PCA)


# Now I split it to Train and Test set, we will split them in two different ways, first in random way, second we choose first 12 seasons to predict last 4

X_train_random, X_test_random, t_train_random, t_test_random = train_test_split(X, T, random_state = 1234, test_size = 0.25) # In random way
X_drop_train_random, X_drop_test_random, t_drop_train_random, t_drop_test_random = train_test_split(X_drop, T, random_state = 1234, test_size = 0.25) # In random way
X_PCA_train_random, X_PCA_test_random, t_PCA_train_random, t_PCA_test_random = train_test_split(X_PCA, T, random_state = 1234, test_size = 0.25) # In random way
X_Transf_train_random, X_Transf_test_random, t_Transf_train_random, t_Transf_test_random = train_test_split(X_Transf, T, random_state = 1234, test_size = 0.25) # In random way
#X_un_train_random, X_un_test_random, t_un_train_random, t_un_test_random = train_test_split(X_un, T, random_state = 42, test_size = 0.25) # In random way
#X_un_drop_train_random, X_un_drop_test_random, t_un_drop_train_random, t_un_drop_test_random = train_test_split(X_un_drop, T, random_state = 42, test_size = 0.25) # In random way
X_train_play_off_random, X_test_play_off_random, t_train_play_off_random, t_test_play_off_random = train_test_split(X_play_off, T_play_off, random_state = 42, test_size = 0.25) # In random way
X_drop_train_play_off_random, X_drop_test_play_off_random, t_drop_train_play_off_random, t_drop_test_play_off_random = train_test_split(X_drop_play_off, T_play_off, random_state = 42, test_size = 0.25) # In random way
X_PCA_train_play_off_random, X_PCA_test_play_off_random, t_PCA_train_play_off_random, t_PCA_test_play_off_random = train_test_split(X_play_off_PCA, T_play_off, random_state = 42, test_size = 0.25) # In random way
X_Transf_train_play_off_random, X_Transf_test_play_off_random, t_Transf_train_play_off_random, t_Transf_test_play_off_random = train_test_split(X_play_off_Transf, T_play_off, random_state = 42, test_size = 0.25) # In random way

first_twelve_seasons = 11*82*30 + 1*66*30
X_train_seasons = X[0:first_twelve_seasons,:] # 12 first seasons
X_test_seasons = X[first_twelve_seasons:,:] # last 3 seasons
t_train_seasons = T[0:first_twelve_seasons,:]
t_test_seasons = T[first_twelve_seasons:,:]

X_drop_train_seasons = X_drop[0:first_twelve_seasons,:] # 12 first seasons
X_drop_test_seasons = X_drop[first_twelve_seasons:,:] # last 3 seasons

X_PCA_train_seasons = X_PCA[0:first_twelve_seasons,:] # 12 first seasons
X_PCA_test_seasons = X_PCA[first_twelve_seasons:,:] # last 3 seasons

X_Transf_train_seasons = X_Transf[0:first_twelve_seasons,:] # 12 first seasons
X_Transf_test_seasons = X_Transf[first_twelve_seasons:,:] # last 3 seasons

first_twelve_play_off_seasons = 8*84*2 + 2*81*2 + 1*79*2 + 1*82*2
X_train_play_off_seasons = X_play_off[0:first_twelve_play_off_seasons,:] # 12 first seasons
X_test_play_off_seasons = X_play_off[first_twelve_play_off_seasons:,:] # last 4 seasons
t_train_play_off_seasons = T_play_off[0:first_twelve_play_off_seasons,:]
t_test_play_off_seasons = T_play_off[first_twelve_play_off_seasons:,:]

X_drop_train_play_off_seasons = X_drop_play_off[0:first_twelve_play_off_seasons,:] # 12 first seasons
X_drop_test_play_off_seasons = X_drop_play_off[first_twelve_play_off_seasons:,:] # last 4 seasons

X_PCA_train_play_off_seasons = X_play_off_PCA[0:first_twelve_play_off_seasons,:] # 12 first seasons
X_PCA_test_play_off_seasons = X_play_off_PCA[first_twelve_play_off_seasons:,:] # last 4 seasons

X_Transf_train_play_off_seasons = X_play_off_Transf[0:first_twelve_play_off_seasons,:] # 12 first seasons
X_Transf_test_play_off_seasons = X_play_off_Transf[first_twelve_play_off_seasons:,:] # last 4 seasons


############################################################################################################################
############################################################################################################################
########################################## Neural Network ##################################################################
############################################################################################################################
############################################################################################################################


########################################## NN without dropping variables ###################################################

###### Regular Season ######
# Setting up layers for a neural network
model_nn = Sequential()
# Adding hidden layer
model_nn.add(Dense(units = 20,             # number of units the layer has
                activation = 'tanh',
                input_dim = 133))     # activation function
# Adding hidden layer
#model_nn.add(Dense(units = 20,             # number of units the layer has
 #               activation = 'tanh'))     # activation function
# Adding hidden layer
#model_nn.add(Dense(units = 40,             # number of units the layer has
 #               activation = 'tanh'))     # activation function
# Adding hidden layer
#model_nn.add(Dense(units = 20,             # number of units the layer has
 #               activation = 'tanh'))     # activation function
# Adding output layer
model_nn.add(Dense(units=1,               # number of units the layer has
                activation = 'sigmoid'))  # activation function
# Compiling the model
model_nn.compile(loss='binary_crossentropy', # Choose loss function to optimize
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),         # Choose optimizer to do the above
              metrics = ['accuracy'])        # Choose metric to print

#fit for the undropped data with random split
history_nn = model_nn.fit(X_train_random,
                       t_train_random,
                       epochs = 50,
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

# Showing the convergency and reason why we should use 'Early Stop'

## First for undropped model with random split
# Plot training & validation accuracy values
plt.plot(history_nn.history['acc'])
plt.plot(history_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy with regular season random split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_nn.history['loss'])
plt.plot(history_nn.history['val_loss'])
plt.title('Model loss with regular season random split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

model_nn = Sequential()
# Adding hidden layer
model_nn.add(Dense(units = 20,             # number of units the layer has
                activation = 'tanh',
                input_dim = 133))     # activation function
# Adding output layer
model_nn.add(Dense(units=1,               # number of units the layer has
                activation = 'sigmoid'))  # activation function
# Compiling the model
model_nn.compile(loss='binary_crossentropy', # Choose loss function to optimize
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),         # Choose optimizer to do the above
              metrics = ['accuracy'])        # Choose metric to print

### Get accuracy with the best epochs
# For the random split
model_nn.fit(X_train_random,
            t_train_random,
            epochs = 12,
            batch_size = 1000,
            verbose = 0)
# One way of predicting, but below is easier way
#t_pred = model_nn.predict(X_test_random).round()
#t_pred = np.float64(t_pred)
#acc = accuracy_score(t_test_random, t_pred)
loss, acc = model_nn.evaluate(X_test_random,t_test_random)
print(f'Accuracy NN without dropped data, regular season and random split: {acc:.3f}')

# Setting up layers for a neural network
model_nn = Sequential()
# Adding hidden layer
model_nn.add(Dense(units = 20,             # number of units in the layer hidden 
                activation = 'tanh',
                input_dim = 133))     # activation function
# Adding hidden layer
#model_nn.add(Dense(units = 90,             # number of units the layer has
 #               activation = 'tanh'))     # activation function
# Adding hidden layer
#model_nn.add(Dense(units = 40,             # number of units the layer has
 #               activation = 'tanh'))     # activation function
# Adding hidden layer
#model_nn.add(Dense(units = 20,             # number of units the layer has
 #               activation = 'tanh'))     # activation function
# Adding output layer
model_nn.add(Dense(units=1,               # number of units the layer has
                activation = 'sigmoid'))  # activation function
# Compiling the model
model_nn.compile(loss='binary_crossentropy', # Choose loss function to optimize
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),         # Choose optimizer to do the above
              metrics = ['accuracy'])        # Choose metric to print

#fit for the undropped data with seasons split
history_seasons_nn = model_nn.fit(X_train_seasons,
                       t_train_seasons,
                       epochs = 50,
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## Next for undropped model with seasons split
# Plot training & validation accuracy values
plt.plot(history_seasons_nn.history['acc'])
plt.plot(history_seasons_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy with regular season seasons split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_seasons_nn.history['loss'])
plt.plot(history_seasons_nn.history['val_loss'])
plt.title('Model loss with regular season seasons split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

model_nn = Sequential()
# Adding hidden layer
model_nn.add(Dense(units = 20,             # number of units the layer has
                activation = 'tanh',
                input_dim = 133))     # activation function
# Adding output layer
model_nn.add(Dense(units=1,               # number of units the layer has
                activation = 'sigmoid'))  # activation function
# Compiling the model
model_nn.compile(loss='binary_crossentropy', # Choose loss function to optimize
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),         # Choose optimizer to do the above
              metrics = ['accuracy'])        # Choose metric to print

### Get accuracy with the best epochs
# For the random split
model_nn.fit(X_train_seasons,
            t_train_seasons,
            epochs = 20,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn.evaluate(X_test_seasons,t_test_seasons)
print(f'Accuracy NN without dropped data, regular season and season split: {acc:.3f}')

###### Play Off ######
# Setting up layers for a neural network
model_nn = Sequential()
# Adding hidden layer
model_nn.add(Dense(units = 89,             # number of units the layer has (133 * 2/3 = 89)
                activation = 'tanh',
                input_dim = 133))     # activation function
# Adding hidden layer
model_nn.add(Dense(units = 40,             # number of units the layer has
                activation = 'tanh'))     # activation function
# Adding hidden layer
model_nn.add(Dense(units = 20,             # number of units the layer has
                activation = 'tanh'))     # activation function
# Adding output layer
model_nn.add(Dense(units=1,               # number of units the layer has
                activation = 'sigmoid'))  # activation function
# Compiling the model
model_nn.compile(loss='binary_crossentropy', # Choose loss function to optimize
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),         # Choose optimizer to do the above
              metrics = ['accuracy'])        # Choose metric to print

#fit for the undropped data with random split
history_PO_random_nn = model_nn.fit(X_train_play_off_random,
                       t_train_play_off_random,
                       epochs = 50,
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## Next for undropped model with random split
# Plot training & validation accuracy values
plt.plot(history_PO_random_nn.history['acc'])
plt.plot(history_PO_random_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy with play off random split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_PO_random_nn.history['loss'])
plt.plot(history_PO_random_nn.history['val_loss'])
plt.title('Model loss with play off random split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn = Sequential()
# Adding hidden layer
model_nn.add(Dense(units = 89,             # number of units the layer has (133 * 2/3 = 89)
                activation = 'tanh',
                input_dim = 133))     # activation function
# Adding hidden layer
model_nn.add(Dense(units = 40,             # number of units the layer has
                activation = 'tanh'))     # activation function
# Adding hidden layer
model_nn.add(Dense(units = 20,             # number of units the layer has
                activation = 'tanh'))     # activation function
# Adding output layer
model_nn.add(Dense(units=1,               # number of units the layer has
                activation = 'sigmoid'))  # activation function
# Compiling the model
model_nn.compile(loss='binary_crossentropy', # Choose loss function to optimize
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),         # Choose optimizer to do the above
              metrics = ['accuracy'])        # Choose metric to print

### Get accuracy with the best epochs
# For the random split
model_nn.fit(X_train_play_off_random,
            t_train_play_off_random,
            epochs = 20,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn.evaluate(X_test_play_off_random,t_test_play_off_random)
print(f'Accuracy NN without dropped data, play off and random split: {acc:.3f}')


# Setting up layers for a neural network
model_nn = Sequential()
# Adding hidden layer
model_nn.add(Dense(units = 89,             # number of units the layer has (133 * 2/3 = 89)
                activation = 'tanh',
                input_dim = 133))     # activation function
# Adding hidden layer
model_nn.add(Dense(units = 40,             # number of units the layer has
                activation = 'tanh'))     # activation function
# Adding hidden layer
model_nn.add(Dense(units = 20,             # number of units the layer has
                activation = 'tanh'))     # activation function
# Adding output layer
model_nn.add(Dense(units=1,               # number of units the layer has
                activation = 'sigmoid'))  # activation function
# Compiling the model
model_nn.compile(loss='binary_crossentropy', # Choose loss function to optimize
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),         # Choose optimizer to do the above
              metrics = ['accuracy'])        # Choose metric to print

#fit for the undropped data with seasons split
history_PO_seasons_nn = model_nn.fit(X_train_play_off_seasons,
                       t_train_play_off_seasons,
                       epochs = 50,
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## Next for undropped model with seasons split
# Plot training & validation accuracy values
plt.plot(history_PO_seasons_nn.history['acc'])
plt.plot(history_PO_seasons_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy with play off seasons split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_PO_seasons_nn.history['loss'])
plt.plot(history_PO_seasons_nn.history['val_loss'])
plt.title('Model loss with play off seasons split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

### Get accuracy with the best epochs
# For the random split
model_nn.fit(X_train_play_off_seasons,
            t_train_play_off_seasons,
            epochs = 32,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn.evaluate(X_test_play_off_seasons,t_test_play_off_seasons)
print(f'Accuracy NN without dropped data, play off and season split: {acc:.3f}')


########################################## NN After Dropping features ######################################################

###### Regular Season ######
# Setting up layers for a neural network
model_nn_dropped = Sequential()
model_nn_dropped.add(Dense(units = 60,
                activation = 'tanh',
                input_dim = 88))
#model_nn_dropped.add(Dense(units = 40,
 #              activation = 'tanh'))
model_nn_dropped.add(Dense(units = 20,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_dropped.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

#fit for the dropped data with random split
history_dropped_nn = model_nn_dropped.fit(X_drop_train_random,
                       t_drop_train_random,
                       epochs = 50,                  # 5 epochs being optimal
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## First for dropped model with random data split
# Plot training & validation accuracy values
plt.plot(history_dropped_nn.history['acc'])
plt.plot(history_dropped_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy after dropping features for regular season with random split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_dropped_nn.history['loss'])
plt.plot(history_dropped_nn.history['val_loss'])
plt.title('Model loss after dropping features for regular season with random split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_dropped = Sequential()
model_nn_dropped.add(Dense(units = 60,
                activation = 'tanh',
                input_dim = 88))
model_nn_dropped.add(Dense(units = 20,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_dropped.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the random split
model_nn_dropped.fit(X_drop_train_random,
            t_drop_train_random,
            epochs = 8,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_dropped.evaluate(X_drop_test_random,t_drop_test_random)
print(f'Accuracy NN with dropped data for regular season and random split: {acc:.3f}')


# Setting up layers for a neural network
model_nn_dropped = Sequential()
model_nn_dropped.add(Dense(units = 60,
                activation = 'tanh',
                input_dim = 88))
model_nn_dropped.add(Dense(units = 40,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units = 10,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_dropped.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

#fit for the dropped data with seasons split
history_dropped_seasons_nn = model_nn_dropped.fit(X_drop_train_seasons,
                       t_train_seasons,
                       epochs = 50,                  # 5 epochs being optimal
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## Next for dropped model with seasons data split
# Plot training & validation accuracy values
plt.plot(history_dropped_seasons_nn.history['acc'])
plt.plot(history_dropped_seasons_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy after dropping features for regular season with seasons split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_dropped_seasons_nn.history['loss'])
plt.plot(history_dropped_seasons_nn.history['val_loss'])
plt.title('Model loss after dropping features for regular season with seasons split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_dropped = Sequential()
model_nn_dropped.add(Dense(units = 60,
                activation = 'tanh',
                input_dim = 88))
model_nn_dropped.add(Dense(units = 40,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units = 10,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_dropped.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the seasons split
model_nn_dropped.fit(X_drop_train_seasons,
            t_train_seasons,
            epochs = 8,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_dropped.evaluate(X_drop_test_seasons,t_test_seasons)
print(f'Accuracy NN with dropped data and seasons split: {acc:.3f}')


###### Play Off ######
# Setting up layers for a neural network
model_nn_dropped = Sequential()
model_nn_dropped.add(Dense(units = 60,
                activation = 'tanh',
                input_dim = 88))
model_nn_dropped.add(Dense(units = 40,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units = 20,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_dropped.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

#fit for the dropped data with random split
history_dropped_nn = model_nn_dropped.fit(X_drop_train_play_off_random,
                       t_drop_train_play_off_random,
                       epochs = 50,                  # 5 epochs being optimal
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## First for dropped model with random data split
# Plot training & validation accuracy values
plt.plot(history_dropped_nn.history['acc'])
plt.plot(history_dropped_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy after dropping features for play off with random split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_dropped_nn.history['loss'])
plt.plot(history_dropped_nn.history['val_loss'])
plt.title('Model loss after dropping features for play off with random split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_dropped = Sequential()
model_nn_dropped.add(Dense(units = 60,
                activation = 'tanh',
                input_dim = 88))
model_nn_dropped.add(Dense(units = 40,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units = 20,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_dropped.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the random split
model_nn_dropped.fit(X_drop_train_play_off_random,
            t_drop_train_play_off_random,
            epochs = 30,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_dropped.evaluate(X_drop_test_play_off_random,t_drop_test_play_off_random)
print(f'Accuracy NN with dropped data for play off and random split: {acc:.3f}')


# Setting up layers for a neural network
model_nn_dropped = Sequential()
model_nn_dropped.add(Dense(units = 60,
                activation = 'tanh',
                input_dim = 88))
model_nn_dropped.add(Dense(units = 40,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units = 20,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_dropped.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

#fit for the dropped data with seasons split
history_dropped_seasons_nn = model_nn_dropped.fit(X_drop_train_play_off_seasons,
                       t_train_play_off_seasons,
                       epochs = 50,                  # 5 epochs being optimal
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## Next for dropped model with seasons data split
# Plot training & validation accuracy values
plt.plot(history_dropped_seasons_nn.history['acc'])
plt.plot(history_dropped_seasons_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy after dropping features for play off with seasons split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_dropped_seasons_nn.history['loss'])
plt.plot(history_dropped_seasons_nn.history['val_loss'])
plt.title('Model loss after dropping features for play off with seasons split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_dropped = Sequential()
model_nn_dropped.add(Dense(units = 60,
                activation = 'tanh',
                input_dim = 88))
model_nn_dropped.add(Dense(units = 40,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units = 20,
               activation = 'tanh'))
model_nn_dropped.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_dropped.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the seasons split
model_nn_dropped.fit(X_drop_train_play_off_seasons,
            t_train_play_off_seasons,
            epochs = 30,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_dropped.evaluate(X_drop_test_play_off_seasons,t_test_play_off_seasons)
print(f'Accuracy NN with dropped data for play off and seasons split: {acc:.3f}')

########################################## NN After PCA ##############################################################

###### Regular Season ######
# Setting up layers for a neural network
model_nn_PCA = Sequential()
model_nn_PCA.add(Dense(units = 10,
                activation = 'tanh',
                input_dim = 33))
#model_nn.add(Dense(units = 10,
 #            activation = 'tanh'))
model_nn_PCA.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_PCA.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])


history_PCA_nn = model_nn_PCA.fit(X_PCA_train_random,
                       t_PCA_train_random,
                       epochs = 100,                  # 5 epochs being optimal?
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## First for PCA model with random data split
# Plot training & validation accuracy values
plt.plot(history_PCA_nn.history['acc'])
plt.plot(history_PCA_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy for regular season with PCA and with random split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_PCA_nn.history['loss'])
plt.plot(history_PCA_nn.history['val_loss'])
plt.title('Model loss for regular season with PCA and with random split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_PCA = Sequential()
model_nn_PCA.add(Dense(units = 10,
                activation = 'tanh',
                input_dim = 33))
model_nn_PCA.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_PCA.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the random split
model_nn_PCA.fit(X_PCA_train_random,
            t_PCA_train_random,
            epochs = 50,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_PCA.evaluate(X_PCA_test_random,t_PCA_test_random)
print(f'Accuracy NN with PCA for regular season and random split: {acc:.3f}')


# Setting up layers for a neural network
model_nn_PCA = Sequential()
model_nn_PCA.add(Dense(units = 15,
                activation = 'tanh',
                input_dim = 33))
#model_nn.add(Dense(units = 10,
 #            activation = 'tanh'))
model_nn_PCA.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_PCA.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

history_PCA_nn = model_nn_PCA.fit(X_PCA_train_seasons,
                       t_train_seasons,
                       epochs = 50,                  # 5 epochs being optimal?
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## Next for PCA model with seasons data split
# Plot training & validation accuracy values
plt.plot(history_PCA_nn.history['acc'])
plt.plot(history_PCA_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy for regular season with PCA and with seasons split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_PCA_nn.history['loss'])
plt.plot(history_PCA_nn.history['val_loss'])
plt.title('Model loss for regular season with PCA and with seasons split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_PCA = Sequential()
model_nn_PCA.add(Dense(units = 15,
                activation = 'tanh',
                input_dim = 33))
model_nn_PCA.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_PCA.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the seasons split
model_nn_PCA.fit(X_PCA_train_seasons,
            t_train_seasons,
            epochs = 5,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_PCA.evaluate(X_PCA_test_seasons,t_test_seasons)
print(f'Accuracy NN with PCA for regular season and seasons split: {acc:.3f}')


###### Play off ######
# Setting up layers for a neural network
model_nn_PCA = Sequential()
model_nn_PCA.add(Dense(units = 31,
                activation = 'tanh',
                input_dim = 31))
model_nn.add(Dense(units = 10,
             activation = 'tanh'))
model_nn_PCA.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_PCA.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])


history_PCA_nn = model_nn_PCA.fit(X_PCA_train_play_off_random,
                       t_PCA_train_play_off_random,
                       epochs = 150,                  # 5 epochs being optimal?
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## First for PCA model with random data split
# Plot training & validation accuracy values
plt.plot(history_PCA_nn.history['acc'])
plt.plot(history_PCA_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy for play off with PCA and with random split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_PCA_nn.history['loss'])
plt.plot(history_PCA_nn.history['val_loss'])
plt.title('Model loss for play off with PCA and with random split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_PCA = Sequential()
model_nn_PCA.add(Dense(units = 31,
                activation = 'tanh',
                input_dim = 31))
model_nn.add(Dense(units = 10,
             activation = 'tanh'))
model_nn_PCA.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_PCA.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])


### Get accuracy with the best epochs
# For the random split
model_nn_PCA.fit(X_PCA_train_play_off_random,
            t_PCA_train_play_off_random,
            epochs = 60,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_PCA.evaluate(X_PCA_test_play_off_random,t_PCA_test_play_off_random)
print(f'Accuracy NN with PCA for regular season and random split: {acc:.3f}')


# Setting up layers for a neural network
model_nn_PCA = Sequential()
model_nn_PCA.add(Dense(units = 10,
                activation = 'tanh',
                input_dim = 31))
#model_nn.add(Dense(units = 10,
 #            activation = 'tanh'))
model_nn_PCA.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_PCA.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

history_PCA_nn = model_nn_PCA.fit(X_PCA_train_play_off_seasons,
                       t_train_play_off_seasons,
                       epochs = 200,                  # 5 epochs being optimal?
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## Next for PCA model with seasons data split
# Plot training & validation accuracy values
plt.plot(history_PCA_nn.history['acc'])
plt.plot(history_PCA_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy for play off with PCA and with seasons split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_PCA_nn.history['loss'])
plt.plot(history_PCA_nn.history['val_loss'])
plt.title('Model loss for play off with PCA and with seasons split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_PCA = Sequential()
model_nn_PCA.add(Dense(units = 10,
                activation = 'tanh',
                input_dim = 31))
model_nn_PCA.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_PCA.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the seasons split
model_nn_PCA.fit(X_PCA_train_play_off_seasons,
            t_train_play_off_seasons,
            epochs = 150,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_PCA.evaluate(X_PCA_test_play_off_seasons,t_test_play_off_seasons)
print(f'Accuracy NN with PCA for play off and seasons split: {acc:.3f}')

########################################## NN After PCA and transformation ##############################################################

###### Regular Season ######
# Setting up layers for a neural network
model_nn_transf = Sequential()
model_nn_transf.add(Dense(units = 594,  # 594*2/3
                activation = 'tanh',
                input_dim = 594))
model_nn_transf.add(Dense(units = 396,
               activation = 'tanh'))
model_nn_transf.add(Dense(units = 200,
               activation = 'tanh'))
model_nn_transf.add(Dense(units = 50,
               activation = 'tanh'))
model_nn_transf.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_transf.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

history_transformed_nn = model_nn_transf.fit(X_Transf_train_random,
                       t_Transf_train_random,
                       epochs = 50,                  # 5 epochs being optimal?
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## First for Transformed model with random data split
# Plot training & validation accuracy values
plt.plot(history_transformed_nn.history['acc'])
plt.plot(history_transformed_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy after polyn. transf. for regular season and random split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_transformed_nn.history['loss'])
plt.plot(history_transformed_nn.history['val_loss'])
plt.title('Model loss after polyn. transf. for regular season and random split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_transf = Sequential()
model_nn_transf.add(Dense(units = 594,  # 594*2/3
                activation = 'tanh',
                input_dim = 594))
model_nn_transf.add(Dense(units = 396,
               activation = 'tanh'))
model_nn_transf.add(Dense(units = 200,
               activation = 'tanh'))
model_nn_transf.add(Dense(units = 50,
               activation = 'tanh'))
model_nn_transf.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_transf.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the random split
model_nn_transf.fit(X_Transf_train_random,
            t_Transf_train_random,
            epochs = 5,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_transf.evaluate(X_Transf_test_random,t_Transf_test_random)
print(f'Accuracy NN with transformation for regular season and random split: {acc:.3f}')


# Setting up layers for a neural network
model_nn_transf = Sequential()
model_nn_transf.add(Dense(units = 594,  # 594*2/3
                activation = 'tanh',
                input_dim = 594))
model_nn_transf.add(Dense(units = 396,
               activation = 'tanh'))
model_nn_transf.add(Dense(units = 200,
               activation = 'tanh'))
model_nn_transf.add(Dense(units = 20,
               activation = 'tanh'))
model_nn_transf.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_transf.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

history_seasons_transformed_nn = model_nn_transf.fit(X_Transf_train_seasons,
                       t_train_seasons,
                       epochs = 50,                  # 5 epochs being optimal?
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## Next for Transformed model with seasons data split
# Plot training & validation accuracy values
plt.plot(history_seasons_transformed_nn.history['acc'])
plt.plot(history_seasons_transformed_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy after polyn. transf. for regular season and seasons split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_seasons_transformed_nn.history['loss'])
plt.plot(history_seasons_transformed_nn.history['val_loss'])
plt.title('Model loss after polyn. transf. for regular season and seasons split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_transf = Sequential()
model_nn_transf.add(Dense(units = 594,  # 594*2/3
                activation = 'tanh',
                input_dim = 594))
model_nn_transf.add(Dense(units = 396,
               activation = 'tanh'))
model_nn_transf.add(Dense(units = 200,
               activation = 'tanh'))
model_nn_transf.add(Dense(units = 50,
               activation = 'tanh'))
model_nn_transf.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_transf.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the seasons split
model_nn_transf.fit(X_Transf_train_seasons,
            t_train_seasons,
            epochs = 5,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_transf.evaluate(X_Transf_test_seasons,t_test_seasons)
print(f'Accuracy NN with transformation for regular season and seasons split: {acc:.3f}')


###### Play Off ######
# Setting up layers for a neural network
model_nn_transf = Sequential()
model_nn_transf.add(Dense(units = 10,
                activation = 'tanh',
                input_dim = 527))
#model_nn_transf.add(Dense(units = 351,
 #              activation = 'tanh'))
#model_nn_transf.add(Dense(units = 200,
 #              activation = 'tanh'))
#model_nn_transf.add(Dense(units = 50,
 #              activation = 'tanh'))
model_nn_transf.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_transf.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

history_transformed_nn = model_nn_transf.fit(X_Transf_train_play_off_random,
                       t_Transf_train_play_off_random,
                       epochs = 100,                  # 20 epochs being optimal?
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## First for Transformed model with random data split
# Plot training & validation accuracy values
plt.plot(history_transformed_nn.history['acc'])
plt.plot(history_transformed_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy after polyn. transf. for play off and random split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_transformed_nn.history['loss'])
plt.plot(history_transformed_nn.history['val_loss'])
plt.title('Model loss after polyn. transf. for play off and random split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_transf = Sequential()
model_nn_transf.add(Dense(units = 10,  # 594*2/3
                activation = 'tanh',
                input_dim = 527))
model_nn_transf.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_transf.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the random split
model_nn_transf.fit(X_Transf_train_play_off_random,
            t_Transf_train_play_off_random,
            epochs = 50,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_transf.evaluate(X_Transf_test_play_off_random,t_Transf_test_play_off_random)
print(f'Accuracy NN with transformation for play off and random split: {acc:.3f}')


# Setting up layers for a neural network
model_nn_transf = Sequential()
model_nn_transf.add(Dense(units = 527,
                activation = 'tanh',
                input_dim = 527))
#model_nn_transf.add(Dense(units = 351,
 #              activation = 'tanh'))
#model_nn_transf.add(Dense(units = 200,
 #              activation = 'tanh'))
model_nn_transf.add(Dense(units = 100,
               activation = 'tanh'))
model_nn_transf.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_transf.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

history_seasons_transformed_nn = model_nn_transf.fit(X_Transf_train_play_off_seasons,
                       t_train_play_off_seasons,
                       epochs = 50,                  # 5 epochs being optimal?
                       batch_size = 1000,
                       verbose = 0,
                       validation_split = 0.3)

## Next for Transformed model with seasons data split
# Plot training & validation accuracy values
plt.plot(history_seasons_transformed_nn.history['acc'])
plt.plot(history_seasons_transformed_nn.history['val_acc'],alpha = 0.5)
plt.title('Model accuracy after polyn. transf. for play off and seasons split')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history_seasons_transformed_nn.history['loss'])
plt.plot(history_seasons_transformed_nn.history['val_loss'])
plt.title('Model loss after polyn. transf. for play off and seasons split')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Setting up layers for a neural network
model_nn_transf = Sequential()
model_nn_transf.add(Dense(units = 527,
                activation = 'tanh',
                input_dim = 527))
#model_nn_transf.add(Dense(units = 351,
 #              activation = 'tanh'))
#model_nn_transf.add(Dense(units = 200,
 #              activation = 'tanh'))
model_nn_transf.add(Dense(units = 100,
               activation = 'tanh'))
model_nn_transf.add(Dense(units=1,
                activation = 'sigmoid'))
model_nn_transf.compile(loss='binary_crossentropy',
              optimizer = optimizers.Adam(lr = 1/1000,beta_1=0.9,beta_2=0.999,epsilon=1/100000000),
              metrics = ['accuracy'])

### Get accuracy with the best epochs
# For the seasons split
model_nn_transf.fit(X_Transf_train_play_off_seasons,
            t_train_play_off_seasons,
            epochs = 5,
            batch_size = 1000,
            verbose = 0)
loss, acc = model_nn_transf.evaluate(X_Transf_test_play_off_seasons,t_test_play_off_seasons)
print(f'Accuracy NN with transformation for play off and seasons split: {acc:.3f}')

############################################################################################################################
############################################################################################################################
########################################## Probit Regression ###############################################################
############################################################################################################################
############################################################################################################################

### This piece of code is here to show that even probit regression does have similar results

#from statsmodels.discrete.discrete_model import Probit
#from statsmodels.tools.tools import add_constant

#p_model = Probit(t_drop_train_random,X_drop_train_random_with_cnst)
#probit_model = p_model.fit()
#probit_predictions = probit_model.predict(X_drop_test_random_with_cnst).round()
#acc_probit = accuracy_score(t_drop_test_random, probit_predictions)
#print(f'Accuracy: {acc_probit:.3f}')
#print(probit_model.summary())

#p_model = Probit(t_train_random,X_train_random)
#probit_model = p_model.fit()
#probit_predictions = probit_model.predict(X_test_random).round()
#acc_probit = accuracy_score(t_test_random, probit_predictions)
#print(f'Accuracy: {acc_probit:.3f}')


############################################################################################################################
############################################################################################################################
########################################## Logistic Regression #############################################################
############################################################################################################################
############################################################################################################################

#log_model = LogisticRegression(solver = 'saga', max_iter = 10000)
#log_model.fit(X_drop_train_random,t_drop_train_random)
#print(log_model.score(X_drop_test_random, t_drop_test_random))
#lin_predictions = lin_model.predict(X_drop_test_random).round()
#acc_lin = accuracy_score(t_drop_test_random, lin_predictions)
#print(lin_model.score(X_drop_train_random,t_drop_train_random))
#print(f'Accuracy: {acc_lin:.3f}')

###### Regular Season ######
# With Random spliting
logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_train_random,t_train_random)
print(f'Accuracy logit without dropped data for regular season and random split: {logcv_model.score(X_test_random, t_test_random):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_drop_train_random,t_drop_train_random)
print(f'Accuracy logit with dropping for regular season and random split: {logcv_model.score(X_drop_test_random, t_drop_test_random):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_PCA_train_random,t_PCA_train_random)
print(f'Accuracy logit with PCA for regular season and random split: {logcv_model.score(X_PCA_test_random, t_PCA_test_random):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_Transf_train_random,t_Transf_train_random)
print(f'Accuracy logit with transformation for regular season and random split: {logcv_model.score(X_Transf_test_random, t_Transf_test_random):.3f}')

# With Season spliting
logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_train_seasons,t_train_seasons)
print(f'Accuracy logit without dropped data for regular season and seasons split: {logcv_model.score(X_test_seasons, t_test_seasons):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_drop_train_seasons,t_train_seasons)
print(f'Accuracy logit with dropping for regular season and seasons split: {logcv_model.score(X_drop_test_seasons, t_test_seasons):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_PCA_train_seasons,t_train_seasons)
print(f'Accuracy logit with PCA for regular season and seasons split: {logcv_model.score(X_PCA_test_seasons, t_test_seasons):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_Transf_train_seasons,t_train_seasons)
print(f'Accuracy logit with transformation for regular season and seasons split: {logcv_model.score(X_Transf_test_seasons, t_test_seasons):.3f}')

###### Play Off ######
# With Random spliting
logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_train_play_off_random,t_train_play_off_random)
print(f'Accuracy logit without dropped data for playoffs and random split: {logcv_model.score(X_test_play_off_random, t_test_play_off_random):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_drop_train_play_off_random,t_drop_train_play_off_random)
print(f'Accuracy logit with dropping for playoffs and random split: {logcv_model.score(X_drop_test_play_off_random, t_drop_test_play_off_random):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_PCA_train_play_off_random,t_PCA_train_play_off_random)
print(f'Accuracy logit with PCA for playoffs and random split: {logcv_model.score(X_PCA_test_play_off_random, t_PCA_test_play_off_random):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_Transf_train_play_off_random,t_Transf_train_play_off_random)
print(f'Accuracy logit with transformation for playoffs and random split: {logcv_model.score(X_Transf_test_play_off_random, t_Transf_test_play_off_random):.3f}')

# With Season spliting
logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_train_play_off_seasons,t_train_play_off_seasons)
print(f'Accuracy logit without dropped data for playoffs and seasons split: {logcv_model.score(X_test_play_off_seasons, t_test_play_off_seasons):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_drop_train_play_off_seasons,t_train_play_off_seasons)
print(f'Accuracy logit with dropping for playoffs and seasons split: {logcv_model.score(X_drop_test_play_off_seasons, t_test_play_off_seasons):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_PCA_train_play_off_seasons,t_train_play_off_seasons)
print(f'Accuracy logit with PCA for playoffs and seasons split: {logcv_model.score(X_PCA_test_play_off_seasons, t_test_play_off_seasons):.3f}')

logcv_model = LogisticRegressionCV(solver = 'saga', max_iter = 10000)
logcv_model.fit(X_Transf_train_play_off_seasons,t_train_play_off_seasons)
print(f'Accuracy logit with transformation for playoffs and seasons split: {logcv_model.score(X_Transf_test_play_off_seasons, t_test_play_off_seasons):.3f}')


############################################################################################################################
########################################## NN Visualization ################################################################
############################################################################################################################

class Neuron():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, neuron_radius):
        circle = plt.Circle((self.x, self.y), radius=neuron_radius, fill=False)
        plt.gca().add_patch(circle)


class Layer():
    def __init__(self, network, number_of_neurons, number_of_neurons_in_widest_layer):
        self.vertical_distance_between_layers = 1000
        self.horizontal_distance_between_neurons = 50
        self.neuron_radius = 0.5
        self.number_of_neurons_in_widest_layer = number_of_neurons_in_widest_layer
        self.previous_layer = self.__get_previous_layer(network)
        self.y = self.__calculate_layer_y_position()
        self.neurons = self.__intialise_neurons(number_of_neurons)

    def __intialise_neurons(self, number_of_neurons):
        neurons = []
        x = self.__calculate_left_margin_so_layer_is_centered(number_of_neurons)
        for iteration in range(number_of_neurons):
            neuron = Neuron(x, self.y)
            neurons.append(neuron)
            x += self.horizontal_distance_between_neurons
        return neurons

    def __calculate_left_margin_so_layer_is_centered(self, number_of_neurons):
        return self.horizontal_distance_between_neurons * (self.number_of_neurons_in_widest_layer - number_of_neurons) / 2

    def __calculate_layer_y_position(self):
        if self.previous_layer:
            return self.previous_layer.y + self.vertical_distance_between_layers
        else:
            return 0

    def __get_previous_layer(self, network):
        if len(network.layers) > 0:
            return network.layers[-1]
        else:
            return None

    def __line_between_two_neurons(self, neuron1, neuron2):
        angle = atan((neuron2.x - neuron1.x) / float(neuron2.y - neuron1.y))
        x_adjustment = self.neuron_radius * sin(angle)
        y_adjustment = self.neuron_radius * cos(angle)
        line = plt.Line2D((neuron1.x - x_adjustment, neuron2.x + x_adjustment), (neuron1.y - y_adjustment, neuron2.y + y_adjustment))
        plt.gca().add_line(line)

    def draw(self, layerType=0):
        for neuron in self.neurons:
            neuron.draw( self.neuron_radius )
            if self.previous_layer:
                for previous_layer_neuron in self.previous_layer.neurons:
                    self.__line_between_two_neurons(neuron, previous_layer_neuron)
        # write Text
        x_text = self.number_of_neurons_in_widest_layer * self.horizontal_distance_between_neurons
        if layerType == 0:
            plt.text(x_text, self.y, 'Input Layer', fontsize = 12)
        elif layerType == -1:
            plt.text(x_text, self.y, 'Output Layer', fontsize = 12)
        else:
            plt.text(x_text, self.y, 'Hidden Layer '+str(layerType), fontsize = 12)

class NeuralNetwork():
    def __init__(self, number_of_neurons_in_widest_layer):
        self.number_of_neurons_in_widest_layer = number_of_neurons_in_widest_layer
        self.layers = []
        self.layertype = 0

    def add_layer(self, number_of_neurons ):
        layer = Layer(self, number_of_neurons, self.number_of_neurons_in_widest_layer)
        self.layers.append(layer)

    def draw(self):
        plt.figure()
        for i in range( len(self.layers) ):
            layer = self.layers[i]
            if i == len(self.layers)-1:
                i = -1
            layer.draw( i )
        plt.axis('scaled')
        plt.axis('off')
        plt.title( 'Neural Network architecture', fontsize=15 )
        plt.show()

class DrawNN():
    def __init__( self, neural_network ):
        self.neural_network = neural_network

    def draw( self ):
        widest_layer = max( self.neural_network )
        network = NeuralNetwork( widest_layer )
        for l in self.neural_network:
            network.add_layer(l)
        network.draw()
        
network = DrawNN( [133,20,1] )
network.draw()

network = DrawNN( [133,89,40,20,1] )
network.draw()

network_dropped = DrawNN( [88,60,20,1] )
network_dropped.draw()

network_dropped = DrawNN( [88,60,40,20,1] )
network_dropped.draw()

network_PCA = DrawNN( [33,10,1] )
network_PCA.draw()

network_PCA = DrawNN( [33,15,1] )
network_PCA.draw()

network_PCA = DrawNN( [31,31,10,1] )
network_PCA.draw()

network_PCA = DrawNN( [31,10,1] )
network_PCA.draw()
