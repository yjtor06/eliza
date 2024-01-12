import tkinter as tk
from tkinter import scrolledtext
from el2 import Eliza  # Assurez-vous que cette importation correspond à votre structure de fichiers

class ChatBubble:
    """ Classe pour créer des bulles de chat dans la fenêtre de conversation. """
    def __init__(self, master, text="", sender="user"):
        self.frame = tk.Frame(master, bg="#E0E0E0")

        self.label = tk.Label(self.frame, text=text, wraplength=400, bg="#E0E0E0", font=("Helvetica", 10))
        self.label.pack(side=tk.RIGHT if sender == "user" else tk.LEFT, padx=10, pady=5)

    def pack(self, **kwargs):
        self.frame.pack(fill=tk.BOTH, **kwargs)

class ElizaApp:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot Eliza")

        # Styles par défaut (mode clair)
        self.bg_color_light = "#f5f5f5"
        self.text_color_light = "#333333"
        self.button_bg_light = "#4CAF50"
        self.button_fg_light = "white"

        # Styles pour le mode sombre
        self.bg_color_dark = "#424242"
        self.text_color_dark = "#E0E0E0"
        self.button_bg_dark = "#26A69A"
        self.button_fg_dark = "#E0E0E0"

        # Initialisation des styles
        self.bg_color = self.bg_color_light
        self.text_color = self.text_color_light
        self.button_bg = self.button_bg_light
        self.button_fg = self.button_fg_light
        master.configure(bg=self.bg_color)

        # Zone de conversation avec Scrollbar
        self.chat_frame = tk.Frame(master, bg="white")
        self.chat_frame.pack(padx=15, pady=5, fill=tk.BOTH, expand=True)

        # Champ de saisie utilisateur
        self.user_input = tk.Entry(master, font=("Helvetica", 12), bg="white", fg=self.text_color)
        self.user_input.pack(fill=tk.BOTH, padx=15, pady=5)
        self.user_input.bind("<Return>", self.on_enter_pressed)

        # Panneau de boutons
        self.button_panel = tk.Frame(master, bg=self.bg_color)
        self.button_panel.pack(fill=tk.BOTH, padx=15, pady=5)

        # Bouton Envoyer
        self.send_button = tk.Button(self.button_panel, text="Envoyer", command=self.send_message, font=("Helvetica", 12), bg=self.button_bg, fg=self.button_fg, relief=tk.FLAT)
        self.send_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Bouton pour changer le thème
        self.theme_button = tk.Button(self.button_panel, text="Mode Sombre/Clair", command=self.toggle_theme, font=("Helvetica", 12), bg=self.button_bg, fg=self.button_fg, relief=tk.FLAT)
        self.theme_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Bouton de fermeture
        self.close_button = tk.Button(self.button_panel, text="Fermer", command=master.destroy, font=("Helvetica", 12), bg=self.button_bg, fg=self.button_fg, relief=tk.FLAT)
        self.close_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.eliza = Eliza()
        self.eliza.load('doctorbis.txt')

    def toggle_theme(self):
        """ Basculer entre le mode sombre et le mode clair. """
        if self.bg_color == self.bg_color_light:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()
        self.update_styles()

    def apply_light_theme(self):
        """ Appliquer le thème clair. """
        self.bg_color = self.bg_color_light
        self.text_color = self.text_color_light
        self.button_bg = self.button_bg_light
        self.button_fg = self.button_fg_light

    def apply_dark_theme(self):
        """ Appliquer le thème sombre. """
        self.bg_color = self.bg_color_dark
        self.text_color = self.text_color_dark
        self.button_bg = self.button_bg_dark
        self.button_fg = self.button_fg_dark

    def update_styles(self):
        """ Mettre à jour les styles des widgets. """
        self.master.configure(bg=self.bg_color)
        self.chat_frame.configure(bg=self.bg_color)
        self.user_input.configure(bg="white", fg=self.text_color)
        self.button_panel.configure(bg=self.bg_color)
        for widget in self.button_panel.winfo_children():
            widget.configure(bg=self.button_bg, fg=self.button_fg)

    def on_enter_pressed(self, event):
        """ Gérer l'événement d'appui sur la touche Entrée. """
        self.send_message()

    def send_message(self):
        """ Envoyer un message et obtenir une réponse d'Eliza. """
        user_text = self.user_input.get()
        if user_text.strip() == "":
            return  # Ne rien faire si l'entrée est vide

        user_bubble = ChatBubble(self.chat_frame, text="Vous: " + user_text, sender="user")
        user_bubble.pack(side=tk.TOP, anchor=tk.E, pady=(0, 2))

        eliza_response = self.eliza.respond(user_text)
        if eliza_response is None:
            self.master.destroy()
            return

        eliza_bubble = ChatBubble(self.chat_frame, text="Eliza: " + eliza_response, sender="eliza")
        eliza_bubble.pack(side=tk.TOP, anchor=tk.W, pady=(2, 0))

        self.user_input.delete(0, tk.END)

    def update_conversation(self, message):
        """ Mettre à jour la conversation dans la zone de texte. """
        self.conversation.config(state='normal')
        self.conversation.insert(tk.END, message + "\n")
        self.conversation.config(state='disabled')
        self.conversation.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")
    app = ElizaApp(root)
    root.mainloop()
