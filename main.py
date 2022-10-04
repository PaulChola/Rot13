mode_algorithm = int(input("Enter(1) to encrypt:\nEnter(2) to decrypt:\n"))
message = input("Enter a words or name:").upper()

if mode_algorithm == 1:

    letters_of_alpha = "abcdefghijklmnopqrstuvwxyz".upper()
    secret = "".join([letters_of_alpha[(letters_of_alpha.find(c)+13)%26] for c in message])
    print(f"ENCRYPTED TEXT {secret}")

elif mode_algorithm == 2:

    letters_of_alpha = "abcdefghijklmnopqrstuvwxyz".upper()
    secret = "".join([letters_of_alpha[(letters_of_alpha.find(c)-13)%26] for c in message])
    print(f"DECRYPTED TEXT {secret}")

else:
   print("ERROR...")
