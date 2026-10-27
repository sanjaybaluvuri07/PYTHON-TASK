
# Nested Loop Examination Seating Generator

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

capacity = 30

if rows <= 0 or cols <= 0 or rows * cols > capacity:
    print("Invalid dimensions! Classroom capacity is 30 seats.")
else:
    reserved = [(1, 2), (2, 3)]
    seat_number = 1

    print("\nEXAMINATION SEATING ARRANGEMENT\n")

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):

            # Reserved seats
            if (r, c) in reserved:
                seat = "RESERVED"

            # Alternate seating restriction
            elif (r + c) % 2 == 0:
                seat = "EMPTY"

            else:
                seat = "S" + str(seat_number)
                seat_number += 1

            print(f"{seat:10}", end=" ")

        print()

    print("\nTotal classroom capacity:", capacity)
    print("Seats occupied:", seat_number - 1)
    print("Reserved positions:", len(reserved))
