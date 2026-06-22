from datetime import datetime
from pathlib import Path


INBOX_FILE = Path(__file__).resolve().parent / "inbox.md"


def append_quick_note(note: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"- [{timestamp}] {note.strip()}\n"

    with INBOX_FILE.open("a", encoding="utf-8", newline="") as file:
        file.write(entry)


def main() -> None:
    note = input("请输入一条快速记录：").strip()
    if not note:
        print("没有输入内容，未保存。")
        return

    append_quick_note(note)
    print(f"已保存到 {INBOX_FILE}")


if __name__ == "__main__":
    main()
