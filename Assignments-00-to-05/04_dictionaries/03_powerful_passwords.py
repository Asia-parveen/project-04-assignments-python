import hashlib 

print("This is 03_powerful_passwords")

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
    "asia@example.com":hash_password("asia123"),
    "admin@example.com":hash_password("admin123")
}

def login(email,password):
  if email in stored_logins:
    return stored_logins[email] == hash_password(password)
  return False


if __name__ == "__main__":
  email = input("Enter your email: ")
  password = input("Enter your password: ")


  if login(email,password):
    print("Login successful!")
  else:
    print("Invalid email or password.")


