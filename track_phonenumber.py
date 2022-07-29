import phonenumbers
from test import number

# To get the Country of Origin
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

# To get the Service provider name
from phonenumbers import carrier
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, 'en'))
