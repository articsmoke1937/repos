def sentence_maker(phrase):
    interrogatives = ('Who','What','Where','Why','When','How','Are')
    capitalized = phrase.capitalize()
    if capitalized.startswith(interrogatives):
        return '{}?'.format(capitalized)
    else:    
        return '{}.'.format(capitalized)

sentence_in = []
while True:
    phrase_in = input("Say something: ")
    if phrase_in == "\end":
        break
    else:
        sentence_in.append(sentence_maker(phrase_in))        

print(" ".join(sentence_in))