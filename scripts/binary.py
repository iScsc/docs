class Base:
    """Base class to convert decimal to binary, hexadecimal, octal and vice-versa"""

    def __init__(self, value: str, base: str) -> None:
        self.value = value
        self.base = base
        if base not in ["binary", "hexadecimal", "octal", "decimal"]:
            raise ValueError("Invalid base")

    def __str__(self) -> str:
        return f"{self.value} ({self.base})"

    def _decimal_to_binary(self) -> str:
        """Convert decimal to binary"""
        assert self.base == "decimal"
        return Base(bin(int(self.value)), "binary")

    def _binary_to_decimal(self) -> str:
        """Convert binary to decimal"""
        assert self.base == "binary"
        return Base(str(int(self.value, 2)), "decimal")

    def _decimal_to_hexadecimal(self) -> str:
        """Convert decimal to hexadecimal"""
        assert self.base == "decimal"
        return Base(hex(int(self.value)), "hexadecimal")

    def _hexadecimal_to_decimal(self) -> str:
        """Convert hexadecimal to decimal"""
        assert self.base == "hexadecimal"
        return Base(str(int(self.value, 16)), "decimal")

    def _decimal_to_octal(self) -> str:
        """Convert decimal to octal"""
        assert self.base == "decimal"
        return Base(oct(int(self.value)), "octal")

    def _octal_to_decimal(self) -> str:
        """Convert octal to decimal"""
        assert self.base == "octal"
        return Base(str(int(self.value, 8)), "decimal")

    def convert_to(self, target_base: str) -> str:
        """Convert to a different base"""
        if target_base == self.base:
            return self
        elif target_base == "decimal":
            if self.base == "binary":
                return self._binary_to_decimal()
            elif self.base == "hexadecimal":
                return self._hexadecimal_to_decimal()
            elif self.base == "octal":
                return self._octal_to_decimal()
        elif target_base == "binary":
            if self.base == "decimal":
                return self._decimal_to_binary()
            elif self.base == "octal":
                return Base._decimal_to_binary(self._octal_to_decimal())
            elif self.base == "hexadecimal":
                return Base._decimal_to_binary(self._hexadecimal_to_decimal())
        elif target_base == "hexadecimal":
            if self.base == "decimal":
                return self._decimal_to_hexadecimal()
            elif self.base == "binary":
                return Base._decimal_to_hexadecimal(self._binary_to_decimal())
            elif self.base == "octal":
                return Base._decimal_to_hexadecimal(self._octal_to_decimal())
        elif target_base == "octal":
            if self.base == "decimal":
                return self._decimal_to_octal()
            elif self.base == "binary":
                return Base._decimal_to_octal(self._binary_to_decimal())
            elif self.base == "hexadecimal":
                return Base._decimal_to_octal(self._hexadecimal_to_decimal())
        else:
            raise ValueError("Invalid target base")
        
    def pm_base(self, other: "Base", op: str = "+") -> "Base":
        """Add two bases"""
        if op == "+":
            if self.base == "decimal":
                return Base(str(int(self.value) + int(other.convert_to("decimal").value)), "decimal")
            elif self.base == "binary":
                return Base(str(int(self.value, 2) + int(other.convert_to("decimal").value)), "decimal")
            elif self.base == "hexadecimal":
                return Base(str(int(self.value, 16) + int(other.convert_to("decimal").value)), "decimal")
            elif self.base == "octal":
                return Base(str(int(self.value, 8) + int(other.convert_to("decimal").value)), "decimal")
            else:
                raise ValueError("Invalid base")
        elif op == "-":
            if self.base == "decimal":
                return Base(str(int(self.value) - int(other.convert_to("decimal").value)), "decimal")
            elif self.base == "binary":
                return Base(str(int(self.value, 2) - int(other.convert_to("decimal").value)), "decimal")
            elif self.base == "hexadecimal":
                return Base(str(int(self.value, 16) - int(other.convert_to("decimal").value)), "decimal")
            elif self.base == "octal":
                return Base(str(int(self.value, 8) - int(other.convert_to("decimal").value)), "decimal")
            else:
                raise ValueError("Invalid base")
        else:
            raise ValueError("Invalid operation")
    
    def multiply_base(self, other: "Base") -> "Base":
        """Multiply two bases"""
        if self.base == "decimal":
            return Base(str(int(self.value) * int(other.convert_to("decimal").value)), "decimal")
        elif self.base == "binary":
            return Base(str(int(self.value, 2) * int(other.convert_to("decimal").value)), "decimal")
        elif self.base == "hexadecimal":
            return Base(str(int(self.value, 16) * int(other.convert_to("decimal").value)), "decimal")
        elif self.base == "octal":
            return Base(str(int(self.value, 8) * int(other.convert_to("decimal").value)), "decimal")
        else:
            raise ValueError("Invalid base")



if __name__ == "__main__":
    a = Base("10", "decimal")
    print(a.value)
    print(a.convert_to("binary"))
    print(a.convert_to("hexadecimal"))
    print(a.convert_to("octal"))
    print(a.convert_to("decimal"))
    b = Base("1010", "binary")
    print(b.convert_to("decimal"))
    print(b.convert_to("hexadecimal"))
    print(b.convert_to("octal"))
    print(b.convert_to("binary"))
    c = Base("A", "hexadecimal")
    print(c.convert_to("decimal"))
    print(c.convert_to("binary"))
    print(c.convert_to("octal"))
    print(c.convert_to("hexadecimal"))
    d = Base("12", "octal")
    print(d.convert_to("decimal"))
    print(d.convert_to("binary"))
    print(d.convert_to("hexadecimal"))
    print(d.convert_to("octal"))
    print(a.pm_base(b))
    print(a.pm_base(c))
    print(a.pm_base(d))
    print(b.pm_base(a))
    print(b.pm_base(c))
    print(b.pm_base(d))
    print(c.pm_base(a))
    print(c.pm_base(b))
    print(c.pm_base(d))
    print(d.pm_base(a))
    print(d.pm_base(b))
    print(d.pm_base(c))
    print(a.pm_base(b,"-"))
    print(a.pm_base(c,"-"))
    print(a.pm_base(d,"-"))
