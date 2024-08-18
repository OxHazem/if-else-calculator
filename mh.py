def add():
    x = input("enter numbers you want to add:").split('+')
    sum = 0
    for i in x:
        sum += int(i)
    print(sum)
    return sum


def subtract():
    x = input("enter numbers you want to subtract:").split('-')
    sum =0
    for i in x:
        sum = int(i)-sum
    print(-sum)
    return sum




def multiply():
    x = input("enter numbers you want to multiply:").split("*")
    sum: int = 1
    for i in x:
        sum *= int(i)
    print(sum)
    return sum





def divide():
    x = input("enter numbers you want to divide:").split('/')
    sum = 1
    for i in x:
        sum = int(i)/sum
    print(1/sum)
    return sum




def power_function():
        base =float(input("enter the number you want to power it:"))
        power =float(input("enter the power you want:"))
        result = base ** power
        print(result)
        return(result)

def convert_milligrams():
    weight_in_milligrams = float(input("Enter weight in milligrams: "))
    weight_in_grams = weight_in_milligrams / 10 ** 3
    weight_in_kilograms = weight_in_milligrams / 10 ** 6
    weight_in_tons = weight_in_milligrams / 10 ** 9
    print(f"{weight_in_milligrams} milligrams is equal to:")
    print(f"{weight_in_grams} grams")
    print(f"{weight_in_kilograms} kilograms")
    print(f"{weight_in_tons} tons")
    return weight_in_grams, weight_in_kilograms, weight_in_tons


def convert_grams():
     weight_in_grams = float(input("Enter weight  in grams: "))
     weight_in_milligrams = weight_in_grams * 10 ** 3
     weight_in_kilograms = weight_in_grams / 10 ** 3
     weight_in_tons = weight_in_grams / 10 ** 6
     print(f"{weight_in_milligrams} milligrams is equal to:")
     print(f"{weight_in_milligrams} milligrams")
     print(f"{weight_in_kilograms} kilograms")
     print(f"{weight_in_tons} tons")
     return weight_in_milligrams, weight_in_kilograms, weight_in_tons






def convert_kilograms():
    weight_in_kilograms = float(input("Enter weight in kilograms: "))
    weight_in_milligrams = weight_in_kilograms * 10 ** 6
    weight_in_grams = weight_in_kilograms * 10 ** 3
    weight_in_tons = weight_in_kilograms / 10 ** 3
    print(f"{weight_in_kilograms} kilograms is equal to:")
    print(f"{weight_in_milligrams} milligrams")
    print(f"{weight_in_grams} grams")
    print(f"{weight_in_tons} tons")
    return weight_in_milligrams, weight_in_grams, weight_in_tons


def convert_tons():
    weight_in_tons = float(input("Enter weight in tons: "))
    weight_in_milligrams = weight_in_tons * 10 ** 9
    weight_in_grams = weight_in_tons * 10 ** 6
    weight_in_kilograms = weight_in_tons * 10 ** 3
    print(f"{weight_in_tons} tons is equal to:")
    print(f"{weight_in_milligrams} milligrams")
    print(f"{weight_in_grams} grams")
    print(f"{weight_in_kilograms} kilograms")
    return weight_in_milligrams, weight_in_grams, weight_in_kilograms





def convert_millimeters():
    lenghts_in_millimeters = float(input("Enter lenghts in millimeters: "))
    lenghts_in_centimeters = lenghts_in_millimeters / 10
    lenghts_in_meters = lenghts_in_millimeters / 10 ** 3
    lenghts_in_kilometers = lenghts_in_millimeters / 10 ** 6
    print(f"{lenghts_in_millimeters} millimeters is equal to:")
    print(f"{lenghts_in_centimeters} centimeters")
    print(f"{lenghts_in_meters} meters")
    print(f"{lenghts_in_kilometers} kilometers")
    return lenghts_in_centimeters, lenghts_in_meters, lenghts_in_kilometers


def convert_centimeters():
    lenghts_in_centimeters = float(input("Enter lenghts in centimeters: "))
    lenghts_in_millimeters = lenghts_in_centimeters * 10
    lenghts_in_meters = lenghts_in_centimeters / 10 ** 2
    lenghts_in_kilometers = lenghts_in_centimeters / 10 ** 5
    print(f"{lenghts_in_centimeters} centimeters is equal to:")
    print(f"{lenghts_in_millimeters} millimeters")
    print(f"{lenghts_in_meters} meters")
    print(f"{lenghts_in_kilometers} kilometers")
    return lenghts_in_millimeters, lenghts_in_meters, lenghts_in_kilometers






def convert_meters():
    lenghts_in_meters = float(input("Enter lenghts in meters: "))
    lenghts_in_millimeters = lenghts_in_meters * 10 ** 3
    lenghts_in_centimeters = lenghts_in_meters * 10 ** 2
    lenghts_in_kilometers =lenghts_in_meters / 10 ** 3
    print(f"{lenghts_in_meters} meters is equal to:")
    print(f"{lenghts_in_millimeters} millimeters")
    print(f"{lenghts_in_centimeters} centimeters")
    print(f"{lenghts_in_kilometers} kilometers")
    return lenghts_in_millimeters, lenghts_in_centimeters, lenghts_in_kilometers



def convert_kilometers():
    lenghts_in_kilometers = float(input("Enter lenghts in kilometers: "))
    lenghts_in_millimeters = lenghts_in_kilometers * 10
    lenghts_in_centimeters = lenghts_in_kilometers * 10 ** 3
    lenghts_in_meters = lenghts_in_kilometers * 10 ** 6
    print(f"{lenghts_in_kilometers} kilometers is equal to:")
    print(f"{lenghts_in_millimeters} millimeters")
    print(f"{lenghts_in_centimeters} centimeters")
    print(f"{lenghts_in_meters} meters")
    return lenghts_in_millimeters, lenghts_in_centimeters, lenghts_in_meters


