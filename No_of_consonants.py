def consonants(s):
    consonant=0
    vowels=0
    st=s.lower()
    for i in st:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels=vowels+1
        else:
            consonant=consonant+1
    print("Count of consonants is: ",consonant)
s=str(input("Enter a word:"))
consonants(s)
