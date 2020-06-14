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
            barcode = input("Item Barcode: ")
            current.whereis(barcode)
            history.check_in(barcode)
            current.check_in(barcode)
        elif initcode == "CHKLOC":
            barcode = input("Item Barcode: ")
            current.whereis(barcode)
        else:
            barcode = input("Item Barcode: ")
            history.check_out(barcode, initcode)


main()
