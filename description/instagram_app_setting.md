# 인스타그램 앱 등록 <sub>ver 1.0</sub>

인스타그램 앱 등록 화면 접속 ( https://www.instagram.com/developer/clients/register/ )

차례대로 입력 후

Website URL ( http://localhost:8000 )과, Valid redirect URLs ( http://localhost:8000/accounts/instagram/login/callback/ )를 입력한다.

=> django-allauth 공식 문서의 providers의 instagram에는 callbackURL 이라고 하지만 정작 인스타그램에서는 redirect URL 이라고 한다.

생성 후 Manage cliente에 출력 된 앱의 MANAGE 버튼을 클릭하여 상세 정보화면 으로 접속 한다.

Client ID 와 Client Secret 을 복사하여


http://localhost:8000/admin/ 접속 후 SOCIAL ACCOUNTS 항목의

Social applications -> ADD SOCIAL APPLICATION -> Client id와 Secret key에 입력 한 후 -> Sites 선택 후 save 한다.
