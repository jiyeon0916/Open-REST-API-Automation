# Open-REST-API-Automation

## [선택과제] Kakao OAuth 2.0 기반 API 자동화 구현 🚀

이 프로젝트는 Kakao Developers의 **Login API**를 활용하여 OAuth 2.0 인증 과정을 자동화한 테스트 예시입니다.

---
## 📂 폴더 구조 및 설명

```
	📁 kakao_api_automation/
	├── 📁 tests/
	│   └── test_kakao_local_api.py
  ├── 📄 requirements.txt
	├── 📄 README.md

```

---

## 📋 과제 개요
- **Open REST API 활용:** Kakao Login API
- **인증 방식:** OAuth 2.0 (Access Token)
- **자동화 항목:** 토큰 발급 → 사용자 정보 조회 → 응답 검증

---

## ⚙️ 구현 내용
1. Kakao Developers 앱 등록 후 REST API 키 발급  
2. OAuth 인증 코드(`authorization_code`) 획득  
3. Access Token을 사용해 `/v2/user/me` API 호출  
4. 응답 데이터 검증  

---

## ▶ 실행 방법
1️⃣ `requirements.txt` 설치  
```bash
pip install -r requirements.txt
```
2️⃣ 환경변수 수정 (또는 코드 내 값 변경)
```
CLIENT_ID = "YOUR_KAKAO_REST_API_KEY" 
REDIRECT_URI = "YOUR_REGISTERED_REDIRECT_URI"
AUTHORIZATION_CODE = "YOUR_AUTH_CODE"
```
3️⃣ 실행
```
pytest -s .\test_kakao_oauth_login.py
```
________________________________________
✅ 예시 결과
```
=========================== test session starts ===========================
collected 1 item

test_kakao_oauth_login.py::test_get_user_info[AccessToken] PASSED
[INFO] Access Token 발급 성공 ✅
[PASS] 사용자 ID: 1234567890, 닉네임: 홍길동
============================ 1 passed in 1.35s ============================
```
________________________________________
🧰 기술 스택
- Python 3.x
- requests
- pytest

________________________________________
📄 참고 문서
- Kakao Developers - 로그인 가이드: https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api

________________________________________
📌 작성자 노트
- 실제 API 호출 시 Kakao Developers(https://developers.kakao.com/) 앱 등록이 필요합니다
