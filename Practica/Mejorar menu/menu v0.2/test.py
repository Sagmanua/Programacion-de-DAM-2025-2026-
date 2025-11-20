import re

def hola():
    print("holamundo")
    qeu()
def qeu():
    print("que estas")

hola()
'''
+1 23 45
+12 345 678
+123-12-3456
123 45 678
+49 30 1234 5678
+1-800-555-1234
12-3456-78
1234567
+44 20 7946 0958
+33 1 23 45 67 89
+81 90 1234 5678
+34 912 34 56 78
+7 495 123 45 67
+61 2 1234 5678
+39 06 1234 5678
+91 22 1234 5678
+86 10 1234 5678
+55 11 2345 6789
+27 11 123 4567
+48 22 123 45 67


user@example.com
john.doe@mail.co
alice_bob123@domain.net
test.email+spam@gmail.com

'''
telefono = '+48 22 123 45 67'
def check_telefono(telefono):
    pattern_telefono = r"^\+?\d{1,3}[- ]?\d{2,4}([- ]?\d{2,4}){1,3}$"
    if re.fullmatch(pattern_telefono, telefono):
        return True
    else:
        return False

if check_telefono(telefono):
    print("valido")
else:
    print("No")

email = 'user@example.com'

def check_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(email_pattern, email):
        return True
    else:
        return False

if check_email(email):
    print("valido email")
else:
    print("No email")