from validate_email import validate_email

ema = input("Type the email to search: ")
is_valid = validate_email(ema, verify=True)
if str(is_valid).upper() == "TRUE":
    print("[+] FOUND")
else:
    print("[!] NOT FOUND")
