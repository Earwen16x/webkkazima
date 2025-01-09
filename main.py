
import csv
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

def yazdirma(isim):
    with open("myfile.csv", mode="a") as myNewFile:
        myNewFile.write(isim +"\n")

def bilgi_topla():
    for i in range(1, 21):
        driver.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[2]/table/tbody/tr[{i}]/td[3]/h4/a").click()
        try:
            profesor_ana_bilgi = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]").text
            yazdirma(profesor_ana_bilgi)
        except:
            yazdirma("Profesör ana bilgi yok")

        try:
            profesor_akedemikbilgi = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]").text
            yazdirma(profesor_akedemikbilgi)

        except:
            yazdirma("Profesör Akedemik bilgi yok")

        try:
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/a").click()
            kitaplar = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]").text
            yazdirma(kitaplar)
        except:
            message = "Kitaplar sayfası yok ééé!!!!!"
            yazdirma(message)
        try:
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/ul/li[3]/a").click()
            makaleler = driver.find_element(By.TAG_NAME,"strong").text
            yazdirma("MAKALELER")
            yazdirma(makaleler)

        except:
            message = "Makaleler sayfası yok ééé!!!"
            yazdirma(message)

        try:
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/ul/li[4]/a").click()
            bildiriler = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div/div[1]/table/tbody").text
            yazdirma("BİLDİRİLER")
            yazdirma(bildiriler)

        except:
            message = "Bildiriler sayfası yok !!!"

            yazdirma(message)

        try:
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/ul/li[5]/a").click()
            projeler = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div[1]/div").text
            yazdirma("PROJELER")
            yazdirma(projeler)

        except:
            message = "Proje sayfası yok ya da uluşılamadı"
            yazdirma(message)

        try:
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/ul/li[6]/a").click()
            dersler1 = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div[1]").text
            yazdirma("DERSLER")
            yazdirma(dersler1)

        except:
            message = "Dersler1 sayfası yok ya da ders yok"
            yazdirma(message)

        try:
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/h4/a").click()
            time.sleep(0.5)
            dersler2 = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div[2]").text
            yazdirma(dersler2)

        except:
            message = "Dersler2 sayfası yok ya da ders yok"
            yazdirma(message)

        try:
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div[3]/div[1]/h4/a").click()
            time.sleep(0.5)
            dersler3 = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div[3]").text
            yazdirma(dersler3)

        except:
            message = "Dersler 3 sayfası yok"
            yazdirma(message)

        try:
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div/div[2]/ul/li[7]/a").click()
            tezler = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div[1]").text
            yazdirma("TEZLER")
            yazdirma(tezler)

        except:
            message="tez yok"
            yazdirma(message)

        try:
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/h4/a").click()
            time.sleep(0.5)
            tezler2 = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div[2]").text
            yazdirma(tezler2)

        except:
            message = "tezler 2 yok"
            yazdirma(message)

        driver.get(base_url)


sayfa_tekrar_sayisi = 0

for i in range(2,3):
    bilgi_topla()
    pagination_element = driver.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[2]/ul/li[{i}]/a")
    pagination_element.click()

sayfa_tekrar_sayisi = sayfa_tekrar_sayisi+1

while sayfa_tekrar_sayisi <11:
    for i in range(3, 13):
        pagination_element = driver.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[2]/ul/li[{i}]/a")
        pagination_element.click()
        bilgi_topla()
    sayfa_tekrar_sayisi = sayfa_tekrar_sayisi + 1



































