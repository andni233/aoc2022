import sys
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class File:
    name: str
    size: int


@dataclass
class Folder:
    parent: Optional["Folder"] = None
    files: List[File] = field(default_factory=list)
    folders: List["Folder"] = field(default_factory=list)
    size: Optional[int] = None


def main():
    lines = [line.strip() for line in sys.stdin.readlines()][1:]

    root = Folder()
    cwd = root

    for line in lines:
        if line.startswith("$ cd"):
            folder = line.split()[-1]
            if folder == "..":
                cwd = cwd.parent
            else:
                cwd.folders.append(Folder(parent=cwd))
                cwd = cwd.folders[-1]
        elif line.startswith("$ ls") or line.startswith("dir "):
            continue
        else:
            size, name = line.split()
            cwd.files.append(File(name, int(size)))

    def _sizes(node):
        node.size = (sum([f.size for f in node.files]) or 0) + sum([_sizes(f) or 0 for f in node.folders])
        return node.size

    def _find_small_folders(node, result=[]):
        if node.size < 100000:
            result.append(node.size)
        for folder in node.folders:
            _find_small_folders(folder)
        return result

    _sizes(root)
    print(sum(_find_small_folders(root)))


if __name__ == "__main__":
    main()
