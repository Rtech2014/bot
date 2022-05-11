from pprint import pprint
import time
import pandas as pd
import re
import asyncio
import yaml
from yaml.loader import SafeLoader
from models import Pattern, Stories, Entities
start = time.perf_counter()

def load_entities():
    # Open the file and load the file
    with open('entities.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data

def extract_pattern():
    # Open the file and load the file
    with open('pattern.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data

def extract_stories():
    # Open the file and load the file
    with open('stories.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data

def parse_entities_relation():
    patterns = extract_pattern()
    extracted_patterns = Pattern.parse_obj(patterns)
    return extracted_patterns

def parse_stories():
    stories = extract_stories()
    extracted_stories = Stories.parse_obj(stories)
    return extracted_stories

def parse_entities():
    stories = load_entities()
    extracted_stories = Entities.parse_obj(stories)
    return extracted_stories

async def preprocess_data(stories, entities):
    make_stories = stories.stories[0].story
    storie_gen = [await generate_story(i, entities) for i in make_stories]

async def generate_story(story,entities):
    data = "name"
    res = getattr(entities[0].name, data)
    print(res)

    for entity in entities:
        if(entity.name == "make"):
            for x in entity.values:
                value = story.replace('(make)', x.lower())
                matching_word = re.compile("{}".format(x.lower()))
                matches = matching_word.finditer(value)
                for match in matches:
                    print(value)
                    print(f"Start: {match.start()}")
                    print(f"Start: {match.end()}")


stories = parse_stories()
# print(stories.stories)
makeStory = stories.stories[0]

entities = parse_entities()

final_data = asyncio.run(preprocess_data(stories=stories, entities=entities.entitiesSlots))

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')


