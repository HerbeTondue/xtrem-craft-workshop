# Example Mapping

## Format de restitution
*(rappel, pour chaque US)*

```markdown
## Titre de l'US (post-it jaunes)

> Question (post-it rouge)

### Règle Métier (post-it bleu)

Exemple: (post-it vert)

- [ ] 5 USD + 10 EUR = 17 USD
```

Vous pouvez également joindre une photo du résultat obtenu en utilisant les post-its.

## Story 1: Define Pivot Currency

```gherkin
As a Foreign Exchange Expert
I want to be able to define a Pivot Currency
So that I can express exchange rates based on it
```

```markdown
## Titre de l'US (post-it jaunes)

As a Foreign Exchange Expert
I want to be able to define a Pivot Currency
So that I can express exchange rates based on it

### Règle Métier (post-it bleu)
- Pouvoir définir une devise pivot
- Pouvoir modifier la devise pivot
- Pouvoir calculer à partir de la devise pivot vers une autre devise

### Exemples (post-it vert)
- EUR as Pivot Currency -> 1.2 exchange rate to USD = 12USD -> 10EUR
- USD as Pivot Currency : EUR -> KRW but i don't know the exchange rate. I know the exchange rate between USD and KRW is 1000 and between USD and EUR is 1.2 so if i have 10EUR i can convert it to 12USD and then to 12000KRW

### Questions (post-it rose)
- Est-il possible de définir plusieurs devises pivot ? Si non, n'est ce pas risqué si notre devise pivot devient défaillante ?
- Est-ce qu'il y a des devises qui ne peuvent pas être la devise pivot ? Et au contraire, des devises plus intéressantes à mettre en pivot que d'autres ?
```

## Story 2: Add an exchange rate
```gherkin
As a Foreign Exchange Expert
I want to add/update exchange rates by specifying: a multiplier rate and a currency
So they can be used to evaluate client portfolios
```

```markdown
## Titre de l'US (post-it jaunes)

As a Foreign Exchange Expert
I want to add/update exchange rates by specifying: a multiplier rate and a currency
So they can be used to evaluate client portfolios

### Règle Métier (post-it bleu)
- Pouvoir ajouter des taux de change avec la devise et un taux de change multiplicateur
- Pouvoir modifier un taux de change existant

### Exemples (post-it vert)
- EUR -> USD : exchange rate = 1.2
- USD -> KRW : exchange rate = 1000

### Questions (post-it rose)
```

## Story 3: Convert a Money

```gherkin
As a Bank Consumer
I want to convert a given amount in currency into another currency
So it can be used to evaluate client portfolios
```
```markdown
## Titre de l'US (post-it jaunes)

As a Bank Consumer
I want to convert a given amount in currency into another currency
So it can be used to evaluate client portfolios

### Règle Métier (post-it bleu)
- Pouvoir convertir dans la même devise sans taux de change
- La conversion vers la devise pivot doit multiplier le montant de 1/taux de change 
- Convertir à partir de la devise pivot vers une autre devise doit multiplier le montant par le taux de change
- Quand on doit convertir entre 2 devises qui ne sont pas la devise pivot, on doit utiliser la devise pivot

### Exemples (post-it vert)
- 10.254 KRW to KRW -> 10.254 KRW
- EUR as Pivot Currency -> 1.2 exchange rate to USD = 12USD -> 10EUR
- EUR as Pivot Currency -> 1.2 exchange rate to USD = 10EUR -> 12USD

### Questions (post-it rose)
- Comment peut-on arrondir les montants ?
```


