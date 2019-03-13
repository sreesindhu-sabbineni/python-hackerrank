if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name,score])
    dictscores = dict(scores)
    onlyscores =[x for x in dictscores.values()]
    onlyscores.sort()
    print(onlyscores)
    firstmin = onlyscores[0]
    secondmin=0
    i=0
    while True:
        if onlyscores[i]==firstmin:
            i+=1
            continue
        if onlyscores[i]!=firstmin:
            secondmin = onlyscores[i]
            break
    print(secondmin)
    names = []
    for key,value in dictscores.items():
        if value==secondmin:
            names.append(key)
    names.sort()
    for i in range(len(names)):
        print(names[i])