def cricketScore(case):
    print("Case ",case,":",sep=" ")
    score = [0,0]
    current_players = [1, 2]
    onStrike = 0
    n,p = map(int,input().split())
    players = ['DNB' for i in range(p)]
    runs = input()
    
    for i in range(6*n):
        temp = runs[i]
        if temp == '0':
            pass
        elif temp == '1':
            score[onStrike] += 1
            onStrike = (onStrike+1)%2
        elif temp == '3':
            score[onStrike] += 3
            onStrike = (onStrike+1)%2
        elif temp == '2':
            score[onStrike] += 2
        elif temp == '4':
            score[onStrike] += 4
        elif temp == '6':
            score[onStrike] += 6
        elif temp == 'W':
            players[current_players[onStrike]-1] = str(score[onStrike])
            current_players[onStrike] = max(current_players)+1
            score[onStrike] = 0
        if(i%6==5):
            onStrike = (onStrike+1)%2
    players[current_players[0]-1] = str(score[0])+"*"
    players[current_players[1]-1] = str(score[1])+"*"
    for i in range(p):
        print("Batsman ",(i+1),": ",players[i],sep="")

cricketScore(10);

