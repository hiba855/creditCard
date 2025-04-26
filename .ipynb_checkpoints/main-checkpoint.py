import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

class WelcomeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Détection de Fraude Bancaire")
        self.setWindowState(self.windowState() | Qt.WindowMaximized)

        # ----- Navbar -----
        navbar = QWidget()
        navbar.setStyleSheet("background-color: #ffffff; padding: 10px 20px; margin-top:25px;")
        navbar.setFixedHeight(120)
        navbar_layout = QHBoxLayout()

        title_label = QLabel("FraudSafe")
        title_label.setFont(QFont("Courier New", 25))
        title_label.setStyleSheet("color: #dec930;")
        navbar_layout.addWidget(title_label)

        # Espace entre le titre et le bouton
        navbar_layout.addStretch()

        # Bouton à droite (sans action)
        nav_button = QPushButton("Charger un fichier")
        nav_button.setStyleSheet("""
            background-color: #eccd55;
            color: white;
            font-size: 30px;
            border: none;
            font-family: Courier New;
            border-radius: 22px;
            padding: 8px 20px;
            margin-right:75px;
        """)
        nav_button.setFixedHeight(87)
        nav_button.setCursor(Qt.PointingHandCursor)
        navbar_layout.addWidget(nav_button)

        navbar.setLayout(navbar_layout)

        # ----- Contenu principal -----
        content = QWidget()
        content_layout = QHBoxLayout()  # Utilise QHBoxLayout pour aligner horizontalement le texte et l'image

        # Texte de bienvenue à gauche
        welcome_label = QLabel("Bienvenue sur notre \nplateforme de détection \nde fraudes bancaires ")
        welcome_label.setFont(QFont("Courier New", 29))
        welcome_label.setAlignment(Qt.AlignLeft)
        welcome_label.setStyleSheet("margin-top: 194px; padding-left: 30px;")

        # Texte en gris sous le texte de bienvenue
        subtitle_label = QLabel("Protégez vos transactions et détectez \nles anomalies en temps réel")
        subtitle_label.setFont(QFont("Courier New", 18))
        subtitle_label.setAlignment(Qt.AlignLeft)
        subtitle_label.setStyleSheet("color: #555555; padding-left: 30px; margin-top: 0px;")  # Réduit la marge entre les deux

        # Crée un QVBoxLayout pour empiler le texte et le texte en gris
        text_layout = QVBoxLayout()
        text_layout.addWidget(welcome_label)
        text_layout.addWidget(subtitle_label)
        text_layout.setSpacing(0)  # Supprime l'espacement entre les deux labels

        # Image à droite
        image_label = QLabel()
        pixmap = QPixmap("image.png")  # Remplace "image.png" par le chemin de ton image
        image_label.setPixmap(pixmap.scaled(890, 710, Qt.KeepAspectRatio))  # Ajuste la taille de l'image si nécessaire

        # Crée un espacement explicite à droite de l'image
        spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)  # Espace expansible à droite

        # Ajoute le texte à gauche et l'image à droite
        content_layout.addLayout(text_layout)  # Ajoute les textes à gauche
        content_layout.addStretch()  # Espacement entre l'image et le texte
        content_layout.addWidget(image_label)  # Ajoute l'image à droite
        content_layout.addItem(spacer)  # Ajoute un espace après l'image

        content.setLayout(content_layout)

        # ----- Layout général -----
        main_layout = QVBoxLayout()
        main_layout.addWidget(navbar)
        main_layout.addWidget(content)

        container = QWidget()
        container.setLayout(main_layout)
        container.setStyleSheet("background-color: white;")

        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeApp()
    window.show()
    sys.exit(app.exec_())
