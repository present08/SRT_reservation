import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main():
    url = "https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000"
    driver = webdriver.Chrome()
    driver.get(url)

    # 도착역 지도 띄우기
    end = '//*[@id="search-form"]/fieldset/div[1]/div/div/div[2]/a'
    driver.find_element(By.XPATH,end).click()

    # 지도 창으로 스위칭 하여 지도위에서 지역 선택
    # line_num ==== # 경부선 1 # 호남선 2 # 전라선 3 # 경정선 4 # 동해선 5
    line_num = 2
    # 노선의 위에서부터 순서 ( 익산 : 7 )
    station_num = 7
    # 오늘 날짜면 1 내일이면 2 -----
    day_num = 2
    # 특실 6 # 일반실 7
    room_num = 7
    # 표에서 몇번 째 탈 건지 순서
    time_num = 10

    line = '//*[@id="srtLine{}Btn2"]'.format(line_num)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH,line).click()

    station = '//*[@id="srtLine{}"]/ul/li/ul/li[{}]/a'.format(line_num,station_num)
    driver.find_element(By.XPATH,station).click()
    check_btn = '//*[@id="srtLine{}"]/div/input'.format(line_num)
    driver.find_element(By.XPATH,check_btn).click()

    day = '//*[@id="dptDt"]/option[{}]'.format(day_num)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH,'//*[@id="dptDt"]').click()
    driver.find_element(By.XPATH,day).click()
    driver.find_element(By.XPATH,'//*[@id="search_top_tag"]/input').click()
    while 1:
        time.sleep(0.5)

        try:
            wait = driver.find_element(By.XPATH,'//*[@id="NetFunnel_Skin_Top"]')
            while 1:
                if wait:
                    time.sleep(0.5)
                else:
                    break
        except:
            pass

        reservation_xpath = '//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{}]/td[{}]/a/span'.format(time_num , room_num)
        reservation = driver.find_element(By.XPATH, reservation_xpath)
        if reservation.text == "예약하기":
            reservation.click()
            break
        else :
            driver.refresh()
            time.sleep(1)
        start_time = driver.find_element(By.XPATH,'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{}]/td[4]/em'.format(time_num))
        start_station = driver.find_element(By.XPATH,'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{}]/td[4]/div'.format(time_num))
        print("출발 역 : ", start_station.text)
        print("출발 시간 : ", start_time.text)

    time.sleep(10000)

if __name__ == '__main__':
    main()


