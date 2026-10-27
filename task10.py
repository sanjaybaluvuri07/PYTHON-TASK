
# Text Compression Using Character Runs

text = input("Enter a string: ")

encoded = ""
i = 0

while i < len(text):
    count = 1

    # Count consecutive repeated characters
    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1

    encoded += text[i] + str(count)
    i += 1

print("\nOriginal string:", text)
print("Encoded string:", encoded)

original_length = len(text)
encoded_length = len(encoded)

print("Original length:", original_length)
print("Encoded length:", encoded_length)

if encoded_length < original_length:
    print("Compression is beneficial.")
else:
    print("Compression is not beneficial.")
