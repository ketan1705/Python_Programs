import phonenumbers
from phonenumbers import geocoder,carrier
phonenumber = phonenumbers.parse("+919559532457")
Carrier = carrier.name_for_number(phonenumber,'en')
Region = geocoder.description_for_number(phonenumber,'en')
print(f"| Country | Supplier|\n-|--------------|\n|{Region} | {Carrier} |")