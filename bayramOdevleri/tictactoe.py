def tahta_görüntüle(tahta):
    print(tahta[7] + '|' + tahta[8] + '|' + tahta[9])
    print('-+-+-')
    print(tahta[4] + '|' + tahta[5] + '|' + tahta[6])
    print('-+-+-')
    print(tahta[1] + '|' + tahta[2] + '|' + tahta[3])

def oyuncu_girişi():
    işaret = ''
    while not (işaret == 'X' or işaret == 'O'):
        işaret = input('Oyuncu 1: X mı yoksa O mu olmak istersiniz? ').upper()
    if işaret == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def işareti_yerleştir(tahta, işaret, pozisyon):
    tahta[pozisyon] = işaret

def kazanan_kontrol(tahta, işaret):
    return ((tahta[7] == işaret and tahta[8] == işaret and tahta[9] == işaret) or 
            (tahta[4] == işaret and tahta[5] == işaret and tahta[6] == işaret) or 
            (tahta[1] == işaret and tahta[2] == işaret and tahta[3] == işaret) or 
            (tahta[7] == işaret and tahta[4] == işaret and tahta[1] == işaret) or 
            (tahta[8] == işaret and tahta[5] == işaret and tahta[2] == işaret) or 
            (tahta[9] == işaret and tahta[6] == işaret and tahta[3] == işaret) or 
            (tahta[7] == işaret and tahta[5] == işaret and tahta[3] == işaret) or 
            (tahta[9] == işaret and tahta[5] == işaret and tahta[1] == işaret))

def boş_alan_kontrol(tahta, pozisyon):
    return tahta[pozisyon] == ' '

def tam_tahta_kontrol(tahta):
    for i in range(1, 10):
        if boş_alan_kontrol(tahta, i):
            return False
    return True

def oyuncu_seçimi(tahta):
    pozisyon = 0
    while pozisyon not in range(1, 10) or not boş_alan_kontrol(tahta, pozisyon):
        pozisyon = int(input('Sıradaki hamlenizi seçin: (1-9) '))
    return pozisyon

def tekrar_oyna():
    return input('Tekrar oynamak istiyor musunuz? Evet veya Hayır girin: ').lower().startswith('e')

print('Tic Tac Toe\'ya Hoşgeldiniz!')

while True:
    tahta = [' '] * 10
    oyuncu1_işareti, oyuncu2_işareti = oyuncu_girişi()
    sıra = 'Oyuncu 1'
    oyun_durumu = True

    while oyun_durumu:
        if sıra == 'Oyuncu 1':
            tahta_görüntüle(tahta)
            pozisyon = oyuncu_seçimi(tahta)
            işareti_yerleştir(tahta, oyuncu1_işareti, pozisyon)

            if kazanan_kontrol(tahta, oyuncu1_işareti):
                tahta_görüntüle(tahta)
                print('Tebrikler! Oyunu kazandınız!')
                oyun_durumu = False
            else:
                if tam_tahta_kontrol(tahta):
                    tahta_görüntüle(tahta)
                    print('Oyun berabere!')
                    break
                else:
                    sıra = 'Oyuncu 2'

        else:
            tahta_görüntüle(tahta)
            pozisyon = oyuncu_seçimi(tahta)
            işareti_yerleştir(tahta, oyuncu2_işareti, pozisyon)

            if kazanan_kontrol(tahta, oyuncu2_işareti):
                tahta_görüntüle(tahta)
                print('Oyuncu 2 kazandı!')
                oyun_durumu = False
            else:
                if tam_tahta_kontrol(tahta):
                    tahta_görüntüle(tahta)
                    print('Oyun berabere!')
                    break
                else:
                    sıra = 'Oyuncu 1'

    if not tekrar_oyna():
        break















