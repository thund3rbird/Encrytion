str=input("Enter the string you want to encrypt:  ")

character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
secret    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
encrypted_message = ""
for Character in str:
    index = character.find(Character)
    encrypted_message = encrypted_message + secret[index] 
  
print(encrypted_message)