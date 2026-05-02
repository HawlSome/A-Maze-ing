# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   read_file.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 15:56:12 by varandri            #+#    #+#            #
#   Updated: 2026/05/01 15:56:13 by varandri           ###   ########.fr      #
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
        if value.startswith("(") and value.endswith(")") and "," in value:
            inner = value[1:-1]
            parts = [p.strip() for p in inner.split(",") if p.strip()]
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
                if not "=" in line:
                    raise Exception
                key, value = line.split("=", 1)
                if "=" in value or not value.strip():
                    raise Exception
                config[key.lower().strip()] = parse_value(value.strip())
        except Exception:
            print("Error")
            sys.exit()
    return config