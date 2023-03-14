import random

# creates a list of jokes
jokes_list = [
    'What do kids play when their mom is using the phone? Bored games.',
    'What do you call an ant who fights crime? A vigilANTe!',
    'Why are snails slow? Because they’re carrying a house on their back.',
    'What’s the smartest insect? A spelling bee!',
    'What does a storm cloud wear under his raincoat? Thunderwear.',
    'What is fast, loud and crunchy? A rocket chip.',
    'How does the ocean say hi? It waves!',
    'What do you call a couple of chimpanzees sharing an Amazon account? PRIME-mates.',
    'Why did the teddy bear say no to dessert? Because she was stuffed.',
    'Why did the soccer player take so long to eat dinner? Because he thought he couldn’t use his hands.',
]

# uses the random module to generate a number based on the length of the jokes_list.
selected_joke_index = round(random.random() * len(jokes_list))

# print the joke using the random number generated.
print(jokes_list[selected_joke_index])