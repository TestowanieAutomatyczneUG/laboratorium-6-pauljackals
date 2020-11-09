class Hamming:
    def distance(self, string1, string2):
        """Takes two same-length strings and counts differences
        >>> h = Hamming()
        >>> h.distance("", "")
        0
        >>> h.distance("A", "A")
        0
        >>> h.distance("G", "T")
        1
        >>> h.distance("GGACTGAAATCTG", "GGACTGAAATCTG")
        0
        >>> h.distance("GGACGGATTCTG", "AGGACGGATTCT")
        9
        >>> h.distance("AATG", "AAA")
        Traceback (most recent call last):
            File "C:\\Users\\paulj\\AppData\\Local\\Programs\\Python\\Python38\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
                h.distance("AATG", "AAA")
            File "C:/Users/paulj/PycharmProjects/stepik/laboratorium-6-pauljackals/src/ex1_doctest/ex1_doctest.py", line 19, in distance
                raise ValueError("Strands must be the same length!")
        ValueError: Strands must be the same length!
        >>> h.distance("ATA", "AGTG")
        Traceback (most recent call last):
            File "C:\\Users\\paulj\\AppData\\Local\\Programs\\Python\\Python38\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
                h.distance("ATA", "AGTG")
            File "C:/Users/paulj/PycharmProjects/stepik/laboratorium-6-pauljackals/src/ex1_doctest/ex1_doctest.py", line 19, in distance
                raise ValueError("Strands must be the same length!")
        ValueError: Strands must be the same length!
        >>> h.distance("", "G")
        Traceback (most recent call last):
            File "C:\\Users\\paulj\\AppData\\Local\\Programs\\Python\\Python38\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
                h.distance("", "G")
            File "C:/Users/paulj/PycharmProjects/stepik/laboratorium-6-pauljackals/src/ex1_doctest/ex1_doctest.py", line 19, in distance
                raise ValueError("Strands must be the same length!")
        ValueError: Strands must be the same length!
        >>> h.distance("G", "")
        Traceback (most recent call last):
            File "C:\\Users\\paulj\\AppData\\Local\\Programs\\Python\\Python38\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
                h.distance("G", "")
            File "C:/Users/paulj/PycharmProjects/stepik/laboratorium-6-pauljackals/src/ex1_doctest/ex1_doctest.py", line 19, in distance
                raise ValueError("Strands must be the same length!")
        ValueError: Strands must be the same length!
        """
        if len(string1) != len(string2):
            raise ValueError("Strands must be the same length!")
        difference = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                difference += 1
        return difference


if __name__ == "__main__":
    import doctest
    doctest.testmod()
