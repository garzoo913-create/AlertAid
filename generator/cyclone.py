import random

CAUSES = [
    "a powerful cyclone",
    "a severe coastal storm",
    "very strong winds",
    "a tropical cyclone",
    "an intense storm",
    "extreme weather conditions",
    "cyclonic winds",
    "a violent storm"
]

LOCATIONS = [
    "our house",
    "our village",
    "the coastal area",
    "the highway",
    "the market",
    "the school",
    "the hospital",
    "our locality",
    "the fishing harbor",
    "the nearby town"
]

ACTIONS = [
    "has lost its roof",
    "has been badly damaged",
    "is surrounded by fallen trees",
    "has no electricity",
    "is inaccessible",
    "has been flooded",
    "is covered with debris"
]

PROBLEMS = [
    "people are stranded",
    "families need immediate help",
    "electricity has been cut off",
    "communication is unavailable",
    "roads are blocked",
    "trees have fallen everywhere",
    "houses are damaged"
]

REQUESTS = [
    "please send emergency teams",
    "urgent rescue is required",
    "medical assistance is needed",
    "please restore electricity",
    "please send relief materials",
    "please help immediately"
]

TEMPLATES = [
    "{cause} has affected {location}.",
    "{location} {action}.",
    "{cause}. {location} {action}.",
    "{cause}. {problem}.",
    "{location} {action}. {request}.",
    "{cause}. {location} {action}. {problem}.",
    "{problem}. {request}.",
    "{cause} has caused widespread destruction.",
    "{location} is unsafe because of strong winds.",
    "{cause}. {request}."
]

def generate_cyclone_description():

    sentence = random.choice(TEMPLATES)

    return sentence.format(
        cause=random.choice(CAUSES),
        location=random.choice(LOCATIONS),
        action=random.choice(ACTIONS),
        problem=random.choice(PROBLEMS),
        request=random.choice(REQUESTS)
    )