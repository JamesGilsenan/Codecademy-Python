def decrypt_message(message, offset):
    decrypted_message = ""
    punctuation = "!?.,' "
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            decrypted_message += alphabet[(letter_value + offset) % 26]
        else:
            decrypted_message += letter
    return decrypted_message
        

print(decrypt_message("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!", 10))
