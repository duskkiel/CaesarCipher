# 65(A) - 90(Z)
# 97(a) - 122(z)
import sys


def main():
    text = open(sys.argv[1])
    text = list(text.read())    # Read txt file

    if len(sys.argv) == 3:
        rotates = int(sys.argv[2])
        if 0 <= int(rotates) <= 25:     # Argument 3
            finalList = []
            for i in range(len(text)):
                ordNum = ord(text[i])        
                
                if 97 <= ordNum <= 122:     # Uppercase
                    if (ord(text[i]) - int(rotates)) < 97:
                        newLetter = (ord(text[i]) - int(rotates)) + 26
                        finalList.append(chr(newLetter))                     
                    else:
                        finalList.append(chr(ord(text[i]) - int(rotates)))
                        
                elif ordNum == 32 or ordNum == 46 or ordNum == 44:      # Special Characters
                    finalList.append(chr(ord(text[i])))
                    
                elif ordNum == 10:      # Enters
                    finalList.append("\n")
                    
                elif 65 <= ordNum <= 90:        # Lowercase
                    if (ord(text[i]) - int(rotates)) < 65:
                        newLetter = (ord(text[i]) - int(rotates)) + 26
                        finalList.append(chr(newLetter))
                    else:
                        finalList.append(chr(ord(text[i]) - int(rotates)))
                        
            final = ""
            for i in range(len(finalList)):
                final += finalList[i]
            print("\n")
            print(final)
        else:
            print("Error. Rotation must be between 0 and 25.")

    elif len(sys.argv) == 2:        # Arguments 2
        for j in range(0, 26):
            finalList = []
            print("\n\n------------------------\nRotated by " + str(j) + " positions:\n------------------------")
            for i in range(len(text)):
                ordNum = ord(text[i])
                
                if 97 <= ordNum <= 122:     # Uppercase
                    if (ord(text[i]) - int(j)) < 97:
                        newLetter = (ord(text[i]) - int(j)) + 26
                        finalList.append(chr(newLetter))
                    else:
                        finalList.append(chr(ord(text[i]) - int(j)))
                        
                elif ordNum == 32 or ordNum == 46 or ordNum == 44:      # SC
                    finalList.append(chr(ord(text[i])))
                    
                elif ordNum == 10:      # Enters
                    finalList.append("\n")
                    
                elif 65 <= ordNum <= 90:        # Lowercase
                    if (ord(text[i]) - int(j)) < 65:
                        newLetter = (ord(text[i]) - int(j)) + 26
                        finalList.append(chr(newLetter))
                    else:
                        finalList.append(chr(ord(text[i]) - int(j)))
                        
            final = ""
            for i in range(len(finalList)):
                final += finalList[i]
            print(final)

    elif len(sys.argv) == 1:        # Arguments 1
        print("Error. Did not supply enough arguments.")


main()
