def simpledice():
    from random import randint
    n = True
    while n:
        r = []
        print('-='*20)
        d = int(input('Quantos dados quer jogar: '))
        l = int(input('Quer dados de quantos lados: '))
        for i in range(1,d+1):
           r.append(randint(1,l))
        print(r)
        while True:
            n1 = input('Quer jogar novamente? [S/N] ').strip().upper()[0]
            if n1 in 'SsnN':
                break
        if n1 == 'N':
            n = False
    print('-='*20)
    print('Obrigado por jogar')
simpledice()
