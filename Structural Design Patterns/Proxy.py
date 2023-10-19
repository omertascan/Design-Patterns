# Subject (Konu) arayüzü
class MathOperation:
    def add(self, a, b):
        pass

# Real Subject (Gerçek Konu)
class RealMathOperation(MathOperation):
    def add(self, a, b):
        return a + b

# Proxy (Vekil)
class MathOperationProxy(MathOperation):
    def __init__(self):
        self.real_math_operation = RealMathOperation()

    def add(self, a, b):
        print("Toplama işlemi başlatılıyor...")
        result = self.real_math_operation.add(a, b)
        print(f"{a} + {b} = {result}")
        print("Toplama işlemi tamamlandı.")

if __name__ == "__main__":
    proxy = MathOperationProxy()

    # Gerçek matematik işlemi kullanımı
    print("Gerçek matematik işlemi kullanımı:")
    real_math = RealMathOperation()
    result = real_math.add(3, 5)
    print(f"Sonuç: {result}")

    # Proxy ile matematik işlemi
    print("\nProxy kullanarak matematik işlemi:")
    proxy.add(7, 2)

