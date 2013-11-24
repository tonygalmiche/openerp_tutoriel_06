InfoSaône / OpenERP Tutoriel 06 - Ajout d'un champ sur un objet
===================

Le but de ce module est de montrer comment ajouter un champ sur un objet existant.

Ce module installe le module CRM pour pouvoir modifier le modèle des clients (partner).

Cet exemple ajoute le champ `prenom` au modèle `partner` : 
* Le fichier `infosaone_partner.py` contient la descrition du champ `prenom` à ajouter au modèle.
* Le fichier `__init__.py` permet de charger le fichier python `infosaone_partner.py`
* Le fichier `infosaone_partner_view.xml` contient la modification de la vue des `partner` pour ajouter le `prenom`


![openerp_tutoriel_06.png](https://raw.github.com/tonygalmiche/openerp_tutoriel_06/master/static/src/img/openerp_tutoriel_06.png) 
