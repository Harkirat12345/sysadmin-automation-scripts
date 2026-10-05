import dns.resolver

while True:
    user_domain = input("What is the domain that you want to look up? ")

    try:
        ip_address = dns.resolver.resolve(user_domain, "A")
        break
    except:
        print("Not a valid domain. Please try again.\n")

print("\nIP Address(es):")
for ip in ip_address:
    print(ip)

print("\nMX Records:")
try:
    mx_record = dns.resolver.resolve(user_domain, "MX")
    for mx in mx_record:
        print(mx)
except:
    print("No MX records found.")

print("\nTXT Records:")
try:
    txt_record = dns.resolver.resolve(user_domain, "TXT")
    for txt in txt_record:
        print(txt)
except:
    print("No TXT records found.")

print("\nCNAME Records:")
try:
    cname_record = dns.resolver.resolve(user_domain, "CNAME")
    for cname in cname_record:
        print(cname)
except:
    print("No CNAME records found.")