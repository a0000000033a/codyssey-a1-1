#!/usr/bin/env python3

"""프롬프트 관리 콘솔 프로그램

기능:
- 로컬 JSON 파일(`prompts.json`)에 프롬프트 목록을 저장/불러오기
- 메뉴 기반 탐색, 각 기능은 하위 메뉴에서 메인으로 복귀 가능
"""

import json
import os
from typing import List, Dict

PROMPTS_FILE = "prompts.json"


def load_prompts() -> List[Dict]:
    """Load prompts from local JSON file.

    If the file doesn't exist or is invalid, create an empty list and save it.
    """
    if not os.path.exists(PROMPTS_FILE):
        prompts: List[Dict] = []
        save_prompts(prompts)
        return prompts

    try:
        with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except Exception:
        pass

    # 실패 시 빈 목록으로 초기화
    prompts: List[Dict] = []
    save_prompts(prompts)
    return prompts


def save_prompts(prompts: List[Dict]) -> None:
    with open(PROMPTS_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)


def show_menu() -> None:
    print("\n메뉴를 선택하세요:")
    print("1. 프롬프트 목록")
    print("2. 프롬프트 추가")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 전체 내보내기 (카테고리별, md)")
    print("0. 종료")


def print_prompt_list(prompts: List[Dict]) -> None:
    if not prompts:
        print("(프롬프트가 없습니다)")
        return
    for i, p in enumerate(prompts, start=1):
        fav = "★" if p.get("favorite") else " "
        print(f"{i}. {fav} {p.get('title')} [{p.get('category')}]")


def view_prompt_detail(prompts: List[Dict], idx: int) -> None:
    if idx < 0 or idx >= len(prompts):
        print("유효하지 않은 번호입니다.")
        return
    p = prompts[idx]
    print("\n--- 상세 보기 ---")
    print(f"제목: {p.get('title')}")
    print(f"카테고리: {p.get('category')}")
    print(f"즐겨찾기: {'예' if p.get('favorite') else '아니오'}")
    print("내용:\n" + p.get("content"))
    print("--- 끝 ---\n")


def prompt_list(prompts: List[Dict]) -> None:
    while True:
        print("\n[프롬프트 목록]")
        print_prompt_list(prompts)
        print("b: 뒤로, 번호: 상세보기")
        cmd = input("선택: ").strip()
        if cmd.lower() == "b":
            return
        if cmd.isdigit():
            idx = int(cmd) - 1
            view_prompt_detail(prompts, idx)


def prompt_add(prompts: List[Dict]) -> None:
    print("\n[프롬프트 추가] (빈 입력시 취소)")
    title = input("제목: ").strip()
    if not title:
        print("추가 취소")
        return
    content = input("내용: ").strip()
    category = input("카테고리: ").strip()
    fav = input("즐겨찾기 등록? (y/N): ").strip().lower() == "y"
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": bool(fav),
    })
    save_prompts(prompts)
    print("프롬프트가 추가되고 저장되었습니다.")


def prompt_by_category(prompts: List[Dict]) -> None:
    while True:
        cats = sorted({p.get("category", "(분류없음)") for p in prompts})
        print("\n[카테고리별 조회]")
        if not cats:
            print("(카테고리가 없습니다)")
            return
        for i, c in enumerate(cats, start=1):
            print(f"{i}. {c}")
        print("b: 뒤로")
        cmd = input("선택: ").strip()
        if cmd.lower() == "b":
            return
        if cmd.isdigit():
            ci = int(cmd) - 1
            if 0 <= ci < len(cats):
                cat = cats[ci]
                matches = [p for p in prompts if p.get("category") == cat]
                print(f"\n[{cat}] 항목들:")
                print_prompt_list(matches)
                print("상세 보려면 번호 입력, 아니면 Enter")
                sub = input("선택: ").strip()
                if sub.isdigit():
                    # map to global index
                    # find absolute index by matching title and category in original list
                    mi = int(sub) - 1
                    # attempt to find the mi-th in matches in prompts
                    if 0 <= mi < len(matches):
                        target = matches[mi]
                        # find first index in prompts that matches
                        for idx, p in enumerate(prompts):
                            if p is target:
                                view_prompt_detail(prompts, idx)
                                break


