import Utilities

finder = Utilities.PrimeFinder(7500)

assert finder.IsPrime(7)
assert finder.IsPrime(23)
assert finder.IsPrime(1987)
assert finder.IsPrime(7993)
assert not finder.IsPrime(1)
assert not finder.IsPrime(49)
assert not finder.IsPrime(3599)
