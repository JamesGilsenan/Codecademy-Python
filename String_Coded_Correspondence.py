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

def encrypt_message(message, offset):
    encrypted_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "!?.,' "
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            encrypted_message += alphabet[(letter_value - offset) % 26]
        else:
            encrypted_message += letter
    return encrypted_message 

def brute_force(message):
    punctuation = "!?.,' "
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    offset = 0
    for i in range(26):
        decrypted_message = ""
        offset += 1
        for letter in message:
            if not letter in punctuation:
                letter_value = alphabet.find(letter)
                decrypted_message += alphabet[(letter_value + offset) % 26]
            else:
                decrypted_message += letter
        print("\nOffset = " + str(offset) + " - " + decrypted_message)       

#print(decrypt_message("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!", 10))
#print(encrypt_message("hey there! I have decrypted your message. This Caeser Cipher is really cool!", 10))
#print(decrypt_message("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))
#print(decrypt_message("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))
brute_force("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")