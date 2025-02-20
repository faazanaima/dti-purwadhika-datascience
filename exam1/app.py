from datetime import datetime, timedelta

room_dict = {
    "R001": {"room_no": "1001", "type": "Junior Suite", "is_smoking": 0, "price": "1000000", "status": ""},
    "R002": {"room_no": "1002", "type": "Junior Suite", "is_smoking": 0, "price": "1000000", "status": ""},
    "R003": {"room_no": "1003", "type": "Junior Suite", "is_smoking": 0, "price": "1000000", "status": ""},
    "R004": {"room_no": "1004", "type": "Junior Suite", "is_smoking": 1, "price": "1000000", "status": ""},
    "R005": {"room_no": "2001", "type": "Standard", "is_smoking": 0, "price": "400000", "status": ""},
    "R006": {"room_no": "2002", "type": "Superior", "is_smoking": 0, "price": "600000", "status": ""},
    "R007": {"room_no": "2003", "type": "Standard", "is_smoking": 0, "price": "400000", "status": ""},
    "R008": {"room_no": "3001", "type": "Standard", "is_smoking": 1, "price": "400000", "status": ""},
    "R009": {"room_no": "3002", "type": "Superior", "is_smoking": 1, "price": "600000", "status": ""},
    "R010": {"room_no": "3003", "type": "Standard", "is_smoking": 1, "price": "400000", "status": ""}
}

def room_view(room_no=None):
    print("\n\t╔════════════════════════════════════════════════════════════════════╗")
    print("\t║                         ROOM INFORMATION                           ║")
    print("\t╚════════════════════════════════════════════════════════════════════╝\n")
    
    print(f"\t{' Room ID':<10}{' Room No':<10}{' Type':<16}{' Smoking':<10}{' Price':<10}{' Status':<10}")
    print("\t", "=" * 68)

    filtered_rooms = [
        (key, value) for key, value in room_dict.items()
        if isinstance(value, dict) and (room_no is None or value.get('room_no') == str(room_no))
    ]

    if filtered_rooms:
        for key, value in filtered_rooms:
            print(f"\t {key:<10}{value['room_no']:<10}{value['type']:<16}{'Yes' if value['is_smoking'] else 'No':<10}{value['price']:<10}{value['status']:<10}")
    else:
        print("\tNo room found with the specified room number.")

    print("\n\t═════════════════════════════════════════════════════════════════════\n")

cust_dict = {
    "CUST001" : {"cust_name": "Andi", "cust_age": "37", "cust_gender": "Male", "cust_address": "Jakarta", "cust_identity_numb": "12345", "cust_numb": "081111111111", "cust_loyalty": "Non_Loyalty"},
    "CUST002" : {"cust_name": "Budi", "cust_age": "27", "cust_gender": "Male", "cust_address": "Bogor", "cust_identity_numb": "23456", "cust_numb": "081222222222", "cust_loyalty": "Non_Loyalty"},
    "CUST003" : {"cust_name": "Cinta", "cust_age": "25", "cust_gender": "Female", "cust_address": "Depok", "cust_identity_numb": "34567", "cust_numb": "081333333333", "cust_loyalty": "Non_Loyalty"},
    "CUST004" : {"cust_name": "Dinda", "cust_age": "28", "cust_gender": "Female", "cust_address": "Tangerang", "cust_identity_numb": "45678", "cust_numb": "081444444444", "cust_loyalty": "Non_Loyalty"},
    "CUST005" : {"cust_name": "Eca", "cust_age": "30", "cust_gender": "Male", "cust_address": "Bekasi", "cust_identity_numb": "56789", "cust_numb": "081555555555", "cust_loyalty": "Non_Loyalty"},
    "CUST006" : {"cust_name": "Faza", "cust_age": "24", "cust_gender": "Female", "cust_address": "Bandung", "cust_identity_numb": "67890", "cust_numb": "081666666666", "cust_loyalty": "Non_Loyalty"},
    "CUST007" : {"cust_name": "Gea", "cust_age": "26", "cust_gender": "Female", "cust_address": "Surabaya", "cust_identity_numb": "78901", "cust_numb": "081777777777", "cust_loyalty": "Non_Loyalty"},
    "CUST008" : {"cust_name": "Hasan", "cust_age": "29", "cust_gender": "Female", "cust_address": "Semarang", "cust_identity_numb": "89012", "cust_numb": "081888888888", "cust_loyalty": "Non_Loyalty"},
    "CUST009" : {"cust_name": "Ina", "cust_age": "35", "cust_gender": "Male", "cust_address": "Yogyakarta", "cust_identity_numb": "90123", "cust_numb": "081999999999", "cust_loyalty": "Non_Loyalty"},
    "CUST010" : {"cust_name": "Joko", "cust_age": "40", "cust_gender": "Male", "cust_address": "Solo", "cust_identity_numb": "01234", "cust_numb": "081000000000", "cust_loyalty": "Non_Loyalty"},
}

