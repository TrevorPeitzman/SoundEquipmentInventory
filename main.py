import history
import current
import utils

print("Welcome to the Sound Equipment Inventory System\nPlease scan a selector barcode to begin.")


def main():
    while True:
        initcode = input("Selector Barcode: ")

        if utils.internet_on():
            pass
        else:
            exit()

        if initcode == "QUIT":
            utils.quitlog()
            exit()

        elif initcode == "":
            print("Blank input. Try again.")
            main()

        elif initcode == "SHOP":
            barcode = input("Item Barcode: ")
            if current.where_is(barcode) == "SHOP":
                print("Item already in SHOP. Please scan another.")
                main()
            else:
                history.check_in(barcode)
                current.add_entry(barcode, initcode)

        elif initcode == "CHKLOC":
            barcode = input("Item Barcode: ")
            print(current.where_is(barcode))

        else:
            barcode = input("Item Barcode: ")
            if current.where_is(barcode) == initcode:
                print("Item already checked out to " + initcode + ". Please scan another.")
                main()
            else:
                history.check_out(barcode, initcode)
                current.update_location(barcode, initcode)


main()
