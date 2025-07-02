import sys
import yaml
from pathlib import Path

def html_escape(text):
    if not isinstance(text, str):
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def underline(text):
    return f"\\underline{{{html_escape(text)}}}"

def generate_md_with_underline(settings_path, output_path):
    with open(settings_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    title = html_escape(config.get("title", ""))
    subtitle = underline(config.get("subtitle",Path(settings_path).resolve().parent.name))
    author = underline(config.get("author", ""))
    teacher = underline(config.get("teacher", ""))
    ex_dates = [underline(d) for d in config.get("experiment_dates", [])]
    submit_date = underline(config.get("submit_date", ""))
    deadline = underline(config.get("deadline", ""))
    final_accept = underline(config.get("final_acceptance_date", ""))

    lines = [
        f"# {title}",
         "",
         "実験題目  ",
        f"　　　　{subtitle}  ",
         "",
         "指導教員  ",
        f"　　　　{teacher}  ",
        "  ",
         "　　　　  ",
        f"　　　　実験日　{ex_dates[0]}  " if ex_dates else "実験日　：",  # 初回
    ]
    lines += [f"　　　　　　　　{d}  " for d in ex_dates[1:]]  # 2行目以降
    lines += [
         "　　　　  ",
         "　　　　  ",
         "　　　　レポート  ",
        f"　　　　提出締切日　　　{deadline}",
         "　　　　  ",
         "　　　　  ",
         "　　　　レポート  ",
        f"　　　　受理最終日　　　{final_accept}",
         "　　　　  ",
         "　　　　  ",
         "　　　　レポート  ",
        f"　　　　提出日　　　　　{submit_date}",
         "　　　　  ",
         "　　　　  ",
         "　　　　  ",
         "　　　　  ",
        f"　　　　報告者　{author}"
    ]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_md_with_underline.py settings.yaml cover.md")
        sys.exit(1)
    generate_md_with_underline(sys.argv[1], sys.argv[2])
