#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   read_file.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 15:24:07 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/02 11:29:44 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
from typing import Any
from exceptions.config_error import MissingConfigError


def parse_config(file: str) -> dict[str, Any]:
    try:
        config_dict: dict[str, Any] = {}
        errors: str = []

        with open(file, 'r') as config_file:
            for line in config_file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '#' in line:
                    line = line[:line.index('#')]

                try:
                    key, value = line.split("=")
                    value = value.strip()
                    key = key.lower()

                    if key in ('width', 'height'):
                        try:
                            config_dict[key] = int(value)
                        except ValueError as e:
                            errors.append("Invalid parameter for "
                                          f"{key}: {str(e)}")

                    elif key in ('entry', 'exit'):
                        try:
                            parts = value.split(',')
                            if len(parts) == 1:
                                errors.append("Invalid parameter for "
                                              f"{key}: missing "
                                              "another point of a coordinate")
                                continue
                            coords = tuple(int(p.strip()) for p in parts)
                            config_dict[key] = coords
                        except ValueError as e:
                            errors.append("Invalid parameter for "
                                          f"{key}: {str(e)}")

                    elif key == 'perfect':
                        config_dict[key] = bool(value)

                    else:
                        config_dict[key] = value

                except ValueError:
                    continue

        if errors:
            for error in errors:
                print(error)
            sys.exit()

    except IOError:
        print(f"<Usage> python3 {sys.argv[0]} config.txt")
        sys.exit()

    else:
        return config_dict


def get_config(file: str) -> dict[str, Any]:
    config = parse_config(file)
    keys = ['width', 'height', 'entry', 'exit', 'output_file', 'perfect']

    for k in keys:
        if k not in config:
            raise MissingConfigError("Invalid config file: "
                                     f"Missing '{k}' in config.txt")
        else:
            continue
    return config
