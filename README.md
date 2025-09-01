# http-monitoring

## Beschreibung
Dieses Projekt ist ein einfaches Monitoring-Dashboard, das die Antwortzeiten von google.com überwacht und visualisiert. Die Daten werden regelmäßig erfasst und in einer CSV-Datei gespeichert. Mit Dash und Plotly werden die Latenzen in einem interaktiven Webinterface dargestellt, inklusive Filtermöglichkeiten nach Zeitbereichen und Fehleranzeige.

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

```cmd
pip install requests pandas plotly dash
```
