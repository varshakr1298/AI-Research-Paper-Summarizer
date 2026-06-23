import re
from pathlib import Path

from .config import SUMMARY_DIR


def safe_filename(
    name: str
) -> str:
    return re.sub(
        r'[<>:"/\\|?*]',
        "",
        name
    )[:100]


def save_summary(
    title: str,
    content: str
):
    Path(
        SUMMARY_DIR
    ).mkdir(
        exist_ok=True
    )

    filename = (
        safe_filename(title)
        + ".md"
    )

    path = (
        Path(SUMMARY_DIR)
        / filename
    )

    path.write_text(
        content,
        encoding="utf-8"
    )

    return path