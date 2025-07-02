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

    # タイトルはconfigから取得
    title = latex_escape(config.get("title", ""))
    subject = latex_escape(Path(settings_path).resolve().parent.name)
    author = latex_escape(config.get("author", ""))
    teacher = latex_escape(config.get("teacher", ""))
    ex_dates = config.get("experiment_dates", [])
    submit_date = latex_escape(config.get("submit_date", ""))
    deadline = latex_escape(config.get("deadline", ""))
    final_accept = latex_escape(config.get("final_acceptance_date", ""))

    # 実験日をparbox用に整形
    ex_dates_lines = "\\\\ \n".join([f"& \\underline{{{latex_escape(d)}}} \\\[0.5cm]" for d in ex_dates])

    lines = [
        "\\begin{titlepage}",
        "\\centering",
        "\\vspace*{2cm}",
        "",
        f"{{\\Huge\\bfseries {title}}}\\\\[2cm]",
        "\\begin{tabular}{@{}l l}",
        "  \\rule{0pt}{2ex}\\textbf{実験題目} & \\\\",
        f"                                    & \\underline{{{subject}}} \\\\",
        "\\end{tabular}\\\\[3cm]",
        "",
        "\\begin{flushleft}",
        "\\begin{tabular}{@{}l l}",
        f"  指導教員 & \\\\",
        f"           & \\underline{{{teacher}}} \\\[0.5cm]",
        "",
        f"  実験日 & \\\\"
        f"         {ex_dates_lines}",
        "レポート \\\\",
        f"  提出締切日 & \\underline{{{deadline}}} \\\[0.5cm]",
        "レポート\\\\",
        f"  提出受理最終日 & \\underline{{{final_accept}}} \\\[0.5cm]",
        "レポート\\\\",
        f"  提出日 & \\underline{{{submit_date}}} \\\[0.5cm]",
        "",
        f"  報告者 & \\underline{{{author}}} ",
        "\\end{tabular}",
        "\\end{flushleft}",
        "",
        "\\vfill",
        "",
        "\\end{titlepage}",
        "",
        "\\end{document}"
    ]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_cover_tex.py settings.yaml cover.tex")
        sys.exit(1)
    generate_cover_tex(sys.argv[1], sys.argv[2])
