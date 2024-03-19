verbs = 'падать, упасть, выпасть, опасть, завалиться, повалиться, отвалиться, обвалиться, сорваться, отскочить, соскочить,рухнуть, обрушиться, сыпаться, высыпаться, осыпаться, шлепнуться, грохнуться, шмякнуться, брякнуться, бултыхнуться, плюхнуться'
list_verbs = verbs.split(', ')
current_sentence = ''
target_verbs = ['\t'+verb for verb in list_verbs]
with open('lines_3000000.txt',  encoding = 'utf-8') as f:
    for line in f:
        if 'SENT' in line:
            current_sentence +='\n\n'
            if any(verb in current_sentence for verb in target_verbs):
                with open('subcorpus.txt', 'a', encoding = 'utf-8') as file:
                    file.write(current_sentence)
            current_sentence = ''
        else:
            current_sentence += line