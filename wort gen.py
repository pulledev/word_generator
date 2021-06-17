import random, os, sys






y = 0

kons = ["n","n","n","n","n","n","n","n","n","n","n","n","n","n","n","n","n","n","n","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","r","r","r","r","r","r","r","r","r","r","r","r","r","r","t","t","t","t","t","t","t","t","t","t","t","t","d","d","d","d","d","d","d","d","d","d","h","h","h","h","h","h","h","h","h","l","l","l","l","l","l","l","l","l","c","c","c","c","c","c","g","g","g","g","g","g","m","m","m","m","m","b","b","b","w","w","w","f","f","f","k","k","z","z"]
vokale = ["u","u","u","u","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","i","i","i","i","i","i","i","i","i","i","i","i","i","i","i","a","a","a","a","a","a","a","a","a","a","a","a","a","o","o","o","o","o",]
anfang = ["d","d","d","d","d","d","d","s","s","s","s","s","s","s","s","s","s","e","e","e","e","i","i","i","i","w","w","w","w"]

anzahlwords = int(input('number of words: '))

words = set()
while y < anzahlwords:
    wortlaengeW = [2,2, 2, 2, 2, 2, 2, 3, 3]
    wortlaenge = random.randint(0, 8)

    x = 0
    wort = []
    while x < wortlaengeW[wortlaenge]:
        konszahl = random.randint(0, len(kons) - 1)

        wort += kons[konszahl]
        vokalezahl = random.randint(0, len(vokale) - 1)

        wort += vokale[vokalezahl]
        x = x + 1

    string = ""
    for char in wort:
        string += char
    y = y+1
    words.add(string)

while True:
  export_path = input('please specify an export path for the 500 words: ')
  if os.path.exists(export_path):
      break
  print('path not valid. please try again.')

with open(export_path, 'w') as export_file:
    for word in words:
        print(word, file=export_file)
