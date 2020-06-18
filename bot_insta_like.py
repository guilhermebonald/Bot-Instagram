from selenium import webdriver
import getpass
from time import sleep

user = input('Digite o nome de usuario: ')
passw = getpass.getpass('Digite a senha: ')
tema = input('Digite pela tag que deseja buscar: ')

wd = webdriver.Chrome()


def start(wd):
    wd.get('https://www.instagram.com/')
    sleep(5)


def login(wd, user, passw):
    login = wd.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    login.click()
    login.send_keys(user)
    key = wd.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    key.click()
    key.send_keys(passw)
    button = wd.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
    button.click()
    sleep(5)
    wd.get(f'https://www.instagram.com/explore/tags/{tema}/')
    sleep(2)


def like(wd):
    for i in range(1, 5):
        wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(5)
    hrefs = wd.find_elements_by_css_selector('article div a') # Encontra todas => (a) filhas de => (div) filhas de => (article)
    lista = []
    for i in hrefs:
         lista.append(i.get_attribute('href'))
    for links in lista:
        wd.get(links)
        sleep(2)
        try:
            like = wd.find_element_by_xpath('//button[@class="wpO6b "]')
            like.click()
            sleep(10)
        except:
            sleep(2)


def main():
    start(wd)
    login(wd, user, passw)
    like(wd)


main()
