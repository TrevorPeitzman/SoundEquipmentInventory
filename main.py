import history
import current
import utils

print("Welcome to the Sound Equipment Inventory System\nPlease scan a selector barcode to begin.")
global barcode


def main():
    while True:
        initcode = input("Selector Barcode: ")

        if utils.internet_on():
            pass

        if initcode == "QUIT":
            utils.quitlog()
            exit()

        elif bool(initcode == "") | bool(initcode == " "):
            print("Blank input. Try again.")
            main()

        elif initcode == "SHOP":
            itemcode = get_barcode(initcode)
            history.check_in(itemcode)
            current.update_location(itemcode, initcode)
            print(itemcode + " checked into SHOP.")

        elif initcode == "RETIRE":
            itemcode = get_barcode(initcode)
            history.check_out(itemcode, initcode)
            current.update_location(itemcode, initcode)
            print(itemcode + " retired. Thank you for your service, " + itemcode + ".")

        elif initcode == "CHKLOC":
            itemcode = get_barcode(initcode)
            print(itemcode + " is checked out to " + current.where_is(itemcode) + ".")

        else:
            itemcode = get_barcode(initcode)
            if current.where_is(itemcode) == initcode:
                print(itemcode + " is already checked out to " + initcode + ". Please scan another.")
                main()
            else:
                history.check_out(itemcode, initcode)
                current.update_location(itemcode, initcode)
                print(itemcode + " checked out to " + initcode + ".")


def get_barcode(initcode: str):
    """ Prompts the user for the input barcode, tests to ensure their input is valid, returns barcode if it is. """
    global barcode
    barcode = input("Item Barcode: ")

    if bool(barcode == "") | bool(barcode == " "):
        print("Blank input. Try again.")
        get_barcode(initcode)

    elif barcode == "CANCEL":
        print("Cancelling.")
        main()

    elif barcode == "QUIT":
        print("Are you sure? Scan QUIT again to stop Sound Equipment Inventory System.")
        main()

    elif bool(current.where_is(barcode) == "SHOP") & bool(initcode == "SHOP"):
        print(barcode + " already in SHOP. Please scan another.")
        get_barcode(initcode)

    elif barcode in current.get_retired():
        print(barcode + " is already retired. Try again.")
        get_barcode(initcode)

    elif barcode in utils.get_barcode_rules():
        print(barcode + " is reserved as a SELECTOR BARCODE. Try again.")
        get_barcode(initcode)

    return str(barcode)


main()
