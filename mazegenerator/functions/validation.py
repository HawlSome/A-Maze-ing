#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   validation.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 23:23:27 by varandri            #+#    #+#            #
#   Updated: 2026/06/19 23:36:26 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any


def process_config(config: dict[str, Any]) -> None:
    for key in config.keys():
        config[key.lower()] = config[key]


def validate_config(config: dict[str, Any]) -> None:
    """
    Validate that a configuration dictionary has required keys and
    correct types.

    Mandatory keys: width, height, entry, exit, output_file, perfect

    Type requirements:
    - width, height: int
    - entry, exit: tuple of 2 ints, must be within maze bounds
    - perfect: bool

    Args:
        config: The configuration dictionary to validate.

    Raises:
        Exception: If any mandatory key is missing, has incorrect type,
                   or is out of bounds for spatial coordinates.
    """
    mandatory: list[str] = [
        "width", "height", "entry",
        "exit", "output_file", "perfect"
    ]
    for key in mandatory:
        if key not in config:
            raise Exception(
                f"Missing mandatory KEY-VALUE: {key.upper()}-VALUE"
            )
    for key, value in config.items():
        if key in ("width", "height") and not isinstance(value, int):
            raise Exception(
                f"Incorrect format for the {key.upper()} value"
            )
        elif key in ("entry", "exit") and not (
            isinstance(value, tuple) and
            len(value) == 2 and
            all(isinstance(part, int) for part in value)
        ):
            raise Exception(
                f"Incorrect format for the {key.upper()} value"
            )
        elif key in ("entry", "exit"):
            w: int
            h: int
            x: int
            y: int
            w, h = ((config["width"]), (config["height"]))
            x, y = config[key]
            if w and h and x and y:
                w -= 1
                h -= 1
            if w < 0 or h < 0:
                raise Exception(
                    "Incorrect value(s) - WIDTH and/or HEIGHT "
                    "cant have negative values ."
                )
            if x < 0 or x > w or y < 0 or y > h:
                raise Exception(
                    f"{key.upper()}({x}, {y}) out of"
                    f" the maze bound ({w}, {h})"
                )
        elif (key == "perfect" and not isinstance(value, bool)):
            raise Exception(
                f"Incorrect format for the {key.upper()} value"
            )
    entry: tuple[int, int] | None = config.get("entry")
    exit: tuple[int, int] | None = config.get("exit")
    if entry and exit and entry == exit:
        raise Exception("Entry and Exit can't be on the same place")
