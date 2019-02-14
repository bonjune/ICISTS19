## 사용법

0. 사용할 id로 로그인 한 후 
    google account > 보안 > 보안 수준이 낮은 앱의 액세스 > 액세스 사용 설정 (권장하지 않음) > 사용함 <br/>
    위를 따라가며 액세스 가능하도록 활성화 시키기
1. SendMail.py 파일 내용을 Copy & Paste 한 후 메모장이나 ide에 붙여넣고 저장한다.
2. SendMail.py의 line **8, 9**를 본인의 ID, App Password로 수정한다.
3. py 파일과 같은 경로에 contents.xlsx 파일을 둔다.

|    #    | Format. Number | Mail Address |  Subject   |    Arguments    |
| :--------: | :-----------: | :---------------: | :---------: | :-----------------: |
| 주석처리 | mail txt 숫자 | 수신자 메일주소 | 메일 제목 | txt 내의 바꿀 내용 |

- 주석처리 : # 을 입력하면 해당 line 메일 보내지 않고 넘어감
- mail txt 숫자 : 수신자별 메일 내용 종류 ( 숫자 N이 입력되면 mailN.txt 파일 불러옴)
- 수신자 메일 주소 : 수신자 메일 주소 
- Arguments :  mailN.txt에 있는 괄호 [] 안에 들어갈 내용 ( , 로 구분되어 적어야 함)

4. openpyxl 을 설치한다
```
pip3 install openpyxl  
```
5. 실행
```
python3 SendMail.py
```
email 제목, 내용, 수신자, 발신자를 확인한 후 맞으면 yes, 틀렸다면 no 를 입력하면 메일 전송됨!

### 참고
0. directory 구조
./mail <br/>
    |_ SendMail.py <br/>
    |_ contents.xlsx <br/>
    |_ mail0.txt <br/>
    |_ mail1.txt <br/>
    |_ .. <br/>
    
1. Requirements
```
openpyxl
```

2. 환경
python3.7.0
___

## 업데이트 노트

1. 메일 전송 및 엑셀 연동(2019-02-13/백승호)l
2. 기능 웹 서버에서 사용할 수 있도록 할 예정(2019-02-14/장봉준)
3. exel 내용 수정 및 format 수정 (2019-02-14/이하연)

