kalimat = input("What do you want to say? ").lower()
kata = kalimat.split()
for i, word in enumerate(kata):
    if word[0] in 'aeiou':
        kata[i]=kata[i]+"ay"
    else:
        vowel=False

        for j, letter in enumerate(word):
            if letter in 'aeiou':
                kata[i]= word[j:]+word[:j]+"ay"
                vowel=True
                break
        if(vowel==False):
            kata[i]=kata[i]+ "ay"
pig=' '.join(kata)
print("This is your sentence in pig latin:", f"'{pig}'")