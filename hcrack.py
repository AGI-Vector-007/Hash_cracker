
# -*- coding: utf-8 -*-
import argparse
import hashlib
import colorama
import time
import threading
import sys
from colorama import Fore, Style

colorama.init(autoreset=True)

def detect_hash_type(hash_value):
    hash_types = {
        32: "md5",
        40: "sha1",
        56: "sha224",
        64: "sha256",
        96: "sha384",
        128: "sha512"
    }
    return hash_types.get(len(hash_value), None)

def hash_password(password, hash_type):
    hash_func = getattr(hashlib, hash_type, None)
    if hash_func:
        return hash_func(password.encode()).hexdigest()
    return None

loading_done = False

def loading_animation():
    global loading_done
    spinner = ["|", "/", "-", "\\"]
    i = 0
    start_time = time.time()
    
    while not loading_done or time.time() - start_time < 3:
        sys.stdout.write("\r" + Fore.CYAN + f"Cracking hash... {spinner[i % len(spinner)]} " + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    sys.stdout.write("\r" + " " * 30 + "\r") 
    sys.stdout.flush()

def crack_hash(hash_value, wordlist_path):
    global loading_done
    hash_type = detect_hash_type(hash_value)
    
    if not hash_type:
        print(Fore.RED + "Unknown hash type!")
        return

    print(Fore.YELLOW + f"Detected Hash Type: {hash_type.upper()}")

    loading_done = False
    loader = threading.Thread(target=loading_animation)
    loader.start()

    try:
        with open(wordlist_path, "r", encoding="utf-8") as file:
            for word in file:
                word = word.strip()
                hashed_word = hash_password(word, hash_type)
                
                if hashed_word == hash_value:
                    loading_done = True
                    loader.join()  
                    print(Fore.GREEN + f"Match Found! Password: {word}")
                    return
                
        loading_done = True
        loader.join()
        print(Fore.RED + "Matching failed.")
    
    except FileNotFoundError:
        loading_done = True
        loader.join()
        print(Fore.RED + "Wordlist file not found!")

def main():
    parser = argparse.ArgumentParser(description="Hash Cracker CLI Tool")
    parser.add_argument("hash", help="The hash to crack")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    
    args = parser.parse_args()
    crack_hash(args.hash, args.wordlist)

if __name__ == "__main__":
    main()
