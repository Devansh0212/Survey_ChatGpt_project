import matplotlib.pyplot as plt 
import pandas as pd

def main_menu():
    print('1. Histogram') 
    
def Histogram():
    df=pd.read_csv('Survey.csv')
    ag=df['Age Group']
    ge=df['Gender']
    af=df['Affiliation']
    fl=df['Field']
    co=df['Continent']
    ch=df['ChatGPT']
    cp=df['CGPT Plagiarism']
    ai=df['Use AI Tools']
    cu=df['ChGPT for University']
    ua=df['University Allow']
    us=df['Usage']
    print('''Select Histogram from 1 to 11: 
    1.  Surveyers Age Group
    2.  Surveyers Gender Identity
    3.  Surveyers Current academic position or Affiliation
    4.  Surveryers Field
    5.  Surveyers Continent
    6.  Have you ever experimented with ChatGPT?
    7.  What did you use ChatGPT for?
    8.  Do you think ChatGPT is plagiarism in and of itself?
    9.  The use of AI tools such as ChatGPT would inhibit education
    10. Students should use the assistance of ChatGPT for University assignments ethically?
    11. Should universities allow students to use ChatGPT?
    ''')
    op=int(input("Enter Choice: "))
    if op==1:
        plt.hist(ag,bins=[0,1,2,3],edgecolor='White') 
        plt.xticks([0,1,2,3],rotation="vertical")
        plt.yticks([0,20,40,60,80,100,120,140,160])
        plt.title("Surveyers Age Group")
    elif op==2:
        plt.hist(ge,bins=[0,1,2],edgecolor='White') 
        plt.xticks([0,1,2,3],rotation="vertical")
        plt.yticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
        plt.title("Gender Identity")
    elif op==3:
        plt.hist(af,bins=[0,1,2,3,4],edgecolor='White') 
        plt.xticks([0,1,2,3,4],rotation="vertical")
        plt.yticks([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150])
        plt.title("Current Academic position or Affiliation")
    elif op==4:
        plt.hist(fl,bins=[0,1,2,3,4,5,6,7,8,9],edgecolor='White') 
        plt.xticks([0,1,2,3,4,5,6,7,8,9],rotation="vertical")
        plt.yticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85])
        plt.title("Surveryers Field")
    elif op==5:
        plt.hist(co,bins=[0,1,2,3,4,5,6],edgecolor='White') 
        plt.xticks([0,1,2,3,4,5,6],rotation="vertical")
        plt.yticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130])
        plt.title("Surveyers Continent") 
    elif op==6:
        plt.hist(ch,bins=[0,1,2],edgecolor='White') 
        plt.xticks([0,1,2],rotation="vertical")
        plt.yticks([0,20,40,60,80,100,120,140,160])
        plt.title("Have you ever experimented with ChatGPT?")
    elif op==7:
        plt.hist(us,bins=[0,1,2,3,4],edgecolor='White') 
        plt.xticks([0,1,2,3,4],rotation="vertical")
        plt.yticks([0,5,10,15,20,25,30,35,40])
        plt.title("What did you use ChatGPT for?")
    elif op==8:
        plt.hist(cp,bins=[0,1,2,3],edgecolor='White') 
        plt.xticks([0,1,2,3],rotation="vertical")
        plt.yticks([0,10,20,30,40,50,60,70])
        plt.title("Do you think ChatGPT is plagiarism in and of itself?") 
    elif op==9:
        plt.hist(ai,bins=[0,1,2,3,4,5],edgecolor='White') 
        plt.xticks([0,1,2,3,4,5],rotation="vertical")
        plt.yticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90])
        plt.title("The use of AI tools such as ChatGPT would inhibit education")
    elif op==10:
        plt.hist(cu,bins=[0,1,2,3,4,5],edgecolor='White') 
        plt.xticks([0,1,2,3,4,5],rotation="vertical")
        plt.yticks([0,10,20,30,40,50,60,70,80])
        plt.title("Students should use the assistance of ChatGPT for University assignments ethically")
    elif op==11:
        plt.hist(ua,bins=[0,1,2,3],edgecolor='White') 
        plt.xticks([0,1,2,3],rotation="vertical")
        plt.yticks([0,20,40,60,80,100,120,140])
        plt.title("Should universities allow students to use ChatGPT?")
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show()

main_menu()

opt=(int(input('Enter 1:'))) 
if opt==1:
    Histogram()
else:
    print("Enter Valid Output")