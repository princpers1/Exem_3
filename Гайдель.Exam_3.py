# Напишите функцию, которая запрашивает у пользователя номер карты, CVC-код и PIN-код.
# После этого выводит на экран номер карты с первыми четырьмя цифрами,
# остальные заменены на звездочки, CVC-код в виде ###,
# # и PIN-код в виде &&&0 (вместо 0 последняя цифра).
def kard(numer_card,cvc,pin):
    print(f"Ваша карта:{numer_card[:4]}{'*' * (len(numer_card)-4)}")
    print(f"CVC:{'#'*len(cvc)}")
    print(f"pin:{'&'*(len(pin)-1)}{pin[-1]}")
kard(numer_card=input("Введите номер карты:"), cvc=input("Введите CVC-код:"), pin=input("Введите PIN-код:"))