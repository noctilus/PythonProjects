import whois
from icecream import ic

domainname = input("Enter the domain you're looking for: ")
z = whois.query(domainname)
print(z)
