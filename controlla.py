import tkinter as tk
import PIL
from PIL import Image, ImageTk
import steampype
import urllib3
import io
window = tk.Tk()
tklist=[]


#color and user settings
clbk='#1b2838'
clbt='#274155'
clbtx='#66c0f4'
coloruser='#16202d'
colormainusr='#283142'
steamid=''

window.title("controller")
window.geometry("400x500")
window.configure(background=clbk)

steamsesh = steampype.steamCon(steamid)

def outputNodes(title,nodes):
    global tklist
    tklist=[]
    tklist=[0 for y in range(len(nodes))]
    i=1
    j=0
    destroy()
    tk.Label(actFrame,text=title,bg=clbk,fg='#2a9bd3').grid(row=0,column=0,sticky='w')
    for friend in nodes:
        nodeFrame=tk.Frame(actFrame)
        nodeFrame.grid(row=i,column=0,sticky='w',padx=5,pady=5)
        nodeFrame.configure(bg=coloruser)
        http= urllib3.PoolManager()
        r= http.request('GET',friend[1])
        img= Image.open(io.BytesIO(r.data))
        resized=img.resize((60,60),Image.ANTIALIAS)
        tklist[j]=(ImageTk.PhotoImage(resized))
        tk.Label(nodeFrame, image=tklist[j]).grid(row=0,column=0, padx=18, pady=18, rowspan=3)
        tk.Label(nodeFrame, text=friend[0], bg=coloruser, fg="white", font=("Helvetica",14)).grid(row=0,column=1, padx=3, pady=3)
        tk.Label(nodeFrame, text=friend[2], bg=coloruser, fg="white", font=("Helvetica",12)).grid(row=1,column=1, padx=3, pady=3)
        i=i+1
        j=j+1


def friends():
    global Can1
    friendlist=steamsesh.friends()
    outputNodes("Friends List: ",friendlist)

def games():
    gameslist=steamsesh.games()
    outputNodes("Games List: ",gameslist)

def badges():
    badgelist=steamsesh.badges()
    outputNodes("Badge List: ",badgelist)


def destroy():
    global actFrame
    global Can1
    actFrame.forget()
    actFrame.destroy()
    actFrame=tk.Frame(window,bg=clbk)
    actFrame.grid(row=2, column=0, sticky='nw')
    print("cleared")



#main profile view
userFrame= tk.Frame(window)
userFrame.configure(background=colormainusr)
userFrame.grid(row=0, column=0, padx=12, pady=12,sticky='w')
url= steamsesh.imgurl
http= urllib3.PoolManager()
r= http.request('GET',url)
img= Image.open(io.BytesIO(r.data))
resized=img.resize((60,60),Image.ANTIALIAS)
tkimage=ImageTk.PhotoImage(resized)
tk.Label(userFrame, image=tkimage).grid(row=0,column=0, padx=18, pady=18, rowspan=3)
tk.Label(userFrame, text=steamid, bg=colormainusr, fg="white", font=("Helvetica",16)).grid(row=0,column=1, padx=3, pady=3)

#actionFrame initialization
actFrame=tk.Frame(window,bg=clbk)
actFrame.grid(row=2, column=0, sticky='nw')



#button selectors
btFrame= tk.Frame(window,bg=clbk)
btFrame.grid(row=1, column=0, pady=4, sticky='w')
tk.Label(btFrame,text="Select an action: ",bg=clbk,fg='#2a9bd3',font=('Helvetica',12)).grid(row=0,column=0,columnspan=3,padx=5,pady=5)
tk.Button(btFrame,text="Friends",bg=clbt,fg=clbtx,command=friends).grid(row=1,column=0,ipadx=4)
tk.Button(btFrame,text="Games",bg=clbt,fg=clbtx,command=games).grid(row=1,column=1,ipadx=4)
tk.Button(btFrame,text="Badges",bg=clbt,fg=clbtx,command=badges).grid(row=1,column=2,ipadx=4)
tk.Button(btFrame,text="Clear Field",bg=clbt,fg=clbtx,command=destroy).grid(row=1,column=3,ipadx=4)

#test Field



window.mainloop()
