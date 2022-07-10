game_lexicon = {
    'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
    }

def scan(input_string):
    words = input_string.split()
    sentence = []
    for word in words:
        if word in game_lexicon['direction']:
            sentence.append(('direction', word))
    return(sentence)
