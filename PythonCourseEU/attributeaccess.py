class A:
    def __init__(self) -> None:
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"