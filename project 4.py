
text = input("Enter a string: ")

encoded = ""
i = 0

while i < len(text):
    count = 1

    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1

    encoded += text[i] + str(count)
    i += 1

print("Original string:", text)
print("Original length:", len(text))

if len(encoded) < len(text):
    print("Compressed string:", encoded)
    print("Compressed length:", len(encoded))
else:
    print("Compression is not beneficial.")
    print("Encoded string:", encoded)
