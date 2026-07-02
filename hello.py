#!/usr/bin/env python3

"""Simple menu-driven console program per requirements.

Each feature is implemented as an empty function (placeholder).
The program shows a menu, accepts numeric input, validates it,
and returns to the menu after each selection. Choosing 0 exits.
"""

def show_menu() -> None:
    print("\n메뉴를 선택하세요:")
    print("1. 프롬프트 목록")
    print("2. 프롬프트 추가")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


# 빈 함수들: 기능 요구사항에 따라 각각 개별 함수로 구현 (현재는 빈 함수)
def prompt_list():
    pass


def prompt_add():
    pass


def prompt_by_category():
    pass


def prompt_search():
    pass


def prompt_detail():
    pass


def favorites_manage():
    pass


def favorites_list():
    pass


def handle_choice(choice: str) -> bool:
    """Handle the user's menu choice.

    Returns False when the program should exit, True to continue.
    """
    if choice == "1":
        prompt_list()
    elif choice == "2":
        prompt_add()
    elif choice == "3":
        prompt_by_category()
    elif choice == "4":
        prompt_search()
    elif choice == "5":
        prompt_detail()
    elif choice == "6":
        favorites_manage()
    elif choice == "7":
        favorites_list()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        return False
    else:
        print("잘못된 입력입니다. 메뉴 번호를 다시 입력하세요.")

    return True


def main() -> None:
    try:
        while True:
            show_menu()
            choice = input("선택: ").strip()
            if not handle_choice(choice):
                break
    except (KeyboardInterrupt, EOFError):
        print("\n입력 종료. 프로그램을 종료합니다.")


if __name__ == "__main__":
    main()
