import palindrom as pd

palindroms = ["Eine güldne, gute Tugend: Lüge nie!",
              "Kobyła ma mały bok.", "oko", "rotor", "kajak"]
non_palindroms = ["Hello", "python",
                  "Another one bites the dust", "LKDS;; ąśśćalsdkf"]

if __name__ == '__main__':
    for x in palindroms + non_palindroms:
        print(x, pd.Palindrom.is_palindrom(x))
