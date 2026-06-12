#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   read_file.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 15:56:12 by varandri            #+#    #+#            #
#   Updated: 2026/06/13 00:02:31 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any
import sys


def parse_value(value: str) -> Any:
    """
    Convert a string value to its appropriate Python type.

    Attempts to parse the input string as (in order):
    - Boolean: "true" or "false" (case-insensitive)
    - Integer: numeric value
    - Tuple: comma-separated values, recursively parsed
    - String: falls back if all other conversions fail

    Args:
        value: The string value to parse.

    Returns:
        The parsed value as bool, int, tuple, or str.

    Raises:
        SystemExit: If tuple parsing fails and raises an exception.
    """
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


def read_file(file: str) -> dict[str, Any]:
    """
    Read and parse a configuration file into a dictionary.

    Reads a configuration file with KEY=VALUE syntax (one per line).
    - Lines are stripped of comments (# and everything after)
    - Empty lines are skipped
    - Each line must contain exactly one '=' separator
    - Values are parsed using parse_value()
    - The resulting config is validated before returning

    Args:
        file: Path to the configuration file.

    Returns:
        A dictionary mapping config keys (lowercase) to parsed values.

    Raises:
        SystemExit: On file not found, malformed syntax, invalid values,
        or missing mandatory keys/incorrect formats (from validate_config).
    """
    config: dict[str, Any] = {}
    try:
        with open(file, "r") as f:
            for line in f:
                if "#" in line:
                    line = line[:line.index("#")].strip()
                if not line or line == "\n":
                    continue
                if "=" not in line:
                    raise Exception("Found KEY with no assigned VALUE")
                key, value = line.split("=", 1)
                if "=" in value or not value.strip():
                    raise Exception("Found a KEY with an incorrect VALUE")
                config[key.lower().strip()] = parse_value(value.strip())
        validate_config(config)
    except (Exception, FileNotFoundError) as e:
        if isinstance(e, FileNotFoundError):
            print("Error: File not found")
            sys.exit()
        print(f"Error: {e}")
        sys.exit()
    return config


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
            if x < 0 or x > w or y < 0 or y > h:
                raise Exception(
                    f"{key.upper()}({x}, {y}) out of"
                    f" the maze bound ({w}, {h})"
                )
        elif (key == "perfect" and not isinstance(value, bool)):
            raise Exception(
                f"Incorrect format for the {key.upper()} value"
            )
