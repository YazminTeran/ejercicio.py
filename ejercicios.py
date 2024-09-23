#Escribir una clase en python llamada rectángulo que contenga una basey una altura, y que contenga un método que devuelva el área del rectángulo

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura


rectangulo = Rectangulo(5, 10)

print(f"El área del rectángulo es: {rectangulo.calcular_area()}")  

#Escribir una clase en python que convierta un número entero a número romano

class IntToRomanConverter:
    def __init__(self):
        
        self.int_to_roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    
    def int_to_roman(self, num):
        result = ""
        for value, symbol in self.int_to_roman_map:
            while num >= value:
                result += symbol
                num -= value
        return result


converter = IntToRomanConverter()


print(f"en numero romanos es:{converter.int_to_roman(1987)}") 



