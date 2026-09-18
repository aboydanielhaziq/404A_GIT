def add_tax(price,tax_rate=0.1):
    return int(price + price * tax_rate)

print("test")

if __name__ == "__main__":
    assert add_tax(1000) == 1100
    assert add_tax(1000,0.08) == 1080
    print("test")