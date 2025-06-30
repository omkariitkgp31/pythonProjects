import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# --- Voice selection ---
print("Available voices:")
for idx, voice in enumerate(voices):
    print(f"{idx + 1}: {voice.name}")

voice_choice = int(input("Choose a voice number (e.g., 1 or 2): ")) - 1
engine.setProperty('voice', voices[voice_choice].id)

# --- Speaking rate selection ---
rate = engine.getProperty('rate')
print("\nChoose speaking pace:")
print("1: Slow")
print("2: Normal")
print("3: Fast")

pace_choice = input("Enter your choice (1/2/3): ")

if pace_choice == '1':
    engine.setProperty('rate', 125)  # Slow
elif pace_choice == '2':
    engine.setProperty('rate', 175)  # Normal
elif pace_choice == '3':
    engine.setProperty('rate', 225)  # Fast
else:
    print("Invalid choice, using normal pace.")
    engine.setProperty('rate', 175)

# --- Read book ---
book = open(r"book.txt")
book_text = book.readlines()
book.close()

for line in book_text:
    engine.say(line)
    engine.runAndWait()
