import re

numbers = {
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
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
}
TEXT2NUM_PATTERNS = []
for key in numbers.keys():
    TEXT2NUM_PATTERNS.append(re.compile(key, re.IGNORECASE))


def text_to_int(sentence: str):
    '''
    English to integers.
    Non standard implementation
    Only supports n < 100.
    '''
    for pattern, key in zip(TEXT2NUM_PATTERNS, numbers.keys()):
        sentence = re.sub(pattern, str(numbers[key]), sentence)
    return sentence
