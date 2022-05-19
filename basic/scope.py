calculation_to_hours = 24
name_of_unit = 'hours'

def days_to_units(number_of_days, custom_message):
    print(f'{number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}')
    print(custom_message)

def scope_check(num_of_days):
    my_var = 'variable inside function'
    print(name_of_unit)     # global variable
    print(num_of_days)   # local variable
    print(my_var)


scope_check(20)
