import json
import difflib

# Load JSON data into a Python dictionary
def load_dictionary(data):
    with open(data, 'r') as f:
        data = json.load(f)
    return data

# Function to get definition of a word
def get_definition(word, dictionary):
    word = word.lower()  # Convert word to lowercase for case-insensitive comparison
    if word in dictionary:
        return dictionary[word]
    else:
        # If word not found, suggest similar words
        similar_words = difflib.get_close_matches(word, dictionary.keys(), n=3, cutoff=0.8)
        if similar_words:
            suggestion = similar_words[0]  # Take the most similar word
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Word not found."

# Main function
def main():
    # Load dictionary
    dictionary = load_dictionary("data.json")

    # Prompt user for input
    word = input("Enter a word to search for its definition: ")

    # Get definition
    definition = get_definition(word, dictionary)
    print(definition)

if __name__ == "__main__":
    main()
