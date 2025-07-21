# Stadt01 PHP-Anwendung

`Stadt01.html` stellt eine kleine PHP-Anwendung dar, die Informationen zu einer Stadt aus Wikipedia ausliest und eine Karte via Google Maps einbettet.

## Voraussetzungen
- PHP ab Version 7.0
- Ein Google-Maps-API-Key (in `Stadt01.html` beim Parameter `key` im IFrame eintragen)

## Anwendung
1. Lokalen PHP-Server starten, z.B.:
   ```bash
   php -S localhost:8000
   ```
2. Die Seite `Stadt01.html` im Browser aufrufen.

Nach Eingabe einer Stadt werden Wikipedia-Daten geladen und auf der Seite angezeigt. Gleichzeitig erscheint eine Karte mit dem angegebenen Ort.
