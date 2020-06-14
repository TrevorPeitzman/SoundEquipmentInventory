import datetime
import history
import current

print("Welcome to the Sound Equipment Inventory System\nPlease scan a selector barcode to begin.")


def main():
    while True:
        initcode = input("Selector Barcode: ")

        try:
            initcode = str(initcode)
        except:
            print("Non-readable barcode entered. Please try again.")
            main()

        if initcode == "QUIT":
            exit()
        elif initcode == "":
            print("Blank input. Try again.")
            main()
        elif initcode == "SHOP":
            history.check_in(input("Item Barcode: "))
        elif initcode == "CHKLOC":
            current.check_location(input("Item Barcode: "))
        else:
            history.check_out(input("Item Barcode: "), initcode)


main()
