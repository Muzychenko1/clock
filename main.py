class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be an integer")
        self.__seconds = seconds % self.__DAY

    def get_time(self):
        s = self.__seconds % 60
        m = (self.__seconds // 60) % 60
        h = (self.__seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Right side must be an integer")

        sc = other
        if isinstance(other, Clock):
            sc = other.__seconds

        return Clock(self.__seconds + sc)


c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(3000)
c4 = c1 + c2 + c3
print(c1.get_time())
print(c2.get_time())
print(c3.get_time())
print(c4.get_time())