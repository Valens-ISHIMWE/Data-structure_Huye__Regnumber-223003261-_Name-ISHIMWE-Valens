from collections import deque

booked_tickets =[]

tickets_list =['VIP','VVIP','REGULAR']

def available_tickets():
    print(' AVAILABLE TICKETS: ')
    for ticket in tickets_list:
        print(f'\t {ticket}')

def booking_ticket():
    booking= input('Enter your ticket you want to book(eg. VIP or regular): ')
    if   booking in tickets_list:
          print(f'{booking} is booked successfully!!')
          booked_tickets.append(booking)
    else:
          print(f'Sorry!!, Your ticket choice is not correct please try again\n')

def undoing_booking():
    if booked_tickets:
        booked_tickets.pop()
        print(f'undoing booking for ticket {booked_tickets} is successful')
    else:
        print('Sorry, No bookings available to undo')

def current_bookings():
    for tickets in booked_tickets:
        print('\tCURRENT BOOKINGS:')
        print(tickets)

def exit():
    print('\nThank you for using Ticket booking system!!')


def TICKET_BOOKING():
    while True:
        print(f'\tWELCOME TO TICKET BOOKING')
        print(f'\t --------------------------\n')
        print(f'\t1. Show available tickets')
        print(f'\t2. Book a ticket')
        print(f'\t3. undo last booking')
        print(f'\t4. View current bookings')
        print(f'\t5. Exiting the system')

        option = int(input('Enter your choice(1 or 2,..): '))
        if option == 1:
            available_tickets()
        elif option ==2:
            booking_ticket()
        elif option ==3:
            undoing_booking()
        elif option ==4:
            current_bookings()
        else:
            exit()
            break
TICKET_BOOKING()
        

