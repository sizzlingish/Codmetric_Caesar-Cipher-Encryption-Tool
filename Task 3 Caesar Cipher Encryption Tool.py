import os

MAX_LENGTH = 500

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char)-start+shift)%26+start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def display_menu():
    print("\n"+"="*60)
    print("        🔐  CAESAR CIPHER ENCRYPTION TOOL")
    print("="*60)

    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Brute Force Decryption")
    print("4. Learn About Caesar Cipher")
    print("5. Exit")

def learn_about():
    print("\n"+"="*60)
    print("ABOUT CAESAR CIPHER".center(60))
    print("="*60)
    print("""The Caesar Cipher is one of the oldest encryption techniques.

It works by shifting each alphabet letter by a fixed number.

Example:
HELLO -> KHOOR (Shift = 3)

Encryption: Letter + Shift
Decryption: Letter - Shift

Numbers, spaces and punctuation remain unchanged.

Why is it insecure?
  • Only 25 possible keys exist.
  • An attacker can try every key in seconds.
  • This is known as a brute-force attack.

Modern encryption algorithms are significantly more secure.
""")
    print("="*60)
    input("Press Enter to continue...")

def get_text():
    while True:
        print("\n1. Enter text manually")
        print("2. Read text from file")
        c=input("Choose option: ").strip()
        if c=="1":
            t=input("Enter text: ").strip()
            if not t:
                print("❌ Text cannot be empty."); continue
            if len(t)>MAX_LENGTH:
                print("❌ Maximum 500 characters."); continue
            return t
        elif c=="2":
            f=input("Filename: ").strip()
            if not f:
                print("❌ Empty filename."); continue
            if not os.path.exists(f):
                print("❌ File not found."); continue
            try:
                txt=open(f,encoding="utf-8").read()
                if not txt.strip():
                    print("❌ File is empty."); continue
                if len(txt)>MAX_LENGTH:
                    print("❌ File exceeds 500 characters."); continue
                return txt
            except PermissionError:
                print("❌ Permission denied.")
            except Exception:
                print("❌ Unable to read file.")
        else:
            print("❌ Invalid choice.")

def get_shift():
    while True:
        try:
            s=int(input("Enter shift (1-25): "))
            if 1<=s<=25: return s
        except ValueError:
            pass
        print("❌ Invalid shift.")

def display_result(title, original, result, shift):
    print("\n"+"="*60)
    print(title.center(60))
    print("="*60)
    print(f"Operation   : {title}")
    print(f"Shift Value : {shift}")
    print("\nOriginal Text\n"+original)
    print("\nResult\n"+result)
    print(f"\nCharacters  : {len(original)}")
    print(f"Letters     : {sum(c.isalpha() for c in original)}")
    print("\nFormula Used")
    print("Encrypted = Letter + Shift" if "ENCRYPT" in title else "Decrypted = Letter - Shift")
    print("="*60)

def brute_force(text):
    print("\n"+"="*60)
    print("BRUTE FORCE RESULTS".center(60))
    print("="*60)
    print("\nCipher Text\n"+text)
    print("\nTrying All Possible Shifts\n")

    # A simple heuristic to guess the "most likely" correct shift:
    # score each candidate by how many common English words it contains.
    common_words = {
        "the","and","is","was","to","of","a","in","it","you","that",
        "he","she","we","they","for","on","are","with","as","this",
        "have","hello","world"
    }

    best_shift = 1
    best_score = -1
    results = []
    for shift in range(1, 26):
        candidate = decrypt(text, shift)
        results.append((shift, candidate))
        words = candidate.lower().split()
        score = sum(1 for w in words if w.strip(".,!?;:\"'") in common_words)
        if score > best_score:
            best_score = score
            best_shift = shift

    for shift, candidate in results:
        marker = "  <-- Most Likely" if shift == best_shift else ""
        print(f"Shift {shift:>2} : {candidate}{marker}")

    print("\n"+"="*60)
    print("\nTip:")
    print("Look for readable English text to identify the correct shift.")
    print("="*60)
    return results, best_shift

def save_to_file(text):
    while True:
        c=input("Save output to file? (Y/N): ").strip().lower()
        if c in ("n","no"): return
        if c in ("y","yes"):
            f=input("Filename: ").strip()
            if not f:
                print("❌ Empty filename."); continue
            try:
                open(f,"w",encoding="utf-8").write(text)
                print("✅ Saved successfully.")
                return
            except Exception as e:
                print("❌",e)
        else:
            print("Please enter Y or N.")

def post_menu():
    while True:
        print("\n1. Another Operation")
        print("2. Main Menu")
        print("3. Exit")
        c=input("Choice: ")
        if c=="1": return
        if c=="2": return
        if c=="3":
            print("="*60)
            print("Thank you for using Caesar Cipher Tool!")
            print("Goodbye!")
            print("="*60)
            raise SystemExit
        print("❌ Invalid choice.")

def main():
    while True:
        display_menu()
        ch=input("Enter your choice: ")
        if ch=="1":
            t=get_text(); s=get_shift()
            r=encrypt(t,s)
            display_result("ENCRYPTION RESULT",t,r,s)
            print("✅ Encryption completed successfully.")
            save_to_file(r)
            input("Press Enter to continue...")
        elif ch=="2":
            t=get_text(); s=get_shift()
            r=decrypt(t,s)
            display_result("DECRYPTION RESULT",t,r,s)
            print("✅ Decryption completed successfully.")
            save_to_file(r)
            input("Press Enter to continue...")
        elif ch=="3":
            t=get_text()
            results, best_shift = brute_force(t)
            print(f"\n✅ Brute force completed. Best guess: Shift {best_shift}.")
            c=input("Save the best guess result to file? (Y/N): ").strip().lower()
            if c in ("y","yes"):
                best_text = dict(results)[best_shift]
                save_to_file(best_text)
            input("Press Enter to continue...")
        elif ch=="4":
            learn_about()
        elif ch=="5":
            print("="*60)
            print("Thank you for using Caesar Cipher Tool!")
            print("Goodbye!")
            print("="*60)
            break
        else:
            print("❌ Invalid choice.")

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")