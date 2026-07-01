# Hetzner VPS Deployment Reference

Complete guide for deploying a React + Vite + Supabase app on a Hetzner Cloud VPS. Written for non-developers using Claude Code — every step is a concrete command or Claude Code prompt.

**When to use Hetzner instead of Railway:**
- You want full server control (custom software, cron jobs, multiple apps)
- Lower monthly cost for multiple services (~4-10 EUR vs. 5-20 USD per service)
- Data residency requirements (Hetzner has datacenters in Germany and Finland)
- You already have a Hetzner account

**When NOT to use Hetzner:**
- You want zero server management → use Railway
- You need the simplest possible deployment → use Railway
- You're uncomfortable with the idea of a server you maintain → use Railway

---

## Architecture overview

```
User Browser
    ↓
Caddy (reverse proxy + automatic SSL)
    ↓
Node.js / Vite static files (port 3000)
    ↓
Supabase Cloud (database, auth, storage — same as Railway setup)
```

Key difference to Railway: You manage the server yourself. Caddy handles SSL automatically (like Railway does behind the scenes), and PM2 keeps your app running.

---

## Phase A: Server bestellen (Hetzner Cloud Console)

### Step 1: Account erstellen
1. Gehe zu https://console.hetzner.cloud/
2. Registrieren mit E-Mail
3. Zahlungsmethode hinzufügen

### Step 2: Server erstellen
1. "Add Server" klicken
2. Einstellungen:

| Einstellung | Empfehlung | Warum |
|-------------|-----------|-------|
| Location | Falkenstein (fsn1) oder Nürnberg (nbg1) | Nah an Zürich, niedrige Latenz |
| Image | Ubuntu 24.04 | LTS, guter Support |
| Type | CX22 (2 vCPU, 4 GB RAM) | Reicht für 1-3 Apps |
| SSH Key | Neu erstellen (siehe unten) | Sicherer als Passwort |
| Networking | IPv4 + IPv6 | IPv4 für Custom Domain |
| Name | z.B. `app-server-01` | Frei wählbar |

Kosten: ~4.35 EUR/Monat für CX22.

### Step 3: SSH Key erstellen (einmalig)

Wenn du noch keinen SSH Key hast, erstelle einen auf deinem Mac:

```bash
ssh-keygen -t ed25519 -C "deine@email.com"
```

Drücke 3x Enter (Standard-Pfad, kein Passwort). Dann den öffentlichen Key kopieren:

```bash
cat ~/.ssh/id_ed25519.pub
```

Diesen Text in der Hetzner Console unter "SSH Keys" einfügen.

### Step 4: Server IP notieren

Nach dem Erstellen zeigt Hetzner die IPv4-Adresse an, z.B. `78.46.123.45`. Diese brauchst du für DNS und SSH.

---

## Phase B: Server einrichten (Claude Code Session-Prompt)

Diesen Prompt in eine frische Claude Code Session kopieren. Claude Code richtet den kompletten Server ein.

````
Du richtest einen frischen Hetzner Ubuntu 24.04 Server ein für eine React + Vite Web-App.

Server-IP: [HIER IP EINSETZEN]
Domain: app.[domain.tld]
App-Name: [app-name]

Verbinde dich per SSH und führe folgende Schritte aus:

1. **System aktualisieren**
   ```bash
   ssh root@[IP]
   apt update && apt upgrade -y
   ```

2. **Non-root User erstellen** (sicherer als root)
   ```bash
   adduser deploy
   usermod -aG sudo deploy
   mkdir -p /home/deploy/.ssh
   cp ~/.ssh/authorized_keys /home/deploy/.ssh/
   chown -R deploy:deploy /home/deploy/.ssh
   chmod 700 /home/deploy/.ssh
   chmod 600 /home/deploy/.ssh/authorized_keys
   ```

3. **Firewall einrichten**
   ```bash
   ufw allow OpenSSH
   ufw allow 80
   ufw allow 443
   ufw enable
   ```

4. **Node.js 20 LTS installieren**
   ```bash
   curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
   apt install -y nodejs
   node --version  # sollte v20.x zeigen
   ```

5. **PM2 installieren** (hält die App am Laufen)
   ```bash
   npm install -g pm2
   ```

6. **Caddy installieren** (Webserver + automatisches SSL)
   ```bash
   apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
   curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
   curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
   apt update
   apt install caddy
   ```

