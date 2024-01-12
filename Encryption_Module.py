shift = 516151611
def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(encrypted_text):
    return encrypt(encrypted_text, -shift)

def search_crypto(file: str, text: str):
    with open(file, mode='r') as soubor:
        obsah = soubor.readlines()
        C = 0  # Inicializujeme proměnnou C mimo cyklus
        for line in obsah:
            line1 = decrypt(line)
            if line1.find(text) != -1:
                C += 1  # Zvýšíme C o 1, když nalezneme hledaný řetězec
                return line1
    return None  # Pokud se řetězec nenalezne, vracíme None