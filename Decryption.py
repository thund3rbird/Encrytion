str=input("Enter the string you want to Decrypt:  ")

character = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
secret    = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
decrypted_message = ""
for Character in str:
    index = character.find(Character)
    decrypted_message = decrypted_message + secret[index] 
  
print(decrypted_message)
