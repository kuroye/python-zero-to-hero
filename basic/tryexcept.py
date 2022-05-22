calculation_to_unit = 24
name_of_unit = 'hours'

def days_to_units(number_of_days):
    return f'{number_of_days} days are {number_of_days * calculation_to_unit} {name_of_unit}'


def validate_and_execute():
    try:

        input_value_number = int(input_value)
        if input_value_number > 0:
            calculated_value = days_to_units(int(input_value))
            print(calculated_value)
        elif input_value_number == 0:
            print('You entered a 0, enter a valid value')
        else:
            print('You entered a negative number')

    except ValueError:
        print('Your input isn\'t a number. Don\'t ruin my program')


input_value = input('Hey, enter some value here\n')
# input() the value always be string type
validate_and_execute()

