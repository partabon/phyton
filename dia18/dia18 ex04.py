import re

sentence = '''%I am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(w):
    matches = re.sub('%', '', w)
    matches = re.sub('@', '', matches)
    matches = re.sub('&', '', matches)
    matches = re.sub('#', '', matches)
    matches = re.sub(';', '', matches)
    matches = re.sub('\$', '', matches)
    return matches

print(clean_text(sentence))

def most_frequent_words(w):
    regex_pattern =r'[^.,\?\! ]+'
    words= re.findall(regex_pattern,w)
    #words.sort()
    print(words)
    set_words = set()
    set_words.update(words)
    list_words = list(set_words)
    list_words.sort()
    print(list_words)
    ocurrencias = list()
    for i in range(len(list_words)):
        ocurrencias.append(0)
    for j in range(len(words)):
        for i in range(len(list_words)):
            if list_words[i] == words[j]: 
                ocurrencias[i]+=1
    #print(ocurrencias)
    n =len(list_words)
    for i in range(n-2):
        for j in range(n-i-1):
            if ocurrencias[j]<ocurrencias[j+1]:
                aux_ocurrencias = ocurrencias[j]
                aux_words = list_words[j]
                ocurrencias[j]=ocurrencias[j+1]
                list_words[j] =list_words[j+1]
                ocurrencias[j+1]=aux_ocurrencias
                list_words[j+1]= aux_words
    #print(ocurrencias)
    dicc =list()
    for i in range(len(list_words)):
        if ocurrencias[i] >1:
            dicc.append((ocurrencias[i],list_words[i]))
    #print(dicc)
    return dicc

cleaned_text = clean_text(sentence)

# [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

print(most_frequent_words(cleaned_text)) 
