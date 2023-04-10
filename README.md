# IPGeolocationtool
Here, we are using the geoip2 library to read the GeoIP2 database file which contains information about IP addresses and their geographical locations.

We then define a function get_location which takes an IP address as input, uses the city method of the geoip2 reader object to retrieve location details from the database, and returns a dictionary with the country name, city name, latitude, and longitude.

You can replace the example IP address ('216.58.194.174') with any IP address you want to check. If the IP address is valid and location details are found, the function will return a dictionary with the location details. If the IP address is invalid or location details cannot be found, the function will return a dictionary with an error message.

Note: You will need to download the GeoLite2-City.mmdb file from MaxMind and replace the path in the code with the path to the downloaded file.

# Before using, install the programs requirements
``sudo pip3 install -r requirements.txt``

# general usage:
``python3 IPgeolocator.py``
