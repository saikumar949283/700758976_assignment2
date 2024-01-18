lines = [
    "Python Course",
    "Deep Learning Course"
]
word_count_result = {}
for line in lines:
    words = line.split()
    for word in words:
        word_count_result[word] = word_count_result.get(word, 0) + 1

# Print the lines
for line in lines:
    print(line)

# Print the word count for each word
print("\nWord_Count:")
for word, count in word_count_result.items():
    print(f"{word}: {count}")

# Store the output in output.txt
with open('output.txt', 'w') as output_file:
    output_file.writelines([line + '\n' for line in lines])
    output_file.write("\nWord_Count:\n")
    output_file.writelines([f"{word}: {count}\n" for word, count in word_count_result.items()])
