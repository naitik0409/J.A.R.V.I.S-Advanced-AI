# Jarvis AI Assistant

A secure, feature-rich voice-controlled AI assistant that helps you with daily tasks and productivity.

## Features

### Core Functions
- Voice command interface
- Weather updates for any city
- Time and date management
- Focus mode tracking
- System monitoring
- WhatsApp integration
- Email functionality

### Voice Commands
- **Basic Controls**
  - "Wake up" - Activate Jarvis
  - "Go to sleep" - Deactivate temporarily
  - "Finally sleep" - Exit program

- **Information & Search**
  - "Time" - Check current time
  - "Date" - Check current date
  - "Temperature in [city]" - Get weather
  - "Search Google [query]" - Search on Google
  - "Wikipedia [query]" - Search on Wikipedia
  - "System info" - Check system resources

- **Media & Entertainment**
  - "Play [song name] YouTube" - Play videos
  - "Play music" - Play random music
  - "Tell me a joke" - Hear a random joke
  - "Open camera" - Access camera
  - "Take photo" - Capture a photo

- **Utility Functions**
  - "Screenshot" - Take screenshot
  - "Set alarm [time]" - Set an alarm
  - "Focus mode" - Start focus mode
  - "Show my focus" - Display focus graph
  - "Battery" - Check battery status
  - "Calculate" - Perform calculations

- **Communication**
  - "WhatsApp" - Send WhatsApp messages
  - "Manage contacts" - Manage WhatsApp contacts
  - "Send email" - Send emails

## Installation

### Prerequisites
- Python 3.8 or higher
- Windows OS (for full functionality)
- Microphone for voice commands
- Internet connection

### Setup
1. Clone the repository:
```bash
git clone https://github.com/naitik0409/jarvis-ai.git
cd jarvis-ai
```

2. Create virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

### Building Executable
To create a standalone executable:
```bash
python build.py
```
The executable will be created in the `dist` folder.

## File Structure
```
jarvis/
├── Jarvis_main.py    # Core assistant
├── FocusMode.py      # Focus tracking
├── FocusGraph.py     # Focus visualization
├── Whatsapp.py       # WhatsApp integration
├── GreetMe.py        # Welcome interface
├── game.py           # Entertainment module
├── build.py          # Executable builder
└── requirements.txt  # Dependencies
```

## Usage Guide

1. Start Jarvis:
```bash
python Jarvis_main.py
```

2. Wake up Jarvis by saying "Wake up"
3. Use any of the voice commands listed above
4. To make Jarvis sleep temporarily, say "Go to sleep"
5. To exit completely, say "Finally sleep"

### Focus Mode
- Tracks your productivity periods
- Generates visual statistics
- Helps maintain work-life balance

### WhatsApp Integration
- Send messages directly through voice commands
- Manage contacts securely
- Schedule messages

### System Controls
- Volume adjustment
- Screenshot capture
- Camera control
- Battery monitoring

## Troubleshooting

If you encounter issues:
1. Check microphone settings
2. Verify internet connection
3. Ensure all dependencies are installed
4. Check Python version compatibility
5. Verify file permissions

## Security Features
- Secure data storage
- Protected user credentials
- Encrypted communications
- Safe file handling

## Development
- Built with Python 3.8+
- Uses PyInstaller for builds
- Cross-platform compatible
- Modular architecture

## Credits
Created by Naitik

## Support
For support and updates:
- Instagram: @naitik__0409
- Create issues on GitHub for bug reports
