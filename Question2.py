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

def open_new_ticket(ticket, customer_name, issue):
    ticket_key = "Ticket" + str(ticket)
    service_tickets[ticket_key] = {"Customer": customer_name, "Issue": issue, "Status": "open"}
    print(f"{customer_name}, your ticket has been opened for {issue}. Your ticket number is {ticket} Returning to the menu.")

def update_ticket(ticket_number, status):
    try:
        service_tickets[ticket_number]["Status"] = status
    except:
        print(f"Ticket number {ticket_number[6:]} was not found.")
    else:
        print(f"Your ticket is now {status}.")
    finally:
        print("\nReturning to the menu.")

def display_tickets(filter):
    if filter == "yes":
        ticket_status = input("Would you like to see open or closed tickets? (open/closed): ").lower()
        if ticket_status == "open":
            print("\nHere is the list of open tickets:")
            for ticket_number, ticket in service_tickets.items():
                if service_tickets[ticket_number]["Status"] == "open":
                    print(f"Ticket number {ticket_number[6:]} for {service_tickets[ticket_number]["Customer"]}. Issue: {service_tickets[ticket_number]["Issue"]}")
        elif ticket_status == "closed":
            print("\nHere is the list of closed tickets:")
            for ticket_number, ticket in service_tickets.items():
                if service_tickets[ticket_number]["Status"] == "closed":
                    print(f"Ticket number {ticket_number[6:]} for {service_tickets[ticket_number]["Customer"]}. Issue: {service_tickets[ticket_number]["Issue"]}")
        else:
            print("Invalid input.")
    else: 
        for ticket_number, ticket in service_tickets.items():
            print(f"Ticket number {ticket_number[6:]} for {service_tickets[ticket_number]["Customer"]}. Issue: {service_tickets[ticket_number]["Issue"]}. Currently {service_tickets[ticket_number]["Status"]}.")
    print("\nReturning to the menu.")


service_tickets = {
    "Ticket1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

next_ticket = 3   # Set the next ticket to be added, if ticket dictionary was empty would set this to 1.

while True:
    menu_action = input("\nOptions:\n1. Open new ticket\n2. Update existing ticket\n3. Display current tickets\n4. Exit\n")
    if menu_action == "1":
        customer_name = input("Please enter your first name: ").capitalize()
        if customer_name.strip() == "":
            print("No name was entered, returning to the menu.")
        else:
            issue = input("Please enter a brief description of the issue you are experiencing: ").capitalize()
            if issue.strip() == "":
                print("No issue was entered, returning to the menu.")
            else:
                open_new_ticket(next_ticket, customer_name, issue)
                next_ticket += 1
    elif menu_action == "2":
        ticket_number = input("Please enter your ticket number: ")
        if ticket_number.strip() == "":
            print("No ticket number was entered, returning to the menu.")
        else:
            ticket_number = "Ticket" + ticket_number
            status = input("Are you closing, or opening a ticket? (open/close): ").lower()
            if status == "open" or status == "close":  
                if status == "close":
                    status = "closed"              
                update_ticket(ticket_number, status)
            else:
                print("Invalid input. Returning to the menu.")
    elif menu_action == "3":
        filter = input("Would you like to filter by ticket status? (yes/no): ")
        display_tickets(filter)
    elif menu_action == "4":
        break
    else:
        print("That is not a valid selection, please enter 1, 2, 3, or 4.")
