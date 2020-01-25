from tkinter import *
from tkinter import messagebox
# import requests
import sys, webbrowser
from mapbox import Uploader
from mapbox import Surface
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

master = Tk()
master.title("AGRO-TECH")
master.geometry("600x600")
master.config(background="light grey")

#Declear heading
heading = Label(master,text="Agro-Tech",font=("Times New Romen",25,"bold"))
heading.place(x=170,y=40)
def photobutton():
    '''This Function for Show google map when Bugtton was clicked'''
    if len(sys.argv) > 1:  # Argument passed
        map_string = ' '.join(sys.argv[1:])
        webbrowser.open('https://www.google.com/maps/place/' + map_string)
        

    else:

        print("Pass the string as command line argument, Try Again")

def photob():
    data = pd.read_csv("agree.csv")
    print("\nDisplay the Key ")
    print(list(data))

    print("\nDisplay the Row and Column")
    print(data.shape)

    print("\nDisplay the All Data present in Dataset")
    print(data.describe)


    data.head()

    # for compare total cost and earning
    data.plot(x='Earning', y='totalcost', style='o')
    plt.title('Earning vs totalcost')
    plt.xlabel('Earning')
    plt.ylabel('totalcost')
    plt.show()

    # for
    plt.figure(figsize=(100, 100))
    plt.tight_layout()
    seabornInstance.distplot(data['Earning'])

    '''this is conversion str to int'''
    file_handler = open("agree.csv", "r")

    # creating a Pandas DataFrame
    # using read_csv function
    # that reads from a csv file.
    data = pd.read_csv(file_handler, sep=",")

    # closing the file handler
    file_handler.close()

    # creating a dict file
    Crop = {'ARHAR': 1, 'COTTON': 2, 'GRAM': 3, 'GROUNDNUT': 4, 'MAIZE': 5, 'OILSEEDS': 6, 'RICE': 7, 'SUGARCANE': 8,
            'WHEAT': 9, 'MOONG': 10}
    answerclass = {'ARHAR': 1, 'COTTON': 2, 'GRAM': 3, 'GROUNDNUT': 4, 'MAIZE': 5, 'OILSEEDS': 6, 'RICE': 7,
                   'SUGARCANE': 8, 'WHEAT': 9, 'MOONG': 10}
    State = {'Uttar Pradesh': 101, 'Karnataka': 102, 'Gujarat': 103, 'Andhra Pradesh': 104, 'Maharashtra': 105,
             'Punjab': 106,
             'Tamil Nadu': 107, 'Bihar': 108, 'Orissa': 109, 'West Bengal': 110,
             'Madhya Pradesh': 111, 'Rajasthan': 112, 'Haryana': 113}
    #
    # # traversing through dataframe
    # Gender column and writing
    # values where key matches
    data.Crop = [Crop[item] for item in data.Crop]
    print(data)

    data.answerclass = [answerclass[item] for item in data.answerclass]
    print(data)

    data.State = [State[item] for item in data.State]
    print(data)
    '''this is conversion str to int'''

    # X = data[['Crop']['State']['2018-19']['Earning']['totalcost']]
    # y = data['answerclass']
    X = data['Earning'].values.reshape(-1, 1)
    y = data['answerclass']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)  # training the algorithm

    # To retrieve the intercept:
    print(regressor.intercept_)
    # For retrieving the slope:
    print(regressor.coef_)

    y_pred = regressor.predict(X_test)

    plt.scatter(X_test, y_test, color='gray')
    plt.plot(X_test, y_pred, color='red', linewidth=2)
    plt.show()
    print(Crop)

f1 = Label(master,text="Feature 1")
f1.place(x=20,y=110)

fenty1 = Entry(master)
fenty1.place(x=90,y=110)


f2 = Label(master,text="Feature 2")
f2.place(x=20,y=140)

fenty2 = Entry(master)
fenty2.place(x=90,y=140)



f3 = Label(master,text="Feature 3")
f3.place(x=20,y=170)

fenty3 = Entry(master)
fenty3.place(x=90,y=170)



f4 = Label(master,text="Feature 4")
f4.place(x=20,y=200)

fenty4 = Entry(master)
fenty4.place(x=90,y=200)


f5 = Label(master,text="Feature 5")
f5.place(x=20,y=230)

fenty5 = Entry(master)
fenty5.place(x=90,y=230)


f6 = Label(master,text="Prediction")
f6.place(x=20,y=260)

fenty6 = Entry(master)
fenty6.place(x=90,y=260)

finalbutt = Button(master,text="Submit",command=calling())
finalbutt.place(x=90,y=300)


#Code for photo img
sate=PhotoImage(file=r"C:\Users\hp\Desktop\heckk\satt.png")
satimg=Button(master,width=140,height=70,image=sate,relief="solid",bd=1,command=lambda: photobutton())
satimg.place(x=180,y=420)

imgtitle = Label(master,text="7/12 on Google Map",bg="light gray")
imgtitle.place(x=200,y=500)


#Code for photo img1
nu=PhotoImage(file=r"C:\Users\hp\Desktop\nu.png")
nuimg=Button(master,width=140,height=70,image=nu,relief="solid",bd=1,command=lambda: photob())
nuimg.place(x=180,y=300)

nutitle = Label(master,text="Prediction",bg="light gray")
nutitle.place(x=220,y=375)


master.mainloop()