7. **App-Verzeichnis erstellen**
   ```bash
   mkdir -p /var/www/[app-name]
   chown deploy:deploy /var/www/[app-name]
   ```

8. **Caddy konfigurieren**
   Erstelle /etc/caddy/Caddyfile:
   ```
   app.[domain.tld] {
       root * /var/www/[app-name]/dist
       file_server
       try_files {path} /index.html
       encode gzip
   }
   ```
   Das `try_files` ist wichtig für React Router (SPA).

9. **Caddy neu starten**
   ```bash
   systemctl restart caddy
   systemctl enable caddy
   ```

10. **Git auf dem Server installieren** (falls nicht vorhanden)
    ```bash
    apt install -y git
    ```

Prüfe am Ende:
- `node --version` → v20.x
- `pm2 --version` → installiert
- `caddy version` → installiert
- `ufw status` → active, ports 22/80/443 offen
- `curl localhost` → Caddy default page
````

---

## Phase C: DNS konfigurieren

Beim Domain-Registrar (z.B. Infomaniak) diese DNS-Einträge setzen:

| Typ | Host | Wert | TTL |
|-----|------|------|-----|
| A | `app` | `[Server-IP]` | 3600 |

Kein CNAME nötig (wie bei Railway) — bei Hetzner hast du eine feste IP.

Nach 10-60 Minuten DNS-Propagation ist `app.[domain.tld]` erreichbar. Caddy holt sich automatisch ein SSL-Zertifikat von Let's Encrypt.

---

## Phase D: App deployen

### Variante 1: Manuelles Deployment (einfach, für den Anfang)

Auf deinem lokalen Rechner:

```bash
# 1. App bauen
cd ~/Documents/[app-name]
npm run build

# 2. Build-Ordner auf Server kopieren
scp -r dist/ deploy@[IP]:/var/www/[app-name]/

# 3. Fertig — Caddy serviert die neuen Dateien sofort
```

### Variante 2: Git-basiertes Deployment (empfohlen ab Tag 2)

Einmalig auf dem Server einrichten — danach deployest du mit `git push`:

**Auf dem Server (als deploy-User):**

```bash
# Bare Git Repo erstellen
mkdir -p /home/deploy/repos/[app-name].git
cd /home/deploy/repos/[app-name].git
git init --bare

# Post-receive Hook erstellen (baut und deployed automatisch)
cat > hooks/post-receive << 'HOOK'
#!/bin/bash
APP_DIR=/var/www/[app-name]
REPO_DIR=/home/deploy/repos/[app-name].git
TEMP_DIR=/tmp/[app-name]-build

echo "==> Deployment gestartet..."

# Checkout in temporäres Verzeichnis
rm -rf $TEMP_DIR
git --work-tree=$TEMP_DIR --git-dir=$REPO_DIR checkout -f

# Build
cd $TEMP_DIR
npm install
npm run build

# Build-Ergebnis kopieren
rm -rf $APP_DIR/dist
cp -r dist/ $APP_DIR/

echo "==> Deployment abgeschlossen!"
HOOK

chmod +x hooks/post-receive
```

**Auf deinem lokalen Rechner (einmalig):**

```bash
cd ~/Documents/[app-name]
git remote add hetzner deploy@[IP]:/home/deploy/repos/[app-name].git
```

**Ab jetzt deployen mit:**

```bash
git push hetzner main
```

Das ist das Äquivalent zu Railwayss Auto-Deploy — nur dass du `git push hetzner main` statt `git push origin main` schreibst. (Du kannst beides machen: `origin` für GitHub Backup, `hetzner` für Deployment.)

---

## Phase E: Umgebungsvariablen

Auf dem Server als deploy-User:

```bash
# .env Datei im App-Verzeichnis erstellen
cat > /var/www/[app-name]/.env << 'EOF'
VITE_SUPABASE_URL=https://[project-ref].supabase.co
VITE_SUPABASE_ANON_KEY=eyJ...
EOF
```

Für Vite-Apps: `VITE_`-Variablen werden zur Build-Zeit eingebunden, nicht zur Laufzeit. Das heisst: nach Änderung muss die App neu gebaut werden.

Für den Railway-Server-Teil (Express API, Stripe Webhooks): Wenn du auch den Backend-Server auf Hetzner laufen lässt:

```bash
# PM2 mit Umgebungsvariablen starten
cd /var/www/[app-name]/server
pm2 start src/index.ts --name "[app-name]-api" --interpreter npx --interpreter-args="ts-node" -- 
pm2 save
pm2 startup  # Auto-Start nach Server-Neustart
```

