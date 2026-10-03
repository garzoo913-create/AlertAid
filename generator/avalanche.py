import random

CAUSES = [
    "heavy snowfall",
    "an avalanche",
    "a snow slide",
    "unstable snow",
    "ice collapse",
    "continuous snowfall",
    "mountain snow movement",
    "snow accumulation"
]

LOCATIONS = [
    "the mountain road",
    "our camp",
    "the highway",
    "our village",
    "the trekking route",
    "the hill station",
    "the mountain pass",
    "our shelter",
    "the nearby valley",
    "the forest trail"
]

ACTIONS = [
    "is blocked by snow",
    "has been buried",
    "cannot be reached",
    "is covered with snow",
    "is unsafe",
    "has become inaccessible",
    "is trapped under snow"
]

PROBLEMS = [
    "people are trapped",
    "vehicles are stuck",
    "tourists need rescue",
    "roads are blocked",
    "families are stranded",
    "medical help is needed",
    "people cannot move"
]

REQUESTS = [
    "please send mountain rescue",
    "urgent rescue is required",
    "medical assistance is needed",
    "please help immediately",
    "send emergency teams",
    "evacuation is required"
]

TEMPLATES = [
    "{cause} has affected {location}.",
    "{location} {action}.",
    "{cause}. {location} {action}.",
    "{cause}. {problem}.",
    "{location} {action}. {request}.",
    "{cause}. {location} {action}. {problem}.",
    "{problem}. {request}.",
    "{cause} has blocked the entire route.",
    "{location} is unsafe because of heavy snowfall.",
    "{cause}. {request}."
]

def generate_avalanche_description():

    sentence = random.choice(TEMPLATES)

    return sentence.format(
        cause=random.choice(CAUSES),
        location=random.choice(LOCATIONS),
        action=random.choice(ACTIONS),
        problem=random.choice(PROBLEMS),
        request=random.choice(REQUESTS)
    )