import dns.resolver

print(" Enter the Domain Name: ")
domain = raw_input()
with open("top20000subs.txt", "r") as ins:
    array = []
    for line in ins:
        line = line.strip()
        array.append(line)
for sub in array:
    subdomain = str(sub)+"."+domain
    try:
        answers = dns.resolver.query(subdomain)
        for rdata in answers: 
            print("Subdomain: "+subdomain+","+str(rdata))
    except:
        pass
