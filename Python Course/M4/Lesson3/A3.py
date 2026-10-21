country_code = {'India' : '0091',
                'Bahrain' : '0973',
                'UAE' : '0975'}
 
# search dictionary for country code of India
print("Country code for India -")
print(country_code.get('India', 'Not Found'))
 
# search dictionary for country code of UAE
print("Country code for UAE -")
print(country_code.get('UAE', 'Not Found'))

# search dictionary for country code of Brazil
print("Country code for Brazil")
print(country_code.get('Brazil', 'Not Found'))