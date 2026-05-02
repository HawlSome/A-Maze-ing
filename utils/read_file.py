# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   read_file.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 15:56:12 by varandri            #+#    #+#            #
#   Updated: 2026/05/02 13:35:26 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from packages import Any, sys


def parse_value(value: str) -> Any:
    if value.lower() in ["true", "false"]:
        return value.lower() == "true"
    else:
        pass

    try:
        return int(value)
    except Exception:
        pass

    try:
        if "," in value:
            parts = [p.strip() for p in value.split(",") if p.strip()]
            return tuple(parse_value(p) for p in parts)
        else:
            pass
    except Exception:
        print("Error")
        sys.exit()

    return value


def read_file(file: "str") -> dict[str, Any]:
    config: dict[str, Any] = {}
    try:
        with open(file, "r") as f:
            for line in f:
                if "#" in line:
                    line = line[:line.index("#")].strip()
                if not line:
                    continue
                if "=" not in line:
                    raise Exception("Key with no assigned value")
                key, value = line.split("=", 1)
                if "=" in value or not value.strip():
                    raise Exception("Key with no value found")
                config[key.lower().strip()] = parse_value(value.strip())
            if not validate_config(config):
                raise Exception("Invalid file/value format")
    except (Exception, FileNotFoundError) as e:
        if isinstance(e, FileNotFoundError):
            print("Error: File not found")
            sys.exit()
        print(f"Error: {e}")
        sys.exit()
    return config


def validate_config(config: dict[str, Any]) -> bool:
    mandatory = [
        "width", "height", "entry",
        "exit", "output_file", "perfect"
    ]
    for key in mandatory:
        if key not in config:
            return False
    for key, value in config.items():
        if key in ("width", "height") and not isinstance(value, int):
            return False
        elif key in ("entry", "exit") and not (
            isinstance(value, tuple) and
            len(value) == 2 and
            all(isinstance(part, int) for part in value)
        ):
            return False
        elif (key == "perfect" and not isinstance(value, bool)):
            return False
    return True
