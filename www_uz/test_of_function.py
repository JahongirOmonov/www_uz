from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://kun.uz")

assert "O‘zbekiston va jahon yangiliklari, eng so‘nggi tezkor xabarlar, qiziqarli maqola, intervyu, foto va video materiallar - KUN.UZ" in browser.title
print("OK")
