game_lexicon = {
    'directions': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
    'verbs': ['go', 'stop', 'kill', 'eat'],
    'stops': ['the', 'in', 'of', 'from', 'at', 'it'],
    'nouns': ['door', 'bear', 'princess', 'cabinet']
    }

# a utility function
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(input_string):
    words = input_string.split()
    sentence = []
    for word in words:
        if word in game_lexicon['directions']:
            sentence.append(('direction', word))
        elif word in game_lexicon['verbs']:
            sentence.append(('verb', word))
        elif word in game_lexicon['stops']:
            sentence.append(('stop', word))
        elif word in game_lexicon['nouns']:
            sentence.append(('noun', word))
        elif (len(word) < 10) & (convert_number(word) is not None):
            sentence.append(('number', convert_number(word)))
        else:
            sentence.append(('error', word))
    return(sentence)
