import re

Story_file = r"D:\SKILLS\PYTHON DEVELOPMENT\3 PYTHON PROJECTS\Project_2.txt"

with open(Story_file, 'r') as file:
    story = file.read()

# Find all the special words enclosed in '<' and '>'
words_list = re.findall(r'<.*?>', story)
distinct_words_list = list(set(words_list))

answers = {}

for word in distinct_words_list:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in distinct_words_list:
    story = story.replace(word, answers[word])

print(story)
    