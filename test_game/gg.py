import random
from list import words
from ss import life
from ss import logo
choice = random.choice(words)
print(choice)
cho = []
lives = 10

for i in range(len(choice)):
   cho.append("_")
end = False
print(logo)
print(f'현재 목숨 {life[lives]}')
while not end:
    alp = str(input("알파벳을 입력해주세요 >>>"))
    print(logo)
    for i in range(len(choice)):
        if alp == choice[i]:
            cho[i] = alp
    print(cho)
    if alp not in choice:
        lives -= 1
        print(f'남은 목숨 {life[lives]}')
        if lives == 0:
            print(logo)
            print("Game Over")
            print(f'정답은 {' '.join(choice)}')
            end = True
    if '_' not in cho:

        print(f'정답입니다 정답은 {' '.join(choice)}')
        end = True







