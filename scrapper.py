import requests  # import : 라이브러리 가져오기
from bs4 import BeautifulSoup    # bs4 라는 라이브러리에서 beautifulsoup 기능을 가져온다.

keyword = "파이썬" # 1. 검색어 설정
pages = 5
jobs = []

def search_incruit():

    for i in range(pages): # 1~5 페이지까지 받아오기
        page = i * 30
        
        url = f'https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}' # 2. 검색 주소 만들기
        r = requests.get(url) # 3. 웹사이트에 get 요청 보내기
        # print(r.status_code)   #웹사이트가 어떤 응답을 보냈는지 확인함. http 상태코드 200은 서버서 요청을 정상적으로 처리했다는 뜻
        # print(r.text)          # d웹페이지에서 받은 html 문자열 (html 이란 : 웹페이지의 구조를 표현하는 언어)
        soup = BeautifulSoup(r.text, "html.parser")   # 4. html 분석 준비
        #beautifulsoup는 필요한 부분만 쉽게 찾기위해 사용= html을 검색하기 편한 구조로 변환 (requests로 html을 가져왔지만, html 전체를 출력하면 너무길어서)
        # html.parser : html을 분석하는 방법
        # print(soup.prettify()) # html을 들여쓰기와 줄바꿈을 적용해 보기 쉽게 출력한다. (채용공고를 추출하는 기능이 아님)

        lis = soup.find_all("li", class_="c_col")   # 5. 채용공고 전체 찾기
        # find_all() : 조건에 맞는 요소 전부 찾기 / find() : 첫 번째 일치 요소 찾기 
        # soup : 분석할 html 전체, 
        # li : li 태그찾기,  
        # class_="c_col" : 클래스가 c_col인 요소만 찾기
        # lis : 찾은 결과를 저장하는 변수
        # print(lis)
        # print(len(lis))
        print(f"{i + 1}")

        for li in lis: # 회사명 하나씩 추출 # lis에 들어있는 요소를 하나씩 꺼내어 li에 넣고 반복하라. for ~ in ~: 하나씩 반복하기
            try:
                company = li.find("a", class_="cpname").text # .text 사용이유 : 불필요한 html 태그를 제거하고 필요한 글자만 가져옴
                title = li.find("div", class_="cell_mid").find("a").text
                location = li.find("div", class_="cl_md").find_all("span")[0].text
                link = li.find("div", class_="cell_mid").find("a").get("href")
                print(company) 
                print(title) 
                print(location) 
                
                job_data = {
                    "company": company,
                    "title": title,
                    "location": location,
                    "link": link
                }
                jobs.append(job_data)
            except:
                pass

            print(jobs)
            print(len(jobs)) # 6. 채용공고 개수 출력
    return jobs
            
            #try : 일단 아래 코드를 실행해보라
            # except : try 안에서 오류가 발생하면 이 부분을 실행한다
            # pass : 아무작업 하지않고 넘어간다
            # try, except, pass 는 모든 오류를 숨기기 때문에 권장하지 않음. 단, 회사명이 없을때만 건너뛰려면 다음 방식이 더 좋다.
            # for li in lis:
            #     company = li.find("a", class=_"cpname")
            #     if company is not None:
            #print(company.get_text(strip=True))