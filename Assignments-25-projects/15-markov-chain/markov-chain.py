import random
import markovify

# Function to load and prepare text
def load_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Function to build the Markov chain model
def build_markov_chain(text, state_size=2):
    model = markovify.Text(text, state_size=state_size)
    return model

# Function to generate random text
def generate_text(model, num_sentences=5):
    generated_text = ""
    for _ in range(num_sentences):
        sentence = model.make_sentence()
        if sentence:  # Check if the sentence is not None
            generated_text += sentence + '\n'
        else:
            generated_text += "[Unable to generate a sentence]\n"  # Add a fallback
    return generated_text

# Main function to run the project
def main():
    # Step 1: Load song lyrics or any text corpus
    file_path =file_path = "my-lyrics.txt"
 # Replace with your file path
    text = load_text(file_path)

    # Step 2: Build the Markov chain model
    model = build_markov_chain(text)

    # Step 3: Generate random text based on the Markov chain model
    num_sentences = 5  # Number of sentences to generate
    generated_text = generate_text(model, num_sentences)

    # Step 4: Output the generated text
    print("Generated Song Lyrics/Text:\n")
    print(generated_text)

if __name__ == "__main__":
    main()

