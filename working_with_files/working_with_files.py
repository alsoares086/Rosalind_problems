'''
Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

'''

with open('sample.txt', 'r') as file:
    content = file.read()
    print(f"Conteúdo do arquivo:\n\n{content}\n")

    file.seek(0) 
    num_lines = 0

    print('Linhas pares:\n')
    for line in file:
        num_lines += 1
        if num_lines % 2 == 0: # printa as linhas pares
            print(line)

    print("Number of lines:", num_lines)