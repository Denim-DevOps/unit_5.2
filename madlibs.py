from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_word(word_type):
    #func to get random words based on type
    words = {
        'character' : ['man', 'woman', 'cat', 'dog', 'prince', 'princess', 'squirrel', 'bat', 'fox'],
        'colour' : ['navy', 'orange', 'teal', 'violet', 'scarlet'],
        'verb' : ['ran', 'jumped', 'hopped', 'skipped', 'flew'],
        'adjective' : ['big', 'small', 'slimy', 'strong', 'gigantic', 'miniscule', 'large', 'tiny'],
        'adverb' : ['hastily', 'slowly', 'happily', 'sadly'],
        'place' : ['home', 'school', 'gym', 'church', 'library', 'forest', 'mountains', 'river', 'aquarium'],
        'exclamation' : ['wow', 'yikes', 'oops', 'ouch', 'hooray']
    }
    return random.choice(words[word_type])

def create_story():
    #func to create random story based on template
    story_template = (
        "Once upon a time there was a {adjective} {character}, who lived in a {adjective} {place}. "
        "{exclamation}! They said as they {verb} {adverb} out of bed. "
        "Today was the day that they would visit the {adjective} {colour} {place} with their friend, the {character}. "
    )

    #replaces placeholder with random words
    story = story_template.format(
        character=get_word('character'),
        colour=get_word('colour'),
        verb=get_word('verb'),
        adjective=get_word('adjective'),
        adverb=get_word('adverb'),
        place=get_word('place'),
        exclamation=get_word('exclamation')
    )

    return story

@app.route('/')
def home():
    return create_story()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

