import time
import os


def geri_sayim(saniye):
    """
    Belirtilen saniye kadar geri sayım yapar
    """
    while saniye > 0:
        # Dakika ve saniye hesapla
        dakika = saniye // 60
        san = saniye % 60

        # Ekranı temizle (Windows için 'cls', Linux/Mac için 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')

        # Geri sayımı göster
        print(f"⏰ Geri Sayım: {dakika:02d}:{san:02d}")
        print("─" * 25)

        # 1 saniye bekle
        time.sleep(1)
        saniye -= 1

    # Süre dolduğunda
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🎉 SÜRE DOLDU! 🎉")
    print("─" * 20)


def ana_program():
    """
    Ana program - kullanıcıdan süre alır ve geri sayımı başlatır
    """
    try:
        print("🕐 GERİ SAYIM SAYACI 🕐")
        print("─" * 30)

        # Kullanıcıdan süre al
        dakika = int(input("Dakika giriniz: "))
        saniye = int(input("Saniye giriniz: "))

        # Toplam saniyeyi hesapla
        toplam_saniye = (dakika * 60) + saniye

        if toplam_saniye <= 0:
            print("❌ Lütfen geçerli bir süre giriniz!")
            return

        print(f"\n✅ {dakika} dakika {saniye} saniye geri sayım başlıyor...")
        time.sleep(2)  # 2 saniye bekle

        # Geri sayımı başlat
        geri_sayim(toplam_saniye)

    except ValueError:
        print("❌ Lütfen sadece sayı giriniz!")
    except KeyboardInterrupt:
        print("\n\n⚠️ Program durduruldu!")


# Alternatif: Hızlı kullanım fonksiyonu
def hizli_geri_sayim(saniye):
    """
    Sadece saniye ile hızlı geri sayım
    """
    print(f"⏰ {saniye} saniye geri sayım başlıyor...\n")

    for i in range(saniye, 0, -1):
        print(f"⏳ {i}", end=" ", flush=True)
        time.sleep(1)

    print("\n\n🎉 Bitti! 🎉")


if __name__ == "__main__":
    # Ana programı çalıştır
    ana_program()

    # Örnek kullanım:
    # hizli_geri_sayim(10)  # 10 saniye hızlı geri sayım