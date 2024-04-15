프로젝트명 :RDS
프로젝트 기간: 2023.01.08~2023.01.17

||이름|담당|
|--|--|--|
|1|박요한|PM|
|2|조유경|만능|
|3|김경하|만능|
## 주제
* 희귀 질환을 위한 검색, 병원 연결 시스템

## 개발환경
> 백엔드

* python

> 프론트엔드

* HTML
* BOOTSTRAP
* JAVASCRIPT

> 설치 모듈


```
~$ pip install fastapi uvicorn jinja2
~$ pip install python-multipart
~$ pip install beanie
~$ pip install pydantic
~$ pip install pydantic-settings
~$ pip install pydantic[email]
~$ pip install python-dotenv
```
## 동작 (Youtube)
* [1차 프로젝트](https://youtu.be/3PTxsHhATEk)

## 마일스톤

### 1차 프로젝트
|시작날짜|업무|기간|완료여부|
|--|--|--|--|
|01.10|기획 1차 종합|1d|완|
||업무 분장|당일|완|
|01.11|페이지 프론트 기본 틀 제작|2d|완|
||벡엔드 구상|1d|완|
|01.12|로그인페이지 기본잡기|1d|완|
||로그인 데이터베이스 테스트|1d|완|
||프론트, 데이터베이스 연결 및 확인|1d|완|
|01.13|[질병 데이터 크롤링 제작](https://github.com/entangelk/study_gatheringdatas/blob/main/docs/selenium/disease_save.py)|1d|완|
|01.14|데이터 베이스 더미 제작 및 점검|1d|완|
|01.15|질병 검색 페이지 제작|2d|완|
||페이지네이션 적용|1d|완|
||질병 검색 페이지 데이터베이스 연결|1d|완|
|01.16|유저 데이터베이스, 로그인 회원가입 연결|2d|완|
|01.17|최종 확인(테스트 케이스 작성)|1d|완|
||각종 문서 작업|1d|완|




## 주요 파일 리스트
### html
|구분|위치|설명|비고|
|--|--|--|--|
|user|[mainpage.html](./templates/mainpage.html)|메인페이지||
||[login.html](./templates/user/user_login.html)|로그인|ID,PW 유효성 포함|
||[join.html](./templates/user/user_join.html)|회원가입|ID,email 유효성 포함|
||[infosearch.html](./templates/user/user_infosearch.html)|회원정보찾기|email 유효성 포함|
||[privacypolicy.html](./templates/user/user_privacypolicy.html)|약관페이지||
|search|[raredisease.html](./templates/search/search_raredisease.html)|희귀질환 리스트|검색 기능|
|other|[FAQ.html](./templates/other/other_FAQ.html)|FAQ||
||[QnA.html](./templates/other/other_QnA.html)|QnA|게시글 읽기, 쓰기|
|manag|[manager.html](./templates/manag/manag_manager.html)|관리자 페에지|QnA 댓글 작성, 삭제|

### py
|구분|위치|설명|비고|
|--|--|--|--|
|라우트|[mainpage.py](./mainpage.py)|메인페이지 라우트||
||[user.py](./route/user.py)|user하위 라우트||
||[search.py](./route/search.py)|정보찾기 하위 라우트||
||[manag.py](./route/manag.py)|관리자 하위 라우트||
||[other.py](./route/other.py)|기타 하위 라우트||
|컨넥터|[connection.py](./database/connection.py)|서버 컨넥터||
|모델|[member.py](./models/member.py)|user 스키마 모델||
||[QnA.py](./models/QnA.py)|QnA 스키마 모델||
||[FAQ.py](./models/FAQ.py)|FAQ 스키마 모델||
||[disease.py](./models/disease.py)|질병정보 스키마 모델||


## 주요 코드
### 박요한
댓글 업데이트 기능 모듈
```
    # 업데이트
    async def update_one(self, id: PydanticObjectId, dic) -> Any:
        doc = await self.model.get(id)
        if doc:
            for key, value in dic.items():
                setattr(doc, key, value)
            await doc.save()
            return True
        return False
```
ID, email 중복확인 후 연결 라우트
```
@router.post("/user_join_finalcheck", response_class=HTMLResponse) 
async def mypage(request:Request ):
    form_data = await request.form()
    dict_form_data = dict(form_data)
    inputID = dict_form_data['user_ID']
    inputEmail = dict_form_data['user_email']


    check_list = await collection_member.get_all()
    checks_list = [check.dict() for check in check_list]
    
    check_ID = False
    # pass
    for i in checks_list:
        if i['user_ID'] == inputID :
            check_ID = True
            break
        else:
            if i['user_email'] == inputEmail:
                check_ID = True
                break

    if check_ID:
        return templates.TemplateResponse(name="user/user_join_fail.html", context={'request':request})
    else :
        member = members(**dict_form_data)
        await collection_member.save(member)
        return templates.TemplateResponse(name="user/user_join_suc.html", context={'request':request})
```

### 조유경
회원 가입시 유효성 검사
```
    <script>
        var form = document.querySelector('.validation-form');

        form.addEventListener('submit', function (event) {
            var password = document.querySelector('#user_pswd').value;
            var passwordCheck = document.querySelector('#user_pswd_check').value;

            if (password !== passwordCheck) {
                alert('비밀번호가 일치하지 않습니다.');
                event.preventDefault();
            }
        });

        function validateForm() {
            var name = document.forms["registerForm"]["user_name"].value;
            var phonenumber = document.forms["registerForm"]["user_phonenumber"].value;
            var ID = document.forms["registerForm"]["user_ID"].value;
            var pswd = document.forms["registerForm"]["user_pswd"].value;
            var pswd_check = document.forms["registerForm"]["user_pswd_check"].value;
            var email = document.forms["registerForm"]["user_email"].value;
            var postcode = document.forms["registerForm"]["user_postcode"].value;
            var address = document.forms["registerForm"]["user_address"].value;
            var detailed_address = document.forms["registerForm"]["user_detailed_address"].value;
            var birth = document.forms["registerForm"]["user_birth"].value;

            if (name == "" || phonenumber == "" || ID == "" || pswd == "" || pswd_check == "" || email == "" || postcode == "" || address == "" || detailed_address == "" || birth == "") {
                alert("필수사항을 모두 입력해주세요.");
                return false;
            }
        }
    </script>
```
약관 동의 체킹 유효성 검사
```
            <script>
                // 모두동의
                function checkAll() {
                    var checkallCheckbox = document.getElementById("chk_checkall");
                    var otherCheckboxes = document.querySelectorAll(".other-checkboxes input[type='checkbox']");
                    var submitButton = document.getElementById("btn_submit");  // 등록 버튼을 가져옵니다.

                    for (var i = 0; i < otherCheckboxes.length; i++) {
                        otherCheckboxes[i].checked = checkallCheckbox.checked;
                    }

                    // '모두 동의' 체크박스의 체크 상태에 따라 '등록' 버튼을 활성화/비활성화 합니다.
                    if (checkallCheckbox.checked) {
                        submitButton.disabled = false;
                    } else {
                        submitButton.disabled = true;
                    }
                }


                // 필수약관 미동의시 가입불가
                function checkAgreement() {
                    var requiredAgreements = document.querySelectorAll(".required-agreement");
                    var agreeAllCheckbox = document.getElementById("chk_checkall");
                    var submitButton = document.getElementById("btn_submit");
                    var allChecked = true;

                    for (var i = 0; i < requiredAgreements.length; i++) {
                        if (!requiredAgreements[i].checked) {
                            allChecked = false;
                            break
                        }

                    }
                    if (allChecked) {
                        submitButton.disabled = false;
                    }
                    else {
                        submitButton.disabled = true;
                    }
                }

            </script>
```

### 김경하

이메일로 사용자의 ID와 PW확인
```
@router.post("/user_searchcheck_emailcheck", response_class=HTMLResponse) 
async def mypage(request:Request):
    form_data = await request.form()
    dict_form_data = dict(form_data)
    inputemail = dict_form_data['user_email']

    check_list = await collection_member.get_all()
    checks_list = [check.dict() for check in check_list]


    member_info = {}
    check_member=False
    for member in checks_list:
        if member['user_email'] == inputemail:
            member_info = {
                "user_ID": member['user_ID'],  
                "user_pswd": member['user_pswd']  
            }
            check_member = True
            break

    if check_member:
        return templates.TemplateResponse("user/user_searchemail_found.html", context={'request': request, "member": member_info})
    else:
        return templates.TemplateResponse("user/user_searchemail_notfound.html", context={'request': request})
```