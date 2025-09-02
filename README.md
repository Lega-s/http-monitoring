# gugl-monitoring

## Beschreibung
Dieses Projekt ist ein einfaches Monitoring-Dashboard, das die Antwortzeiten von google.com überwacht und visualisiert. Die Daten werden regelmäßig erfasst und in einer CSV-Datei gespeichert. Mit Dash und Plotly werden die Latenzen in einem interaktiven Webinterface dargestellt, inklusive Filtermöglichkeiten nach Zeitbereichen und Fehleranzeige.

## CSV Bearbeiten

Die srv.py Datei wird verwendet als Funktion für die CSV-Datei, das man neue Logs innerhalb des netzwerkes schreiben kann mit einer simplen HTTP Request was man direkt in das app.py integrieren kann. Diese Funktion braucht es nur auf einem Client der die CSV-Datei verwaltet.

### HTTP-Methode

```cmd
[POST]  http://192.168.1.116:5000/log  (IP muss natürlich angepasst werden)
```
```json
{
  "timestamp": "2025-09-01 12:35:00",
  "latency_ms": 520,
  "error": "HTTPConnectionPool(host='userproxy.pnet.ch', port=3128): Max retries exceeded with url: http://www.google.com/"
}
```

## Installation

### Repository Clonen

Wenn git auf dem Client installiert ist kann man das Repository einfach wie unten gezeigt clonen wenn nicht kann man das dies einfach über die Weboberfläche machen also die Files Herunterladen.

```cmd
git clone https://github.com/Lega-s/http-monitoring/
cd http-monitoring
```

### Python 

Für das Projekt braucht man zwingen Python das man online im ITShop bestellen kann, das ist das einzige was man braucht das Deployment.

### Artifactory setzen

Für das man alle benötigten Librarys installieren kann muss man die pip config auf das Interne Artifactory setzen das geht mit volgendem Befehl:


```python
pip config set --user global.index-url https://artifactory.tools.post.ch/artifactory/api/pypi/python-virtual/simple
```
### Librarys Installieren 

- Dash für das Webinterface
- Plotly für die Visualisierung
- Pandas für die Datenverarbeitung
- Requests für die Messungen
- Flask für die Rest-API

```cmd
pip install requests pandas plotly dash flask
```

### Run the Script

Für einen Client der nur daten liefern soll braucht es nur 1 File (file gibt es noch nicht...) das man mit folgendem Befehl starten kann:

```cmd
py app.py
```