def prompt_search(prompts: List[Dict]) -> None:
    print("\n[프롬프트 검색] (빈 입력시 취소)")
    q = input("검색어: ").strip()
    if not q:
        return
    ql = q.lower()
    results = [p for p in prompts if ql in (p.get("title", "").lower() + p.get("content", "").lower())]
    print(f"\n검색 결과 {len(results)}개:")
    if not results:
        return
    print_prompt_list(results)
    print("상세 보려면 번호 입력, 아니면 Enter")
    sub = input("선택: ").strip()
    if sub.isdigit():
        mi = int(sub) - 1
        if 0 <= mi < len(results):
            target = results[mi]
            for idx, p in enumerate(prompts):
                if p is target:
                    view_prompt_detail(prompts, idx)
                    break


def prompt_detail(prompts: List[Dict]) -> None:
    print("\n[프롬프트 상세 보기]")
    print_prompt_list(prompts)
    print("b: 뒤로")
    cmd = input("번호: ").strip()
    if cmd.lower() == "b" or not cmd:
        return
    if cmd.isdigit():
        idx = int(cmd) - 1
        view_prompt_detail(prompts, idx)


def favorites_manage(prompts: List[Dict]) -> None:
    while True:
        print("\n[즐겨찾기 관리]")
        print_prompt_list(prompts)
        print("b: 뒤로, 번호: 토글(즐겨찾기/해제)")
        cmd = input("선택: ").strip()
        if cmd.lower() == "b":
            return
        if cmd.isdigit():
            idx = int(cmd) - 1
            if 0 <= idx < len(prompts):
                prompts[idx]["favorite"] = not prompts[idx].get("favorite", False)
                save_prompts(prompts)
                print("토글 완료. 저장되었습니다.")


def favorites_list(prompts: List[Dict]) -> None:
    while True:
        favs = [p for p in prompts if p.get("favorite")]
        print("\n[즐겨찾기 목록]")
        if not favs:
            print("(즐겨찾기 항목이 없습니다)")
            return
        print_prompt_list(favs)
        print("b: 뒤로, 번호: 상세보기")
        cmd = input("선택: ").strip()
        if cmd.lower() == "b":
            return
        if cmd.isdigit():
            mi = int(cmd) - 1
            if 0 <= mi < len(favs):
                target = favs[mi]
                for idx, p in enumerate(prompts):
                    if p is target:
                        view_prompt_detail(prompts, idx)
                        break


def export_markdown(prompts: List[Dict]) -> None:
    """Export all prompts grouped by category into a markdown file.

    Prompts are grouped by category (sorted). User provides a filename.
    Empty filename cancels and returns to main menu.
    """
    print("\n[전체 내보내기 (카테고리별, md)]")
    fname = input("파일명 (확장자 포함, 빈 입력시 취소): ").strip()
    if not fname:
        print("내보내기 취소")
        return
    if not fname.lower().endswith('.md'):
        fname += '.md'

    # group by category
    cats = sorted({p.get('category', '(분류없음)') for p in prompts})
    lines: List[str] = []
    lines.append('# Prompts by Category')
    lines.append('')
    if not cats:
        lines.append('(프롬프트가 없습니다)')
    else:
        for cat in cats:
            lines.append(f'## {cat}')
            lines.append('')
            items = [p for p in prompts if p.get('category', '(분류없음)') == cat]
            for p in items:
                star = '★' if p.get('favorite') else ''
                lines.append(f"- **{p.get('title')}** {star}")
                content = p.get('content', '')
                if content:
                    # blockquote each line
                    for ln in content.splitlines():
                        lines.append('> ' + ln)
                lines.append('')

    try:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"내보내기 완료: {fname}")
    except Exception as e:
        print(f"파일 저장 실패: {e}")


def handle_choice(choice: str, prompts: List[Dict]) -> bool:
    if choice == "1":
        prompt_list(prompts)
    elif choice == "2":
        prompt_add(prompts)
    elif choice == "3":
        prompt_by_category(prompts)
    elif choice == "4":
        prompt_search(prompts)
    elif choice == "5":
        prompt_detail(prompts)
    elif choice == "6":
        favorites_manage(prompts)
    elif choice == "7":
        favorites_list(prompts)
    elif choice == "8":
        export_markdown(prompts)
    elif choice == "0":
        print("프로그램을 종료합니다.")
        return False
    else:
        print("잘못된 입력입니다. 메뉴 번호를 다시 입력하세요.")

    return True


def main() -> None:
    prompts = load_prompts()
    try:
        while True:
            show_menu()
            choice = input("선택: ").strip()
            if not handle_choice(choice, prompts):
                break
    except (KeyboardInterrupt, EOFError):
        print("\n입력 종료. 프로그램을 종료합니다.")


if __name__ == "__main__":
    main()
