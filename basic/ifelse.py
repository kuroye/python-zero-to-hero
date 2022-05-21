calculation_to_unit = 24
name_of_unit = 'hours'

def days_to_units(number_of_days):
    if number_of_days > 0:
        return f'{number_of_days} days are {number_of_days * calculation_to_unit} {name_of_unit}'
    else:
        return 'You entered a negative value'
input_value = input('Hey, enter some value here\n')
# input() the value always be string type

calculated_value = days_to_units(int(input_value))
# if want to pass the integer value convert str to int

print(calculated_value)
