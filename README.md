# 📌 Guide d'installation et d'utilisation de Mosquitto et MQTT Explorer

Ce guide explique comment installer Mosquitto et MQTT Explorer, configurer Mosquitto, ouvrir les ports nécessaires, lire les messages avec MQTT Explorer et exécuter un script Python pour interagir avec MQTT.

---

## 🛠️ 1. Prérequis : Installation de Mosquitto et MQTT Explorer

### 📌 Installer Mosquitto (Serveur MQTT)
#### 🔹 Sur Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients -y
```

#### 🔹 Sur Windows
- Télécharger Mosquitto depuis : [Mosquitto MQTT](https://mosquitto.org/download/)
- Exécuter l'installateur en laissant les options par défaut.

#### 🔹 Sur macOS (via Homebrew)
```bash
brew install mosquitto
```

### 📌 Installer MQTT Explorer
1. Télécharger **MQTT Explorer** depuis : [http://mqtt-explorer.com/](http://mqtt-explorer.com/)
2. Installer l'application et l'ouvrir.

---

## ⚙️ 2. Configuration de Mosquitto

### 📌 Modifier le fichier de configuration de Mosquitto
1. Ouvrir le fichier de configuration avec un éditeur de texte :
   ```bash
   sudo nano /etc/mosquitto/mosquitto.conf  # Sur Linux/macOS
   ```
   **Ou sous Windows**, ouvrir `C:\Program Files\mosquitto\mosquitto.conf` avec un éditeur.

2. Ajouter ou modifier les lignes suivantes :
   ```ini
   listener 1883  # Port MQTT
   allow_anonymous true  # Permet les connexions sans authentification
   log_type all  # Active tous les logs pour le debug
   persistence true  # Sauvegarde les messages persistants
   ````
3. Enregistrer (`CTRL+X`, `Y`, puis `Enter`).

### 📌 Redémarrer Mosquitto pour appliquer les modifications
```bash
sudo systemctl restart mosquitto
sudo systemctl enable mosquitto
```

### 📌 Vérifier que Mosquitto fonctionne
```bash
sudo systemctl status mosquitto
```
Si Mosquitto est bien actif, vous verrez un message indiquant qu'il est en cours d'exécution.

---

## 🔓 3. Ouvrir les ports pour Mosquitto

### 📌 Sur Linux (Ubuntu/Debian) avec UFW
```bash
sudo ufw allow 1883/tcp
```

### 📌 Sur Windows (via PowerShell en administrateur)
```powershell
New-NetFirewallRule -DisplayName "Mosquitto MQTT" -Direction Inbound -Protocol TCP -LocalPort 1883 -Action Allow
```

---

## 🕵️ 4. Lire les messages avec MQTT Explorer

### 📌 Configuration de MQTT Explorer
1. Ouvrir **MQTT Explorer**.
2. Ajouter une nouvelle connexion en renseignant :
   - **Host** : `10.70.4.114`
   - **Port** : `1883`
   - **Client ID** : `mqtt-explorer`
   - **Keep Alive** : `60`
   - **Cocher : Auto Subscribe**
3. Cliquer sur **Connect**.
4. Dans l'interface, souscrire au topic `maison/#` pour voir tous les messages.

---

## 🐍 5. Exécuter et tester le script Python MQTT

### 📌 Installer Python et les dépendances
Si Python n'est pas encore installé, téléchargez-le depuis : [https://www.python.org/downloads/](https://www.python.org/downloads/)

Installer la bibliothèque MQTT avec :
```bash
pip install paho-mqtt
```

### 📌 Lancer le script Python
```bash
python mqtt_domotique.py
```

Si tout fonctionne correctement, le script écoutera les messages MQTT envoyés sur `maison/#` et répondra dynamiquement avec les états des appareils.

---

## 🎯 6. Tester l'envoi de messages MQTT

### 📌 Envoyer un message de test via MQTT Explorer ou Terminal

#### 🖥️ **Avec Mosquitto (Terminal Linux/macOS/Windows WSL)**
```bash
mosquitto_pub -h 10.70.4.114 -t maison/salon -m '{"name": "lampadaire", "instruction": "allumer"}'
```

#### 📡 **Avec MQTT Explorer**
1. Aller dans l'onglet **Publish**.
2. Saisir le **Topic** : `maison/salon`
3. Entrer le **Message** :
   ```json
   {
     "name": "lampadaire",
     "instruction": "allumer"
   }
   ```
4. Cliquer sur **Publish**.

✅ **Si tout fonctionne bien, le script Python répondra sur** `maison/salon/lampadaire/status` avec :
```json
{
  "status": "on"
}
```

---

## 🚀 Conclusion
Votre serveur Mosquitto est maintenant en place et vous pouvez envoyer/recevoir des messages MQTT facilement avec MQTT Explorer et un script Python ! 🎉

Si vous souhaitez aller plus loin, pensez à ajouter des fonctionnalités comme :
- Sécuriser Mosquitto avec un identifiant/mot de passe.
- Ajouter d'autres types d'appareils dans le script Python.

📩 **Besoin d'aide ?** N'hésitez pas à poser vos questions ! 😊
