from itertools import count
from tkinter import*
from tkinter import messagebox #paziņojumi, ieteikumi

mansLogs=Tk()
mansLogs.title("TicTicToe")


speletajsX=True
count=0

def btnClick(button): #padod visu pogu
    global speletajsX, count #kādi mainīgie tiks izmantoti visā programmā
    if button["text"]==""and speletajsX==True: #spēlē X spēlētājs
        button["text"]="X" #maina uz X
        speletajsX=False
        count+=1 #palielina rūtiņu skaitu
        checkWinner()
    elif button["text"]=="" and speletajsX==False:
        button["text"]='O'
        speletajsX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror('TicTocToe', 'Šeit kāds jau ir ieklišķinājis')


def infoLogs():
    newLogs=Toplevel()
    newLogs.title('Info par programmu')
    newLogs.geometry("715x240")
    desc=Label(newLogs, text='')
    desc.grid(row=0, column=0)
    desc=Label(newLogs, text='SPĒLES NOTEIKUMI',bg = "#F4C2C2", font=('Helvica 10 bold') )
    desc.grid(row=1, column=0)
    desc=Label(newLogs, text='')
    desc.grid(row=2, column=0)
    desc=Label(newLogs, text='Spēlē piedalās divi spēlētāji, viens spēlē ar X simbolu, otrs ar O.')
    desc.grid(row=3, column=0)
    desc=Label(newLogs, text='Gājienus veic pamīšus, sākot ar X spēlētāju, katrā gājienā var novietot tikai vienu X vai O simbolu.')
    desc.grid(row=4, column=0)
    desc=Label(newLogs, text='Sākotnēji laukumu veido 9 tukši kvadrāti, simbolus var novietot tikai tukšajos laukumos, un, kad laukums ir aizpildīt, viņu nevar mainīt.')
    desc.grid(row=5, column=0)
    desc=Label(newLogs, text='Uzvarētājs ir pirmais, kurš taisnā līnijā iegūst 3 simbolus (līnija var būt novietota pa diagonāli, vertikāli vai horizontāli).')
    desc.grid(row=6, column=0)
    desc=Label(newLogs, text='Spēle ir beigusies, kad visi 9 lauciņi ir aizpildīti ar simboliem, pat ja nevienam no spēlētājiem nav taisnas linijas ar 3 simboliem.')
    desc.grid(row=7, column=0)
    desc=Label(newLogs, text='Ja nevienam spēlētājam nav 3 simbolu līnija, tas tiek uzskatīts par neizšķirtu.')
    desc.grid(row=8, column=0)
    desc=Label(newLogs, text='')
    desc.grid(row=9, column=0)
    desc=Label(newLogs, text='Opcijās ir iespēja spēli aizvērt vai sākt visu pa jaunam.')
    desc.grid(row=10, column=0)
    return 0

def disableButtons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return 0

def reset():
    global count, speletajsX
    count = 0
    speletajsX=True
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1['text']=''
    btn2['text']=''
    btn3['text']=''
    btn4['text']=''
    btn5['text']=''
    btn6['text']=''
    btn7['text']=''
    btn8['text']=''
    btn9['text']=''
    return 0

def checkWinner():
    global winner 
    winner=False #noteikts, ja būs neizškirts
    if(btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X" or btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" or btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X" or
      btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X" or btn3["text"]=="X"and btn5["text"]=="X" and btn7["text"]=="X" or 
      btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X" or btn2["text"]=="X"and btn5["text"]=="X" and btn8["text"]=="X" or btn3["text"]=="X" and btn6["text"]=="X"and btn9["text"]=="X"): #vertikāli
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe", "X ir uzvarētājs")
    elif(btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O" or btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" or btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O" or
      btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O" or btn3["text"]=="O"and btn5["text"]=="O" and btn7["text"]=="O" or 
      btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O" or btn2["text"]=="O"and btn5["text"]=="O" and btn8["text"]=="O" or btn3["text"]=="O" and btn6["text"]=="O"and btn9["text"]=="O"):
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe", "O ir uzvarētājs")
    elif count==9 and winner==False:
        disableButtons()
        messagebox.showinfo("TicTacToe", "Neizšķirts")


btn1=Button(mansLogs, text="", width=6, height=3, font=('Helvica 24 bold'),command=lambda:btnClick(btn1))
btn2=Button(mansLogs, text="", width=6, height=3, font=('Helvica 24 bold'),command=lambda:btnClick(btn2))
btn3=Button(mansLogs, text="", width=6, height=3, font=('Helvica 24 bold'),command=lambda:btnClick(btn3))
btn4=Button(mansLogs, text="", width=6, height=3, font=('Helvica 24 bold'),command=lambda:btnClick(btn4))
btn5=Button(mansLogs, text="", width=6, height=3, font=('Helvica 24 bold'),command=lambda:btnClick(btn5))
btn6=Button(mansLogs, text="", width=6, height=3, font=('Helvica 24 bold'),command=lambda:btnClick(btn6))
btn7=Button(mansLogs, text="", width=6, height=3, font=('Helvica 24 bold'),command=lambda:btnClick(btn7))
btn8=Button(mansLogs, text="", width=6, height=3, font=('Helvica 24 bold'),command=lambda:btnClick(btn8))
btn9=Button(mansLogs, text="", width=6, height=3, font=('Helvica 24 bold'),command=lambda:btnClick(btn9))

btn1.config(bd=8, bg = "#F4C2C2")
btn2.config(bd=8, bg = "#FFE0E0")
btn3.config(bd=8, bg = "#F4C2C2")
btn4.config(bd=8, bg = "#FFE0E0")
btn5.config(bd=8, bg = "#F4C2C2")
btn6.config(bd=8, bg = "#FFE0E0")
btn7.config(bd=8, bg = "#F4C2C2")
btn8.config(bd=8, bg = "#FFE0E0")
btn9.config(bd=8, bg = "#F4C2C2")

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

galvenalzvelne=Menu(mansLogs)#izveido galveno izvelni
mansLogs.config(menu=galvenalzvelne)#pievieno gara...

opcijas=Menu(galvenalzvelne, tearoff=False)#maza izvēlne
galvenalzvelne.add_cascade(label="Opcijas", menu=opcijas)#lejupkritošais  saraksts

opcijas.add_command(label="Jauna spēle", command=reset)
opcijas.add_command(label="Iziet", command=mansLogs.quit)
galvenalzvelne.add_command(label="Par programmu", command=infoLogs)






mansLogs.mainloop()