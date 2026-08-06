#!/usr/bin/env python3
"""4パターンの文字数をカウントするスクリプト。

使い方:
    python count_chars.py <ファイルパス>
    python count_chars.py -          # 標準入力から読み込む
"""
import sys

# 全角スペース(U+3000)・半角スペース・タブをスペースとして扱う
SPACE_CHARS = ("　", " ", "\t")
# \r\n, \r, \n をすべて改行コードとして扱う
NEWLINE_CHARS = ("\r", "\n")


def strip_chars(text: str, chars: tuple[str, ...]) -> str:
    return "".join(c for c in text if c not in chars)


def count_all_patterns(text: str) -> dict[str, int]:
    no_space = strip_chars(text, SPACE_CHARS)
    no_newline = strip_chars(text, NEWLINE_CHARS)
    no_space_no_newline = strip_chars(no_space, NEWLINE_CHARS)

    return {
        "改行含む・スペース含む（合計文字数）": len(text),
        "改行含む・スペース含まない": len(no_space),
        "改行含まない・スペース含む": len(no_newline),
        "改行含まない・スペース含まない": len(no_space_no_newline),
    }


def main() -> None:
    if len(sys.argv) != 2:
        print("使い方: python count_chars.py <ファイルパス|->", file=sys.stderr)
        sys.exit(1)

    source = sys.argv[1]
    if source == "-":
        text = sys.stdin.read()
    else:
        with open(source, "r", encoding="utf-8") as f:
            text = f.read()

    results = count_all_patterns(text)
    for label, count in results.items():
        print(f"{label}: {count}")


if __name__ == "__main__":
    main()
