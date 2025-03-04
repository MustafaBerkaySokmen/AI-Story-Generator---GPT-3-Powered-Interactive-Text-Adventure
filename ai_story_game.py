import openai

# Set your OpenAI API key here
openai.api_key = "Set your OpenAI API key here"

# Define a function that uses the OpenAI API to generate a story prompt
def generate_story_prompt():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a story prompt",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    prompt = response.choices[0].text.strip()
    return prompt

# Define a function that uses the OpenAI API to continue a story
def continue_story(prompt, choice):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt + "\n\n" + choice + "\n\n",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    story = response.choices[0].text.strip()
    return story

# Define the main function to run the game
def story_game():
    print("Welcome to the AI-generated story game!")
    prompt = generate_story_prompt()
    while True:
        choice = input("What do you want to do next?\n")
        story = continue_story(prompt, choice)
        print(story)
        play_again = input("Do you want to continue the story? (y/n): ")
        if play_again.lower() != "y":
            break
    print("Thanks for playing!")

# Call the main function to run the game
if __name__ == "__main__":
    story_game()

