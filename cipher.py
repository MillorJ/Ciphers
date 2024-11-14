import random

# Caesar Cipher
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_value = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_value + shift) % 26 + shift_value)
        else:
            result += char
    return result
    
# Vigenère Cipher
def vigenere_cipher(text, keyword, mode='encrypt'):
    result = ''
    keyword = (keyword * (len(text) // len(keyword))) + keyword[:len(text) % len(keyword)]
    for i, char in enumerate(text):
        if char.isalpha():
            shift_value = 65 if char.isupper() else 97
            key_shift = ord(keyword[i].upper()) - 65
            if mode == 'encrypt':
                result += chr((ord(char) - shift_value + key_shift) % 26 + shift_value)
            else:
                result += chr((ord(char) - shift_value - key_shift) % 26 + shift_value)
        else:
            result += char
    return result

# Columnar Transposition Cipher
def columnar_transposition_cipher(text, keyword, mode='encrypt'):
    num_columns = len(keyword)
    num_rows = len(text) // num_columns + (1 if len(text) % num_columns else 0)
    
    sorted_keyword = sorted(list(keyword))
    column_order = [sorted_keyword.index(k) for k in keyword]

    if mode == 'encrypt':
        grid = ['' for _ in range(num_rows)]
        for i, char in enumerate(text):
            grid[i % num_rows] += char

        encrypted_text = ''.join(
            ''.join([grid[row][col] for row in range(num_rows) if col < len(grid[row])]) 
            for col in column_order
        )
        return encrypted_text

    else:
        # Calculate column lengths for each column
        full_columns = len(text) % num_columns
        col_lengths = [num_rows if i < full_columns else num_rows - 1 for i in range(num_columns)]
        col_data = []
        current_index = 0

        for col_length in col_lengths:
            col_data.append(text[current_index:current_index + col_length])
            current_index += col_length

        decrypted_text = ''
        for i in range(num_rows):
            for col in column_order:
                if i < len(col_data[col]):
                    decrypted_text += col_data[col][i]
        return decrypted_text

# Atbash Cipher
def atbash_cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            shift_value = 65 if char.isupper() else 97
            result += chr(shift_value + (25 - (ord(char) - shift_value)))
        else:
            result += char
    return result

# Vernam Cipher (One-Time Pad)
def vernam_cipher(text, key, mode='encrypt'):
    if len(key) < len(text):
        print("Error: The key must be at least as long as the text for Vernam Cipher.")
        return None
    
    result = ''
    for i in range(len(text)):
        if text[i].isalpha():
            shift_value = 65 if text[i].isupper() else 97
            key_val = ord(key[i].upper()) - 65
            if mode == 'encrypt':
                result += chr((ord(text[i]) - shift_value + key_val) % 26 + shift_value)
            else:
                result += chr((ord(text[i]) - shift_value - key_val) % 26 + shift_value)
        else:
            result += text[i]
    return result

# Main function
def main():
    text = input("Enter the text to encrypt/decrypt: ")
    mode = input("Enter mode (encrypt/decrypt): ").lower()

    # Caesar Cipher
    print("\nCaesar Cipher:")
    shift = int(input("Enter the Caesar shift value: "))
    caesar_result = caesar_cipher(text, shift) if mode == 'encrypt' else caesar_cipher(text, -shift)
    print(caesar_result)

    # Vigenère Cipher
    print("\nVigenère Cipher:")
    keyword = input("Enter the keyword for Vigenère Cipher: ")
    vigenere_result = vigenere_cipher(text, keyword, mode)
    print(vigenere_result)

    # Columnar Transposition Cipher
    print("\nColumnar Transposition Cipher:")
    columnar_keyword = input("Enter the keyword for Columnar Transposition: ")
    columnar_result = columnar_transposition_cipher(text, columnar_keyword, mode)
    print(columnar_result)

    # Atbash Cipher
    print("\nAtbash Cipher:")
    atbash_result = atbash_cipher(text)
    print(atbash_result)

    # Vernam Cipher
    print("\nVernam Cipher (One-Time Pad):")
    key = input("Enter the key for Vernam Cipher: ")
    vernam_result = vernam_cipher(text, key, mode)
    if vernam_result:
        print(vernam_result)

if __name__ == "__main__":
    main()
