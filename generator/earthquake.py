import random

CAUSES = [
    "strong earthquake",
    "ground shaking",
    "powerful tremors",
    "sudden earthquake",
    "continuous tremors",
    "seismic activity",
    "earthquake shock",
    "violent shaking"
]

LOCATIONS = [
    "our house",
    "our apartment",
    "the school",
    "the hospital",
    "the office",
    "the bridge",
    "the road",
    "our village",
    "the market",
    "our building"
]

ACTIONS = [
    "has developed cracks",
    "has collapsed",
    "is shaking",
    "has partially collapsed",
    "is unsafe",
    "has severe structural damage",
    "is damaged"
]

PROBLEMS = [
    "people are trapped",
    "many people are injured",
    "we need medical help",
    "roads are blocked",
    "families are stranded",
    "people are panicking",
    "buildings are collapsing"
]

REQUESTS = [
    "please send rescue teams",
    "ambulance is needed",
    "please send NDRF",
    "urgent rescue is required",
    "medical assistance is needed",
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
    "{cause} has caused severe damage to {location}.",
    "{location} is no longer safe after the earthquake.",
    "{cause}. {request}."
]

def generate_earthquake_description():
    sentence = random.choice(TEMPLATES)

    return sentence.format(
        cause=random.choice(CAUSES),
        location=random.choice(LOCATIONS),
        action=random.choice(ACTIONS),
        problem=random.choice(PROBLEMS),
        request=random.choice(REQUESTS)
    )