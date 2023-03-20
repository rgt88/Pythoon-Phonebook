data_contact = {
        '888' :
            {'Sektor':'Pertolongan',
             'Nama':'Polisi Jakarta  '
             ,'Alamat':'Jl. Pasar Minggu No 4'
             ,'Provinsi': 'DKI Jakarta'
             ,'Phone':'888'},
        '14042' :
            {'Sektor':'Makanan',
             'Nama':'KFC Matraman Gondang',
             'Alamat':'Jl. Matraman IV',
             'Provinsi':'DKI Jakarta',
             'Phone':'14042'},
        '14045' :
            {'Sektor':'Makanan',
             'Nama':'McDonald Matraman',
             'Alamat':'Jl. Stc Senayan',
             'Provinsi':'Jawa Timur',
             'Phone':'14045'},
        '9999' :
            {'Sektor':'Consumer',
             'Nama':'Bengkel Toyota Tebet',
             'Alamat':'Jl. Benda Raya 2',
             'Provinsi':'Papua Barat',
             'Phone':'9999'},
        '7777' :
            {'Sektor':'Consumer',
             'Nama':'Bengkel Toyota Tebet',
             'Alamat':'Jl. Hang Jebat',
             'Provinsi':'Jawa Barat',
             'Phone':'7777'},
        '987654' :
            {'Sektor':'Kebutuhan',
             'Nama':'K-Mart Laris Manis',
             'Alamat':'Jl. Hang Jebat',
             'Provinsi':'Jawa Barat',
             'Phone':'987654'}
}

def default_contact():
    if len(data_contact) == 0:
        print('Contact is not Found')
    else:
        print('='*100)
        print(' ' *40+'List Contact')
        print('='*100)
        print(f"{'Sektor':<20} | {'Nama':<20} |{'Alamat':<30}  | {'Provinsi':<20} | {'Phone':<20}")
        for key in data_contact.keys():
            print(f"{data_contact[key]['Sektor']:<20} | {data_contact[key]['Nama']:<20} | {data_contact[key]['Alamat']:<30} | {data_contact[key]['Provinsi']:<20} | {data_contact[key]['Phone']:<20}")
        print('----------------------------------------------------------------------------------------------------------------------------')

def view_contact():
    while len(data_contact) == 0:
        print('Contact is not Found')
        break
    else:
        while True:
            pilih_menu = input('----Contact Data---- \n1. View All Contacts\n2. View By Numbers\n3. View by Name \n4. Back to Main Menu\n Choose Menu Number: ')
            if pilih_menu == '1':
                default_contact()
            elif pilih_menu == '2':
                search = input("Search Number: ")
                print(f"{'Sektor':<20} | {'Nama':<20} |{'Alamat':<30}  | {'Provinsi':<20} | {'Phone':<20}")
                x = 0
                for key in data_contact.keys():
                    if search in data_contact[key]["Phone"]:
                        print(f"{data_contact[key]['Sektor']:<20} | {data_contact[key]['Nama']:<20} | {data_contact[key]['Alamat']:<30} | {data_contact[key]['Provinsi']:<20} | {data_contact[key]['Phone']:<20}")
                    else:
                        x+=1
                        if x == len(data_contact):   
                            print ("contact not found")  
            elif pilih_menu == '3':
                search_name = input('Search Name: ')
                search_name_1 = search_name.replace(' ',' ')
                print(f"{'Sektor':<20} | {'Nama':<20} |{'Alamat':<30}  | {'Provinsi':<20} | {'Phone':<20}")
                x = 0
                for key in data_contact.keys():
                    if search_name_1.lower() in data_contact[key]["Nama"].lower():
                        print(f"{data_contact[key]['Sektor']:<20} | {data_contact[key]['Nama']:<20} | {data_contact[key]['Alamat']:<30} | {data_contact[key]['Provinsi']:<20} | {data_contact[key]['Phone']:<20}")
                    else :
                        x += 1
                        if x == len(data_contact):   
                            print ("contact not found")            
            elif pilih_menu == '4':
                break
            else:
                print('Menu not Found')  
                continue

