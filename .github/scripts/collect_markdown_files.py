import sys
import yaml

def collect_markdown_files(settings_path):
    with open(settings_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    files = config.get("markdown", [])
    if isinstance(files, str):
        files = [files]
    print(" ".join(files))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: collect_markdown_files.py settings.yaml")
        sys.exit(1)
    collect_markdown_files(sys.argv[1])
