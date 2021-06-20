import re

numbers = {
    'ninety': 90,
    'eighty': 80,
    'seventy': 70,
    'sixty': 60,
    'fifty': 50,
    'forty': 40,
    'thirty': 30,
    'twenty': 20,
    'nineteen': 19,
    'eighteen': 18,
    'seventeen': 17,
    'fifteen': 15,
    'fourteen': 14,
    'thirteen': 13,
    'twelve': 12,
    'eleven': 11,
    ' and one-half': '.5',
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
}
TEXT2NUM_PATTERNS = []
for key in numbers.keys():
    TEXT2NUM_PATTERNS.append(re.compile(key, re.IGNORECASE))


def text_to_int(sentence: str):
    '''
    English to integers.
    This is terrible, I would write something better but low priority and too lazy for now.
    Only supports n < 100, also only multiples of 10 beyond 19.
    '''
    for pattern, key in zip(TEXT2NUM_PATTERNS, numbers.keys()):
        sentence = re.sub(pattern, str(numbers[key]), sentence)
    return sentence
