code ={
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":".--",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    ".":".-.-.-",
    ",":"--..--",
    "?":"..--..",
    "/":"-..-.",
    "@":".--.-.",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----"
}

value = input("Enter a letter: ")
value = value.upper()
morse = ""

for i in value:
    if(i==" "):
        morse+="   "
        continue
    morse+= code[i]
    morse+= " "

print(morse)
    