def add_contact():
    while True:
        default_contact()
        print('Please fill in the new contact information')
        input_number_new_phone = input('Enter number: ')
        while True:
            if input_number_new_phone.isdigit():
                break
            else:
                print('Please fill the numbers with integers')
                input_number_new_phone = input('Enter number: ')
        if input_number_new_phone not in data_contact.keys():
            input_sektor = input('Enter Sektor: ')
            input_name = input('Enter Name: ')
            input_address = input('Enter Address: ')
            input_provinsi = input('Enter provinsi: ')
            input_phone = input_number_new_phone
            cek = input(f'Are you sure you want to add this all information = {input_sektor},{input_name},{input_address},{input_provinsi},{input_phone} Yes/No: ')
            if cek.lower() != 'yes':
                print('Contact is cancel to add')
                break
            else:
                data_contact[input_number_new_phone]={'Sektor' : input_sektor, 'Nama': input_name,'Alamat': input_address,'Provinsi': input_provinsi,'Phone': input_phone}
                default_contact()
                print('Contact added to list')
                break
        else:
            print(f' Number {input_number_new_phone} already in list')
            add_contact()
            break


def update_contact():
    while True:
        input_menu_update = input('---- Contact Update ----\n1. Update by Number\n2. Update by name \n0.Back to main menu \nEnter menu number: ')
        if input_menu_update == '1': 
            default_contact()
            update_contact_input = input('Enter numbers to update: ')   
            while True:
                if update_contact_input.isdigit():
                    break
                else:
                    print('Please fill the numbers with integers')
                    update_contact_input = input('Enter numbers to update: ')
            while update_contact_input in data_contact.keys():
                pilih_update = input('----Contact Update----\nWhat would you like to update? :\n1. Sector\n2. Nama\n3. Alamat\n4. Provinsi\n5. Phone\n6. Back to Main Menu\nEnter number: ')
                if pilih_update == '1':
                    new_sector_update = input('Enter new sector: ')
                    check_yesno_sector= input('Are you sure want update? Yes/No: ')
                    if check_yesno_sector.lower() != 'yes':
                        print('Update canceled')
                        break
                    else:
                        data_contact[update_contact_input]['Sektor'] = new_sector_update
                        default_contact()
                        print('Sector updated')
                        break
                elif pilih_update == '2':    
                    update_name = input('Enter new name: ')
                    new_name_update = update_name.replace(' ',' ')
                    check_yesno_name= input('Are you sure want update? Yes/No: ')
                    if check_yesno_name.lower() != 'yes':
                        print('Update canceled')
                        break
                    else:
                        data_contact[update_contact_input]['Nama']=new_name_update
                        default_contact()
                        print('Name updated')
                        break
                elif pilih_update == '3':
                    new_address_update = input('Enter new address: ')
                    check_yesno_address= input('Are you sure want update? Yes/No: ')
                    if check_yesno_address.lower() != 'yes':
                        print('Update canceled')
                        break
                    else:
                        data_contact[update_contact_input]['Alamat'] = new_address_update
                        default_contact()
                        print('Address updated')
                        break
                elif pilih_update == '4':
                    new_provinsi_update = input('Enter Provinsi: ')
                    check_yesno_provinsi= input('Are you sure want update? Yes/No: ')
                    if check_yesno_provinsi.lower() != 'yes':
                        print('Update canceled')
                        break
                    else:
                        data_contact[update_contact_input]['Provinsi'] = new_provinsi_update
                        default_contact()
                        print('Provinsi updated')
                        break
                elif pilih_update == '5':
                    new_phone_update = input('Enter new phone number: ')
                    while new_phone_update in data_contact.keys():
                        print('Number already exist')
                        new_phone_update = input('Enter new number: ')
                    while True:
                        if new_phone_update.isdigit():
                            break
                        else:
                            print('Please fill the numbers with integers')
                            new_phone_update = input('Enter number: ')
                    check_yesno_phone= input('Are you sure want update? Yes/No: ')
                    if check_yesno_phone.lower() != 'yes':
                        print('Update canceled')
                        break
                    else:
                        print (f"{data_contact[update_contact_input]}")
                        data_contact[new_phone_update] = data_contact[update_contact_input]
                        del data_contact[update_contact_input]
                        data_contact[new_phone_update]['Phone'] = new_phone_update
                        default_contact()
                        print('Phone updated')
                        break   
                else :
                    break 
            else:    
                print('Contact number doesnt exist')               
                break
        elif input_menu_update == '2':
            search_name = input('Search Name: ')
            search_name_1 = search_name.replace(' ',' ')
            print(f"{'Sektor':<20} | {'Nama':<20} |{'Alamat':<30}  | {'Provinsi':<20} | {'Phone':<20}")
            for key in data_contact.keys():
                if search_name_1.lower() in data_contact[key]["Nama"].lower():
                    print(f"{data_contact[key]['Sektor']:<20} | {data_contact[key]['Nama']:<20} | {data_contact[key]['Alamat']:<30} | {data_contact[key]['Provinsi']:<20} | {data_contact[key]['Phone']:<20}")
            y = 0
            for key in data_contact:
                if search_name_1.lower() in data_contact[key]["Nama"].lower():
                    update_contact_input = input('Enter phone numbers to update: ')
                    while True:
                        if update_contact_input in data_contact:
                            break
                        else:
                            print('The number is not found')
                            break
                    while True:
                        if update_contact_input.isdigit():
                            break
                        else:
                            print('Please fill the numbers with integers')
                            update_contact_input = input('Enter numbers to update: ')
                    while update_contact_input in data_contact.keys():
                        pilih_update = input('----Contact Update----\nWhat would you like to update? :\n1. Sector\n2. Nama\n3. Alamat\n4. Provinsi\n5. Phone\n6. Back to Main Menu\nEnter number: ')
                        if pilih_update == '1':
                            new_sector_update = input('Enter new sector: ')
                            check_yesno_sector= input('Are you sure want update? Yes/No: ')
                            if check_yesno_sector.lower() != 'yes':
                                print('Update canceled')
                                break
                            else:
                                data_contact[update_contact_input]['Sektor'] = new_sector_update
                                default_contact()
                                print('Sector updated')
                                break
                        elif pilih_update == '2':    
                            update_name = input('Enter new name: ')
                            new_name_update = update_name.replace(' ',' ')
                            check_yesno_name= input('Are you sure want update? Yes/No: ')
                            if check_yesno_name.lower() != 'yes':
                                print('Update canceled')
                                break
                            else:
                                data_contact[update_contact_input]['Nama']=new_name_update
                                default_contact()
                                print('Name updated')
                                break
                        elif pilih_update == '3':
                            new_address_update = input('Enter new address: ')
                            check_yesno_address= input('Are you sure want update? Yes/No: ')
                            if check_yesno_address.lower() != 'yes':
                                print('Update canceled')
                                break
                            else:
                                data_contact[update_contact_input]['Alamat'] = new_address_update
                                default_contact()
                                print('Address updated')
                                break
                        elif pilih_update == '4':
                            new_provinsi_update = input('Enter Provinsi: ')
                            check_yesno_provinsi= input('Are you sure want update? Yes/No: ')
                            if check_yesno_provinsi.lower() != 'yes':
                                print('Update canceled')
                                break
                            else:
                                data_contact[update_contact_input]['Provinsi'] = new_provinsi_update
                                default_contact()
                                print('Provinsi updated')
                                break
                        elif pilih_update == '5':
                            new_phone_update = input('Enter new phone number: ')
                            while new_phone_update in data_contact.keys():
                                print('Number already exist')
                                new_phone_update = input('Enter new number: ')
                            while True:
                                if new_phone_update.isdigit():
                                    break
                                else:
                                    print('Please fill the numbers with integers')
                                    new_phone_update = input('Enter number: ')
                            check_yesno_phone= input('Are you sure want update? Yes/No: ')
                            if check_yesno_phone.lower() != 'yes':
                                print('Update canceled')
                                break
                            else:
                                print (f"{data_contact[update_contact_input]}")
                                data_contact[new_phone_update] = data_contact[update_contact_input]
                                del data_contact[update_contact_input]
                                data_contact[new_phone_update]['Phone'] = new_phone_update
                                default_contact()
                                print('Phone updated')
                        elif pilih_update == '6':
                           break 
                    break
                else:
                    y+=1
                    if y == len(data_contact):
                        print('Name is not found')
        elif input_menu_update == '0':
            break   
    
    
def delete_contact():
    default_contact()
    delete_contact = input('Enter numbers you want to delete: ')
    while True:
            if delete_contact.isdigit():
                break
            else:
                print('Please fill the numbers with integers')
                delete_contact = input('Enter numbers to update: ')
    new_delete_contact = delete_contact
    while new_delete_contact not in data_contact.keys():
        print('Contact not Found')
        break
    else:
        check_delete = input(f'Are you sure want to delete {delete_contact} ? Yes/No: ')
        while check_delete.lower() != 'yes':
            print('Contact not deleted')
            break
        else:
            del data_contact[new_delete_contact]
            default_contact()
            print('Contact deleted')
        
while True:
    pilih_menu = input('''
    MAIN MENU:
    1. Read contacts
    2. Add a contact
    3. Update contact
    4. Delete contact
    0. Exit program
    
    Please enter menu number: ''')
    if pilih_menu == '1':
        view_contact()
    elif pilih_menu == '2':
        add_contact()
    elif pilih_menu == '3':
        update_contact()
    elif pilih_menu =='4':
        delete_contact()
    elif pilih_menu == '0':
        print('Terima kasih')
        break
    else:
        print('Menu not Found')
        continue

