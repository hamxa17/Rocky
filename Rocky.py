import tkinter as tk
import threading
import speech_recognition as sr

class RockyApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Rocky")
        self.root.geometry("450x450")

        self.bg_colour = "#EDE8D0"
        self.text_colour = "#5d6658"
        self.font_family = "Roboto Mono"

        self.root.configure(bg=self.bg_colour)
        self.recogniser = sr.Recogniser()
        self.is_listening = False

        self.title_label = tk.Label(
            root,
            text="Speech-to-text Translator",
            font=(self.font_family, 16, "bold"),
            bg=self.bg_colour,
            fg=self.text_colour
        )
        self.title_label.pack(pady=20)


        self.mic_button = tk.Button(
            root,
            text="Speak",
            font=(self.font_family, 12, "bold"),
            bg=self.text_colour,    
            fg=self.bg_colour,     
            activebackground="#4a5246", 
            activeforeground=self.bg_colour,
            padx=20,
            pady=10,
            borderwidth=0,           
            cursor="hand2",
            command=self.toggle_listening
        )
        self.mic_button.pack(pady=20)

        self.text_output = tk.Text(
            root,
            font=(self.font_family, 12),
            wrap=tk.WORD,
            width=42,
            height=12,
            bd=1,
            bg="#F5F2E4",
            fg=self.text_colour,
            highlightthickness=1,
            highlightbackground=self.text_colour
        )
        self.text_output.pack(pady=20)

    def istening(self):
        if not self.is_listening:
            self.is_listening=True
            self.mic_button.config(text="Listening..", bg="#b85d53")
            self.text_output.config(state=tk.NORMAL)
            self.text_output.delete("1.0",tk.END)
            self.text_output.config(state=tk.DISABLED)

            threading.Thread(target=self.process_audio, daemon=True).start()
        else:
            self.is_listening=False
            self.reset_ui()
    