Oder mit einer ecosystem.config.js:

```javascript
// /var/www/[app-name]/server/ecosystem.config.js
module.exports = {
  apps: [{
    name: '[app-name]-api',
    script: 'dist/index.js',
    env: {
      PORT: 3001,
      DATABASE_URL: 'postgresql://...',
      STRIPE_SECRET_KEY: 'sk_live_...',
      STRIPE_WEBHOOK_SECRET: 'whsec_...',
      SUPABASE_URL: 'https://[ref].supabase.co',
      SUPABASE_SERVICE_ROLE_KEY: 'eyJ...',
      ANTHROPIC_API_KEY: 'sk-ant-...',
    }
  }]
}
```

Dann: `pm2 start ecosystem.config.js`

---

## Phase F: Caddy für Backend-API erweitern

Wenn du auch einen Express-Server auf Hetzner hast (statt Railway):

```
# /etc/caddy/Caddyfile
app.[domain.tld] {
    # API-Requests zum Express Server
    handle /api/* {
        reverse_proxy localhost:3001
    }
    
    # Alles andere: statische Dateien (React App)
    handle {
        root * /var/www/[app-name]/dist
        file_server
        try_files {path} /index.html
    }
    
    encode gzip
}
```

Caddy-Reload: `systemctl reload caddy`

---

## Wartung und Monitoring

### App-Status prüfen
```bash
pm2 status          # Zeigt laufende Apps
pm2 logs [app-name] # Live-Logs
pm2 monit           # CPU/RAM Monitoring
```

### Server aktualisieren (monatlich empfohlen)
```bash
sudo apt update && sudo apt upgrade -y
```

### SSL-Zertifikat
Caddy erneuert SSL automatisch — kein manuelles Eingreifen nötig.

### Backups
Hetzner bietet automatische Backups für ~1.20 EUR/Monat. Aktivieren im Hetzner Dashboard unter Server → Backups.

### Mehrere Apps auf einem Server
Einfach weitere Blöcke in der Caddyfile:

```
app1.[domain.tld] {
    root * /var/www/app1/dist
    file_server
    try_files {path} /index.html
}

app2.[domain.tld] {
    root * /var/www/app2/dist
    file_server
    try_files {path} /index.html
}
```

Das ist der grosse Vorteil gegenüber Railway: Ein Server, beliebig viele Apps, ein Preis.

---

## Troubleshooting

| Problem | Ursache | Lösung |
|---------|---------|--------|
| SSH "Permission denied" | Key nicht auf Server | `ssh-copy-id deploy@[IP]` |
| Seite nicht erreichbar | Firewall blockiert | `ufw allow 80 && ufw allow 443` |
| SSL-Fehler | DNS noch nicht propagiert | 30-60 Min warten, dann `caddy reload` |
| App zeigt alte Version | Build nicht deployed | Neu bauen und kopieren oder `git push hetzner main` |
| "502 Bad Gateway" für /api/ | Express Server nicht gestartet | `pm2 start` prüfen |
| Server reagiert nicht | RAM voll | `htop` prüfen, ggf. grösseren Server |
| React Router 404 | try_files fehlt in Caddyfile | `try_files {path} /index.html` hinzufügen |

---

## Claude Code Prompt für Server-Einrichtung

Wenn der Skill die Hetzner-Option wählt, generiert er als **Session-Prompt 0** einen speziellen Server-Setup-Prompt. Dieser kommt VOR den Feature-Prompts und richtet den kompletten Server ein:

```
Session 0 (Hetzner): Server-Einrichtung
Session 1: Auth + Rollen
Session 2: Dashboard Layout
Session 3-N: Features (gleich wie bei Railway)
```

Der Setup-Prompt enthält alle Befehle aus Phase B-F oben, angepasst auf die konkreten Projekt-Werte (IP, Domain, App-Name).

### Täglicher Workflow mit Hetzner

```
1. Claude Code öffnen im Projektordner
2. Feature beschreiben, Claude baut es
3. Lokal testen: npm run dev → http://localhost:5173
4. Wenn es funktioniert:
   git add . && git commit -m "feat: ..." && git push hetzner main
5. Fertig — der Post-receive Hook baut und deployed automatisch
```

Identisch zum Railway-Workflow, nur `git push hetzner main` statt `git push origin main`.
