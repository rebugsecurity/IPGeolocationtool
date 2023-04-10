import geoip2.database

# Replace the path below with the path to your GeoIP2 database file
reader = geoip2.database.Reader('/path/to/GeoLite2-City.mmdb')

def get_location(ip_address):
    """
    This function takes an IP address as input and returns a dictionary with location details.
    """
    try:
        response = reader.city(ip_address)
        country_name = response.country.name
        city_name = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        return {'Country': country_name, 'City': city_name, 'Latitude': latitude, 'Longitude': longitude}
    except:
        return {'Error': 'Invalid IP address or cannot find location'}

# Example usage
print(get_location('216.58.194.174')) # Replace this with the IP address you want to check 
