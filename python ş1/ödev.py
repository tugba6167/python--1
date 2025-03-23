def hesap_makinesi(sayi1, sayi2):
  """
  İki sayının toplamını, farkını, çarpımını ve bölümünü hesaplar.

  Args:
    sayi1: Birinci sayı.
    sayi2: İkinci sayı.

  Returns:
    Bir tuple olarak (toplam, fark, çarpım, bölüm) değerlerini döndürür.
  """
  toplam = sayi1 + sayi2
  fark = sayi1 - sayi2
  carpim = sayi1 * sayi2
  if sayi2 != 0:
    bolum = sayi1 / sayi2
  else:
    bolum = "Bölen sıfır olamaz"
  return toplam, fark, carpim, bolum

def palindrom_kontrol(kelime):
  """
  Bir kelimenin palindrom olup olmadığını kontrol eder.

  Args:
    kelime: Kontrol edilecek kelime.

  Returns:
    Kelime palindrom ise True, değilse False döndürür.
  """
  kelime = kelime.lower()  # Büyük/küçük harf duyarlılığını ortadan kaldır
  ters_kelime = kelime[::-1]  # Kelimeyi ters çevir
  return kelime == ters_kelime

def yuz_yas_hesapla(yas):
  """
  Kullanıcının kaç yıl sonra 100 yaşına ulaşacağını hesaplar.

  Args:
    yas: Kullanıcının yaşı.

  Returns:
    Kullanıcının 100 yaşına ulaşmasına kaç yıl kaldığını döndürür.
  """
  if yas >= 100:
    return "Zaten 100 yaşındasınız veya daha büyüksünüz."
  return 100 - yas

# Örnek Kullanım
sayi1 = 10
sayi2 = 5
toplam, fark, carpim, bolum = hesap_makinesi(sayi1, sayi2)
print(f"{sayi1} + {sayi2} = {toplam}")
print(f"{sayi1} - {sayi2} = {fark}")
print(f"{sayi1} * {sayi2} = {carpim}")
print(f"{sayi1} / {sayi2} = {bolum}")

kelime1 = "kek"
kelime2 = "masa"
print(f"{kelime1} palindrom mu? {palindrom_kontrol(kelime1)}")
print(f"{kelime2} palindrom mu? {palindrom_kontrol(kelime2)}")

yas = 30
yuz_yas = yuz_yas_hesapla(yas)
print(f"{yas} yaşındaysanız, 100 yaşına {yuz_yas} yıl sonra ulaşacaksınız.")