# Prompt Manager

간단한 콘솔 기반 프롬프트 관리 프로그램입니다. 로컬 JSON(`prompts.json`)에 프롬프트를 저장하고, 메뉴를 통해 추가/조회/검색/즐겨찾기 관리 및 카테고리별 Markdown 내보내기를 지원합니다.

## 주요 기능
- 프롬프트 목록 보기
- 프롬프트 추가 (제목/내용/카테고리 필수)
- 카테고리별 조회
- 프롬프트 검색
- 상세 보기
- 즐겨찾기 토글 및 즐겨찾기 목록
- 전체 내보내기: 카테고리별 정렬된 Markdown 파일 생성

## 요구사항
- Python 3.8 이상

## 실행 방법
터미널에서 작업 디렉터리로 이동한 뒤:

```bash
python3 hello.py
```

메인 메뉴에서 번호를 입력하여 기능을 선택합니다. 대부분의 하위 메뉴에서 `b`를 입력하면 메인 메뉴로 돌아갑니다.

## git log 
> ![git log](<screenshot/git graph.png>)

## 개발 환경
### git
https://github.com/a0000000033a/codyssey-a1-1

> **git config**
> ![git config](<screenshot/git config.png>)

### python
> **python version**
>![python version](<screenshot/python config.png>)


## menu screenshot
> **프로그램 실행 시 메인 메뉴**
> ![main](<screenshot/0. menu.png>)

> **프롬프트 목록**
> ![alt text](<screenshot/1. prompt list.png>)

> **프롬프트 추가**
> ![alt text](<screenshot/2. prompt add.png>)

> **카테고리별 조회**
> ![alt text](<screenshot/3. search category.png>)

> **프롬프트 검색**
> ![alt text](<screenshot/4. search prompts.png>)

> **프롬프트 상세 보기**
> ![alt text](<screenshot/5. view detail.png>)

> **즐겨찾기 관리**
> ![alt text](<screenshot/6. manage favorits.png>)

> **즐겨찾기 목록**
> ![alt text](<screenshot/7. favorits list.png>)

> **전체 내보내기 (카테고리별, md)**
> ![alt text](<screenshot/8. export md.png>)
ㄴ