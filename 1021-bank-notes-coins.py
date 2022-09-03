N, C = input().split('.')
N, C = int(N), int(C)

NoteList = ['100', '50', '20', '10', '5', '2']
CoinList = ['1.00', '0.50', '0.25', '0.10', '0.05', '0.01']
REMAIN = N + (C/100)

print('NOTAS:')

for NOTES in NoteList:
    NOTES = int(NOTES)
    NoteCount = int((REMAIN - (REMAIN % NOTES))/NOTES)
    RES = f"{NoteCount} nota(s) de R$ {NOTES:.2f}"
    print(RES)
    REMAIN = REMAIN - (NoteCount * NOTES)

print('MOEDAS:')
for COINS in CoinList:
    COINS = float(COINS)
    NoteCount = int((REMAIN - (REMAIN % COINS))/COINS)
    RES = f"{NoteCount} moeda(s) de R$ {COINS:.2f}"
    REMAIN = REMAIN - (NoteCount * COINS)
    print(RES)
