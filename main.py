import pyttsx3
import sys
from PIL import Image


# speech library initialization
engine = pyttsx3.init()


# Prompt the user to choose between ROT13 and visual cryptography

program_choice = input("Choose a program: ROT13 (R) or visual cryptography (V)? ")

if program_choice.upper() == "R":
     
    # Prompt user to choose encryption or decryption mode
    mode_algorithm = int(input("Enter 1 for encryption mode or 2 for decryption mode: "))
    message = input("Enter a message to encrypt or decrypt: ")
   
    if mode_algorithm == 1:
        # If encryption mode is chosen, prompt user to input shift value
        shift = int(input("Enter a shift value: "))
        encrypted_message = ""

        # Iterate over each character in the message and shift its ASCII value by the given shift value
        for char in message:
            if char.isalpha(): # Only shift alphabetic characters
                if char.isupper(): # Handle uppercase letters
                    encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
                else: # Handle lowercase letters
                    encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
            else: # Leave non-alphabetic characters as-is
                encrypted_message += char
        engine.say("The encrypted message is " + encrypted_message)
        print("Encrypted message:", encrypted_message)
        engine.runAndWait()
    
    elif mode_algorithm == 2:
        # If decryption mode is chosen, prompt user to input the shift value used to encrypt the message
        shift = int(input("Enter the shift value used to encrypt the message: "))
        decrypted_message = ""
    
        # Iterate over each character in the message and shift its ASCII value by the inverse of the given shift value
        for char in message:
            if char.isalpha(): # Only shift alphabetic characters
                if char.isupper(): # Handle uppercase letters
                    decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
                else: # Handle lowercase letters
                    decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
            else: # Leave non-alphabetic characters as-is
                decrypted_message += char
        print("Decrypted message:", decrypted_message)
        engine.say("The decrypted message is " + decrypted_message)
        engine.runAndWait()

elif program_choice.upper() == "V":
    
    # Load two images to scramble
    try:
        img1 = Image.open("scrambled1.png")
        img2 = Image.open("scrambled2.png")
    except FileNotFoundError:
        error3 = "Error: could not find image files."
        engine.say(error3)
        print(error3)
        engine.runAndWait()
        sys.exit()
    except:
        error3 = "Error: could not open image files."
        engine.say(error3)
        print(error3)
        engine.runAndWait()
        sys.exit()

    # Validate that the images have the same size
    if img1.size != img2.size:
        error4 = "Error: images are not the same size."
        engine.say(error4)
        print(error4)
        engine.runAndWait()
        sys.exit()

    # Scramble the images
    pixels1 = img1.load()
    pixels2 = img2.load()
    output_img = Image.new("RGB", img1.size)
    output_pixels = output_img.load()

    for row in range(img1.size[1]):
        for col in range(img1.size[0]):
            output_pixels[col,row]=(
                (pixels1[col,row][0]+pixels2[col,row][0])%256,
                (pixels1[col,row][1]+pixels2[col,row][1])%256,
                (pixels1[col,row][2]+pixels2[col,row][2])%256)

    # Save the output image
    output_img.save("output.png")
    engine.say("Visual Decryption complete")
    engine.runAndWait()
    
else:
    # Invalid choice of program
    error2 = "Invalid message. Please enter only letters ROT13 (R) or (V) visual cryptography."
    engine.say(f"{error2}, {print(error2)}")
    engine.runAndWait()
    sys.exit()