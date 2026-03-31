#!/usr/bin/env python3
from pathlib import Path
import shutil

SOURCE = Path('/mnt/disk/live/zeroclaw-enterprise/library.txt')
TARGET = Path('/home/thikhina/.zeroclaw/workspace/library.txt')


def main() -> int:
    if not SOURCE.exists():
        raise SystemExit(f'Source manifest not found: {SOURCE}')
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    print(f'Synced {SOURCE} -> {TARGET}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
