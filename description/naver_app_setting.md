# 네이버 앱 등록 <sub>ver 1.0</sub>

네이버 개발자 센터 앱 등록 접속 ( https://developers.naver.com/apps/#/wizard/register )

애플리케이션 등록 (API 이용신청) 접속

애플리케이션 이름 설정

사용 API 선택 ( 네아로 (네이버 아이디로 로그인) )

환경 PC웹 선택

서비스URL 입력

Callback URL 입력 ( http://localhost:8000/accounts/naver/login/callback )

등록하기

개요 메뉴의 Client ID 와 Client Secret 을 복사 한 후

http://localhost:8000/admin/ 접속 후 SOCIAL ACCOUNTS 항목의

Social applications -> ADD SOCIAL APPLICATION -> Client id 와 Secret key에 입력 한 후 -> Sites 선택 후 save 한다.




## 로그인 계정 수가 부족하거나 서비스 운영으로 전환 될 경우

API 설정 탭의 로그인 오픈 API 서비스 환경 메뉴의 네아로 검수 요청을 클릭 한다.

개발 중 상태에서는 아이디 로그인이 최대 20개 밖에 되지 않음.