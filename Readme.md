# 기차 예매 자동화 스크립트

이 Python 스크립트는 [SRT](https://etk.srail.kr) 웹사이트에서 기차 예매를 자동화하는 프로그램입니다.
Selenium WebDriver를 사용하여 웹사이트와 상호작용하며, 기차 노선, 역, 날짜를 선택하고 예약을 진행합니다.
※ 수서역에서 출발하는 기차만 가능합니다.

## 개발 환경
- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (ChromeDriver)

## 기차 노선, 도착역, 날짜 선택
### line_num ==== # 경부선 1 # 호남선 2 # 전라선 3 # 경정선 4 # 동해선 5
line_num = 2

### 노선의 위에서부터 순서 ( 호남선의 익산 = 7번째 )
station_num = 7

### 오늘 날짜면 1 내일이면 2
day_num = 2

### 특실 6 / 일반실 7
room_num = 7

### 선택한 날짜의 몇번째 기차인지 선택
time_num = 10
