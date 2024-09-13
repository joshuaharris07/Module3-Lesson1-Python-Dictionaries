# Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested 
# collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:

# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.

def open_new_ticket(ticket, customer_name, issue, status=open):
    ticket_key = "Ticket" + str(ticket)
    service_tickets[ticket_key] = {"Customer": customer_name, "Issue": issue, "Status": status}
    print(f"{customer_name}, your ticket has been opened for {issue}. Your ticket number is {ticket} Returning to the menu.")

def update_ticket(ticket_number, status):
    try:
        service_tickets[ticket_number]["Status"] = status
    except:
        print(f"Ticket number {ticket_number[6:]} was not found.") #TODO, continue from here.
    print(service_tickets[ticket_number])

def display_tickets(status=all):
    pass #can filter by status


service_tickets = {
    "Ticket1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

starting_ticket = 3   # Set the next ticket to be added

while True:
    menu_action = input("Options:\n1. Open new ticket\n2. Update existing ticket\n3. Display current tickets\n4. Exit")
    if menu_action == "1":
        customer_name = input("Please enter your first name: ").capitalize()
        issue = input("Please enter a brief description of the issue you are experiencing: ").capitalize()
        open_new_ticket(starting_ticket, customer_name, issue)
        starting_ticket += 1
    elif menu_action == "2":
        ticket_number = input("Please enter your ticket number: ")
        # try:
        #     ticket_number = int(ticket_number)
        # except:
        #     print("Invalid input.")
        # else:
        ticket_number = "Ticket" + ticket_number
        print(f"Ticket entered was {ticket_number}")
        status = input("Are you closing, or opening a ticket? (open/close): ").lower()
        if status == "open" or "close": 
            update_ticket(ticket_number, status)
        else:
            print("Invalid input, please enter open or close. Returning to the menu.")
    # elif menu_action == "3":
    #     update_ticket(status)
    elif menu_action == "4":
        break
    else:
        print("That is not a valid selection, please enter 1, 2, 3, or 4.")
