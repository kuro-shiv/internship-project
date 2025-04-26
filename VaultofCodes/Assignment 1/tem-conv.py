def convert_temperature(temp, unit):
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = (temp - 32) * 5/9
        return round(converted_temp, 2)
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = (temp * 9/5) + 32
        return round(converted_temp, 2)
    else:
        # Handle invalid input
        return "Invalid unit. Use 'F' for Fahrenheit or 'C' for Celsius."

# User input
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (F for Fahrenheit, C for Celsius): ").strip().upper()

# Display result
print("Converted temperature:", convert_temperature(temp, unit))