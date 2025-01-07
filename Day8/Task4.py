alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def decrypt(original_text, shift_amount):
#     cipher = ""
#     for i in original_text:
#         shift_pos = alphabet.index(i) - shift_amount
#         shift_pos %= 26
#         cipher += alphabet[shift_pos]
#     print(f"The decoded text is {cipher}")
# decrypt(original_text=text, shift_amount=shift)
# def encrypt(original_text, shift_amount):
#     cipher = ""
#     for i in original_text:
#         shift_pos = alphabet.index(i) + shift_amount
#         shift_pos %= 26
#         cipher += alphabet[shift_pos]
#     print(f"The encoded text is {cipher}")
# encrypt(original_text=text , shift_amount=shift)

def caesar(original_text, shift_amount):
    cipher = ""
    for i in original_text:
        if direction =="encode":
            shift_pos = alphabet.index(i) + shift_amount
            shift_pos %= 26
            cipher += alphabet[shift_pos]
        elif direction =="decode":
            shift_pos = alphabet.index(i) - shift_amount
            shift_pos %= 26
            cipher += alphabet[shift_pos]
        else:
            print("Invalid input")
    print(f"The {direction}d text is {cipher}")

caesar(original_text=text, shift_amount=shift)
    
    


