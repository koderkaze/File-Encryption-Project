import os
from cryptography.fernet import Fernet
from os.path import exists
import time

decide = input("Would you like to 1) encrypt or 2) decrypt a file? Specify which number: ")


        

    
def create_key():
    """Generate a new encryption key and save it to a file."""
    if os.path.exists("\FileEncryptionProject\encryption_key.key") == False:
        key = Fernet.generate_key()
        with open("encryption_key.key", "wb") as key_file:
            key_file.write(key)    
    else:
        key = load_key
        
def load_key():
    """Load the encryption key from a file."""
    return open("encryption_key.key", "rb").read()

def encrypt_file(filename, key):
    """Encrypt a file."""
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt_file(encrypted_filename, key):
    """Decrypt an encrypted file."""
    fernet = Fernet(key)
    with open(encrypted_filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(encrypted_filename[:-4], "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)


def main():
    current_time = time.time()
    delete_time_stamp = current_time - (90 * 24 * 60 * 60)

    if os.path.getmtime("encryption_key.key") < delete_time_stamp:

     #Automatic expiry
      os.remove("encryption_key.key")
      
    if decide == "1":
        if os.path.exists("encryption_key.key") == False:
            
            create_key()
      
        key = load_key()
        filename = input("What is the path of the file you are encrypting? ")
        if os.path.exists(filename):
            encrypt_file(filename, key)
            print("File encrypted successfully.")
        else:
            print("File not found.")
   
    
    elif decide == "2":
         key = load_key() 
         encrypted_filename = input("What is the path of the file you are decrypting? ")
         if os.path.exists(encrypted_filename):
            decrypt_file(encrypted_filename, key)
            print("File decrypted successfully.")
         else:
            print("Encrypted file not found.")
    
     
     
    
    else :
        print("Invalid input! Please enter '1' for encryption or '2' for decryption.")
    
if __name__ == "__main__":
    main()
