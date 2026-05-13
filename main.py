def toplamlar_ishori(toplam1, toplam2):
    kesishma = set(toplam1) & set(toplam2)
    birlashma = set(toplam1) | set(toplam2)
    farq = set(toplam1) - set(toplam2)
    return kesishma, birlashma, farq

toplam1 = [1, 2, 3, 4, 5]
toplam2 = [4, 5, 6, 7, 8]

kesishma, birlashma, farq = toplamlar_ishori(toplam1, toplam2)

print("Kesishma:", kesishma)
print("Birlashma:", birlashma)
print("Farq:", farq)
```

```python
def toplamlar_ishori(toplam1, toplam2):
    kesishma = set(toplam1) & set(toplam2)
    birlashma = set(toplam1) | set(toplam2)
    farq = set(toplam1) - set(toplam2)
    return kesishma, birlashma, farq

toplam1 = [1, 2, 3, 4, 5]
toplam2 = [4, 5, 6, 7, 8]

kesishma, birlashma, farq = toplamlar_ishori(toplam1, toplam2)

print("Kesishma:", kesishma)
print("Birlashma:", birlashma)
print("Farq:", farq)
