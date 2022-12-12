# to convert string into int we need to use int before variable otherwise it takes it as string and produce error msg
birth_year = input( 'Birth year: ')
age = 2022 - int(birth_year)
print( age )