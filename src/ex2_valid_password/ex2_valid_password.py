class ValidPassword:
    def valid_password(self, password):
        """Takes a string and checks for required characters
        >>> vp = ValidPassword()
        >>> vp.valid_password('fEr!gr9ht')
        True
        >>> vp.valid_password('FER!GR9T')
        True
        >>> vp.valid_password('4r3ff')
        False
        >>> vp.valid_password('fer!gr9ht')
        False
        >>> vp.valid_password('fEr!grht')
        False
        >>> vp.valid_password('feRgr9ht')
        False
        >>> vp.valid_password([])
        Traceback (most recent call last):
            File "C:\\Users\\paulj\\AppData\\Local\\Programs\\Python\\Python38\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.ValidPassword.valid_password[7]>", line 1, in <module>
                vp.valid_password([])
            File "C:/Users/paulj/PycharmProjects/stepik/laboratorium-6-pauljackals/src/ex2_valid_password/ex2_valid_password.py", line 21, in valid_password
                raise ValueError('Password must be a string!')
        ValueError: Password must be a string!
        """
        if type(password) != str:
            raise ValueError('Password must be a string!')
        if len(password) < 8:
            return False
        upper = 0
        special = 0
        digit = 0
        for letter in password:
            if letter.isupper():
                upper += 1
            if letter in '!@#$%^&*(){}[]\\|:";\'<>?,./':
                special += 1
            if letter.isdigit():
                digit += 1
        if upper == 0 or special == 0 or digit == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
