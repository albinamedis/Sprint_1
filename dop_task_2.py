def digit_root(num):
    if (num >= 10000000) or (int(num)!=num) or (num==0):
        print('Число должно быть натуральным и не должно превышать 10 000 000')
    else:
        sum=0
        kol_znakov = len(str(num))
        if kol_znakov > 1:
            for i in range(0,kol_znakov):
                sum += int(str(num)[i])

        if len(str(sum))>1:
            digit_root(sum)
        else:
            print(sum)

digit_root(4851)
digit_root(97569)
digit_root(889987)
digit_root(1)
digit_root(8.2)