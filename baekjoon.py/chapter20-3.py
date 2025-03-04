N = int(input())
danceCharacter = {"ChongChong"}

for _ in range(N):
    A, B = input().split()

    if A in danceCharacter:
        danceCharacter.add(B)
    if B in danceCharacter:
        danceCharacter.add(A)
    
print(len(danceCharacter))