class Reservations:
    def __init__(self):
        self.bookings = {
            "Jonas": "000001",
            "Petras": "000002",
            "Ona": "000003",
            "Marytė": "000004",
            "Kazimieras": "000005",
            "Gabija": "000006",
            "Tomas": "000007",
            "Eglė": "000008",
            "Gintaras": "000009",
            "Ieva": "000010",
            "Mantas": "000011",
            "Rūta": "000012",
            "Artūras": "000013",
            "Laura": "000014",
            "Žygimantas": "000015",
            "Milda": "000016",
            "Algirdas": "000017",
            "Inga": "000018",
            "Paulius": "000019",
            "Greta": "000020",
        }

    def check_booking(self):
        check_booking = input("Do you have a booking nr? (yes = y; no = n): ")

        if check_booking.lower() == "n":
            choice = input(
                "Would you like to reserve a table or walk in? (reserve = r; walk in = w): "
            )
            if choice.lower() == "r":
                enter_name = input("Please enter your name for the reservation: ")
                # Atnaujinimas užsakymo numerio
                new_booking_number = str(int(max(self.bookings.values())) + 1).zfill(6)
                self.bookings[enter_name] = new_booking_number
                print(
                    f"Great {enter_name}! Your table has been reserved. Your booking nr is: {new_booking_number}"
                )
            elif choice.lower() == "w":
                print("Welcome to Cafeteria! Feel free to walk in.")
            else:
                print("Invalid choice. Please try again.")
        elif check_booking.lower() == "y":
            enter_booking_nr = input("Enter your booking nr: ")
            if enter_booking_nr in self.bookings.values():
                name = [
                    key
                    for key, value in self.bookings.items()
                    if value == enter_booking_nr
                ][0]
                print(f"Welcome, {name}!")
            else:
                print("Incorrect booking number.")
        else:
            print("Invalid input. Please try again.")


reservations = Reservations()
reservations.check_booking()