def cust_view(cust_identity_numb=None):
    print("\n\t╔══════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("\t║                                     GUEST INFORMATION                                        ║")
    print("\t╚══════════════════════════════════════════════════════════════════════════════════════════════╝\n")
    
    print(f"\t{' CUST ID':<10}{' Guest':<15}{' Age':<5}{' Gender':<10}{' Address':<15}{' ID Numb':<12}{' Phone Numb':<15}{' Loyalty':<10}")
    print("\t", "=" * 94)

    def match_identity(item):
        key, value = item 
        return value["cust_identity_numb"] == cust_identity_numb

    if cust_identity_numb is not None:
        filtered_data = dict(filter(match_identity, cust_dict.items()))
    else:
        filtered_data = cust_dict
    
    for key, value in filtered_data.items():
        print(f"\t {key:<10}{value['cust_name']:<15}{value['cust_age']:<5}{value['cust_gender']:<10}{value['cust_address']:<15}{value['cust_identity_numb']:<12}{value['cust_numb']:<15}{value['cust_loyalty']:<10}")

    print("\n\t═══════════════════════════════════════════════════════════════════════════════════════════════\n")

emp_dict = {
    "EMP001": {"emp_name": "Zara", "emp_role": "Staff", "emp_age": "24", "emp_gender": "Female", "emp_address": "Jakarta", "emp_identity_numb": "98765", "emp_numb": "085111111111"},
    "EMP002": {"emp_name": "Yeni", "emp_role": "Staff", "emp_age": "24", "emp_gender": "Female", "emp_address": "Bogor", "emp_identity_numb": "87654", "emp_numb": "085222222222"},
    "EMP003": {"emp_name": "Wendi", "emp_role": "Staff", "emp_age": "30", "emp_gender": "Male", "emp_address": "Depok", "emp_identity_numb": "76543", "emp_numb": "085333333333"},
    "EMP004": {"emp_name": "Vina", "emp_role": "Staff", "emp_age": "28", "emp_gender": "Female", "emp_address": "Tangerang", "emp_identity_numb": "65432", "emp_numb": "085444444444"},
    "EMP005": {"emp_name": "Umar", "emp_role": "Staff", "emp_age": "35", "emp_gender": "Male", "emp_address": "Bekasi", "emp_identity_numb": "54321", "emp_numb": "085555555555"},
    "EMP006": {"emp_name": "Tina", "emp_role": "Staff", "emp_age": "26", "emp_gender": "Female", "emp_address": "Bandung", "emp_identity_numb": "43210", "emp_numb": "085666666666"},
    "EMP007": {"emp_name": "Satria", "emp_role": "Manager", "emp_age": "40", "emp_gender": "Male", "emp_address": "Surabaya", "emp_identity_numb": "32109", "emp_numb": "085777777777"},
    "EMP008": {"emp_name": "Rina", "emp_role": "Staff", "emp_age": "25", "emp_gender": "Female", "emp_address": "Semarang", "emp_identity_numb": "21098", "emp_numb": "085888888888"},
    "EMP009": {"emp_name": "Qori", "emp_role": "Supervisor", "emp_age": "32", "emp_gender": "Male", "emp_address": "Yogyakarta", "emp_identity_numb": "10987", "emp_numb": "085999999999"},
    "EMP010": {"emp_name": "Pandu", "emp_role": "Staff", "emp_age": "27", "emp_gender": "Male", "emp_address": "Solo", "emp_identity_numb": "09876", "emp_numb": "085000000000"}
}

def emp_view():
    """Menampilkan daftar karyawan dengan format tabel yang rapi"""
    print("\n\t╔════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("\t║                                      EMPLOYEE INFORMATION                                      ║")
    print("\t╚════════════════════════════════════════════════════════════════════════════════════════════════╝\n")

    print(f"\t{' EMP ID':<10}{' STAFF':<15}{' POSITION':<15}{' AGE':<5}{' GENDER':<10}{' ADDRESS':<15}{' ID NUMB':<12}{' PHONE NUMB':<15}")
    print("\t", "=" * 96)

    for key, value in emp_dict.items():
        print(f"\t {key:<10}{value['emp_name']:<15}{value['emp_position']:<15}{value['emp_age']:<5}{value['emp_gender']:<10}{value['emp_address']:<15}{value['emp_identity_numb']:<12}{value['emp_numb']:<15}")

    print("\n\t═════════════════════════════════════════════════════════════════════════════════════════════════\n")

booking_dict = {
    "BK001": {"cust_id": "CUST001", "cust_name": "Andi", "reserved_by": "Andi", "room_no": "1001",
              "arr_date": "07/02/2025", "dpt_date": "08/02/2025", "days_stay": 1, "room_status": "", "price": 1000000,
              "discount": "0", "hotel_tax": "100000", "ppn": "110000", "service_tax": "0",
              "total_price": 1210000, "total_payment": 1210000, "change": 0, "payment_method": "Debit Card", "notes": ""},

    "BK002": {"cust_id": "CUST002", "cust_name": "Budi", "reserved_by": "Budi", "room_no": "2001",
              "arr_date": "10/02/2025", "dpt_date": "12/02/2025", "days_stay": 2, "room_status": "", "price": 1000000,
              "discount": "5", "hotel_tax": "190000", "ppn": "209000", "service_tax": "0",
              "total_price": 2399000, "total_payment": 2399000, "change": 0, "payment_method": "Credit Card", "notes": ""},

    "BK003": {"cust_id": "CUST003", "cust_name": "Cinta", "reserved_by": "Cinta", "room_no": "1003",
              "arr_date": "09/02/2025", "dpt_date": "13/02/2025", "days_stay": 4, "room_status": "", "price": 600000,
              "discount": "10", "hotel_tax": "216000", "ppn": "237600", "service_tax": "0",
              "total_price": 2613600, "total_payment": 2613600, "change": 0, "payment_method": "Bank Transfer", "notes": ""},

    "BK004": {"cust_id": "CUST004", "cust_name": "Dinda", "reserved_by": "Dinda", "room_no": "2003",
              "arr_date": "12/02/2025", "dpt_date": "15/02/2025", "days_stay": 3, "room_status": "", "price": 400000,
              "discount": "5", "hotel_tax": "114000", "ppn": "125400", "service_tax": "0",
              "total_price": 1379400, "total_payment": 1379400, "change": 0, "payment_method": "QRIS", "notes": ""},

    "BK005": {"cust_id": "CUST001", "cust_name": "Andi", "reserved_by": "Andi", "room_no": "1002",
              "arr_date": "15/02/2025", "dpt_date": "17/02/2025", "days_stay": 2, "room_status": "", "price": 400000,
              "discount": "0", "hotel_tax": "80000", "ppn": "88000", "service_tax": "0",
              "total_price": 968000, "total_payment": 1000000, "change": 32000, "payment_method": "Cash", "notes": ""},

    "BK006": {"cust_id": "CUST005", "cust_name": "Eca", "reserved_by": "Eca", "room_no": "3002",
              "arr_date": "18/02/2025", "dpt_date": "19/02/2025", "days_stay": 1, "room_status": "", "price": 750000,
              "discount": "5", "hotel_tax": "71250", "ppn": "78375", "service_tax": "0",
              "total_price": 821625, "total_payment": 821625, "change": 0, "payment_method": "GL", "notes": ""},

    "BK007": {"cust_id": "CUST006", "cust_name": "Faza", "reserved_by": "Faza", "room_no": "1001",
              "arr_date": "20/02/2025", "dpt_date": "23/02/2025", "days_stay": 3, "room_status": "", "price": 500000,
              "discount": "10", "hotel_tax": "135000", "ppn": "148500", "service_tax": "0",
              "total_price": 1633500, "total_payment": 1633500, "change": 0, "payment_method": "QRIS", "notes": ""},

    "BK008": {"cust_id": "CUST007", "cust_name": "Gea", "reserved_by": "Gea", "room_no": "1001",
              "arr_date": "24/02/2025", "dpt_date": "27/02/2025", "days_stay": 3, "room_status": "", "price": 450000,
              "discount": "0", "hotel_tax": "135000", "ppn": "148500", "service_tax": "0",
              "total_price": 1633500, "total_payment": 1650000, "change": 16500, "payment_method": "Cash", "notes": ""},

    "BK009": {"cust_id": "CUST008", "cust_name": "Hasan", "reserved_by": "Hasan", "room_no": "1002",
              "arr_date": "28/02/2025", "dpt_date": "02/03/2025", "days_stay": 2, "room_status": "", "price": 550000,
              "discount": "5", "hotel_tax": "104500", "ppn": "114950", "service_tax": "0",
              "total_price": 1248450, "total_payment": 1248450, "change": 0, "payment_method": "Credit Card", "notes": ""},

    "BK010": {"cust_id": "CUST009", "cust_name": "Ina", "reserved_by": "Ina", "room_no": "1002",
              "arr_date": "03/03/2025", "dpt_date": "06/03/2025", "days_stay": 3, "room_status": "", "price": 350000,
              "discount": "10", "hotel_tax": "94500", "ppn": "103950", "service_tax": "0",
              "total_price": 1149450, "total_payment": 1149450, "change": 0, "payment_method": "Bank Transfer", "notes": ""}
}

def booking_view():
    print("\n\t╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("\t║                                                                                          BOOKING INFORMATION                                                                                         ║")
    print("\t╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\n")

    print(f"\t{' Booking ID':<12}{' Cust ID':<10}{' Guest':<15}{' Reserved By':<12}{' Room No':<8}{' Arr Date':<12}{' Dpt Date':<12}{' Days':<5}{' Status':<12}{' Price':<12}{' Discount':<10}{' Tax':<12}{' PPN':<12}{' Service':<12}{' Total':<12}{' Paid':<12}{' Change':<12}{' Method':<12}{' Notes':<10}")
    print("\t", "=" * 214)  # Lebarkan batas sesuai tambahan kolom

    for key, value in booking_dict.items():
        print(f"\t {key:<12}{value['cust_id']:<10}{value['cust_name']:<15}{value['reserved_by']:<12}{value['room_no']:<8}{value['arr_date']:<12}{value['dpt_date']:<12}{value['days_stay']:<5}{value.get('room_status', ''):<12}{value['price']:<12}{value['discount']:<10}{value['hotel_tax']:<12}{value['ppn']:<12}{value['service_tax']:<12}{value['total_price']:<12.2f}{value['total_payment']:<12.2f}{value['change']:<12.2f}{value['payment_method']:<12}{value['notes']:<10}")

    print("\n\t════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n")

def display_menu():
    print("\n\t╔════════════════════════════════════════════════════════════════╗")
    print("\t║                   WELCOME TO 'PURWADHIKA' HOTEL                ║")
    print("\t║                                                                ║")
    print("\t║                Jl. Jendral Sudirman, No. 21 10 Lt 13A          ║")
    print("\t║     Kuningan, Karet, Setiabudi, Jakarta Selatan, DKI Jakarta   ║")
    print("\t╚════════════════════════════════════════════════════════════════╝\n")

    print("\t\t\t\t  MAIN MENU  ")
    print("\t══════════════════════════════════════════════════════════════════")
    print("\t1. Check Room Availability")
    print("\t2. Guest Registration")
    print("\t3. Room Booking & Invoice") 
    print("\t4. Amend Booking") 
    print("\t5. Cancel Booking")
    print("\t6. Administrative Page")  
    print("\t7. Exit System")
    print("\t══════════════════════════════════════════════════════════════════\n")

    print("\t\t     ───────────────────────────────────────────")
    print("\t\t       Managed by Purwadhika Hotel Management")
    print("\t\t   Delivering Excellence in Hospitality Since 1987")
    print("\t\t     ───────────────────────────────────────────\n")

def is_available(item):
    key, value = item
    return value["status"].lower() == "available"

def room_checking():
    while True:
        check_date_input = input("\tEnter the date to check availability (DD/MM/YYYY): ")
        try:
            check_date = datetime.strptime(check_date_input, "%d/%m/%Y").date()
            break
        except ValueError:
            print("\tInvalid date format! Please enter the date in DD/MM/YYYY format.")
    
    print("\tCheck Date:", check_date)
    print("\n\t╔══════════════════════════════════════════════════════════════════╗")
    print("\t║                         ROOM AVAILABILITY                        ║")
    print("\t╚══════════════════════════════════════════════════════════════════╝\n")
    print(f"\t{' Room ID':<10}{' Room No':<10}{' Type':<16}{' Smoking':<10}{' Price':<11}{' Status':<10}")
    print("\t", ("=" * 66))

    for key, value in room_dict.items():
        room_no = value["room_no"]
        is_booked = False
        for booking in booking_dict.values():
            if booking["room_no"] == room_no:
                booked_arr = datetime.strptime(booking["arr_date"], "%d/%m/%Y").date()
                booked_dpt = datetime.strptime(booking["dpt_date"], "%d/%m/%Y").date()

                if booked_arr <= check_date < booked_dpt:
                    is_booked = True
                    break

        if not is_booked:
            value["status"] = "Available"
        else:
            value["status"] = "Occupied/Booked"

    available_rooms = filter(is_available, room_dict.items())

    for key, value in available_rooms:
        print(f"\t {key:<10}{value['room_no']:<10}{value['type']:<16}{'Yes' if value['is_smoking'] else 'No':<10}{value['price']:<11}{value['status']:<10}")

    print("\n\t════════════════════════════════════════════════════════════════════\n")

def add_cust():
    def generate_cust_id():
        if not cust_dict:
            return "CUST001"
        last_id = max(int(key.lstrip("CUST")) for key in cust_dict.keys())
        return f"CUST{last_id+1:03d}"

    cust_identity_numb = input("\tEnter Customer Identity Number: ").strip()

    existing_cust_id = next((key for key, value in cust_dict.items() if value["cust_identity_numb"] == cust_identity_numb), None)

    if existing_cust_id:
        print(f"\n\tProcess : Updating Customer {existing_cust_id}")
        existing_data = cust_dict[existing_cust_id]

        def update_field(prompt, key):
            new_value = input(prompt).strip()
            return new_value if new_value else existing_data[key]

        cust_dict[existing_cust_id] = {
            "cust_name": update_field("\tEnter Customer Name: ", "cust_name"),
            "cust_age": update_field("\tEnter Customer Age: ", "cust_age"),
            "cust_gender": update_field("\tEnter Customer Gender (Male/Female): ", "cust_gender"),
            "cust_address": update_field("\tEnter Customer Address: ", "cust_address"),
            "cust_numb": update_field("\tEnter Customer Phone Number: ", "cust_numb"),
            "cust_loyalty": update_field("\tEnter Customer Loyalty Status (Loyal/Non_Loyalty): ", "cust_loyalty"),
            "cust_identity_numb": cust_identity_numb
        }

        print(f"\tMessage : Customer {existing_cust_id} has been successfully updated!")
    else:
        cust_id = generate_cust_id()
        cust_dict[cust_id] = {
            "cust_name": input("\tEnter Customer Name: ").strip(),
            "cust_age": input("\tEnter Customer Age: ").strip(),
            "cust_gender": input("\tEnter Customer Gender (Male/Female): ").strip(),
            "cust_address": input("\tEnter Customer Address: ").strip(),
            "cust_identity_numb": cust_identity_numb,
            "cust_numb": input("\tEnter Customer Phone Number: ").strip(),
            "cust_loyalty": input("\tEnter Customer Loyalty Status (Loyal/Non_Loyalty): ").strip()
        }
        print(f"\tMessage : Customer {cust_id} has been successfully added!")
    
    cust_view(cust_identity_numb)
    
def update_room_status():
    global today
    today = datetime.today().date()

    for key, booking in booking_dict.items():
        arr_date = datetime.strptime(booking['arr_date'], "%d/%m/%Y").date()
        dpt_date = datetime.strptime(booking['dpt_date'], "%d/%m/%Y").date()
        
        if arr_date <= today < dpt_date:
            booking['room_status'] = "Running"
        elif arr_date > today:
            booking['room_status'] = "Booked"
        elif today >= dpt_date:
            booking['room_status'] = "Finished"
    
    return booking_dict 

def add_booking():
    global today

    def generate_booking_id():
        if booking_dict:
            last_id = max(int(key[2:]) for key in booking_dict.keys() if key.startswith("BK"))
            new_id = last_id + 1
        else:
            new_id = 1
        return f"BK{new_id:03d}"

    def days_stay(arr_date, dpt_date):
        return (dpt_date - arr_date).days

    def get_stay_dates(arr_date, dpt_date):
        return [(arr_date + timedelta(days=i)).strftime("%d/%m/%Y") for i in range((dpt_date - arr_date).days)]

    booking_id = generate_booking_id()
    
    while True:
        cust_id = input("\tEnter Customer ID: ").strip()
        if cust_id.upper() not in cust_dict:
            print("\tError: Customer ID not found. Please enter a valid ID.\n")
            continue
        break

    while True:
        cust_name = input("\tEnter Customer Name: ").strip()
        if cust_name.lower() != cust_dict[cust_id.upper()]["cust_name"].lower():
            print("\tError: Guest name does not match the Customer ID. Please enter a valid name.\n")
            continue
        break

    while True:
        reserved_by = input("\tEnter Reserved By (Customer ID/ Customer Name): ").strip()
        if reserved_by.upper() not in cust_dict and all(reserved_by.lower() != details["cust_name"].lower() for details in cust_dict.values()):
            print("\tError: Customer ID or Name not found. Please enter a valid ID or Name.\n")
            continue
        break 
  
    while True:
        while True:
            room_no = input("\tEnter Room Number: ").strip()
            room_key = next(
            (key for key, value in room_dict.items() if isinstance(value, dict) and value.get("room_no") == room_no), None
            )
            if room_key is None:
                print("\tError: Room number not found.")
                continue
            break
        
        try:
            arr_date = datetime.strptime(input("\tEnter Arrival Date (DD/MM/YYYY): ").strip(), "%d/%m/%Y").date()
            dpt_date = datetime.strptime(input("\tEnter Departure Date (DD/MM/YYYY): ").strip(), "%d/%m/%Y").date()

            if dpt_date <= arr_date:
                print("\tError: Departure date must be after arrival date.")
                continue

        except ValueError:
            print("\tError: Invalid date format. Use DD/MM/YYYY.")
            continue

        for booking in booking_dict.values():
            if booking["room_no"] == room_no:
                booked_arr = datetime.strptime(booking["arr_date"], "%d/%m/%Y").date()
                booked_dpt = datetime.strptime(booking["dpt_date"], "%d/%m/%Y").date()
 
                if not (dpt_date <= booked_arr or arr_date > booked_dpt):  
                    print(f"\tError: Sorry, room {room_no} is already booked from {booked_arr.strftime('%d/%m/%Y')} to {booked_dpt.strftime('%d/%m/%Y')}.")
                    break
        else:
            print(f"\tMessage: Room {room_no} is available from {arr_date.strftime('%d/%m/%Y')} to {dpt_date.strftime('%d/%m/%Y')}. Booking confirmed!")
            break
    
    while True:
        try:
            price = float(room_dict[room_key]["price"])
        except (ValueError, TypeError, KeyError):
            print("\tError: Invalid room price.")
            continue
        break
    
    while True:
        try:
            disc_input = input("\tEnter Discount Percentage (e.g., 10 for 10% or 0 for no discount): ").strip()
            disc_percent = float(disc_input) if disc_input else 0.0
            if disc_percent < 0 or disc_percent > 100:
                print("\tError: Discount percentage must be between 0 and 100.")
                continue
        except ValueError:
            print("\tError: Invalid discount percentage.")
            continue
        break

    stay_days = days_stay(arr_date, dpt_date)
    stay_dates = get_stay_dates(arr_date, dpt_date)

    room_cost = price * stay_days
    disc_val = (disc_percent / 100) * room_cost
    net_price = room_cost - disc_val
    hotel_tax_val = 0.10 * net_price
    ppn_value = 0.11 * net_price
    service_tax_val = 0
    total_price = net_price + hotel_tax_val + ppn_value + service_tax_val

    while True:
        try:
            total_payment = float(input(f"\n\tTotal Price: Rp{total_price:,.2f} (Room Cost: Rp{room_cost:,.2f})\n\tEnter Total Payment: ").strip())
            if total_payment < total_price:
                print("\tError: Total Payment must be at least equal to Total Price. Please enter a valid amount.")
                continue
        except ValueError:
            print("\tError: Total Payment must be a valid number. Please try again.")
            continue
        break

    change = total_payment - total_price
    payment_method = input("\tEnter Payment Method (e.g., Cash, Debit Card, Credit Card, Bank Transfer, GL): ").strip()
    notes = input("\tEnter Notes (if any): ").strip()
        
    booking_dict[booking_id] = {
        "cust_id": cust_id, "cust_name": cust_name, "reserved_by": reserved_by, "room_no": room_no,
        "arr_date": arr_date.strftime("%d/%m/%Y"), "dpt_date": dpt_date.strftime("%d/%m/%Y"), "days_stay": stay_days,
        "room_status":"","price": price, "discount": disc_val, "hotel_tax": hotel_tax_val, "ppn": ppn_value, "service_tax": service_tax_val,
        "total_price": total_price, "total_payment": total_payment, "change": change,
        "payment_method": payment_method, "notes": notes
    }

    print("\n\t╔════════════════════════════════════════════════════════════════════════════╗")
    print("\t║                               RECEIPT                                      ║")
    print("\t╚════════════════════════════════════════════════════════════════════════════╝\n")
    print("\t  PURWADHIKA HOTEL")
    print("\t  Jl. Menteng Raya, Telp. 123456")
    print("\t  Kebon Sirih, Menteng, Jakarta Pusat, DKI Jakarta")
    print(f"\t\t\t\t\t\t\t\t     Come Back Soon")
    print(f"\t  {cust_name}")
    print("\t ────────────────────────────────────────────────────────────────────────────\n")
    print(f"\t  Room Number        : {room_no}")
    print(f"\t  Arrival Date       : {arr_date}")
    print(f"\t  Departure Date     : {dpt_date}")
    print(f"\t  Payment Bill       : {booking_id}")
    print("\t", "=" * 76)
    
    print(f"\t{'  Date':<12} {'  Description':<20}{'\tQty':<8}{'\tRoom':<8}{'\t      Amount':<12}")
    print("\t", "=" * 76)

    for date in stay_dates:
        print(f"\t  {date:<12}{' Room Charge':<20}{'\t 1':<8} {room_no:<8}      Rp{price:,.2f}")
    print(f"\t\t\t\t\t\t\t Balance    : Rp{room_cost:,.2f}")

    print("\n\t ────────────────────────────────────────────────────────────────────────────\n")

    print(f"\t  Room Price        : Rp{room_cost:,.2f}")
    print(f"\t  Discount ({disc_percent}%)   : Rp{disc_val:,.2f}")
    print(f"\t  Hotel Tax (10%)   : Rp{hotel_tax_val:,.2f}")
    print(f"\t  PPN (11%)         : Rp{ppn_value:,.2f}")
    print(f"\t  Service Tax       : Rp{service_tax_val:,.2f}")
    print(f"\t  Total Price       : Rp{total_price:,.2f}")
    print(f"\t  Total Paid        : Rp{total_payment:,.2f}")
    print(f"\t  Change            : Rp{change:,.2f}")

    print("\n\n\t Please check that you have not left any valuables in the in-room personal safe. ")
    print("\tThank you for choosing to stay with us and we wish you a pleasant onward journey.")
    
    update_room_status()

def amend_booking():
    def days_stay(arr_date, dpt_date):
        return (dpt_date - arr_date).days

    
    def get_stay_dates(arr_date, dpt_date):
        return [(arr_date + timedelta(days=i)).strftime("%d/%m/%Y") for i in range((dpt_date - arr_date).days)]
    
    while True:
        booking_id = input("\tEnter Booking ID to amend: ").strip().upper()
        if booking_id.upper() not in (key.upper() for key in booking_dict.keys()):
            print("\tError: Booking ID not found. Please try again.\n")
            continue
        break

    
    booking = booking_dict[booking_id]
    
    print("\n\tBooking Details :\n")
    print(f"\t{'Booking ID':<12}{' Cust ID':<10}{' Guest':<15}{' Reserved By':<12}{' Room No':<8}{' Arr Date':<12}{' Dpt Date':<12}{' Days':<5}{' Price':<12}{' Discount':<10}{' Tax':<12}{' PPN':<12}{' Service':<12}{' Total':<12}{' Paid':<12}{' Change':<12}{' Method':<12}{' Notes':<10}")
    print("\t","=" * 198)
    
    value = booking_dict[booking_id]
    print(f"\t{booking_id:<12}{value['cust_id']:<10}{value['cust_name']:<15}{value['reserved_by']:<12}{value['room_no']:<8}{value['arr_date']:<12}{value['dpt_date']:<12}{value['days_stay']:<5}{value['price']:<12}{value['discount']:<10}{value['hotel_tax']:<12}{value['ppn']:<12}{value['service_tax']:<12}{value['total_price']:<12.2f}{value['total_payment']:<12.2f}{value['change']:<12.2f}{value['payment_method']:<12}{value['notes']:<10}")
    
    print("\n\tMessage : System can modify the following fields: Guest, Room Number, Arrival Date, Departure Date, Total Paid")
    
    while True:
        cust_name = input("\tEnter new Guest Name (leave blank to keep current): ").strip() or booking["cust_name"]
        if cust_name.lower() not in {data["cust_name"].lower() for data in cust_dict.values() if "cust_name" in data}:
            print("\tError: Customer name not found. Please enter a valid name.\n")
            continue
        break

    while True:
        while True:
            room_no = input("\tEnter new Room Number (leave blank to keep current): ") or booking["room_no"]
            room_key = next(
                (key for key, value in room_dict.items() if isinstance(value, dict) and value.get("room_no") == room_no), None
            )
            if room_key is None:
                print("\tError: Room number not found. Please try again.")
                continue
            break
        
        try:
            arr_date_input = input("\tEnter new Arrival Date (DD/MM/YYYY, leave blank to keep current): ").strip()
            dpt_date_input = input("\tEnter new Departure Date (DD/MM/YYYY, leave blank to keep current): ").strip()

            arr_date = datetime.strptime(arr_date_input, "%d/%m/%Y").date() if arr_date_input else booking["arr_date"]
            dpt_date = datetime.strptime(dpt_date_input, "%d/%m/%Y").date() if dpt_date_input else booking["dpt_date"]
            
            if isinstance(arr_date, str):
                arr_date = datetime.strptime(arr_date, "%d/%m/%Y").date()
            if isinstance(dpt_date, str):
                dpt_date = datetime.strptime(dpt_date, "%d/%m/%Y").date()
                
            if dpt_date <= arr_date:
                print("\tError: Departure date must be after arrival date. Please try again.")
                continue

            if arr_date_input or dpt_date_input:
                for key, booking in booking_dict.items():
                    if booking["room_no"] == room_no:
                        if key == booking_id:
                            continue
                        booked_arr = datetime.strptime(booking["arr_date"], "%d/%m/%Y").date()
                        booked_dpt = datetime.strptime(booking["dpt_date"], "%d/%m/%Y").date()

                        if not (dpt_date <= booked_arr or arr_date > booked_dpt):
                            print(f"\tError: Room {room_no} is already booked from {booked_arr.strftime('%d/%m/%Y')} to {booked_dpt.strftime('%d/%m/%Y')}.")
                            break
                else:
                    print(f"\tMessage: Room {room_no} is available from {arr_date.strftime('%d/%m/%Y')} to {dpt_date.strftime('%d/%m/%Y')}. Booking confirmed!")
                    break
            else:
                print("\tMessage: Booking updated without date change.")
                break

        except ValueError:
            print("\tError: Invalid date format. Use DD/MM/YYYY.")
            continue
    
    try:
        price = float(room_dict[room_key]["price"])
    except (ValueError, TypeError, KeyError):
        print("Error: Invalid room price.")
        return

    stay_days = days_stay(arr_date, dpt_date)
    stay_dates = get_stay_dates(arr_date, dpt_date)

    room_cost = price * stay_days
    disc_val = booking_dict.get(booking_id, {}).get("disc_val", 0)
    net_price = room_cost - disc_val
    hotel_tax_val = 0.10 * net_price
    ppn_value = 0.11 * net_price
    service_tax_val = 0
    total_price = net_price + hotel_tax_val + ppn_value + service_tax_val
    
    old_total_payment = booking["total_price"]
    
    additional_payment = 0
    if old_total_payment != total_price:
        additional_payment = total_price - old_total_payment
        if additional_payment > 0:
            while True:
                try:
                    add_payment_input = float(input(f"\tEnter additional payment (Rp{additional_payment:,.2f} required): Rp").strip())
                    if add_payment_input >= additional_payment:
                        total_payment = old_total_payment + add_payment_input
                        change = add_payment_input - additional_payment
                        break
                    else:
                        print("\tError: Total Payment must be at least equal to Total Price.")
                        continue
                except ValueError:
                    print("\tError: Invalid input. Please enter a valid number.")
                    continue
        else:
            total_payment, change = old_total_payment, 0
    else:
        total_payment, change = old_total_payment, 0
    
    booking_dict[booking_id].update({
        "cust_name": cust_name,
        "room_no": room_no,
        "arr_date": arr_date.strftime("%d/%m/%Y"),
        "dpt_date": dpt_date.strftime("%d/%m/%Y"),
        "total_price": total_price,
        "total_payment": total_payment
    })
    
    print("\tMessage: Booking updated successfully!")
    
    print("\n\t╔════════════════════════════════════════════════════════════════════════════╗")
    print("\t║                            REVISED RECEIPT                                 ║")
    print("\t╚════════════════════════════════════════════════════════════════════════════╝\n")
    print("\t  PURWADHIKA HOTEL")
    print("\t  Jl. Menteng Raya, Telp. 123456")
    print("\t  Kebon Sirih, Menteng, Jakarta Pusat, DKI Jakarta")
    print(f"\t\t\t\t\t\t\t     Come Back Soon")
    print(f"\t  {cust_name}")
    print("\t ────────────────────────────────────────────────────────────────────────────\n")
    print(f"\t  Room Number        : {room_no}")
    print(f"\t  Adults/Child       : 1")
    print(f"\t  Arrival Date       : {arr_date.strftime('%d/%m/%Y')}")
    print(f"\t  Departure Date     : {dpt_date.strftime('%d/%m/%Y')}")
    print(f"\t  Payment Bill       : {booking_id}")
    print("\t", "=" * 76)
    print(f"\t{'  Date':<12} {'  Description':<20}{'\tQty':<8}{'\tRoom':<8}{'\t      Amount':<12}")
    print("\t", "=" * 76)
    for date in stay_dates:
        print(f"\t  {date:<12}{' Room Charge':<20}{'\t 1':<8} {room_no:<8}      Rp{price:,.2f}")
    print(f"\t\t\t\t\t\t\t Balance    : Rp{room_cost:,.2f}")
    print("\n\t ────────────────────────────────────────────────────────────────────────────\n")
    print(f"\t  Room Price        : Rp{room_cost:,.2f}")
    print(f"\t  Discount          : Rp{disc_val:,.2f}")
    print(f"\t  Hotel Tax (10%)   : Rp{hotel_tax_val:,.2f}")
    print(f"\t  PPN (11%)         : Rp{ppn_value:,.2f}")
    print(f"\t  Service Tax       : Rp{service_tax_val:,.2f}")
    print(f"\t  Total Price       : Rp{total_price:,.2f}")
    print(f"\t  Total Paid        : Rp{total_payment:,.2f}")
    print(f"\t  Additional Paid   : Rp{additional_payment:,.2f}")
    print(f"\t  Change            : Rp{change:,.2f}")
    print("\n\t╔════════════════════════════════════════════════════════════════════════════╗")
    print("\t║ I agree to remain personally responsible for payment of this account if    ║")
    print("\t║ the company or any third party billed fails to pay any or all of these     ║")
    print("\t║ charges.                                                                   ║")
    print("\t╚════════════════════════════════════════════════════════════════════════════╝\n")
    print("\n\n\t Please check that you have not left any valuables in the in-room personal safe. ")
    print("\tThank you for choosing to stay with us and we wish you a pleasant onward journey.")

    update_room_status()

def cancel_booking():
    while True:
        booking_id = input("\n\tEnter Booking ID to Cancel: ").strip().upper()
        
        if booking_id in booking_dict:
            break
        else:
            print("\tError: Booking ID not found. Please try again.")

    print("\n\t Booking Details :")
    print(f"\t{' Booking ID':<12}{' Cust ID':<10}{' Guest':<15}{' Reserved By':<12}{' Room No':<8}{' Arr Date':<12}{' Dpt Date':<12}{' Days':<5}{' Price':<12}{' Discount':<10}{' Tax':<12}{' PPN':<12}{' Service':<12}{' Total':<12}{' Paid':<12}{' Change':<12}{' Method':<12}{' Notes':<10}")
    print("\t", "=" * 198)

    value = booking_dict[booking_id]
    room_no = value['room_no']
    room_status = value.get("room_status") 
    
    if room_status in ["Running", "Finished"]:
        print(f"\tError: Room {room_no} status is {room_status}, cannot cancel booking.")
        return

    print(f"\t {booking_id:<12}{value['cust_id']:<10}{value['cust_name']:<15}{value['reserved_by']:<12}{value['room_no']:<8}{value['arr_date']:<12}{value['dpt_date']:<12}{value['days_stay']:<5}{value['price']:<12}{value['discount']:<10}{value['hotel_tax']:<12}{value['ppn']:<12}{value['service_tax']:<12}{value['total_price']:<12.2f}{value['total_payment']:<12.2f}{value['change']:<12.2f}{value['payment_method']:<12}{value['notes']:<10}")

    confirm = input(f"\n\tAre you sure you want to cancel Booking {booking_id}? (yes/no): ").strip().lower()
    if confirm == "yes":
        del booking_dict[booking_id]

        for key, room in room_dict.items():
            if isinstance(room, dict) and room.get("room_no") == room_no:
                room["status"] = "Available"
                break

        print(f"\n\n\t Message: Booking {booking_id} has been deleted.")
    else:
        print("\tAction canceled.")

def admin():
    print("\n\t╔════════════════════════════════════════════════════════════════╗")
    print("\t║                   WELCOME TO ADMINISTRATIVE PAGE                ║")
    print("\t║                                                                ║")
    print("\t║                Jl. Jendral Sudirman, No. 21 10 Lt 13A          ║")
    print("\t║     Kuningan, Karet, Setiabudi, Jakarta Selatan, DKI Jakarta   ║")
    print("\t╚════════════════════════════════════════════════════════════════╝\n")

    total_sales = 0
    for booking in booking_dict.values():
        total_sales += booking["total_payment"]

    print("\n\t══════════════════════════════════════════════════════════════════")
    print("\t                       SALES SUMMARY")
    print("\t──────────────────────────────────────────────────────────────────")
    print(f"\t    Total Revenue :      {total_sales:,.0f} IDR")
    print("\t══════════════════════════════════════════════════════════════════\n")

    print("\t══════════════════════════════════════════════════════════════════")
    print("\t                       EMPLOYEES SUMMARY")
    print("\t──────────────────────────────────────────────────────────────────")   
    emp = len(emp_dict)
    print(f"\t    Total Employees: {emp} employees")
    print("\t──────────────────────────────────────────────────────────────────") 
    employee_types = {}
    for employee in emp_dict.values():
        emp_type = employee["emp_role"]
        employee_types[emp_type] = employee_types.get(emp_type, 0) + 1

    for emp_type, count in employee_types.items():
        print(f"\t    {emp_type}\t: {count} employees")
    
    print("\t══════════════════════════════════════════════════════════════════")

    gender_count = {"Male": 0, "Female": 0}
    for employee in emp_dict.values():
        gender = employee["emp_gender"]
        if gender in gender_count:
            gender_count[gender] += 1

    for gender, count in gender_count.items():
        print(f"\t    {gender.ljust(8)}\t: {count} employees")

    print("\t══════════════════════════════════════════════════════════════════\n")

    print("\t══════════════════════════════════════════════════════════════════")
    print("\t                       ROOMS SUMMARY")
    print("\t──────────────────────────────────────────────────────────────────")

    total_rooms = len(room_dict)
    room_types = {}

    for room in room_dict.values():
        room_type = room["type"]
        room_types[room_type] = room_types.get(room_type, 0) + 1

    print(f"\t    Total Rooms : {total_rooms} rooms")
    print("\t──────────────────────────────────────────────────────────────────")

    for room_type, count in room_types.items():
        print(f"\t    {room_type.ljust(12)}: {count} rooms")

    print("\t══════════════════════════════════════════════════════════════════\n")

    print("\t\t     ───────────────────────────────────────────")
    print("\t\t       Managed by Purwadhika Hotel Management")
    print("\t\t   Delivering Excellence in Employee Service")
    print("\t\t     ───────────────────────────────────────────\n")

def app():
    global today

    while True:
        today = datetime.today().date()
        staff = input("\tPlease enter your name, staff on duty: ").strip().lower()
        if any(staff == emp_data["emp_name"].lower() for emp_data in emp_dict.values()):
            print(f"\n\tDate: {today}")
            print(f"\tHello, {staff}. You are on duty.\n")
            break
        else:
            print("\tError: Sorry, your name was not found in our staff list.")

    while True:
        display_menu()
        try:
            opt = int(input("\tPlease enter the menu number you'd like to access: ").strip())
            if opt == 1:
                update_room_status()
                room_checking()
            elif opt == 2:
                add_cust()
            elif opt == 3:
                update_room_status()
                add_booking()
            elif opt == 4:
                update_room_status()
                amend_booking()
            elif opt == 5:
                update_room_status()
                cancel_booking()
            elif opt == 6:
                admin()
            elif opt == 7:
                print("\tExiting the program. See you next time!")
                break
            else:
                print("\tInvalid option, Dear. Please choose a valid option from the menu.")
            update_room_status()
        except ValueError:
            print("Invalid input, Dear. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    app()
