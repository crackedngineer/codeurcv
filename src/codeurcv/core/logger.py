import logging
from pathlib import Path


def setup_logger(
    debug: bool = False, log_file: Path = Path("app.log")
) -> logging.Logger:
    level = logging.DEBUG if debug else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8")],
    )

    return logging.getLogger("codeurcv")
