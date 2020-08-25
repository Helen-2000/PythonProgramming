# '''
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for word in sentence:
    print(word)


# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5,31,5):
    print(i)


# '''
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    name = name.lower().replace(' ','_')
    usernames.append(name)

print(usernames)


# Modify Usernames with Range
# Write a for loop that uses range() to iterate over the positions in usernames
# to modify the list. Like you did in the previous quiz, change each name to be
# lowercase and replace spaces with underscores.

# write your for loop here
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(' ','_')

print(usernames)


# Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts how
# many of them are XML tags. XML is a data language similar to HTML. You can
# tell if a string is an XML tag if it begins with a left angle bracket "<" and
# ends with a right angle bracket ">". Keep track of the number of tags using
# the variable count.
# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if '<' in token and '>' in token:
        count += 1

print(count)


# Creat an HTML list
# Write some code, including a for loop, that iterates over a list of strings
# and creates a single string, html_str, which is an HTML list.
# That is, the string's first line should be the opening tag <ul>. Following
# that is one line per element in the source list, surrounded by <li> and
# </li> tags. The final line of the string should be the closing tag </ul>.

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += '<li>{}</li>\n'.format(item)
html_str += '</ul>'

print(html_str)
