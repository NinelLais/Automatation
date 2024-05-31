def bank (X, Y):
    for i in range(1, Y+1):
        count = X+(X/10)
        X = count
    print(round(count, 4))

bank(13000, 5)