from datetime import datetime

def add_guest(guest_list):
    try:
        guest_name = str(input("Please enter guest name - ")).strip()
        if guest_name not in guest_list:
            guest_list.append(guest_name)
            g_id = str(guest_list.index(guest_name))
            print ("Guest " + guest_name + " has been created with guest ID: " + g_id + "\n")
            add_guest_option()
        else:
            print("Guest already exists With this name please try with another name \n ")
            add_guest_option()
    except Exception as e:
        raise e


def add_guest_option():
    try:
        option1 = str(input("Would you like to [A]dd a new guest or [R]eturn to the previous menu?  ")).lower().strip()
        if option1 == "a":
            add_guest(guest_list)
        elif option1 == "r":
            options_func()
        else:
            print("Invaid input \n")
            add_guest_option()
    except Exception as e:
        raise e


def add_room(rooms):
    try:
        r_no = str(input("Please enter room number : ")).strip()
        if r_no not in rooms.keys():
            r_cap = int(input("Please enter room capacity : "))
            rooms[r_no] = {"cap": r_cap}
            add_room_option()
        else:
            print("Room already exists")
            add_room(rooms)
    except Exception as e:
        raise e


def add_room_option():
    try:
        option2 = str(input("Would you like to [A]dd a new room or [R]eturn to the previous menu?  ")).lower().strip()
        if option2 == "a":
            add_room(rooms)
        elif option2 == "r":
            options_func()
        else:
            print("Invaid input \n")
            add_room_option()
    except Exception as e:
        raise e


def get_room_no():
    room_no = ""
    try:
        room_no = str(input("Please enter room number: ")).strip()
        if room_no in rooms.keys():
            no_of_mems = int(input("Please enter number of guests: "))
            if no_of_mems > rooms[room_no]["cap"]:
                print("Guest count exceeds room capacity of: " + str(rooms[room_no]["cap"]))
                room_no = get_room_no()
            else:
                return room_no
        else:
            print("Room does not exist. \n")
            room_no = get_room_no()
    except Exception as e:
        raise e
    return room_no


def dateToDayNumber(month, day):
    try:
        print (month)
        print (day)
        if (month < 1 and month > 12 and day < 1 and day > 31):
            return 0
        if (month == 1):
            return day
        if (month == 2):
            return 31 + day
        if (month == 3):
            return 59 + day
        if (month == 4):
            return 90 + day
        if (month == 5):
            return 120 + day
        if (month == 6):
            return 151 + day
        if (month == 7):
            return 181 + day
        if (month == 8):
            return 212 + day
        if (month == 9):
            return 243 + day
        if (month == 10):
            return 273 + day
        if (month == 11):
            return 304 + day
        return 334 + day
    except Exception as e:
        raise e


def get_day(check):
    day_inn = 0
    try:
        day_inn = int(input("Please enter " + check + " day: "))
        if 0 < day_inn < 32:
            pass
        else:
            print("Invalid day.")
            day_inn = get_day(check)
    except Exception as e:
        raise e
    return day_inn


def get_month(check):
    month_and_day = 0
    day_input = 0
    num = 0
    try:
        month_in = int(input("Please enter " + check + " month: "))
        if 0 < month_in < 13:
            day_input = get_day(check)
            month_and_day = str(month_in) + "/" + str(day_input)
            try:
                datetime.strptime(month_and_day, '%m/%d')
                print('The date {} is valid.'.format(month_and_day))
                in_month = int(month_and_day.strip().split("/")[0])
                in_day = int(month_and_day.strip().split("/")[1])
                num = dateToDayNumber(in_month, in_day)
            except ValueError:
                print('The date {} is invalid'.format(month_and_day))
                month_and_day, num = get_month(check)
        else:
            print("Invalid month.")
            month_and_day, num = get_month(check)
    except Exception as e:
        raise e
    return month_and_day, num


def get_checkin_out():
    month_and_day_cin = ""
    num_cin = ""
    month_and_day_cout = ""
    num_cout = ""
    try:
        month_and_day_cin, num_cin = get_month("check-in")
        month_and_day_cout, num_cout = get_month("check-out")
        if num_cin < num_cout:
            pass
        else:
            print("Invalid checkin date or checkout date \n")
            month_and_day_cin, num_cin, month_and_day_cout, num_cout = get_checkin_out()
    except Exception as e:
        raise e
    return month_and_day_cin, num_cin, month_and_day_cout, num_cout


def add_booking_option():
    try:
        option3 = str(input("Would you like to [A]dd a new booking or [R]eturn to the previous menu?   ")).lower().strip()
        if option3 == "a":
            add_booking()
        elif option3 == "r":
            options_func()
        else:
            print("Invaid input \n")
            add_booking_option()
    except Exception as e:
        raise e


