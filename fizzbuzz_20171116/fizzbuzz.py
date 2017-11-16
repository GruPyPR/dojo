def fizzbuzz(numero):
    result = FizzBuzzInt(numero)
    return result.to_fizzbuzz()

class FizzBuzzInt(int):
    def is_multiple(self, d: int) -> bool:
        return self % d == 0

    def to_fizzbuzz(self):
        if self.is_multiple(15):
            return 'fizzbuzz'
        if self.is_multiple(3):
            return 'fizz'
        if self.is_multiple(5):
            return 'buzz'
 
        return int(self)

    def __repr__(self):
        return repr(self.to_fizzbuzz())
