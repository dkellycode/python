def calculateCheckDigit(gtin: str):
    multiplication_array = [3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3]

    formatted_gtin = ''
    
    if len(gtin) < 17:
        prefix_digits = (17 - len(gtin)) * '0'
        formatted_gtin = prefix_digits + gtin

    gtin_list = list(formatted_gtin)
    sum = 0

    for i in range(len(gtin_list)):
        sum += (int(gtin_list[i]) * multiplication_array[i])

    check_digit = (10 - sum % 10)

    if check_digit == 10:
        check_digit = 0

    return gtin + str(check_digit)


def calculateAllGTIN14s(gtin: str, specific_leading_digit = '') -> list:
    stripped_gtin = gtin[:-1]
    resulting_gtins = []

    if specific_leading_digit != '':
        resulting_gtins.append(calculateCheckDigit(f"{specific_leading_digit}{stripped_gtin}"))
    else:
        for i in range(1, 10):
            resulting_gtins.append(calculateCheckDigit(f"{i}{stripped_gtin}"))

    return resulting_gtins

def DisplayGTINS(original_gtin: str, calculated_gtins: list):
    result_str = f"{original_gtin}:\n"
    for gtin in calculated_gtins: 
        result_str += f"{gtin}\n"
    return (result_str + "\n")

def display_simple_gtin(gtins: list):
    result_str = ""
    for gtin in gtins:
        result_str += f"{gtin}\n"
    return result_str

def main():

    input_path = "gtin13s.txt"
    output_path = "gtin14s.txt"

    specific_leading_digit = input("What is the specific prefix digit you're looking for: ")
    f = open(input_path, "r")

    gtins = f.readlines()

    resulting_file = open(output_path, 'w')
    simplified_resulting_file = open(f'Simplified_{output_path}', 'w')

    for i in range(len(gtins)):
        gtins[i] = gtins[i].strip()

    for gtin in gtins:
        gtin14s = calculateAllGTIN14s(gtin, specific_leading_digit)
        resulting_file.write(DisplayGTINS(gtin, gtin14s))
        simplified_resulting_file.write(display_simple_gtin(gtin14s))

if __name__ == "__main__":
    main()