def add_booking():
    try:
        guest_id = str(input("Please enter guest ID: ")).strip()
        if int(guest_id) < len(guest_list):
            in_r_no = get_room_no()
            checkin, checkin_num, checkout, checkout_num = get_checkin_out()
            if len(bookings) > 0:
                for i in bookings:
                    if i["room_no"] == in_r_no:
                        if i["checkin_num"] <= checkin_num <= i["checkout_num"]:
                            print("Room is not available during that period.")
                            add_booking()
                        else:
                            bookings.append({"guest_id": guest_id, "guest_name": guest_list[int(guest_id)], "room_no": in_r_no, "room_cap": rooms[in_r_no]["cap"], "checkin": checkin, "checkout": checkout, "checkin_num": checkin_num, "checkout_num": checkout_num})
                            print("*** Booking successful! *333333333**")
                            add_booking_option()
                            # print (bookings)
                    else:
                        bookings.append({"guest_id": guest_id, "guest_name": guest_list[int(guest_id)], "room_no": in_r_no, "room_cap": rooms[in_r_no]["cap"], "checkin": checkin, "checkout": checkout, "checkin_num": checkin_num, "checkout_num": checkout_num})
                        print("*** Booking successful! ***222222222")
                        # print (bookings)
                        add_booking_option()

            else:
                bookings.append({"guest_id": guest_id, "guest_name": guest_list[int(guest_id)], "room_no": in_r_no, "room_cap": rooms[in_r_no]["cap"], "checkin": checkin, "checkout": checkout, "checkin_num": checkin_num, "checkout_num": checkout_num})
                print("*** Booking successful! ***1111111111")
                add_booking_option()
                # print (bookings)
            options_func()
        else:
            print("Guest does not exist. \n")
            add_booking()
    except Exception as e:
        raise e


def view_guest_booking():
    try:
        guest_id = str(input("Please enter guest ID: ")).strip()
        if len(bookings) > 0:
            print (bookings)
            guest_ids_list = []
            for i in bookings:
                guest_ids_list.append(i["guest_id"])
            print(guest_ids_list)
            print(guest_id)
            if guest_id in guest_ids_list:
                for i in bookings:
                    if i["guest_id"] == guest_id:
                        print("\nGuest " + i["guest_id"] + ": " + i["guest_name"] + "\nBooking : Room " + i["room_no"] + ", " + str(i["room_cap"]) + " guest(s) from " + i["checkin"] + " to " + i["checkout"])
                        view_booking()
            else:
                print ("Guest does not exist. \n")
                view_guest_booking()
        else:
            print (" No bookings on this guest ID " + guest_id)
            view_booking()
    except Exception as e:
        raise e


def view_room_booking():
    try:
        room_no = str(input("Please enter room number:")).strip()
        if len(bookings) > 0:
            print (bookings)
            room_no_list = []
            for i in bookings:
                room_no_list.append(i["room_no"])
            print(room_no_list)
            print(room_no)
            if room_no in room_no_list:
                for i in bookings:
                    if i["room_no"] == room_no:
                        print("\nGuest " + i["guest_id"] + ": " + i["guest_name"] + "\nBooking : Room " + i["room_no"] + ", " + str(i["room_cap"]) + " guest(s) from " + i["checkin"] + " to " + i["checkout"])
                        view_booking()
            else:
                print ("Room does not exist. \n")
                view_room_booking()
        else:
            print (" No bookings on this room no " + room_no)
            view_booking()
    except Exception as e:
        raise e


def view_booking():
    try:
        option4 = str(input("Would you like to view [G]uest bookings, [R]oom booking, or e[X]it?  ")).lower().strip()
        if option4 == "g":
            view_guest_booking()
        elif option4 == "r":
            view_room_booking()
        elif option4 == "x":
            options_func()
        else:
            print("Invaid input \n")
            view_booking()
    except Exception as e:
        raise e


def options_func():
    try:
        input_options = str(input("\nMain Menu - please select an option:\n\t 1.) Add guest\n  \t 2.) Add room \n \t 3.) Add booking \n \t 4.) View bookings \n \t 5.) Quit \n")).strip()
        if input_options == "1":
            add_guest(guest_list)
        elif input_options == "2":
            add_room(rooms)
        elif input_options == "3":
            add_booking()
        elif input_options == "4":
            view_booking()
        elif input_options == "5":
            print ("---------------------------------------------------\n---- Thanks for using HERE_4_U Hotel Bookings! ----\n---------------------------------------------------")
        else:
            print ("Invalid input ")
            options_func()
            pass
    except Exception as e:
        raise e


def main():
    global guest_list
    guest_list = []
    global rooms
    rooms = {}
    global bookings
    bookings = []
    print ("---------------------------------------------------\n-------- Welcome to HERE_4_U Hotel Bookings -------\n---------------------------------------------------")
    options_func()
main()
