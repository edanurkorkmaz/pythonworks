def tahta_görüntüle(tahta):
    print(tahta[7] + '|' + tahta[8] + '|' + tahta[9])
    print('-+-+-')
    print(tahta[4] + '|' + tahta[5] + '|' + tahta[6])
    print('-+-+-')
    print(tahta[1] + '|' + tahta[2] + '|' + tahta[3])

def oyuncu_girişi():
    işaret = ''
    while işaret not in ('X', 'O'):
        try:
            işaret = input('Oyuncu 1: X mi yoksa O mu olmak istersiniz? ').upper()
            if işaret not in ('X', 'O'):
                raise ValueError('Yanlış giriş, lütfen "X" veya "O" seçin.')
        except ValueError as e:
            print(e)
    return ('X', 'O') if işaret == 'X' else ('O', 'X')

def işareti_yerleştir(tahta, işaret, pozisyon):
    tahta[pozisyon] = işaret

def kazanan_kontrol(tahta, işaret):
    return (
        (tahta[7] == işaret and tahta[8] == işaret and tahta[9] == işaret) or
        (tahta[4] == işaret and tahta[5] == işaret and tahta[6] == işaret) or
        (tahta[1] == işaret and tahta[2] == işaret and tahta[3] == işaret) or
        (tahta[7] == işaret and tahta[4] == işaret and tahta[1] == işaret) or
        (tahta[8] == işaret and tahta[5] == işaret and tahta[2] == işaret) or
        (tahta[9] == işaret and tahta[6] == işaret and tahta[3] == işaret) or
        (tahta[7] == işaret and tahta[5] == işaret and tahta[3] == işaret) or
        (tahta[9] == işaret and tahta[5] == işaret and tahta[1] == işaret)
    )

def boş_alan_kontrol(tahta, pozisyon):
    return tahta[pozisyon] == ' '

def tam_tahta_kontrol(tahta):
    return all(not boş_alan_kontrol(tahta, i) for i in range(1, 10))

def oyuncu_seçimi(tahta):
    while True:
        try:
            pozisyon = int(input('Sıradaki hamlenizi seçin: (1-9) '))
            if pozisyon not in range(1, 10):
                raise ValueError('Lütfen 1 ile 9 arasında bir sayı girin.')
            if not boş_alan_kontrol(tahta, pozisyon):
                raise ValueError('Bu pozisyon zaten dolu, başka birini seçin.')
            return pozisyon
        except ValueError as e:
            print(f'Hata: {e}')

def tekrar_oyna():
    while True:
        try:
            cevap = input('Tekrar oynamak istiyor musunuz? Evet veya Hayır girin: ').lower()
            if cevap not in ('evet', 'hayır'):
                raise ValueError('Yanlış giriş, lütfen "evet" veya "hayır" girin.')
            return cevap.startswith('e')
        except ValueError as e:
            print(e)

print("Tic Tac Toe'ya Hoşgeldiniz!")

while True:
    tahta = [' '] * 10
    oyuncu1_işareti, oyuncu2_işareti = oyuncu_girişi()
    sıra = 'Oyuncu 1'
    oyun_durumu = True

    while oyun_durumu:
        tahta_görüntüle(tahta)

        if sıra == 'Oyuncu 1':
            pozisyon = oyuncu_seçimi(tahta)
            işareti_yerleştir(tahta, oyuncu1_işareti, pozisyon)

            if kazanan_kontrol(tahta, oyuncu1_işareti):
                tahta_görüntüle(tahta)
                print("Tebrikler! Oyunu kazandınız!")
                oyun_durumu = False
            elif tam_tahta_kontrol(tahta):
                tahta_görüntüle(tahta)
                print("Oyun berabere!")
                break
            else:
                sıra = 'Oyuncu 2'

        else:
            pozisyon = oyuncu_seçimi(tahta)
            işareti_yerleştir(tahta, oyuncu2_işareti, pozisyon)

            if kazanan_kontrol(tahta, oyuncu2_işareti):
                tahta_görüntüle(tahta)
                print("Oyuncu 2 kazandı!")
                oyun_durumu = False
            elif tam_tahta_kontrol(tahta):
                tahta_görüntüle(tahta)
                print("Oyun berabere!")
                break
            else:
                sıra = 'Oyuncu 1'

    if not tekrar_oyna():
        break















