import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = 'a sweet, orange, citrus fruit'
    fruit['apple'] = 'good for making cider'
    fruit['lemon'] = 'a sweet, orange, citrus fruit'
    fruit['grape'] = 'a sweet, orange, citrus fruit'
    fruit['lime'] = 'a sweet, orange, citrus fruit'