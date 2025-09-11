import gdown

url = "https://docs.google.com/spreadsheets/d/1P9EfZ3nWMFqp7q04alhIatXZRWWodirq/edit?usp=sharing"
output = '../data/raw/raw.csv'

gdown.download(url, output, quiet=False, fuzzy=True)