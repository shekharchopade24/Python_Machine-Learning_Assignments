
def VowelCheck(Ch):

    Ch = Ch.lower()

    if(Ch == 'a' or Ch == 'e' or Ch == 'i' or Ch == 'o' or Ch == 'u'):

        print("Vowel")

    else:

        print("Consonant")

def main():

    cValue = input("Enter Character :")

    VowelCheck(cValue)

if __name__ == "__main__":

    main()