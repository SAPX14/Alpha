n  = int(input('Enter number of words you wanna give:'))

word_list = [] # empty list for adding words
dict = {}      # dictionary for keeping repetitions

for i in range(n):
    word = input()
    if word in word_list: # word is repeated
         dict[word] += 1  #therefore counter increased
    else:

       word_list.append(word) #to add given word to list
       dict[word] = 1         #counter not increased 

print(len(word_list)) #to print number of distinct words
print(' '.join(list(map(str, dict.values())))) #to print number of repitions of distinct words