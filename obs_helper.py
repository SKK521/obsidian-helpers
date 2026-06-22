import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "config.json"


def load_config() -> dict:
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_target_file() -> Path:
    config = load_config()
    vault_path = Path(config["vault_path"])
    target_file = Path(config["target_file"])
    return vault_path / target_file


def append_quick_note(note: str) -> Path:
    target_path = get_target_file()
    target_path.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"- [{timestamp}] {note.strip()}\n"

    with target_path.open("a", encoding="utf-8", newline="") as file:
        file.write(entry)

    return target_path


def main() -> None:
    note = input("请输入一条快速记录：").strip()
    if not note:
        print("没有输入内容，未保存。")
        return

    target_path = append_quick_note(note)
    print(f"已保存到 {target_path}")


if __name__ == "__main__":
    main()
