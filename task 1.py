def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of temperature (Celsius/C/Fahrenheit/F/Kelvin/K): ").upper()

    if unit == 'C' or unit == 'CELSIUS':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{temperature} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin.")
    elif unit == 'F' or unit == 'FAHRENHEIT':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{temperature} degrees Fahrenheit is equal to {celsius} degrees Celsius and {kelvin} Kelvin.")
    elif unit == 'K' or unit == 'KELVIN':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{temperature} Kelvin is equal to {celsius} degrees Celsius and {fahrenheit} Fahrenheit.")
    else:
        print("Invalid unit entered. Please enter either Celsius/C, Fahrenheit/F, or Kelvin/K.")
