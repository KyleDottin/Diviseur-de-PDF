# Diviseur-de-PDF

**Outils Python pour extraire et fusionner des PDF — 100 % local, sans internet, sans tracking.**

---

## Pourquoi ce projet ?

### Les dangers des solutions en ligne
- Vos documents sont **téléversés sur des serveurs tiers**
- Aucune garantie sur le **stockage**, **l’analyse** ou la **revente** de vos données
- Même les outils "gratuits" peuvent insérer des **pixels de tracking** dans les PDF générés

### Même les outils open source ne sont pas toujours sûrs
Prenons l’exemple de **[Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)** :
- Open source
- Auto-hébergeable
- **Pourtant, une version contenait un mécanisme de tracking utilisateur**  
  → [Issue #3283](https://github.com/Stirling-Tools/Stirling-PDF/issues/3283)

> **Open source ≠ sécurisé par défaut.**  
> Un projet peut être audité, mais une **mise à jour malveillante** ou un **serveur compromis** suffit.

### Solution : **Tout se passe en local**
- **Aucune connexion internet** → vos PDF ne quittent jamais votre machine  
- **Aucun tracking** → pas de pixel, pas de log, pas de télémétrie  
- **Modification simple du registre (regedit)** → intégration fluide au clic droit  
- **Code minimaliste & transparent** → quelques dizaines de lignes, **impossible d’y dissimuler un mécanisme malveillant**

---

## Fonctionnalités

| Outil | Action | Menu contextuel |
|------|-------|-----------------|
| `Split PDF` | Extraire des pages (ex: 1-3,5,7 va extraire les pages de 1 à 3 puis la page 5 et 7) | Clic droit sur 1 PDF |

---

## Installation (Windows 11)

### 1. Prérequis
- Python 3.11 installé
- `PyPDF2` installé :
  ```bash
  py -m pip install PyPDF2

### 2. Comment activer le clic droit
- Modifier le chemin d'accès vers le code python dans le .reg
- Exécuter le .reg. 
