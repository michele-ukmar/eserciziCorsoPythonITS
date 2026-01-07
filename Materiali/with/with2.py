from decimal import Decimal, localcontext

with localcontext() as ctx:
     ctx.prec = 42
     print(Decimal("1") / Decimal("42"))

# Decimal('0.0238095238095238095238095238095238095238095')

print(Decimal("1") / Decimal("42"))
# Decimal('0.02380952380952380952380952381')