while True:

    tc_kimlik_no = input("TC Kimlik Numaranizi Giriniz: ")

    if str(tc_kimlik_no).startswith('0'):
        print("TC Kimlik No 0 ile baslayamaz!")
    elif not tc_kimlik_no.isdigit():
        print("Hatali giris.TC kimlik no sadece ramaklardan olusmalidir!")
    elif len(tc_kimlik_no) < 11:
        print("TC Kimlik No 11 haneden az olamaz!")
    elif len(tc_kimlik_no) > 11:
        print("TC Kimlik No 11 haneden fazla olamaz!")
    else:
        number = str(int(tc_kimlik_no[0:9]) - 29999)
        toplam = sum(int(number[i]) for i in range(0, 9, 2))
        toplam_2 = sum(int(number[i]) for i in range(1, 9, 2))
        hane_10 = (toplam * 7 - toplam_2) % 10
        hane_11 = (toplam + toplam_2 + hane_10) % 10
        print(f"Sizden bir onceki kisinin TC kimlik numarasi : {number + str(hane_10) + str(hane_11)}")
        number_2 = str(int(tc_kimlik_no[0:9]) - 29999)
        toplam_3 = sum(int(number_2[i]) for i in range(0, 9, 2))
        toplam_4 = sum(int(number_2[i]) for i in range(1, 9, 2))
        hane_10_2 = (toplam_3 * 7 - toplam_4) % 10
        hane_11_2 = (toplam_3 + toplam_4 + hane_10_2) % 10
        print(f"Sziden bir sonraki kisinin TC kimlik numnarasi : {number_2 + str(hane_10_2) + str(hane_11_2)}")
        break
