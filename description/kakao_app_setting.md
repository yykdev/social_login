# 카카오 앱 등록 <sub>ver 1.0</sub>

카카오 개발자 센터 앱 등록 접속 ( https://developers.kakao.com/apps/new )

앱 만들기 앱 이름 선택 후 등록

카카오 oauth 설정에는 시크릿 키가 없음

내 애플리케이션 화면의

설정 탭의 일반 메뉴 클릭

플랫폼 추가 버튼 클릭

웹 선택 후 사이트 도메인 입력 ( http://localhost:8000 ) 추가 클릭

Redirect Path 설정 ( 카카오는 호스트 네임을 사용하지 않고 oauth 패스만 입력 해 주면 됨 )

/accounts/kakao/login/callback/ 입력 후 저장


카카오 개발자 센터 내애플리케이션 화면의

설정 탭의 사용자 관리 선택하여 사용 여부를 ON으로 변경 한다.

개인정보 보호항목의 수집 목적을 입력한다. ( ex 사용자 식별 )

저장 클릭

다시 설정 탭의 일반 메뉴 클릭

RestAPI 키를 복사하여

http://localhost:8000/admin/ 접속 후 SOCIAL ACCOUNTS 항목의

Social applications -> ADD SOCIAL APPLICATION -> Client id에 입력 한 후 -> Sites 선택 후 save 한다.

카카오는 Secret Key를 사용하지 않지만 Django에서는 기본 필수 값이다.

카카오 로그인 에서는 사용하지 않으니 임의의 값을 입력 해주면 된다.
