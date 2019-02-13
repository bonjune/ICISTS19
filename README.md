# 2019-ICISTS

## 목차

[1.Front-End](#front-end)

[2.Back-End](#back-end-서버)

[3.메인 홈페이지](#squarespace)

[4.기타](#ETC)

​	[1.Mail](https://github.com/TheStarkor/ICISTS19/tree/master/Mail)

___

## Front-End

개발 과정의 작업일지와 당면한 다양한 문제들, 해결과정을 정리하는 편이 인수인계 과정에서 좋을 것 같아서 정리합니다. 그리고 진행하는 과정에서 다양한 팁이 존재한다면 따로 정리해두도록 하겠습니다.

제작 : Progressive Web App (이하 PWA)

프레임워크 : Vue.js

## 작업일지

- date: 2019-02-12
- author: 백승호

<공부한 내용>

- PWA ServiceWorker
- PWA manifest
- HTTPS 프로토콜

<요약>

1. ServiceWorker와 manifest가 적용이 되어야 PWA를 적용 할 수 있다.
2. Lighthouse를 쓰면 PWA 진행 과정에서 생기는 문제점들을 확인 할 수 있다.
3. 인스톨 배너, 푸시 알람을 적용하고자 하는데 아직 다양한 문제가 존재.

## 문제점, 해결과정

1. 19-02-12 / 백승호 / https 전부 적용되지 않는 문제.
   - 문제점
     - index.html은 https 프로토콜이 적용되는데 다른 파일들은 적용이 되고 있지 않음
       http가 되는데 어떻게 전부 일괄적으로 적용하는지 확인해 봐야 함. (19-02-12)
     - 소스 코드 href 부분을 https:// ~ 이런식으로 하면 될 것 같은데 그럼 local server 웹팩에서
       테스트 하는 과정에도 잘 적용되는지를 모르겠음. (19-02-12)

## Back-End 서버

## 작업일지

작업한 사항에 대하여 기록을 해둘 예정입니다. 신입부원 혹은 나중에 테크부에서 일하게 될 분들을 위해 정리해놓습니다. 추후에 테크부를 위한 공부 자료 정리용 프로젝트(e.g. ICISTS Wiki)도 진행하면 좋겠네요. 공부할 양이 방대하기 때문에 빠르게 실무에 투입할 수 있는 알짜 지식들을 정리해 놔야 할 것 같습니다.

작업일지는 아래와 유사한 형식으로 작성해 주시기 바랍니다. 양이 방대해지면 따로 정리할 예정입니다. 일단 여기에 모두 작성합시다.

---
* date: 2019-02-11
* author: 장봉준

<공부한 내용>
* Django
* AWS

<요약>
1. Django(이하 장고)를 공부중입니다. 이 리포지터리에 장고를 이용해 프로젝트를 생성했습니다. 프로젝트명은 icists19이며, 튜토리얼로 polls(질문 및 답변 기능) 어플 개발을 진행하였습니다. 아직 완성하지는 않았지만 기본적인 기능을 갖추었습니다. 하지만 하드코딩된 부분이 있기 때문에 점차 진행해가며 장고를 배울 예정입니다.

2. AWS EC2 가상 서버를 개설하였습니다. 하지만 아직 localhost에서 서버 개발중입니다. 이번주 중(~2019-02-15)까지 AWS EC2 서버에 장고 프로젝트를 설치할 예정입니다.

<장고 프레임워크 간단 설명>
장고 프레임워크는 MVC 패턴을 따릅니다. MVC는 모델, 뷰, 컨트롤러를 말합니다. 모델은 DB를 관리하며, 뷰는 웹페이지에 노출되는 내용을 관리합니다. 컨트롤러는 모델과 뷰에 명령을 내리는 역할을 합니다. 장고 앱에서는 사실상 models.py가 모델 부분을, templates 디렉터리가 뷰 부분을, views.py가 컨트롤러를 담당합니다. (이름을 혼동하지 마십시오.) models.py 에서는 관계형 DB의 구조를 설정(SQL의 column name 등)을 설정할 수 있으며, templates에서는 웹 페이지의 구조를 저장하며, 스크립트를 통해 특정 요소를 노출시킬지 말지 결정할 수 있습니다. views.py 에서는 위에서 설정한 내용들을 execute할 함수들을 정의합니다.  
urls.py에서는 장고의 url pattern을 정의합니다. 예를 들어 <hostname>/<year>/<month>/<day>/<index>와 같이 사용자가 알아보기 쉽도록 url pattern을 구성할 수 있습니다. 또한 admin.py 에서는 장고가 자동으로 제공하는 admin 페이지에서 DB를 관리할 수 있도록 설정합니다. polls 튜토리얼을 진행하면서 내용들을 주석으로 정리해놓았으니 참고바랍니다.  
[AWS를 이용한 장고 프로젝트 배포](https://nachwon.github.io/django-deploy-1-aws/)

---

---
* date: 2019-02-12
* author: 장봉준

<요약>

백 서버의 아웃라인을 잡았으니 인터페이스 서버, 웹 서버를 이용하여야 합니다. 설치 후에 프론트까지 개발을 가속할 수 있을 것 같습니다.  
풀스택의 구조는 다음과 같습니다.  
사용자(Client) <-> 웹 서버 <-> 인터페이스 서버 <-> 백 서버  
웹 서버 : 사용자의 HTTP, HTTPS 요청을 인터페이스로 변환하여 인터페이스 서버에 전달. 또한 인터페이스의 return을 static 파일로 변환하여 전달.  
인터페이스 서버 : 인터페이스 call을 백 서버의 controller에 전달. 또한 백 서버의 view를 웹 서버를 전달.  
백 서버 : controller의 작동을 통해 model, view 제어. 

---
* date : 2019-02-13
* author : Bongjun Jang

<summary>
1. Changed AWS EC2 Instance. You can now access the web server [here](http://ec2-54-180-8-50.ap-northeast-2.compute.amazonaws.com/).
2. Server System Discription Below. Please Check.
3. If you want to access the server on ssh, please let me know. I'll provide public key.

<server system discription>
- spec : aws ec2 t2.small
   this is not suitable for providing real services. Need upgrade. Can someone find how-to?
- server stack :
   the server stack is composed of 3 layers: Nginx, uWSGI, Django. Nginx is web server, uWSGI is interface, and Django is back-end server.
   Client <-> nginx <-> uWSGI <-> Django
- file system summary :
   all server files are at /srv  
/srv  
└── icists19  
    ├── front  
    │   ├── migrations  
    │   └── __pycache__  
    ├── icists19  
    │   └── __pycache__  
    ├── participant_manager  
    │   ├── migrations  
    │   │   └── __pycache__  
    │   ├── __pycache__  
    │   └── templates  
    │       └── participant_manager  
    └── polls  
        ├── migrations  
        │   └── __pycache__  
        ├── __pycache__  
        └── templates  
            └── polls  

---

## Squarespace

## 작업일지

- date: 2019-02-12
- author: 백승호

<내용>

1. 가을학기에 구상한 내용으로 업데이트 진행중
2. 모든 내용들을 MarkDown 문법으로 바꿀 계획 중
   - 수정, 보완에 장점이 있을 듯
3. pages에 다양한 기능들이 있음.
4. contact us 맨 위에 내용 추가 및 회장 번호 추가
5. 메인 페이지 2019로 변경
6. Recruiting 페이지 업데이트

___

## ETC

[1. Mail](https://github.com/TheStarkor/ICISTS19/tree/master/Mail)

