# AI Story Generator - GPT-3 Powered Interactive Text Adventure

## Overview
The **AI Story Generator** is a **GPT-3 API-powered interactive storytelling application**. Users engage in a **dynamic text-based adventure**, where their choices influence the narrative in real-time. The application utilizes **OpenAI's GPT-3 API** to generate storylines, creating a **unique and adaptive storytelling experience**.

## Features
- **GPT-3 AI-Powered Story Generation**: Real-time narrative expansion based on user input.
- **User-Driven Dynamic Decision Making**: The story evolves with each decision.
- **Replayability with Adaptive Storylines**: Different choices create unique experiences.
- **Secure API Key Handling**: Uses environment variables for OpenAI API authentication.

## Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/AI-Story-Generator.git
cd AI-Story-Generator
```

### **2. Set Up a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**
```bash
pip install openai
```

### **4. Set Up OpenAI API Key Securely**
🔴 **DO NOT Hardcode Your API Key!** Use environment variables instead:
```bash
export OPENAI_API_KEY="your-api-key"  # Mac/Linux
set OPENAI_API_KEY="your-api-key"     # Windows
```

## Running the Application
```bash
python ai_story_generator.py
```

## How It Works
1. The application **initializes GPT-3 API** and generates an **opening story prompt**.
2. The user **enters choices**, which are passed as context to the **GPT-3 API**.
3. GPT-3 **processes the user’s input and generates the next section of the story**.
4. The player can **continue the narrative indefinitely** or exit at any point.

## Example Gameplay
```
Initializing AI Story Generator...
Connecting to GPT-3 API...

Story Prompt: You are an astronaut who has just woken up from cryosleep on an abandoned spaceship...
What do you want to do next?
> Check the control panel.
AI Response: You approach the control panel, its screen flickering with an unreadable message...
What do you want to do next?
> Attempt to decipher the message.
AI Response: The symbols slowly start making sense—it’s a distress signal sent from Earth...
Do you want to continue the story? (y/n): y
```

## Future Enhancements
- **Multi-Genre Story Modes**: Sci-Fi, Fantasy, Horror, Adventure.
- **GPT-4 Upgrade**: Future integration with OpenAI’s latest models.
- **Memory Persistence**: Implement a database to track user decisions.
- **Multiplayer Mode**: Collaborative AI storytelling.
- **Advanced NLP Processing**: Improve context retention for better storytelling.

## License
This project is licensed under the **MIT License**.

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact
For any questions or support, please open an issue on GitHub.

