from selenium import webdriver
import getpass
from time import sleep

user = input('Digite o nome de usuario: ')
passw = getpass.getpass('Digite sua senha: ')
tema = input('Digite o tema de pesquisa: ')
wd = webdriver.Chrome()
wd.get('https://www.instagram.com/')
sleep(5)


def log_src(wd, user, passw):
    email = wd.find_element_by_xpath('//input[@class="_2hvTZ pexuQ zyHYP"]')
    email.click()
    email.send_keys(user)
    key = wd.find_element_by_xpath('//input[@class="_2hvTZ pexuQ zyHYP"]')
    key.click()
    key.send_keys(passw)
    bt = wd.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')
    bt.click() 
    sleep(5)
    wd.get(f'https://www.instagram.com/explore/tags/{tema}/') 
    sleep(3)


def follow_click(wd):
    for i in range(1, 10):
        wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(5)
    hrefs = wd.find_elements_by_css_selector('article div a')
    sleep(3)
    href_list = []
    for h in hrefs:
        href_list.append(h.get_attribute('href'))
    for g in href_list:
        wd.get(g)
        sleep(3) 
        try:
            follow = wd.find_element_by_xpath('//button[@class="oW_lN sqdOP yWX7d    y3zKF     "]')
            follow.click()
            sleep(20)
        except:
            name = wd.find_element_by_tag_name('a').text
            print(f'Você já segue {name}.')


def main():
    log_src(wd, user, passw)
    follow_click(wd)


main()