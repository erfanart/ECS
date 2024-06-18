import os,sys
import json
import base64
import sqlite3
from Crypto.Cipher import AES
import shutil

def get_encryption_key(local_state_path):
    with open(local_state_path, 'r', encoding='utf-8') as file:
        local_state = json.loads(file.read())
    encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
    encrypted_key = encrypted_key[5:]  # Remove "DPAPI" prefix
    return encrypted_key

def decrypt_password(encrypted_password, key):
    try:
        iv = encrypted_password[3:15]
        encrypted_password = encrypted_password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_password = cipher.decrypt(encrypted_password)[:-16].decode()
        return decrypted_password
    except Exception as e:
        print(f"Failed to decrypt password: {e}")
        return ""

def main(local_state_path,login_data_path):

    if not os.path.exists(local_state_path) or not os.path.exists(login_data_path):
        print("Make sure you have both 'Local State' and 'Login Data' files in the script directory.")
        return

    key = get_encryption_key(local_state_path)

    shutil.copy2(login_data_path, "Login Data.db")  # Copy the database to avoid locking issues

    conn = sqlite3.connect("Login Data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    
    for row in cursor.fetchall():
        origin_url = row[0]
        username = row[1]
        encrypted_password = row[2]
        decrypted_password = decrypt_password(encrypted_password, key)
        print(f"Origin URL: {origin_url}")
        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
        print("="*50)
    
    cursor.close()
    conn.close()
    os.remove("Login Data.db")

if __name__ == "__main__":
    login_data_path = sys.argv[2]
    local_state_path = sys.argv[1]
    main(local_state_path,login_data_path)
