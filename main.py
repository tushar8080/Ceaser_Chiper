from ceaser_cipher import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos + shift_amount
            end_text += alphabet[new_pos]
        else:
            end_text += char
    print(f"the {direction}d is {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    ceaser(cipher_direction=direction, start_text=text, shift_amount=shift)

    result = input("Type 'yes' if you want to it again. Otherwise say 'no':")
    if result == "no":
        should_continue = False
print("goodbye")
