import random

CAUSES = [
    "heavy rainfall",
    "continuous rain",
    "loose soil",
    "hill slope failure",
    "mountain erosion",
    "soil erosion",
    "rockfall",
    "unstable hillside"
]

LOCATIONS = [
    "the mountain road",
    "our village",
    "the highway",
    "the hillside",
    "our house",
    "the bridge",
    "the school",
    "the forest road",
    "the valley",
    "our locality"
]

ACTIONS = [
    "is blocked by rocks",
    "is covered with mud",
    "has collapsed",
    "is buried under debris",
    "cannot be reached",
    "is completely blocked",
    "has been damaged"
]

PROBLEMS = [
    "people are stranded",
    "vehicles are trapped",
    "families need rescue",
    "roads are closed",
    "people cannot leave",
    "rescue teams are needed",
    "transport has stopped"
]

REQUESTS = [
    "please send rescue teams",
    "urgent help is needed",
    "road clearance is required",
    "please send medical assistance",
    "please help immediately",
    "emergency rescue is required"
]

TEMPLATES = [
    "{cause} has triggered a landslide near {location}.",
    "{location} {action}.",
    "{cause}. {location} {action}.",
    "{cause}. {problem}.",
    "{location} {action}. {request}.",
    "{cause}. {location} {action}. {problem}.",
    "{problem}. {request}.",
    "{cause} has caused a major landslide.",
    "{location} is unsafe because of falling rocks.",
    "{cause}. {request}."
]

def generate_landslide_description():

    sentence = random.choice(TEMPLATES)

    return sentence.format(
        cause=random.choice(CAUSES),
        location=random.choice(LOCATIONS),
        action=random.choice(ACTIONS),
        problem=random.choice(PROBLEMS),
        request=random.choice(REQUESTS)
    )