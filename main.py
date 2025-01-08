

from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()

#Siteye ulaştık
driver.get("https://akademik.yok.gov.tr/AkademikArama/AkademisyenArama?islem=_2oe51n-Xm-NEy9bBcUysZwOklyFNc3AjFbWZgZKgsTGrwTClGJU9GpHP-_2xehJ")
base_url = driver.current_url

sayfa_tekrar_sayisi = 0
'''
for i in range(2,12):
    pagination_element = driver.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[2]/ul/li[{i}]/a")
    pagination_element.click()
sayfa_tekrar_sayisi = sayfa_tekrar_sayisi+1

while sayfa_tekrar_sayisi <12:
    for i in range(3, 13):
        pagination_element = driver.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[2]/ul/li[{i}]/a")
        pagination_element.click()
    sayfa_tekrar_sayisi = sayfa_tekrar_sayisi + 1
'''


def bilgi_topla():
    for i in range(1, 21):
        driver.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[2]/table/tbody/tr[{i}]/td[3]/h4/a").click()
        profesor_ana_bilgi = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]").text
        print(profesor_ana_bilgi)
        profesor_akedemikbilgi = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]").text
        print(profesor_akedemikbilgi)

        try:
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/a").click()
            kitaplar = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]").text
            print(kitaplar)
        except:
            print("Kitaplar sayfası yok ééé!!!!!")

        #en son kitapları çektim

        driver.get(base_url)




bilgi_topla()

























