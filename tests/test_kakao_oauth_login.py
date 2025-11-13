import requests
import pytest

# Kakao Developers에서 발급받은 앱 키와 리다이렉트 URI
CLIENT_ID = "client_id"  # REST API Key
REDIRECT_URI = "https://localhost/oauth"  # Kakao Developers에 등록된 Redirect URI
AUTHORIZATION_CODE = "authorization_code"  # 카카오 로그인 완료 후 발급받은 코드

@pytest.fixture(scope="session")
def access_token():
    """
    Kakao OAuth 2.0 Access Token 발급
    """
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "code": AUTHORIZATION_CODE
    }

    response = requests.post(url, data=data)
    assert response.status_code == 200, f"토큰 발급 실패: {response.status_code}"
    token_data = response.json()

    access_token = token_data.get("access_token")
    assert access_token, "access_token이 응답에 없음"
    print(f"[INFO] Access Token 발급 성공 ✅")
    return access_token

def test_get_user_info(access_token):
    """
    Kakao 사용자 정보 조회 API 테스트
    - 발급받은 Access Token으로 사용자 정보 요청
    - 응답 상태 및 필드 검증
    """
    url = "https://kapi.kakao.com/v2/user/me"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers, verify=False)

    assert response.status_code == 200, f"사용자 정보 요청 실패: {response.status_code}"
    data = response.json()

    # 응답 필드 검증
    assert "id" in data, "사용자 ID 필드 누락"
    assert "kakao_account" in data, "kakao_account 필드 누락"

    profile = data["kakao_account"].get("profile", {})
    print(f"[PASS] 사용자 ID: {data['id']}, 닉네임: {profile.get('nickname', 'N/A')}")
