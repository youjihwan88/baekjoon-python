from decimal import Decimal

a, b, c = map(int, input().split())
print(f"{Decimal(a) * Decimal(b) / Decimal(c):.10f}")
