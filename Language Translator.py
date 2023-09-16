import tkinter as tk
from tkinter import ttk
from googletrans import Translator
import pyttsx3

def translate_text():
    input_text = input_textbox.get("1.0", "end-1c")
    dest_languages = selected_languages.get().split(",")  # Get a list of selected languages
    translations = {}  # Store translations for each language

    # Translate text into each selected language
    for lang_code in dest_languages:
        translator = Translator()
        translated_text = translator.translate(input_text, dest=lang_code).text
        translations[lang_code] = translated_text

    # Display translations in the output Text widget
    output_textbox.delete("1.0", "end")
    for lang_code, translated_text in translations.items():
        output_textbox.insert("end", f"{lang_code}: {translated_text}\n\n")

    # Add translation to history
    history_textbox.insert("end", f"From: {translator.detect(input_text).lang}, To: {','.join(dest_languages)}\n{input_text}\n")
    for lang_code, translated_text in translations.items():
        history_textbox.insert("end", f"{lang_code}: {translated_text}\n")
    history_textbox.insert("end", "\n")

def auto_detect_language():
    input_text = input_textbox.get("1.0", "end-1c")
    translator = Translator()
    detected_lang = translator.detect(input_text).lang
    selected_language.set(detected_lang)

def text_to_speech():
    translated_text = output_textbox.get("1.0", "end-1c")
    engine = pyttsx3.init()
    engine.say(translated_text)
    engine.runAndWait()

app = tk.Tk()
app.title("Language Translator")

# Styling
app.geometry("800x600")
app.configure(bg="#F0F0F0")

# Frame for Input
input_frame = ttk.Frame(app)
input_frame.pack(pady=10, padx=10, fill=tk.BOTH)

# Input Text
input_label = ttk.Label(input_frame, text="Enter text to translate:", font=("Helvetica", 14))
input_label.pack()
input_textbox = tk.Text(input_frame, height=5, width=60, font=("Helvetica", 12))
input_textbox.pack()

# Frame for Output
output_frame = ttk.Frame(app)
output_frame.pack(pady=10, padx=10, fill=tk.BOTH)

# Output Text
output_label = ttk.Label(output_frame, text="Translated text:", font=("Helvetica", 14))
output_label.pack()
output_textbox = tk.Text(output_frame, height=10, width=60, font=("Helvetica", 12))
output_textbox.pack()

# Frame for Controls
controls_frame = ttk.Frame(app)
controls_frame.pack(pady=10, padx=10, fill=tk.BOTH)

# Language selection
supported_languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-cn",
    "Russian": "ru",
    "Arabic": "ar",
    "Hindi": "hi",
    "Korean": "ko",
    "Italian": "it",
    # Add more languages here
}

selected_language = tk.StringVar(app)
selected_language.set("English")
language_label = ttk.Label(controls_frame, text="Select language:", font=("Helvetica", 12))
language_label.pack(side=tk.LEFT, padx=5)
language_menu = ttk.Combobox(controls_frame, textvariable=selected_language, values=list(supported_languages.keys()))
language_menu.config(font=("Helvetica", 12))
language_menu.pack(side=tk.LEFT, padx=5)

# Multi-Language Selection
multi_language_label = ttk.Label(controls_frame, text="Select target languages (comma-separated):", font=("Helvetica", 12))
multi_language_label.pack(side=tk.LEFT, padx=5)
selected_languages = tk.StringVar(app)
selected_languages.set("es,fr,de")  # Default selected languages
multi_language_entry = ttk.Entry(controls_frame, textvariable=selected_languages, font=("Helvetica", 12))
multi_language_entry.pack(side=tk.LEFT, padx=5)

# Auto-Detect Language Button
auto_detect_button = ttk.Button(controls_frame, text="Auto-Detect Language", command=auto_detect_language, style='TButton')
auto_detect_button.pack(side=tk.LEFT, padx=5)

# Translate Button
translate_button = ttk.Button(controls_frame, text="Translate", command=translate_text, style='TButton')
translate_button.pack(side=tk.LEFT, padx=5)

# Text-to-Speech Button
text_to_speech_button = ttk.Button(controls_frame, text="Text to Speech", command=text_to_speech, style='TButton')
text_to_speech_button.pack(side=tk.LEFT, padx=5)

# Frame for History
history_frame = ttk.Frame(app)
history_frame.pack(pady=10, padx=10, fill=tk.BOTH)

# Language History
history_label = ttk.Label(history_frame, text="Translation History:", font=("Helvetica", 14))
history_label.pack()
history_textbox = tk.Text(history_frame, height=10, width=60, font=("Helvetica", 12))
history_textbox.pack()

app.mainloop()
