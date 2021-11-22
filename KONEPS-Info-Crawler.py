import sys
from selenium import webdriver
import chromedriver_autoinstaller
import csv

#텍스트 파일열기, csv생성
droppedFile = sys.argv[1] #드래그 앤 드롭 파일 경로
fr = open(droppedFile, mode="r")
fw = open("품명설명_결과.csv",'w',newline='')
w = csv.writer(fw)
w.writerow(['세부품명번호','품명설명'])

#셀레니움 크롬드라이버 준비
chromedriver_autoinstaller.install(cwd=True)
driver = webdriver.Chrome()

#텍스트 라인수 구하기
lines = len(fr.readlines())
fr.seek(0)

#크롤링
for i in range(lines):
    try:
        line = str(fr.readline())
        url = "https://www.g2b.go.kr:8053/search/classificationSearchView.do?goodsClsfcNo="+line
        driver.get(url)
        namenum = driver.find_element_by_xpath("""/html/body/div[1]/div[1]/div/article/div/table/tbody/tr[1]/td[1]""").text
    
        comment = driver.find_element_by_xpath("""/html/body/div[1]/div[1]/div/article/div/table/tbody/tr[4]/td""").text
        w.writerow([line.strip(),comment.strip()])
        print(comment)
    except:
        w.writerow([line.strip(),"ERROR"])
        continue

#종료
fr.close()
fw.close()
driver.quit()