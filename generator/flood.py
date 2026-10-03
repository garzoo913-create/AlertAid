import random

# --------------------------
# Vocabulary
# --------------------------

CAUSES = [
    "heavy rainfall",
    "continuous rainfall",
    "river overflow",
    "dam overflow",
    "blocked drainage",
    "clouds burst with intense rain",
    "water released from the dam",
    "monsoon rain"
]

LOCATIONS = [
    "our house",
    "our village",
    "the road",
    "the school",
    "the hospital",
    "the market",
    "the bridge",
    "our farm",
    "our colony",
    "the highway"
]

ACTIONS = [
    "is flooded",
    "is submerged",
    "is underwater",
    "has been washed away",
    "is surrounded by water",
    "is filled with water",
    "cannot be reached"
]

PROBLEMS = [
    "my family is trapped",
    "people need rescue",
    "electricity is unavailable",
    "roads are blocked",
    "we need food",
    "we need drinking water",
    "ambulance cannot reach",
    "people are stranded"
]

REQUESTS = [
    "please send help immediately",
    "urgent rescue is needed",
    "please send an ambulance",
    "please send NDRF",
    "please send a rescue boat",
    "medical help is required"
]

TEMPLATES = [

    "{cause} has caused flooding in {location}.",

    "{location} {action}.",

    "{cause} has caused {location} to become flooded.",

    "{location} {action} and {problem}.",

    "{cause}. {location} {action}. {request}.",

    "{problem}. {request}.",

    "{cause} has resulted in severe flooding.",

    "{location} has become unsafe because of floodwater.",

    "{location} is surrounded by rising water.",

    "{cause}. {problem}."
]

def generate_flood_description():

    sentence = random.choice(TEMPLATES)

    return sentence.format(

        cause=random.choice(CAUSES),

        location=random.choice(LOCATIONS),

        action=random.choice(ACTIONS),

        problem=random.choice(PROBLEMS),

        request=random.choice(REQUESTS)

    )