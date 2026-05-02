# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   read_file.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 15:56:12 by varandri            #+#    #+#            #
#   Updated: 2026/05/02 11:55:29 by varandri           ###   ########.fr      #
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
    with open(file, "r") as f:
        try:
            for line in f:
                if "#" in line:
                    line = line[:line.index("#")].strip()
                if not line:
                    continue
                if "=" not in line:
                    raise Exception
                key, value = line.split("=", 1)
                if "=" in value or not value.strip():
                    raise Exception
                config[key.lower().strip()] = parse_value(value.strip())
            if not validate_config(config):
                raise Exception
        except Exception:
            print("Error")
            sys.exit()
    return config


def validate_config(config: dict[str, Any]) -> bool:
    mandatory = [
        "width", "height", "entry",
        "exit", "output_file", "perfect"
    ]
    for key in mandatory:
        if key not in list(config.keys()):
            return False
    for key, value in config.items():
        if key == "width" or key == "height" and not isinstance(int, value):
            return False
        elif (key == "entry" or key == "exit" and
              not isinstance(tuple[int, int], value)):
            return False
        elif (key == "perfect" and not isinstance(bool, value)):
            return False
    return True
