class PersegiPanjang:
    """Representasi objek persegi panjang dengan ukuran panjang dan lebar."""

    def __init__(self, panjang, lebar):
        if not isinstance(panjang, (int, float)) or not isinstance(lebar, (int, float)):
            raise TypeError("Panjang dan lebar harus berupa angka (int/float).")
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih dari 0.")

        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return (
            f"Persegi Panjang: panjang = {self.panjang} cm, "
            f"lebar = {self.lebar} cm"
        )


if __name__ == "__main__":
    try:
        pp = PersegiPanjang(3, 2)
        print(pp)
        print(f"Keliling: {pp.keliling()} cm")
        print(f"Luas: {pp.luas()} cm²")

        print("\nContoh validasi error:")
        PersegiPanjang(0, 2)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")