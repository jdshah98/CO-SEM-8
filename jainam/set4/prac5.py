try:
    fin = open("input.txt","r")
    lines = fin.readlines()
    if lines==[]:
        print("File is Empty")
    else:
        old_word = input("Enter word to be replaced: ")
        new_word = input("Enter new word: ")
        content=''.join(lines)
        content = content.replace(old_word,new_word)
        fout = open("prac5.txt","w")
        fout.write(content)
        fout.close()
    fin.close()
except FileNotFoundError:
    print("File Doesn't exist")
