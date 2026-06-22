# 프로젝트 최상위에 'Dockerfile' 이라는 이름으로 생성
FROM nginx:alpine

# 예시: 내가 만든 웹 소스코드(index.html)가 있다면 컨테이너로 복사
# (실습용이라면 이 라인은 없어도 작동합니다)
# COPY ./index.html /usr/share/nginx/html/index.html

EXPOSE 80