pending_orders = [] 
canceled_tickets = []  
concert_details = {}  

def cancel_ticket(ticket_id):
    canceled_tickets.append(ticket_id)

def place_order(ticket_id):
    pending_orders.append(ticket_id)

def process_order():
    if pending_orders:
        ticket_id = pending_orders.pop(0)
        if ticket_id in concert_details:
            if concert_details[ticket_id] > 0:
                concert_details[ticket_id] -= 1
                print(f"Order for ticket {ticket_id} processed successfully.")
            else:
                print(f"Ticket {ticket_id} is sold out.")
                canceled_tickets.append(ticket_id)
        else:
            print(f"Ticket {ticket_id} is invalid.")
            canceled_tickets.append(ticket_id)
    else:
        print("No pending orders.")

def undo_cancellation():
    if canceled_tickets:
        ticket_id = canceled_tickets.pop()
        concert_details[ticket_id] += 1
        print(f"Canceled ticket {ticket_id} restored.")
    else:
        print("No canceled tickets.")

concert_details["Ticket 1"] = 10
concert_details["Ticket 2"] = 5
concert_details["Ticket 3"] = 2

place_order("Ticket 1")
place_order("Ticket 1")
place_order("Ticket 2")
place_order("Ticket 3")
place_order("Ticket 3")
place_order("Ticket 3") 
process_order()
process_order()
process_order()
process_order()
cancel_ticket("Ticket 1")
cancel_ticket("Ticket 1")
cancel_ticket("Ticket 2")
cancel_ticket("Ticket 1")
cancel_ticket("Ticket 3")
undo_cancellation()
undo_cancellation()
undo_cancellation()
undo_cancellation()

print("list to  for queue(FIFO):", concert_details)