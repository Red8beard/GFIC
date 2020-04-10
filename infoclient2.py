from tkinter import *
#from PIL import ImageTk,Image
import sqlite3


root = Tk()
#root.title('Codemy.com - Learn To Code!')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x600")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
#def create_table():
c.execute('CREATE TABLE IF NOT EXISTS addresses(prenom TEXT, nom TEXT, addresse TEXT, ville TEXT, province TEXT, codepostal TEXT)')

# Create Update function to update a record
def update():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()

	c.execute("""UPDATE addresses SET
		prenom = :prenom,
		nom = :nomdefamille,
		addresse = :addresse,
		ville = :ville,
		province = :province,
		codepostal = :codepostal

		WHERE oid = :oid""",
		{
		'prenom': f_name_editor.get(),
		'nomdefamille': l_name_editor.get(),
		'addresse': address_editor.get(),
		'ville': city_editor.get(),
		'province': state_editor.get(),
		'codepostal': zipcode_editor.get(),
		'oid': record_id
		})


	#Commit Changes
	conn.commit()

	# Close Connection
	conn.close()

	editor.destroy()
	root.deiconify()

# Create Edit function to update a record
def edit():
	root.withdraw()
	global editor
	editor = Tk()
	editor.title('Mettre a jour')
	editor.geometry("400x300")
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()
	# Query the database
	c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
	records = c.fetchall()

	#Create Global Variables for text box names
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global zipcode_editor

	# Create Text Boxes
	f_name_editor = Entry(editor, width=30)
	f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
	l_name_editor = Entry(editor, width=30)
	l_name_editor.grid(row=1, column=1)
	address_editor = Entry(editor, width=30)
	address_editor.grid(row=2, column=1)
	city_editor = Entry(editor, width=30)
	city_editor.grid(row=3, column=1)
	state_editor = Entry(editor, width=30)
	state_editor.grid(row=4, column=1)
	zipcode_editor = Entry(editor, width=30)
	zipcode_editor.grid(row=5, column=1)

	# Create Text Box Labels
	f_name_label = Label(editor, text="Prenom")
	f_name_label.grid(row=0, column=0, pady=(10, 0))
	l_name_label = Label(editor, text="Nom de famille")
	l_name_label.grid(row=1, column=0)
	address_label = Label(editor, text="Addresse")
	address_label.grid(row=2, column=0)
	city_label = Label(editor, text="Ville")
	city_label.grid(row=3, column=0)
	state_label = Label(editor, text="Province")
	state_label.grid(row=4, column=0)
	zipcode_label = Label(editor, text="Code Postal")
	zipcode_label.grid(row=5, column=0)

	# Loop thru results
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zipcode_editor.insert(0, record[5])


	# Create a Save Button To Save edited record
	edit_btn = Button(editor, text="Sauvegarder", command=update)
	edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)




# Create Function to Delete A Record
def delete():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor
	c = conn.cursor()

	# Delete a record
	c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

	delete_box.delete(0, END)

	#Commit Changes
	conn.commit()

	# Close Connection
	conn.close()



# Create Submit Function For database
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO addresses VALUES (:prenom, :nomdefamille, :addresse, :ville, :province, :codepostal)",
			{
				'prenom': f_name.get(),
				'nomdefamille': l_name.get(),
				'addresse': address.get(),
				'ville': city.get(),
				'province': state.get(),
				'codepostal': zipcode.get()
			})


	#Commit Changes
	conn.commit()

	# Close Connection
	conn.close()

	# Clear The Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)

# Create Query Function
def query():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	# print(records)

	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[6]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)

	#Commit Changes
	conn.commit()

	# Close Connection
	conn.close()


# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


# Create Text Box Labels
f_name_label = Label(root, text="Prenom")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Nom de famille")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Addresse")
address_label.grid(row=2, column=0)
city_label = Label(root, text="Ville")
city_label.grid(row=3, column=0)
state_label = Label(root, text="Province")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Code Postal")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Enregistrer", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Liste complete", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Supprimer", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Modifier", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


#Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()

