#Password Strength Checker
#created by : Tanushka Rai

print("=" * 45)
print("PASSWORD STRENGTH CHECKER")
print("=" * 45)

print("This tool checks whether your password is Strong, Medium or Weak.")
print()

password = input("Enter your password:")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for letter in password:
    if letter.isupper():
        has_upper = True

    if letter.islower():
          has_lower = True

    if letter.isdigit():
        has_digit = True

    if not letter.isupper() and not letter.islower() and not letter.isdigit():
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
         print("✅ Strong Password")
         print("Excellent! Your password follows recommended security practices.")

elif len(password) >= 8:
         print("⚠️ Medium Password")
         print("Good! Your password is acceptable but can be stronger.")
         print()
         print("Password Improvement Tips:")

         if not has_upper:
          print("- Add at least one uppercase letter.")
         if not has_lower:
            print("- Add at least one lowercase letter.")

         if not has_digit:
            print("- Add at least one number.")

         if not has_special:
            print("- Add at least one special character.")

         if len(password) < 8:
            print("- Use at least 8 characters.")

else:
         print("❌ Weak Password")
         print("Your password needs improvement.")
         print()
         print("Password Improvement Tips:")
         if not has_upper:
          print("- Add at least one uppercase letter.")

         if not has_lower:
          print("- Add at least one lowercase letter.")
 
         if not has_digit:
          print("- Add at least one number.")

         if not has_special:
          print("- Add at least one special character.")

         if len(password) < 8:
          print("- Use at least 8 characters.")
print()
print("=" * 45)
print("Thank you for using Password Strength Checker!")
print("=" * 45)