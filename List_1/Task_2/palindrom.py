from string import punctuation


class Palindrom():
    @classmethod
    def is_palindrom(cls, string: str) -> bool:
        """Checks if given string is an palindrom. 
           During check all whitespace and punctuation characters are stripped,
           string is also converted to lowercase"""
        raw_string = "".join(string.lower().split()).translate(
            str.maketrans('', '', punctuation))
        return raw_string == raw_string[::-1]
