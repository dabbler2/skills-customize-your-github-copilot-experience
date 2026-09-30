# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

FastAPI 프레임워크를 사용하여 책 정보를 관리하는 REST API를 구축합니다. API 라우팅, JSON 데이터 처리, 요청 검증, HTTP 상태 코드를 직접 실습합니다.

## 📝 Tasks

### 🛠️ FastAPI 프로젝트 설정

#### Description

FastAPI 애플리케이션을 생성하고 서버를 실행하세요. `/` 경로에서 API가 정상적으로 실행 중임을 확인할 수 있어야 합니다.

#### Requirements

Completed program should:

- FastAPI 애플리케이션을 생성할 것
- `uvicorn`으로 개발 서버를 실행할 수 있을 것
- `GET /` 요청에 JSON 응답을 반환할 것
- `/docs`에서 자동 생성된 API 문서를 확인할 수 있을 것

### 🛠️ 책 목록 조회 API 만들기

#### Description

메모리의 리스트에 책 데이터를 저장하고, 책 전체 목록과 특정 책을 조회할 수 있는 API를 구현하세요.

#### Requirements

Completed program should:

- `GET /books`로 모든 책을 반환할 것
- `GET /books/{book_id}`로 특정 책을 반환할 것
- 책마다 `id`, `title`, `author`, `year` 필드를 포함할 것
- 존재하지 않는 책을 요청하면 `404 Not Found`를 반환할 것

### 🛠️ 책 생성 및 수정 API 만들기

#### Description

Pydantic 모델을 사용하여 새로운 책을 추가하고 기존 책 정보를 수정하는 API를 구현하세요.

#### Requirements

Completed program should:

- `POST /books`로 새 책을 추가할 것
- `PUT /books/{book_id}`로 기존 책을 수정할 것
- 요청 본문의 데이터 형식을 Pydantic 모델로 검증할 것
- 필수 필드가 없거나 잘못된 데이터 형식이면 `422 Unprocessable Entity`를 반환할 것
- 새 책을 생성하면 `201 Created` 상태 코드를 반환할 것

예시 요청:

```json
{
  "title": "Python으로 배우는 웹 개발",
  "author": "Kim",
  "year": 2026
}
```
