import random
listword = []
with open("Example1.txt", "r") as file1:
  for n in file1:
    a = n.rstrip()
    listword.append(a[7:])
word = random.choice(listword)
len_word = len(word)
guessword = '.'
for n in range (1,len_word):
  guessword += "."
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','s','y','z']
guess = 0
availableguess = 0
listword = list(word)
difficulty = 0
f = input("Chooose your difficulty(easy, normal, hard, impossible)")
if f == 'easy': difficulty = 15
elif f == 'normal': difficulty = 10
elif f == 'hard': difficulty = 5
elif f == 'impossible': difficulty = 1
print(f"You get {difficulty} times to guess the word!")
while availableguess < difficulty + 1:
  print(guessword)
  if guessword == word:
    print("WIN!")
    break
  guess = input("Please guess?: ")  
  while guess not in alphabet:
    print("Please insert valid value")
    guess = input("Please guess?: ")
  statement = word.find(guess)
  if statement == -1:
    availableguess += 1
    ava = difficulty - availableguess
    print("WRONG!")
    print(f"You have {ava} chance left")
    statement = 0
  else:
    print("CORRECT!")
    for m in range (0,len(listword)):
      if listword[m] == guess:
        listguess = list(guessword)
        listguess[m] = guess
        guessword = "".join(listguess)
print(word)
