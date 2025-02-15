def count_words():
    while True:
        # Prompt the user to enter a sentence or paragraph
        user_input = input("Enter a sentence or paragraph (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break 
        
        # Check for empty input
        if not user_input.strip():
            print("You entered an empty string. Please enter some text.")
            continue
        
        # Count the number of words
        word_count = len(user_input.split())
        
        # Display the word count
        print(f"Word count: {word_count}\n")
        
        # Prompt the user for another input
        print("Enter another sentence or paragraph, or type 'exit' to quit.")

# Run the function
count_words()
