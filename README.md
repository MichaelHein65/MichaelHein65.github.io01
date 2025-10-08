# Stadt01 PHP-Anwendung

`Stadt01.html` stellt eine kleine PHP-Anwendung dar, die Informationen zu einer Stadt aus Wikipedia ausliest und eine Karte via Google Maps einbettet. Zusätzlich gibt es unter `index.html` eine bildbasierte Galerie, in der eigene Fotos ausgewählt, betrachtet und als Video exportiert werden können.

## Voraussetzungen
- PHP ab Version 7.0
- Ein Google-Maps-API-Key (in `Stadt01.html` beim Parameter `key` im IFrame eintragen)

## Anwendung Stadt01
1. Lokalen PHP-Server starten, z.B.:
   ```bash
   php -S localhost:8000
   ```
2. Die Seite `Stadt01.html` im Browser aufrufen.

Nach Eingabe einer Stadt werden Wikipedia-Daten geladen und auf der Seite angezeigt. Gleichzeitig erscheint eine Karte mit dem angegebenen Ort.

## Anwendung Bildgalerie (`index.html`)
1. Die Datei `index.html` direkt im Browser öffnen **oder** im Projektverzeichnis einen kleinen Webserver starten, zum Beispiel
   ```bash
   python3 -m http.server 8000
   ```
   und anschließend `http://localhost:8000/index.html` im Browser aufrufen.
2. Über die Schaltfläche **Bilder auswählen** die gewünschten Bilddateien wählen. Sie werden lokal im Browser gespeichert und bleiben somit auch nach einem Neustart erhalten.
3. Ein Bild in der Liste anklicken, um es in der großen Ansicht mit Maus-Zoom und -Verschiebung zu betrachten.
4. Optional mit **Video erstellen** ein automatisch animiertes WebM-Video aus den geladenen Bildern erzeugen und herunterladen.

## Dateien herunterladen
- **Direkter Download:** Auf GitHub oben rechts auf **Code** klicken und **Download ZIP** wählen. Das heruntergeladene Archiv entpacken und die Dateien lokal verwenden.
- **Mit Git:**
  ```bash
  git clone https://github.com/MichaelHein65/MichaelHein65.github.io01.git
  ```
  Dadurch erhalten Sie eine lokale Kopie, die Sie jederzeit mit `git pull` aktualisieren können.
