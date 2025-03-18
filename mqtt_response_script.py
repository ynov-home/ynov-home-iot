import paho.mqtt.client as mqtt
import json

# Configuration du broker MQTT
BROKER_ADDRESS = "10.70.4.114" # IP à remplacer par celle de votre serveur 
PORT = 1883
TOPIC_SUBSCRIBE = "maison/#"  # Écoute tous les sous-topics de maison

# Stocker l'état des appareils sous forme de dictionnaire
appareils_status = {}

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connecté au broker MQTT")
        client.subscribe(TOPIC_SUBSCRIBE)  # S'abonner à tous les sous-topics de "maison"
    else:
        print("❌ Échec de connexion, code de retour :", rc)

def on_message(client, userdata, msg):
    try:
        topic_levels = msg.topic.split("/")  # Découper le topic reçu
        if len(topic_levels) != 2 and not msg.topic.endswith("/status"):  
            print(f"⚠️ Message ignoré, format incorrect: {msg.topic}")
            return
        
        if msg.topic.endswith("/status"):  # Ignorer les messages de statut envoyés par nous-mêmes
            print(f"✅ Confirmation de mise à jour: {msg.topic} -> {msg.payload.decode('utf-8')}")
            return

        piece = topic_levels[1]  # Extraire uniquement la pièce depuis le topic
        payload = json.loads(msg.payload.decode("utf-8"))  # Charger le JSON du message

        # Vérifier si le message contient un nom d'appareil et une instruction
        if "name" in payload and "instruction" in payload:
            appareil = payload["name"]
            instruction = payload["instruction"]

            # Mettre à jour l'état de l'appareil
            if instruction == "allumer":
                appareils_status[(piece, appareil)] = "on"
            elif instruction == "eteindre":
                appareils_status[(piece, appareil)] = "off"
            else:
                print(f"⚠️ Instruction inconnue: {instruction}")
                return
        else:
            print(f"⚠️ Message JSON incorrect: {msg.payload}")
            return

        # Construire le topic de réponse
        topic_reponse = f"maison/{piece}/{appareil}/status"
        status_message = json.dumps({"status": appareils_status[(piece, appareil)]})

        # Publier l'état mis à jour
        client.publish(topic_reponse, status_message)
        print(f"✅ {appareil} dans {piece} mis à jour: {appareils_status[(piece, appareil)]} (→ {topic_reponse})")

    except json.JSONDecodeError:
        print("❌ Erreur de décodage du message MQTT")

# Configuration du client MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, PORT, 60)
client.loop_forever()