from typing import *
from collections import defaultdict
def zmx_reader(file_name: str) -> Dict[str, Union[dict, str]]:
    """Read Zemax *.zmx file.

    Args:
        file_name (str): zmx file name
    """
    parsed_data: DefaultDict[str, List[str]] = defaultdict(lambda: [])
    with open(file_name, "r", encoding="utf-16") as f:
        line = f.readline()
        while line:
            key, value = line.split(" ", 1)
            if key == "SURF":
                if "SURF" not in parsed_data:
                    parsed_data["SURF"] = {}
                surface: DefaultDict[str, List[str]] = defaultdict(lambda: [])
                line = f.readline()
                while line.startswith("  "):
                    key_surf, value_surf = line[2:].split(" ", 1)
                    surface[key_surf] = value_surf
                    line = f.readline()
                parsed_data[key][value] = dict(surface)

            else:
                parsed_data[key].append(value.split("\n")[0])
                line = f.readline()
    return dict(parsed_data)