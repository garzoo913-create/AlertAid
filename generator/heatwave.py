import random

CAUSES = [
    "extreme heat",
    "very high temperature",
    "heatwave conditions",
    "scorching weather",
    "continuous hot weather",
    "intense sunlight",
    "record high temperature",
    "prolonged heat"
]

LOCATIONS = [
    "our city",
    "our village",
    "our locality",
    "the highway",
    "the school",
    "the market",
    "the construction site",
    "the farm",
    "our workplace",
    "the nearby town"
]

ACTIONS = [
    "has become extremely hot",
    "is unsafe during the afternoon",
    "has no drinking water",
    "is experiencing severe heat",
    "is difficult to work in",
    "has become unbearable",
    "is facing extreme temperatures"
]

PROBLEMS = [
    "people are fainting",
    "many people are dehydrated",
    "people are suffering from heatstroke",
    "medical help is needed",
    "drinking water is unavailable",
    "elderly people need help",
    "people are collapsing"
]

REQUESTS = [
    "please send medical assistance",
    "urgent help is needed",
    "please provide drinking water",
    "ambulance is required",
    "please help immediately",
    "medical teams are needed"
]

TEMPLATES = [
    "{cause} has affected {location}.",
    "{location} {action}.",
    "{cause}. {location} {action}.",
    "{cause}. {problem}.",
    "{location} {action}. {request}.",
    "{cause}. {location} {action}. {problem}.",
    "{problem}. {request}.",
    "{cause} is causing health problems.",
    "{location} is unsafe because of extreme heat.",
    "{cause}. {request}."
]

def generate_heatwave_description():

    sentence = random.choice(TEMPLATES)

    return sentence.format(
        cause=random.choice(CAUSES),
        location=random.choice(LOCATIONS),
        action=random.choice(ACTIONS),
        problem=random.choice(PROBLEMS),
        request=random.choice(REQUESTS)
    )