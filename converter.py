def binaryToDecimal(binary):
    binary1 = str(binary)[::-1]  # reverse number and convert to
    result = 0

    for x in range(0, len(binary1)):  # exec until len is reached
        if int(binary1[x]) != 0 and int(binary1[x]) != 1:
            print("Wrong binary number.")
        else :
            target = int(binary1[x])  # choose the number w/ int()
            step = target * (2 ** x)  # multiply number w/ 2 power x
            result += step  # add up every step
            print("Processing: %s * (2 ** %s) = %s" % (target, x, step))
    print("Completed:", result)


def decimalToBinary(decimal):
    binary = ""
    while decimal > 0:  # tant que decimal > 0
        decimal = decimal / 2  # divide dec by 2
        number_dec = str(decimal - int(decimal))[1:]  # gets floating decimal
        decimal = int(float(decimal) - float(number_dec))  # decimal minus floating

        def result():
            print("Divided result: ", decimal)
            print("Decimal:        ", number_dec)
            print("Binary added:   ", currentbinary)
            print("Operation:      ", "%s / 2" % decimal)
            print("Binary:         ", int(str(binary)[::-1]))
            print('__________________________________')

        if number_dec != ".0":  # if there's a decimal
            currentbinary = "1"
            binary += currentbinary
            print("--- Retenue ---")
            result()

        else:
            currentbinary = "0"  # add 0 to binary
            print("Non retenue")
            binary += currentbinary
            result()

    true_binary = binary[::-1]
    return true_binary


def decimalVirguleToBinary(decimal):
    binary = ""
    while decimal > 0:  # tant que decimal > 0
        decimal = decimal * 2  # multiply dec by 2

        def result():
            print("Amputed result: ", decimal)
            print("Binary added:   ", currentbinary)
            print("Operation:      ", "%s * 2" % decimal)
            print("Binary:         ", int(str(binary)[::-1]))
            print('__________________________________')

        if decimal >= 1:
            currentbinary = "1"
            binary += currentbinary
            print("Current number: ", decimal)
            decimal -= 1
            result()

        else:
            currentbinary = "0"
            binary += currentbinary
            result()

    true_binary = binary[::-1]
    return true_binary


def binaryToHexadecimal(binary):
    hexalist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    binarylist = [0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111]
    if len(binary) % 2 != 0:
        binary = binary[::-1] + "0"

    processedBinary = binary[::-1]
    total_legth = len(binary)
    binary_docks = int(total_legth / 4)

    while len(processedBinary) != 0:
        for i in range(0, 4):
            binary += processedBinary[i]
            processedBinary -= processedBinary[i]

        for i in range(0, binary_docks):
            dock[i]
            #  I need to create a dock list for each 4 binary numbers
            #  and put each 4 numbers in the [i] dock, once dock has
            #  reached '4' go to the second dock.

decimalToBinary(29)