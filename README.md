📩 ThylTech Mail Puller - Intégration Discord

🔥 Description

ThylTech Mail Puller est un script Python permettant de récupérer automatiquement les e-mails des clients et prospects de ThylTech et de les afficher directement dans le serveur Discord de l'équipe projet. Cela permet à toute l'équipe d'avoir une vision centralisée des nouveaux messages entrants en temps réel.

🚀 Fonctionnalités

Connexion à une boîte mail via IMAP

Récupération des e-mails non lus

Affichage des e-mails dans un canal Discord prédéfini

Exécution automatique toutes les 60 secondes

Sécurisation des identifiants via un fichier .env

🛠 Prérequis

Avant d'exécuter le script, assurez-vous d'avoir :

Python 3.x installé

Un serveur Discord avec un bot configuré

Un compte mail compatible IMAP

Un fichier .env contenant les identifiants (voir ci-dessous)

📦 Installation

Clonez ce repo :

git clone https://github.com/Yns1000/thyltech-pull-mail.git
cd thyltech-pull-mail

Installez les dépendances :

pip install -r requirements.txt

Créez un fichier .env à la racine du projet et ajoutez vos informations sensibles :

DISCORD_TOKEN=Votre_Token_Discord
DISCORD_CHANNEL_ID=ID_du_Canal_Discord
IMAP_SERVER=imap.votremail.com
EMAIL_ACCOUNT=votre@email.com
EMAIL_PASSWORD=VotreMotDePasse

▶ Utilisation

Lancez le script en exécutant :

python main.py

Le bot se connectera à votre serveur mail, récupérera les e-mails non lus et les enverra dans le canal Discord configuré.

❗ Remarque

Pensez à ne jamais partager votre fichier .env ou vos identifiants sur GitHub !
Ajoutez-le à votre fichier .gitignore pour éviter qu'il ne soit suivi par Git.

💡 Améliorations futures

Ajout d'un filtre pour n'afficher que certains types d'e-mails

📝 Licence

Projet interne ThylTech - Tous droits réservés.
