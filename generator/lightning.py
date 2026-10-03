import random

CAUSES = [
    "a lightning strike",
    "a severe thunderstorm",
    "continuous lightning",
    "intense thunder",
    "stormy weather",
    "electrical discharge",
    "lightning during heavy rain",
    "a powerful lightning strike"
]

LOCATIONS = [
    "our house",
    "our village",
    "the school",
    "the hospital",
    "the farm",
    "the market",
    "the highway",
    "our locality",
    "the nearby forest",
    "an electric pole"
]

ACTIONS = [
    "has caught fire",
    "has lost electricity",
    "has been damaged",
    "is unsafe",
    "has suffered a power outage",
    "is surrounded by fallen trees",
    "cannot be accessed"
]

PROBLEMS = [
    "a person has been injured",
    "people need medical help",
    "electricity is unavailable",
    "fire has started",
    "people are scared",
    "communication has stopped",
    "emergency help is needed"
]

REQUESTS = [
    "please send an ambulance",
    "medical assistance is required",
    "please send firefighters",
    "urgent help is needed",
    "please help immediately",
    "emergency rescue is required"
]

TEMPLATES = [
    "{cause} has affected {location}.",
    "{location} {action}.",
    "{cause}. {location} {action}.",
    "{cause}. {problem}.",
    "{location} {action}. {request}.",
    "{cause}. {location} {action}. {problem}.",
    "{problem}. {request}.",
    "{cause} has caused severe damage.",
    "{location} is unsafe after the lightning strike.",
    "{cause}. {request}."
]

def generate_lightning_description():

    sentence = random.choice(TEMPLATES)

    return sentence.format(
        cause=random.choice(CAUSES),
        location=random.choice(LOCATIONS),
        action=random.choice(ACTIONS),
        problem=random.choice(PROBLEMS),
        request=random.choice(REQUESTS)
    )