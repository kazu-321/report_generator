import sys
import yaml
from pathlib import Path

def latex_escape(text):
    if not isinstance(text, str):
        return ""
    return text.replace("&", "\\&").replace("_", "\\_").replace("%", "\\%")

def generate_cover_tex(settings_path, output_path):
    with open(settings_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    title = latex_escape(Path(settings_path).parent.name)
    author = latex_escape(config.get("author", ""))
    teacher = latex_escape(config.get("teacher", ""))
    ex_dates = config.get("experiment_dates", [])
    submit_date = latex_escape(config.get("submit_date", ""))
    deadline = latex_escape(config.get("deadline", ""))
    final_accept = latex_escape(config.get("final_acceptance_date", ""))

    lines = [
        "\\begin{titlepage}",
        "\\centering",
        f"\\Huge\\bfseries {title}\\\\[2cm]",
        f"\\large \\textbf{{氏名}}: {author}\\\\",
        f"\\textbf{{担当教員}}: {teacher}\\\\",
    ]

    if ex_dates:
        ex_dates_escaped = ", ".join(latex_escape(d) for d in ex_dates)
        lines.append(f"\\textbf{{実験日}}: {ex_dates_escaped}\\\\")
    if submit_date:
        lines.append(f"\\textbf{{提出日}}: {submit_date}\\\\")
    if deadline:
        lines.append(f"\\textbf{{提出締切日}}: {deadline}\\\\")
    if final_accept:
        lines.append(f"\\textbf{{提出受理最終日}}: {final_accept}\\\\")
    lines += [
        "\\vfill",
        "\\end{titlepage}"
    ]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_cover_tex.py settings.yaml cover.tex")
        sys.exit(1)
    generate_cover_tex(sys.argv[1], sys.argv[2])
