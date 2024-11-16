country_code = {'India' : '0091', 
                'Australia' : '0025',
                'Nepal' : '00977',
                "Bangladesh" : "00880",
                "Portugal" : "00351",
                "Nigeria" : "00234"}

print("Country code for Bangladesh : ")
print(country_code.get("Bangladesh","Not found"))


print("Country code for Vatican City : ")
print(country_code.get("Vatican City","Not found"))


