# 📌 Guide d'installation et d'utilisation de Mosquitto et MQTT Explorer

Ce guide explique comment installer Mosquitto et MQTT Explorer sur **Windows, Linux et macOS**, configurer Mosquitto, ouvrir les ports nécessaires, lire les messages avec MQTT Explorer et exécuter un script Python pour interagir avec MQTT.

---

## 🛠️ 1. Prérequis : Installation de Mosquitto et MQTT Explorer

### 📌 Installer Mosquitto (Serveur MQTT)
#### 🔹 Sur **Linux (Debian/Ubuntu)**
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients -y
```

#### 🔹 Sur **Windows**
1. Télécharger Mosquitto depuis : [Mosquitto MQTT](https://mosquitto.org/download/)
2. Exécuter l'installateur et cocher **Mosquitto Service** pour qu’il démarre automatiquement.

#### 🔹 Sur **macOS** (via Homebrew)
```bash
brew install mosquitto
```

---

### 📌 Installer MQTT Explorer
#### 🔹 Sur **Windows, Linux et macOS**
1. Télécharger **MQTT Explorer** depuis : [http://mqtt-explorer.com/](http://mqtt-explorer.com/)
2. Installer l'application et l'ouvrir.

---

## ⚙️ 2. Configuration de Mosquitto

### 📌 Modifier le fichier de configuration de Mosquitto
#### 🔹 Sur **Linux et macOS**
1. Ouvrir le fichier de configuration avec :
   ```bash
   sudo nano /etc/mosquitto/mosquitto.conf
   ```
2. Ajouter/modifier les lignes suivantes :
   ```ini
   listener 1883  # Port MQTT
   allow_anonymous true  # Autorise les connexions sans authentification
   log_type all  # Active tous les logs pour le debug
   persistence true  # Sauvegarde les messages persistants
   ```
3. Enregistrer (`CTRL+X`, `Y`, `Enter`).

#### 🔹 Sur **Windows**
1. Ouvrir `C:\Program Files\mosquitto\mosquitto.conf` avec un éditeur de texte (Notepad++, VS Code…).
2. Ajouter les mêmes lignes que ci-dessus.

### 📌 Redémarrer Mosquitto pour appliquer les modifications
#### 🔹 Sur **Linux/macOS**
```bash
sudo systemctl restart mosquitto
sudo systemctl enable mosquitto
```
#### 🔹 Sur **Windows** (Invite de commande en administrateur)
```powershell
net stop mosquitto
net start mosquitto
```

### 📌 Vérifier que Mosquitto fonctionne
#### 🔹 Sur **Linux/macOS**
```bash
sudo systemctl status mosquitto
```
#### 🔹 Sur **Windows**
```powershell
sc query mosquitto
```

---

## 🔓 3. Ouvrir les ports pour Mosquitto

### 📌 Sur **Linux (Ubuntu/Debian) avec UFW**
```bash
sudo ufw allow 1883/tcp
```

### 📌 Sur **Windows** (via PowerShell en administrateur)
```powershell
New-NetFirewallRule -DisplayName "Mosquitto MQTT" -Direction Inbound -Protocol TCP -LocalPort 1883 -Action Allow
```

### 📌 Sur **macOS**
```bash
sudo pfctl -F all
sudo pfctl -E
```

---

## 🕵️ 4. Lire les messages avec MQTT Explorer

### 📌 Configuration de MQTT Explorer
1. Ouvrir **MQTT Explorer**.
2. Ajouter une nouvelle connexion en renseignant :
   - **Host** : `votre ip`
   - **Port** : `1883`
   - **Client ID** : `mqtt-explorer`
3. Cliquer sur **Connect**.
4. Dans l'interface, souscrire au topic `maison/#` pour voir tous les messages.

---

## 🐍 5. Exécuter et tester le script Python MQTT

### 📌 Installer Python et les dépendances
#### 🔹 Sur **Linux/macOS**
```bash
sudo apt install python3 python3-pip -y  # Linux
brew install python3  # macOS
pip3 install paho-mqtt
```

#### 🔹 Sur **Windows**
1. Télécharger Python depuis : [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Pendant l'installation, cocher **Add Python to PATH**.
3. Installer les dépendances :
   ```powershell
   pip install paho-mqtt
   ```

### 📌 Lancer le script Python
#### 🔹 Sur **Linux/macOS**
```bash
python3 mqtt_domotique.py
```

#### 🔹 Sur **Windows**
```powershell
python mqtt_domotique.py
```

---

## 🎯 6. Tester l'envoi de messages MQTT

### 📌 Envoyer un message de test via MQTT Explorer ou Terminal

#### 🖥️ **Avec Mosquitto (Terminal)**
##### 🔹 Sur **Linux/macOS**
```bash
mosquitto_pub -h 10.70.4.114 -t maison/salon -m '{"name": "lampadaire", "instruction": "allumer"}'
```
##### 🔹 Sur **Windows** (Invite de commande dans le dossier Mosquitto)
```powershell
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

