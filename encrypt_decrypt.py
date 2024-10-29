#ceaser's cipher project

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

msg = input("enter a message you wish to encrypt:  ").lower()

offset_num = int(input("enter a offset number: "))

secret_msg = ""

for i in msg:
  if i in alphabet:
#encrypting
    secret_letter= alphabet.index(i) - offset_num
    secret_msg = secret_msg + alphabet[secret_letter] 
  elif i in ("?!,. "):
    secret_msg = secret_msg + i 

print(secret_msg)

#decrypting
msg_2_decrypt = input("Enter a message you wish to decrypt: ").lower()
offset_num = int(input("enter a offset number: "))
decrypted_msg = ""

for i in msg_2_decrypt:
  if i in alphabet:
    real_letter = (alphabet.index(i) + offset_num) % 26
    decrypted_msg = decrypted_msg + alphabet[real_letter]


  elif i in ("?!,. "):
    decrypted_msg = decrypted_msg + i

print(decrypted_msg)




