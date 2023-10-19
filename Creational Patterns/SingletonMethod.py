class Singleton:
    _instance = None  # Örneğin depolanacağı özel bir değişken

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None  # Özgün özellikler burada tanımlanabilir
        return cls._instance

# Singleton sınıfından yalnızca bir örnek oluşturulur
singleton1 = Singleton()
singleton1.value = "Örnek 1 Değeri"

# İkinci bir örnek oluşturulduğunda, ilk örneğe erişilir
singleton2 = Singleton()
print(singleton2.value)  # "Örnek 1 Değeri"

# Her iki örnek aynı örneği paylaşır
print(singleton1 is singleton2)  # True
