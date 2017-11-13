# 소셜 로그인 사이트 별 취급 데이터 테스트

**social_login/adapter/social_account_adapter.py**

- SocialAccountAdapter 클래스의 내의 sociallogin 인자로 확인 할 수 있음.


## 인스타그램

> print(sociallogin.account.get_avatar_url())

```
https://scontent.cdninstagram.com/t51.2885-19/s150x150/19050253_128946777683349_7663697750424289280_a.jpg
```


> print(sociallogin.account.provider.upper())

```
INSTAGRAM
```


> print(self.get_signup_form_initial_data(sociallogin))

```
{'email': '', 'username': 'assavictory', 'first_name': '', 'last_name': ''}
```

> print(json.dumps(sociallogin.account.extra_data, indent=4))

```
{
    "id": "5574657500",
    "username": "assavictory",
    "profile_picture": "https://scontent.cdninstagram.com/t51.2885-19/s150x150/19050253_128946777683349_7663697750424289280_a.jpg",
    "full_name": "\uae40\uc6a9\uc5f0",
    "bio": "",
    "website": "",
    "is_business": false,
    "counts": {
        "media": 0,
        "follows": 13,
        "followed_by": 15
    }
}
```


---


## 페이스북

> print(sociallogin.account.provider.upper())

```
FACEBOOK
```

> print(self.get_signup_form_initial_data(sociallogin))

```
{'email': '', 'username': 'user43', 'first_name': '용연', 'last_name': '김'}
```


> print(json.dumps(sociallogin.account.extra_data, indent=4))

```
{
    "id": "514320388934000",
    "name": "\uae40\uc6a9\uc5f0",
    "first_name": "\uc6a9\uc5f0",
    "last_name": "\uae40",
    "verified": true,
    "locale": "ko_KR",
    "timezone": 0,
    "link": "https://www.facebook.com/app_scoped_user_id/514320388934000/",
    "gender": "male",
    "updated_time": "2017-11-05T06:55:27+0000"
}
```

---


## 카카오

> print(sociallogin.account.provider.upper())

```
KAKAO
```

> print(self.get_signup_form_initial_data(sociallogin))

```
{'email': '', 'username': 'user', 'first_name': '', 'last_name': ''}
```

> print(json.dumps(sociallogin.account.extra_data, indent=4))

```
{
    "kaccount_email": "the_promise011@nate.com",
    "kaccount_email_verified": true,
    "id": 559769815,
    "properties": {
        "profile_image": "http://k.kakaocdn.net/dn/A4hHm/btqilWt4VFq/bj5iH2KYjcHtK1jQg6k2K0/profile_640x640s.jpg",
        "nickname": "\uae40\uc6a9\uc5f0",
        "thumbnail_image": "http://k.kakaocdn.net/dn/A4hHm/btqilWt4VFq/bj5iH2KYjcHtK1jQg6k2K0/profile_110x110c.jpg"
    }
}
```

---

## 네이버

> print(sociallogin.account.provider.upper())

```
NAVER
```

> print(self.get_signup_form_initial_data(sociallogin))

```
{'email': '', 'username': 'user93', 'first_name': '', 'last_name': ''}
```

> print(json.dumps(sociallogin.account.extra_data, indent=4))
```
{
    "nickname": "\uc6a9\uc5f0",
    "enc_id": "3f9e538e9b6c777d52284b0490f7219522ad985369c78398fadb36062658fdd2",
    "profile_image": "https://phinf.pstatic.net/contact/20161130_164/1480481097237kUz5y_JPEG/PHOTO0510110011-assavictory.jpg",
    "age": "30-39",
    "gender": "M",
    "id": "39154659",
    "birthday": "01-01"
}
```
