import random
logo = '''
┓       ┳┳┓    
┣┓┏┓┏┓┏┓┃┃┃┏┓┏┓
┛┗┗┻┛┗┗┫┛ ┗┗┻┛┗
       ┛                                                  
'''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
word_list = ["achieve", "acquire", "adequate", "adjust", "admire", "admit", "advantage", "affect", "afford", "agency", "allow", "amount", "ancient", "announce", "anxiety", "apologize", "apparent", "approach", "argue", "artificial", "associate", "attitude", "available", "avoid", "aware",
    "behavior", "benefit", "beyond", "budget",
    "candidate", "capacity", "career", "challenge", "character", "circumstance", "civilization", "climate", "collapse", "commercial", "commit", "communicate", "community", "company", "compare", "complex", "concern", "conclude", "condition", "conduct", "conference", "conflict", "connect", "consider", "constant", "construct", "consume", "contain", "contrast", "contribute", "convenient", "convert", "convince", "cooperate", "corporate", "counselor", "courage", "critical", "culture",
    "damage", "decrease", "define", "demand", "demonstrate", "depend", "describe", "design", "despite", "determine", "develop", "devise", "difficult", "direction", "disadvantage", "discuss", "distant", "distinguish", "distribute", "diverse",
    "economic", "economy", "effective", "effort", "eliminate", "emotional", "employee", "enable", "encourage", "engage", "entire", "environment", "especially", "essential", "establish", "estimate", "evidence", "evolve", "exceed", "excellent", "exchange", "exist", "expect", "expensive", "experience", "explain", "explore", "expose", "express", "extend",
    "familiar", "fantastic", "feature", "finance", "firm", "flexible", "force", "foreign", "frequent", "fulfill", "function",
    "generation", "global", "graduate", "growth",
    "historical", "however",
    "identity", "imagine", "immediate", "impact", "implement", "imply", "impress", "incident", "income", "increase", "indicate", "individual", "industry", "influence", "initial", "innocent", "innovate", "input", "instead", "institution", "instruction", "insurance", "intend", "interpret", "interview", "investigate", "involve", "issue",
    "journal", "judge", "knowledge", "major", "manage", "material", "measure", "mention", "mindset", "negative", "negotiate", "obtain", "occasionally", "opportunity", "organization", "original", "perform", "personal", "persuade", "potential", "practical", "predict", "preference", "pressure", "previous", "primary", "private", "process", "produce", "profession", "progress", "promote", "proper", "propose", "protect", "provide", "purchase", "quality", "rather", "recognize", "recover", "reduce", "regard", "region", "relate", "release", "relevant", "rely", "require", "research", "responsible", "reveal", "satisfy", "secure", "select", "significant", "similar", "society", "solution", "source", "specific", "strength", "structure", "sufficient", "suggest", "support", "technology", "tendency", "theory", "threat", "though", "traditional", "transfer", "transform", "ultimate", "understand", "unique", "variety", "various", "violence", "visible", "volunteer", "whereas", "whatever"]
chosen_word = random.choice(word_list)
display = []

for letter in range(len(chosen_word)):
    display.append("_")
end_of_game = False
print(logo)
while not end_of_game:
    print(stages[lives])
    print(' '.join(display))
    print(f'남은 목숨 {lives}')
    guess = input('알파벳을 입력하세요 >>>').lower()
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives}번 남았습니다.')
        if lives == 0:
            print(logo)
            print('모든 기회를 잃었습니다.')
            end_of_game = True
            print(f'정답은{chosen_word}입니다.')
    if '_' not in display:
        print('정답입니다.')
        end_of_game = True
        print(f'정답은{chosen_word}입니다.')
        break