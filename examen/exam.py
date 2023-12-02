import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit

class Fenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.compteur = 0
        self.timer = QTimer(self)

        self.init_ui()

    # Partie 1 : réaliser l'interface graphique
    def init_ui(self):
        self.label_compteur = QLabel('Compteur:', self)
        self.label_affichage = QLabel('0', self)
        self.edit_connect = QLineEdit(self)

        layout_principal = QVBoxLayout(self)
        layout_boutons = QGridLayout()

        # Création des boutons
        bouton_start = QPushButton('Start', self)
        bouton_stop = QPushButton('Stop', self)
        bouton_reset = QPushButton('Reset', self)
        bouton_connect = QPushButton('Connect', self)
        bouton_quitter = QPushButton('Quitter', self)

        # Ajouter les boutons à la mise en page
        layout_boutons.addWidget(bouton_start, 0, 0)
        layout_boutons.addWidget(bouton_stop, 0, 1)
        layout_boutons.addWidget(bouton_reset, 1, 0)
        layout_boutons.addWidget(bouton_connect, 1, 1)
        layout_boutons.addWidget(bouton_quitter, 2, 0, 1, 2)

        # Connecter les signaux des boutons à des emplacements spécifiques
        bouton_start.clicked.connect(self.start_compteur)
        bouton_stop.clicked.connect(self.stop_compteur)
        bouton_reset.clicked.connect(self.reset_compteur)
        bouton_connect.clicked.connect(self.connect_to_edit)
        bouton_quitter.clicked.connect(self.quit_application)

        # Ajouter le compteur à la mise en page
        layout_principal.addWidget(self.label_compteur)
        layout_principal.addWidget(self.label_affichage)
        layout_principal.addLayout(layout_boutons)
        layout_principal.addWidget(self.edit_connect)

        self.setLayout(layout_principal)
        self.setWindowTitle('Chronometre')
        self.timer.timeout.connect(self.add_compteur)

        self.setGeometry(300, 300, 300, 200)
        self.show()

    # Partie 2 : Bouton Start - démarrer le compteur
    def start_compteur(self):
        self.timer.start(1000)

    # Partie 3 : Bouton Stop - arrêter le compteur
    def stop_compteur(self):
        self.timer.stop()

    # Partie 3 : Bouton Reset - réinitialiser le compteur
    def reset_compteur(self):
        self.compteur = 0
        self.label_affichage.setText(str(self.compteur))

    # Partie 3 : Bouton Connect - se connecter au serveur
    def connect_to_edit(self):
        texte_edit = self.edit_connect.text()
        try:
            valeur = int(texte_edit)
            self.compteur = valeur
            self.label_affichage.setText(str(self.compteur))
        except ValueError:
            print("Mettre un nombre qui s'ajoute au compteur et connect")

    # Partie 4 : Bouton Quitter - quitter l'application
    def quit_application(self):
        self.stop_compteur()
        self.close()

    # Partie 5 : Bouton Connect (connexion au serveur)
    def connect_to_server(self):
        try:
            pass
        except Exception as e:
            # Partie 6 : Gestion des erreurs
            print(f"Erreur de connexion: {e}")

    # Partie 2 : Incrémenter le compteur et mettre à jour l'affichage
    def add_compteur(self):
        self.compteur += 1
        self.label_affichage.setText(str(self.compteur))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    sys.exit(app.exec())
