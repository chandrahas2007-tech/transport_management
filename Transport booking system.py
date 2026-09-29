print("====== Transort Service Booking System ======")
users = {}

def registration():
    user_name = input("Enter username : ")
    password = input("Make strong Password: ")

    
    if user_name in users:
        print("username already taken, try another")
    else:
        users[user_name] = password
        print("===================================")
        print("Registration Successful")
        print("===================================")

Ticket = {}
def Ticket_booking():
    Name = input("Enter Passenger name - ")
    email = input("Enter email - ")
    destination = input("Enter Destination - ")
    Transport = input("Enter mode of Transport [Train / Bus] - ")
    Ticket_id = int(input("Make your integer ticket_id - "))
    
    
    Ticket[Ticket_id] = {"Ticket_id": Ticket_id,
                         "Name": Name,
                         "email": email,
                         "Destination": destination,
                         "transport": Transport}
    
    print("Ticket Booked Successfully")
    options()
    
def show_ticket():
    Ticket_id = int(input("Enter your Ticket Id - "))
    if Ticket_id in Ticket:
        print("TICKET DETAILS ")
        print("Ticket_id", Ticket[Ticket_id]["Ticket_id"])
        print("Name : ", Ticket[Ticket_id]["Name"])
        print("Email : ", Ticket[Ticket_id]["email"])
        print("Destination : ", Ticket[Ticket_id]["Destination"])
        print("mode of Transport : ", Ticket[Ticket_id]["transport"])
        options()
        
    else:
        print("Sorry Ticket not found")
        options()

def Ticket_cancel():
    Ticket_id = int(input("Enter Ticket_id : "))
    
    if Ticket_id in Ticket:
        del Ticket[Ticket_id]
        print("Ticket Cancelled sucessfully, your money will be refunded in 7-8 buisness days")
        options()
    else:
        print("Ticket not found")
        options()
        
def options():
    print("1. Book Ticket")
    print("2. View Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")
        
    option = int(input("choose option to proceed - "))
        
    if option == 1:
            Ticket_booking()
            
    elif option == 2:
            show_ticket()
        
    elif option == 3:
            Ticket_cancel()
        
    elif option == 4:
            print("Thank you for using our site, Happy Journey")
           
            
    else:
            print("Invalid choice")
    
 
def login():
    user_name = input("Enter your username - ")
    password = input("Enter password - ")
    
    if user_name in users and users[user_name] == password:
        print("========================")
        print("Login successful")
        print("========================")
        print("Welcome to the Transport Booking Site")
        options()
    else:
        print("invalid username or password")
       
while True:
    print("1. Register [New to the site]")
    print("2. Login [Already Registered]")
    print("3. Exit")
    
    choice = int(input("Enter your choice"))
    
    if choice == 1:
        registration() 
    
    elif choice == 2:
        login()
    
    elif choice == 3: 
        print("Thank you, visit again")
        break

    else:
        print("invalid choice")