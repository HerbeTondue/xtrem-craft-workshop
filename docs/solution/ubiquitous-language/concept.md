# Concept

> Bank 

## Properties

contient des taux de change

## Responsibilities

entité covertit de l'argent dans différentes devises / contenir les taux de change

## Invariants

ne doit pas pouvoir convertir quand il manque un taux de change

## Collaborators

intérager avec le concept de Money et le concept de Portfolio

###
###
###

# Concept

> Portfolio 

## Properties

- Money 

## Responsibilities

agrégation d'argent dans différentes devises

## Invariants

lui ajouter de l'argent avec une devise et un montant
pouvoir évaluer le montant d'argent dans notre Portfolio

## Collaborators

intérager avec le concept de Money et le concept de Bank

###
###
###

# Concept

> Money 

## Properties
 - amout : float
 - currency : Currency
 
# Responsibilities
- Doit pouvoir être ajouter a une autre somme d'argent dans une même devise
- Peut etre multiplier par une val numérique 
- Peut etre diviser par une val numérique 

## Invariants

- doit toujours être positif
- le montant et la devise sont toujours obligatoire
- le montant et la devise doivent être immuables

## Collaborators
- Avec une banque 
- Avec le portefeuille 
