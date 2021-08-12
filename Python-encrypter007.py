from sagol import pagol

a = input("Enter anything: ")

print(pagol(a.encode('utf-8')).hexdigest())
