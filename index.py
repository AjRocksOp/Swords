# To Perform CRUD Operations on 'swords.csv' 

from menu import menu
import csv

# Function to read all Sword data from CSV
def read_data():
    with open('data.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)

        swords_data = [row for row in reader]
        # swords_data = []
        # for row in reader:
        #     swords_data.append(row)

    return swords_data

# Function to write all Sword data to CSV
def write_data(swords_data):
    with open('data.csv', mode='w', newline='') as file:
        
        fieldnames = swords_data[0].keys() if swords_data else []
        # if swords_data:
        #     fieldnames = swords_data[0].keys()
        # else
        #     fieldnames = []

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(swords_data)

def view_by_name(name):
    swords_data = read_data()
    found = False
    for sword in swords_data:
        if sword['name'] == name:
            print('\n\n=====', sword['name'], '=====')

            sword_keys = list(sword.keys())
            sword_keys.pop(sword_keys.index('name'))

            for i in sword_keys :
                print(i, '\t : ', sword[i])
            
            found = True
            break
            
    if not found:
        print(f"Sword '{name}' not found.")

def view_by_num(num):
    swords_data = read_data()
    
    if(num > len(swords_data)):
        print(f"Sword #{num+1} does not exist.")
    else:
        sword = swords_data[num]
        print('\n\n=====', sword['name'], '=====')

        sword_keys = list(sword.keys())
        sword_keys.pop(sword_keys.index('name'))

        for i in sword_keys:
            print(i, '\t : ', sword[i])
        
# Function to create a new Sword entry
def create_sword(name,att_1,att_2,spl_ability,defence,hp):
    new_sword = {
        'name': name,
        'att 1': att_1,
        'att 2': att_2,
        'spl.ability': spl_ability,
        'defence': defence,
        'hp': hp,
        'bst':att_1+att_2+spl_ability+defence+hp
    }
    swords_data = read_data()
    swords_data.append(new_sword)
    write_data(swords_data)
    print(f"swords '{name}' added successfully!")

# Function to update existing Sword's information
def update_sword(name, key, value):
    swords_data = read_data()
    updated = False
    for sword in swords_data:
        if sword['name'] == name:
            sword[key] = value
            updated = True
            break
    if updated:
        write_data(swords_data)
        print(f"swords '{name}' updated successfully!")
    else:
        print(f"swords '{name}' not found.")

# Function to delete a Sword entry
def delete_sword(name):
    swords_data = read_data()
    updated_data = [swords for swords in swords_data if swords['name'] != name]
    if len(updated_data) < len(swords_data):
        write_data(updated_data)
        print(f"swords '{name}' deleted successfully!")
    else:
        print(f"swords '{name}' not found.")


options = ['View by Name', 'View by No.', 'Add New', 'Update', 'Delete', 'Exit']
choice = 'a'

while (choice != '6'):
    menu(options, '====== Swordex ======')
    choice = input('Enter your choice (1-6) : ')

    if choice == '1':
        pokename = input('Enter swords Name: ')
        view_by_name(pokename)
    elif choice == '2':
        pokenum = int(input('Enter swords No. : '))
        view_by_num(pokenum-1)
    elif choice == '3':
        name= input('Enter Sword name : ')
        att_1= int(input('Enter First Attack (60-150) : '))
        att_2= int(input('Enter Second Attack (60-150) : '))
        spl_ability= int(input('Enter Special Ability (150-200) : '))
        defence= int(input('Enter Sword Defence : '))
        hp= int(input('Enter Sword HP: '))

        create_sword(name,att_1,att_2,spl_ability,defence,hp)
    elif choice == '4':
        name = input('Enter swords Name to Update: ')

        # You can display a menu here for choosing property
        key = input('Enter Attribute Name: ') 
        value = input('Enter New Value: ')

        update_sword(name,key,value)
    elif choice == '5':
        name = input('Enter swords Name to Delete: ')
        delete_sword(name)
    elif choice != '6':
        print('Invalid Input')
