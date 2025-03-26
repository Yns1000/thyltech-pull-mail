import asyncio
import email
import imaplib
from email.header import decode_header
import os
from dotenv import load_dotenv

import discord

# Charger les variables d'environnement
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
IMAP_SERVER = os.getenv("IMAP_SERVER")
EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def check_email():
    """Vérifie les nouveaux emails toutes les 60 secondes."""
    while True:
        try:
            mail = imaplib.IMAP4_SSL(IMAP_SERVER)
            mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
            mail.select("inbox")

            status, messages = mail.search(None, "UNSEEN")
            message_ids = messages[0].split()

            if message_ids:
                for msg_id in message_ids:
                    status, msg_data = mail.fetch(msg_id, "(RFC822)")
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_bytes(response_part[1])
                            subject, encoding = decode_header(msg["Subject"])[0]
                            if isinstance(subject, bytes):
                                subject = subject.decode(encoding if encoding else "utf-8")

                            sender = msg["From"]

                            channel = client.get_channel(CHANNEL_ID)
                            if channel:
                                await channel.send(
                                    f"📩 **Nouveau mail reçu !**\n\n📧 **Expéditeur :** {sender}\n📌 **Sujet :** {subject}")

            mail.close()
            mail.logout()
        except Exception as e:
            print(f"Erreur lors de la vérification des emails : {e}")

        await asyncio.sleep(60*30)  # Vérifie toutes les 30 secondes


@client.event
async def on_ready():
    print(f"{client.user} est connecté.")
    client.loop.create_task(check_email())


client.run(TOKEN)