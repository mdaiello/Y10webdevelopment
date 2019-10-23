import tkinter as tk
import requests
from tkinter import *
import webbrowser
from os import path
from PIL import ImageTk,Image
import cgi


def write_slogan():
    print("Welcome to Tkinter Window. Want to acess my site, please click below")
    
def openfile():
    myrequest = requests.get("https://clinicaltrials.gov/api/query/full_studies?expr=heart+attack&fmt=json")
    datajson = myrequest.json()
    ofile = open("forfun.html","w")
    study = datajson['FullStudiesResponse']['FullStudies'][0]
    print(str(study['Study']))
    ofile.write("<!DOCTYPE html>")
    ofile.write("<head>")
    ofile.write("<title>Heart Attack JSON Data</title>")
    ofile.write("<style>")
    ofile.write("body {")
    ofile.write("font-family: Arial;")
    ofile.write("margin: 0;")
    ofile.write("}")
    ofile.write(".header {")
    ofile.write("padding: 60px;")
    ofile.write("text-align: center;")
    ofile.write("background: #1abc9c;")
    ofile.write("color: white;")
    ofile.write("font-size: 30px;")
    ofile.write("}")
    ofile.write(".content {padding:20px;}")
    ofile.write("</style>")
    ofile.write("</head>")
    ofile.write("<body>")
    ofile.write("<div class=header>")
    ofile.write("<h1>Heart Attack Data</h1>")
    ofile.write("</div>")
    ofile.write("</body>")
    ofile.write("</html>")
    ofile.write("<style>")
    ofile.write("table {")
    ofile.write("font-family: arial, sans-serif;")
    ofile.write("border-collapse: collapse;")
    ofile.write("width: 100%;")
    ofile.write("}")
    ofile.write("td, th {")
    ofile.write("border: 1px solid #dddddd;")
    ofile.write("text-align: left;")
    ofile.write("padding: 8px;")
    ofile.write("}")
    ofile.write("tr:nth-child(even) {")
    ofile.write("background-color: #dddddd;")
    ofile.write("}")
    ofile.write("</style>")
    ofile.write("<center><img src=ha.jpg width=300 height=300></center>")
    ofile.write("<table>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Type of Disease" + "</td>")
    ofile.write("<td>" + "The data that you have been shown is for" + " " + datajson['FullStudiesResponse']['Expression'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Summary of Disease" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['DescriptionModule']['BriefSummary'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Registry" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['IdentificationModule']['BriefTitle'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Outcomes of this Disease" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")  
    ofile.write("<tr>")
    ofile.write("<td>" + "Primary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Expected Time Frame for treatment" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Time Frame" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeTimeFrame']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Other Outomes" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['OtherOutcomeList']['OtherOutcome'][0]['OtherOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Other Outcomes Time Frame " + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['OtherOutcomeList']['OtherOutcome'][0]['OtherOutcomeTimeFrame']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Criteria" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['EligibilityModule']['EligibilityCriteria']) + "</td>")
    ofile.write("</tr>")
    ofile.write("</table>")
    ofile.close()
    print("This is the JSON data for Heart Attack.  Have a Great Day!")



def openfile1():
    myrequest = requests.get("https://clinicaltrials.gov/api/query/full_studies?expr=cancer&fmt=json")
    datajson = myrequest.json()
    ofile = open("forfun.html","w")
    study = datajson['FullStudiesResponse']['FullStudies'][0]
    print(str(study['Study']))
    ofile.write("<!DOCTYPE html>")
    ofile.write("<head>")
    ofile.write("<title>Cancer JSON Data</title>")
    ofile.write("<style>")
    ofile.write("body {")
    ofile.write("font-family: Arial;")
    ofile.write("margin: 0;")
    ofile.write("}")
    ofile.write(".header {")
    ofile.write("padding: 60px;")
    ofile.write("text-align: center;")
    ofile.write("background: #1abc9c;")
    ofile.write("color: white;")
    ofile.write("font-size: 30px;")
    ofile.write("}")
    ofile.write(".content {padding:20px;}")
    ofile.write("</style>")
    ofile.write("</head>")
    ofile.write("<body>")
    ofile.write("<div class=header>")
    ofile.write("<h1>Cancer Data</h1>")
    ofile.write("</div>")
    ofile.write("</body>")
    ofile.write("</html>")
    ofile.write("<style>")
    ofile.write("<center><img src=cancer.jpg width=300 height=300></center>")
    ofile.write("table {")
    ofile.write("font-family: arial, sans-serif;")
    ofile.write("border-collapse: collapse;")
    ofile.write("width: 100%;")
    ofile.write("}")
    ofile.write("td, th {")
    ofile.write("border: 1px solid #dddddd;")
    ofile.write("text-align: left;")
    ofile.write("padding: 8px;")
    ofile.write("}")
    ofile.write("tr:nth-child(even) {")
    ofile.write("background-color: #dddddd;")
    ofile.write("}")
    ofile.write("</style>")
    ofile.write("<table>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Type of Disease" + "</td>")
    ofile.write("<td>" + "The data that you have been shown is for" + " " + datajson['FullStudiesResponse']['Expression'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Summary of Disease" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['DescriptionModule']['BriefSummary'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Registry" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['IdentificationModule']['BriefTitle'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Outcomes of this Disease" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")     
    ofile.write("<tr>")
    ofile.write("<td>" + "Primary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Expected Time Frame for treatment" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Time Frame" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeTimeFrame']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Criteria" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['EligibilityModule']['EligibilityCriteria']) + "</td>")
    ofile.write("</tr>")
    ofile.close()
    print("This is the JSON data for Cancer.  Have a Great Day!")

def openfile2():
    myrequest = requests.get("https://clinicaltrials.gov/api/query/full_studies?expr=malaria&fmt=json")
    datajson = myrequest.json()
    ofile = open("forfun.html","w")
    study = datajson['FullStudiesResponse']['FullStudies'][0]
    print(str(study['Study']))
    ofile.write("<!DOCTYPE html>")
    ofile.write("<head>")
    ofile.write("<title>Malaria JSON Data</title>")
    ofile.write("<style>")
    ofile.write("body {")
    ofile.write("font-family: Arial;")
    ofile.write("margin: 0;")
    ofile.write("}")
    ofile.write(".header {")
    ofile.write("padding: 60px;")
    ofile.write("text-align: center;")
    ofile.write("background: #1abc9c;")
    ofile.write("color: white;")
    ofile.write("font-size: 30px;")
    ofile.write("}")
    ofile.write(".content {padding:20px;}")
    ofile.write("</style>")
    ofile.write("</head>")
    ofile.write("<body>")
    ofile.write("<div class=header>")
    ofile.write("<h1>Malaria Data</h1>")
    ofile.write("</div>")
    ofile.write("</body>")
    ofile.write("</html>")
    ofile.write("<style>")
    ofile.write("<center><img src=malaria.jpg width=300 height=300></center>")
    ofile.write("table {")
    ofile.write("font-family: arial, sans-serif;")
    ofile.write("border-collapse: collapse;")
    ofile.write("width: 100%;")
    ofile.write("}")
    ofile.write("td, th {")
    ofile.write("border: 1px solid #dddddd;")
    ofile.write("text-align: left;")
    ofile.write("padding: 8px;")
    ofile.write("}")
    ofile.write("tr:nth-child(even) {")
    ofile.write("background-color: #dddddd;")
    ofile.write("}")
    ofile.write("</style>")
    ofile.write("<table>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Type of Disease" + "</td>")
    ofile.write("<td>" + "The data that you have been shown is for" + " " + datajson['FullStudiesResponse']['Expression'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Summary of Disease" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['DescriptionModule']['BriefSummary'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Registry" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['IdentificationModule']['BriefTitle'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Outcomes of this Disease" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")      
    ofile.write("<tr>")
    ofile.write("<td>" + "Primary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Expected Time Frame for treatment" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Time Frame" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeTimeFrame']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Criteria" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['EligibilityModule']['EligibilityCriteria']) + "</td>")
    ofile.write("</tr>")
    ofile.write("</table>")
    ofile.close()
    print("This is the JSON data fo Malaria.  Have a Great Day!")

def openfile3():
    myrequest = requests.get("https://clinicaltrials.gov/api/query/full_studies?expr=HIV&fmt=json")
    datajson = myrequest.json()
    ofile = open("forfun.html","w")
    study = datajson['FullStudiesResponse']['FullStudies'][0]
    print(str(study['Study']))
    ofile.write("<!DOCTYPE html>")
    ofile.write("<head>")
    ofile.write("<title>HIV JSON Data</title>")
    ofile.write("<style>")
    ofile.write("body {")
    ofile.write("font-family: Arial;")
    ofile.write("margin: 0;")
    ofile.write("}")
    ofile.write(".header {")
    ofile.write("padding: 60px;")
    ofile.write("text-align: center;")
    ofile.write("background: #1abc9c;")
    ofile.write("color: white;")
    ofile.write("font-size: 30px;")
    ofile.write("}")
    ofile.write(".content {padding:20px;}")
    ofile.write("</style>")
    ofile.write("</head>")
    ofile.write("<body>")
    ofile.write("<div class=header>")
    ofile.write("<h1>HIV Data</h1>")
    ofile.write("</div>")
    ofile.write("</body>")
    ofile.write("</html>")
    ofile.write("<style>")
    ofile.write("<center><img src=HIV.jpg></center>")
    ofile.write("table {")
    ofile.write("font-family: arial, sans-serif;")
    ofile.write("border-collapse: collapse;")
    ofile.write("width: 100%;")
    ofile.write("}")
    ofile.write("td, th {")
    ofile.write("border: 1px solid #dddddd;")
    ofile.write("text-align: left;")
    ofile.write("padding: 8px;")
    ofile.write("}")
    ofile.write("tr:nth-child(even) {")
    ofile.write("background-color: #dddddd;")
    ofile.write("}")
    ofile.write("</style>")
    ofile.write("<table>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Type of Disease" + "</td>")
    ofile.write("<td>" + "The data that you have been shown is fpr" + " " + datajson['FullStudiesResponse']['Expression'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Summary of Disease" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['DescriptionModule']['BriefSummary'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Registry" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['IdentificationModule']['BriefTitle'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Outcomes of this Disease" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Primary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Expected Time Frame for treatment" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Time Frame" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeTimeFrame']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Criteria" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['EligibilityModule']['EligibilityCriteria']) + "</td>")
    ofile.write("</tr>")
    ofile.write("</table>")
    ofile.close()
    print("This is the JSON data for HIV. Have a Great Day!")
    

    
def openfile5():
    myrequest = requests.get("https://clinicaltrials.gov/api/query/full_studies?expr=pneumonia&fmt=json")
    datajson = myrequest.json()
    ofile = open("forfun.html","w")
    study = datajson['FullStudiesResponse']['FullStudies'][0]
    print(str(study['Study']))
    ofile.write("<!DOCTYPE html>")
    ofile.write("<head>")
    ofile.write("<title>Pneumonia JSON Data</title>")
    ofile.write("<style>")
    ofile.write("body {")
    ofile.write("font-family: Arial;")
    ofile.write("margin: 0;")
    ofile.write("}")
    ofile.write(".header {")
    ofile.write("padding: 60px;")
    ofile.write("text-align: center;")
    ofile.write("background: #1abc9c;")
    ofile.write("color: white;")
    ofile.write("font-size: 30px;")
    ofile.write("}")
    ofile.write(".content {padding:20px;}")
    ofile.write("</style>")
    ofile.write("</head>")
    ofile.write("<body>")
    ofile.write("<div class=header>")
    ofile.write("<h1>Pneumonia Data</h1>")
    ofile.write("</div>")
    ofile.write("</body>")
    ofile.write("</html>")
    ofile.write("<style>")
    ofile.write("table {")
    ofile.write("font-family: arial, sans-serif;")
    ofile.write("border-collapse: collapse;")
    ofile.write("width: 100%;")
    ofile.write("}")
    ofile.write("td, th {")
    ofile.write("border: 1px solid #dddddd;")
    ofile.write("text-align: left;")
    ofile.write("padding: 8px;")
    ofile.write("}")
    ofile.write("tr:nth-child(even) {")
    ofile.write("background-color: #dddddd;")
    ofile.write("}")
    ofile.write("</style>")
    ofile.write("<table>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Type of Disease" + "</td>")
    ofile.write("<td>" + "The data that you have been shown is for" + " " + datajson['FullStudiesResponse']['Expression'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Summary of Disease" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['DescriptionModule']['BriefSummary'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Registry" + "</td>")
    ofile.write("<td>" + study['Study']['ProtocolSection']['IdentificationModule']['BriefTitle'] + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Outcomes of this Disease" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>") 
    ofile.write("<tr>")
    ofile.write("<td>" + "Primary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Expected Time Frame for treatment" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]['PrimaryOutcomeMeasure']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Time Frame" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeTimeFrame']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Secondary Outcome Description" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['OutcomesModule']['SecondaryOutcomeList']['SecondaryOutcome'][0]['SecondaryOutcomeDescription']) + "</td>")
    ofile.write("</tr>")
    ofile.write("<tr>")
    ofile.write("<td>" + "Criteria" + "</td>")
    ofile.write("<td>" + str(study['Study']['ProtocolSection']['EligibilityModule']['EligibilityCriteria']) + "</td>")
    ofile.write("</tr>")
    ofile.write("</table>")
    ofile.close()
    print("This is the JSON data for Pneumonia.  Have a Great Day!") 

def test(event):
    print(event) 

def clickme():
    print(tkvar.get())
    x = " "
    b1 = Button(command=webbrowser.open('file://' + path.realpath('forfun.html')))

root = Tk()
root.title("Welcome to my API Application!!")
root.geometry("2000x2000")
root.configure(background='#4045D2')
imageFile = "HIV.jpg"
root.im1 = Image.open(imageFile)

tkvar = StringVar(root)
topframe = Frame(root,bg='#4045D2',height='20')
topframe.pack(fill=X) # make as wide as root
can1 = Canvas(topframe,height='25',width='25',bg="#4045D2",highlightthickness=5)
can1.create_line(0, 5, 20, 5,fill='red')
can1.create_line(0, 10, 20, 10,fill='orange')
can1.create_line(0, 15, 20, 15,fill='blue')
can1.bind("<Button-1>",test ) # keyword 
can1.pack(side=LEFT, padx=5, pady=5)

spaceframe = Frame(root,height=10)
spaceframe.pack(fill=X)
frame = Frame(root,borderwidth = 3, relief=RAISED, width=700,height=550)
frame.pack(fill=None, expand=False)
label = tk.Label(frame,
                  text="Please select a Disease and then press Access Site",
                  fg="orange",
                 font="Verdana 20 bold")
label.pack(padx=0, pady=4)
label.config( height = 3, width = 60)
button1 = tk.Button(frame,
                   text="Heart Attack",
                   fg="blue",
                font="Verdana 19 bold",
                   command=openfile)
button1.config( height = 3, width = 60)
button1.pack(padx=0, pady=5)
button2 = tk.Button(frame,
                    text="Cancer",
                    fg="blue",
                    font="Verdana 19 bold",
                    command=openfile1)
button2.config( height = 3, width = 60)
button2.pack(padx=0, pady=6)
button4 = tk.Button(frame,
                    text="Malaria",
                    fg="blue",
                    font="Verdana 19 bold",
                    command=openfile2)
button4.config( height = 3, width = 60)
button4.pack(padx=0, pady=7)
button5 = tk.Button(frame,
                    text="HIV",
                    fg="blue",
                    font="Verdana 19 bold",
                    command=openfile3)
button5.pack(padx=0, pady=8)
button5.config( height = 3, width = 60)
button6 = tk.Button(frame,
                    text="Pneumonia",
                    fg="blue",
                    font="Verdana 19 bold",
                    command=openfile5)
button6.pack(padx=0, pady=12)
button6.config( height = 3, width = 60)
button1 = tk.Button(frame,
                    text="Access Site",
                    fg="dark green",
                    font="Verdana 19 bold",
                    command=clickme)
button1.pack(padx=0, pady=11)
button1.config( height = 3, width = 60)
spaceframe = Frame(root,height=10)
button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit,
                   font="Verdana 19 bold")
button.pack(padx=0, pady=12)
button.config( height = 3, width = 60)
spaceframe.pack(fill=X)
















