# TrophyListChanger
PlayStation Trophy Cafe 트로피 리스트 게시판 양식으로 자동변환

카페 트로피 리스트 게시판 양식에 맞게 자동으로 태그를 변환시켜 줍니다.
<img id="http://cafefiles.naver.net/MjAxNzA4MDNfMTkw/MDAxNTAxNzMxNTU3MTAx.mQP8WqogVXO_EJzgE70-btrLIRIhng5i-Y1rJwiKAUAg.PZ-IW0fQgT8rdFYobHvl8zXd-gTPWwdEe2kB-OUNT68g.PNG.newtype0096/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2017-08-03_%EC%98%A4%ED%9B%84_12.37.52.png" src="http://cafefiles.naver.net/MjAxNzA4MDNfMTkw/MDAxNTAxNzMxNTU3MTAx.mQP8WqogVXO_EJzgE70-btrLIRIhng5i-Y1rJwiKAUAg.PZ-IW0fQgT8rdFYobHvl8zXd-gTPWwdEe2kB-OUNT68g.PNG.newtype0096/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2017-08-03_%EC%98%A4%ED%9B%84_12.37.52.png" width="740" height="520.6787330316743">

사용 방법은 정말 간단합니다. (사용 방법 : https://github.com/newtype0096/TrophyListChanger/wiki/사용-방법)

트로피 리스트 양식과 트로피 공략 양식이 서로 같기 때문에 공략 작성에도 용이할 것으로 생각됩니다 ^_^

### 주의 사항
1. 관리자 권한으로 실행해주세요. 유료 인증서를 발급받지 않아서 그렇습니다 :(
2. 이미지 저장은 링크에 아이디가 포함되어 있어도 상관없습니다. 
3. 태그 변환 시 링크에 아이디가 포함되어 있으면 안 됩니다. 본인이 획득한 트로피는 숨겨진 트로피에서 제외하기 때문에 검색에서 제외됩니다. 
4. Windows는 이미지 저장 속도가 느립니다. OS X, Unix 계열과는 멀티 프로세싱 방식이 조금 다르다고 하네요.
5. DLC만 따로 분리하는 기능은 계획에 없습니다.

### 기능
- 트로피 이미지 로컬에 자동 저장
- 트로피 등급별 개수 합계 자동 판별
- 숨겨진 트로피 자동 판별
- 게시판 양식에 맞게 html 태그 변환

### 개발 도구
- Python 3.6.2
- PyQt 5.9
- SIP 4.19.3
- BeautifulSoup 4.6.0
- Requests 2.18.2
- py2app 0.14
- pyInstaller 3.2.1 
