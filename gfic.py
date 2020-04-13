from tkinter import*
import sys
import os

root=Tk()

def fiche_client():
    os.system('python3 ~/Programmation/infoclient2.py')


######### GRAPHICS ##########

frame=Frame(root, bg='#FFFF99', height = 600, width = 800)
frame.pack()

#framegrid=Frame(root, bg='#FFFF99', height=600, width=800)
#framegrid.grid(column=0, row=0, sticky=(N,W,E,S))
#framegrid.columnconfigure(0, weight=1)
#framegrid.rowconfigure(0, weight=1)
#framegrid.pack()

#Compte Client
L1=Button(frame, text="Numero Client ;")
L1.place(x=10, y=30)
E1=Entry(frame, bd=3, width=17)
E1.place(x=158, y=30)

#Bouton Fiches clients
B1=Button(frame, text="Fiches clients F3", width=15, command=fiche_client)
B1.place(x=500, y=30)

#Bouton historique
B2=Button(frame, text="Historique F4", width=15)
B2.place(x=650, y=30)

#Info client sur facture
infoc=Frame(frame, bg="white", highlightbackground="black", highlightthickness=1, relief="sunken", height=90, width=300)
infoc.place(x=10, y=70)

#################Tracking###################
infot=Entry(frame, bd=3, width=30)
infot.place(x=520, y=80)
#Selection transport
tkvar=StringVar(frame)

#Choix du Menu
choices={'Purolator', 'Poste Canada', 'Autres'}
tkvar.set('Transport') #set the default option

#Menu de Selection transport
popupMenu=OptionMenu(frame, tkvar, *choices)
popupMenu.place(x=350, y=80, width=150)

# change dropdown Value
def change_dropdown(*args):
    print(tkvar.get())



##################NOTE###################
notes=Label(frame, text='References:')
notes.place(x=420, y=135)

notes1=Entry(frame, bd=3, width=30)
notes1.place(x=520, y=130)



######### INVENTAIRE ###########
######BOUTON DE RECHERCHE PRODUITS
B3=Button(frame, text="Articles F2", width=15)
B3.place(x=350, y=30)


#######ITEM SUR FACTURE#######
#articles=Label(framegrid, text="Articles").grid(row=5, column=1)
#description=Label(framegrid, text="Description").grid(row=5, column=2)
#quantite=Label(framegrid, text="Quantite").grid(row=5, column=3)
#prix=Label(framegrid, text="Prix Unitaire").grid(row=5, column=4)
#extension=Label(framegrid, text="Extension").grid(row=5, column=5)
fondfacture=Frame(frame, height=230, width=780, bg='white', highlightbackground="black", highlightthickness=1)
fondfacture.place(x=10, y=200)



######ITEM POUR RENTRER SUR FACTURE#####
itemf=Entry(frame, bd=3, width=30)
itemf.place(x=10, y=435)



######NOTES FIN DE PAGE######
notef=Entry(frame, bd=3, width=45, text="Notes")
notef.place(height=100, x=10, y=470)



###### MENU BANQUAIRE#####
tkvar2=StringVar(frame)
choices={'Virement Banquaire', 'Paypal', 'Square', 'Autres'}
tkvar2.set('Type Paiement') #set the default option
popupMenu=OptionMenu(frame, tkvar2, *choices)
popupMenu.place(x=390, y=450, width=180)



# change dropdown Value
def change_dropdown2(*args):
    print(tkvar2.get())



#######SOUS TOTAUX######
mt=Label(frame, text="Sous-Totaux")
mt.place(x=580, y=450)



#######TPS######
mt=Label(frame, text="TPS 5%")
mt.place(x=580, y=475)



#######TVQ####
mt=Label(frame, text="TVQ 9.975%")
mt.place(x=580, y=500)



#######TOTAL####
mt=Label(frame, text='Total', font=('none', 20))
mt.place(x=580, y=550)



######BOUTON IMPRIMER######
bi=Button(frame, text="Facturer F9")
bi.place(x=450, y=550)


tkvar2.trace('w', change_dropdown2) #pour le dropdown menu

root.mainloop()

