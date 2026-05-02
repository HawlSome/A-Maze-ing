#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   config_error.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 11:03:42 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/02 11:05:16 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class MissingConfigError(Exception):
    def __init__(self, message: str = "Missing mandatory key in config.txt"):
        super().__init__(message)
