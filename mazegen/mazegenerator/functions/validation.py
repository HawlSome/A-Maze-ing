#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   validation.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 23:23:27 by varandri            #+#    #+#            #
#   Updated: 2026/06/21 21:51:47 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any


def process_config(config: dict[str, Any]) -> None:
    """Normalize all configuration dictionary keys to lowercase.

    Converts any dictionary keys that contain uppercase letters to their
    lowercase equivalents, removing the original uppercase keys. This is
    useful for handling configuration inputs from various sources with
    inconsistent capitalization (e.g., user input, environment variables).

    The function modifies the dictionary in-place. Values remain unchanged;
    only keys are normalized.

    Args:
        config (dict[str, Any]): Configuration dictionary to normalize.
            Modified in-place; original uppercase keys are removed.
    """
    for key in list(config.keys()):
        if key != key.lower():
            config[key.lower()] = config.pop(key)


def validate_config(config: dict[str, Any]) -> None:
    """Validate maze configuration dictionary for required keys, types,
    and bounds.

    Ensures the configuration contains all mandatory keys with correct types
    and valid values. Spatial coordinates (entry, exit) must fall within the
    maze bounds defined by width and height.

    Mandatory keys and validation rules:
        - width (int): Positive integer, used for bounds checking
        - height (int): Positive integer, used for bounds checking
        - entry (tuple[int, int]): 2-element tuple of ints, within bounds
        - exit (tuple[int, int]): 2-element tuple of ints, within bounds
        - output_file (str): Output file path (type checked only)
        - perfect (bool): Maze generation mode flag

    Spatial bounds validation:
        - Coordinates are 0-indexed and
        must satisfy: 0 <= x < width, 0 <= y < height
        - entry and exit must be different locations

    Args:
        config (dict[str, Any]): Configuration dictionary to validate.

    Raises:
        Exception: If any of the following occur:
            - Any mandatory key is missing
            - Type mismatch for width, height, entry, exit, or perfect
            - entry or exit is not a 2-tuple of integers
            - width or height is negative
            - entry or exit coordinates exceed maze bounds
            - entry and exit are at the same location
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
        if key == "imperfection_rate":
            perfection = config.get("perfect")
            if perfection is not None and perfection is False:
                try:
                    val: float = float(value)
                    if 0.0 >= val or val > 1.0:
                        raise Exception(
                            f"The value of {key.upper()} is"
                            " out of bound(0 < value <= 1)."
                        )
                except ValueError:
                    raise ValueError(
                        f"Incorrect format for the {key.upper()} value"
                    )
    entry: tuple[int, int] | None = config.get("entry")
    exit: tuple[int, int] | None = config.get("exit")
    if entry and exit and entry == exit:
        raise Exception("Entry and Exit can't be on the same place")
