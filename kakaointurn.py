def taxiDriver(pickup, drop, tip):
    answer = []

    for i in range(len(pickup)-1):
        income = []
        income.append(drop[i]-pickup[i]+tip[i])

        if pickup[i+1] < drop[i]:
            pass
        elif pickup[i+1] >= drop[i]:
            income.append(drop[i]-pickup[i]+tip[i])
            print(income)


print(taxiDriver([0, 2, 9, 10, 11, 12], [
      5, 9, 11, 11, 14, 17], [1, 2, 3, 2, 2, 1]))
