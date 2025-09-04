import random

word_list = ['apple' , 'banana' , 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
#todo - 1 : 비어있는 list인 display를 만드시오.
display = []
#todo - 2: 이상의 코드라인을 참조하여 chosen_word의 각 문자 개수 마다 '_'를 추가하시오. 예를 들어 chosen_word == 'apple'이라면 display [ "_","_","_","_","_"]이 되어야 한다. 즉 , chosen_word의 문자 개수 만큼 "_"가 있어야 한다
for letter in range(len(chosen_word)):
    display.append("_")
# todo - 3: chosen-word의 각 문자들을 반복시키세요. 만약 그 위치의 문자가 guess와 일치하면, 해당 위치의 display에서 문자를 공개하시오. 예를 들어 사용자가 'p'를 입력했고, chosen_word가 apple이라면 display = ["_", "p","p","_","_"]로 바뀌어야 한다
guess = input('알파벳 하나를  입력하세요 >>>').lower()
for letter in range(len(chosen_word)):
    if chosen_word[letter] == guess:
        display[letter] = guess
print(display)
