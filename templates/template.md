## Résumé des actus du {{ data[0].date }}

{% for article in data %}{{ article.summary }} ([source]({{ article.link }}))
{% endfor %}

---
