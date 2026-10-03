import random

CAUSES = [
    "a forest fire",
    "a wildfire",
    "dry weather",
    "extreme heat",
    "strong winds",
    "burning vegetation",
    "a spreading fire",
    "high temperature"
]

LOCATIONS = [
    "the forest",
    "the wildlife sanctuary",
    "the nearby village",
    "our locality",
    "the highway",
    "the hills",
    "the national park",
    "the farmland",
    "the mountain forest",
    "the nearby town"
]

ACTIONS = [
    "is covered with smoke",
    "is burning rapidly",
    "is filled with flames",
    "has been evacuated",
    "is unsafe",
    "is surrounded by fire",
    "has poor visibility"
]

PROBLEMS = [
    "people are evacuating",
    "animals are trapped",
    "breathing has become difficult",
    "houses are at risk",
    "roads are closed",
    "fire is spreading quickly",
    "people need immediate help"
]

REQUESTS = [
    "please send firefighters",
    "urgent evacuation is required",
    "please send emergency teams",
    "medical assistance is needed",
    "please control the fire",
    "help is needed immediately"
]

TEMPLATES = [
    "{cause} has affected {location}.",
    "{location} {action}.",
    "{cause}. {location} {action}.",
    "{cause}. {problem}.",
    "{location} {action}. {request}.",
    "{cause}. {location} {action}. {problem}.",
    "{problem}. {request}.",
    "{cause} is spreading rapidly.",
    "{location} is unsafe because of heavy smoke.",
    "{cause}. {request}."
]

def generate_forest_fire_description():

    sentence = random.choice(TEMPLATES)

    return sentence.format(
        cause=random.choice(CAUSES),
        location=random.choice(LOCATIONS),
        action=random.choice(ACTIONS),
        problem=random.choice(PROBLEMS),
        request=random.choice(REQUESTS)
    )