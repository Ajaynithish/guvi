inp=str(input())
ch=inp.lower()
if('a'<=ch<='z'):
    if(ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
