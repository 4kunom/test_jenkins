# test_jenkins

Jenkins + Docker를 활용한 CI/CD 파이프라인 프로젝트입니다.

---

## 프로젝트 구조

| 파일 | 설명 |
|------|------|
| `Jenkinsfile` | Jenkins 파이프라인 정의 |
| `Dockerfile` | nginx 기반 Docker 이미지 설정 |
| `jenkins.py` | Jenkinsfile 스테이지 검증 스크립트 |

---

## 파이프라인 흐름

1. **Checkout** — GitHub에서 소스 코드 클론
2. **Docker Image Build** — Dockerfile 기반 이미지 빌드 및 태그
3. **Docker Image Push** — Docker Hub에 이미지 업로드
4. **Cleaning up** — 로컬 이미지 삭제

---

## 환경 변수

| 변수 | 기본값 | 설명 |
|------|--------|------|
| `DOCKERHUB_USER` | `aprkunni` | Docker Hub 계정 |
| `IMAGE_NAME` | `my-app` | 이미지 이름 |
| `IMAGE_TAG` | `BUILD_NUMBER` | 빌드 번호를 태그로 사용 |

---

## 사전 요구 사항

- Jenkins에 `dockerhub-credentials` Credentials 등록 필요
- Jenkins 서버에 Docker 설치 필요

---

## Jenkinsfile 검증

```bash
python jenkins.py Jenkinsfile
```

특정 스테이지 지정 시:

```bash
python jenkins.py Jenkinsfile --stages Checkout Build Push
```

### 종료 코드

| 코드 | 의미 |
|------|------|
| `0` | 검증 통과 |
| `1` | 누락된 스테이지 있음 |
| `2` | 파일을 찾을 수 없음 |
