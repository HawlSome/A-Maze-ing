#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/06/19 15:12:41 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

if __name__ == "__main__":
    try:
        from app import a_maze_ing
        import sys
        _, file = sys.argv
        a_maze_ing(file)
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")
        if e.__class__.__name__ == "ModuleNotFoundError":
            print("\n==== Follow the instructions bellow =====\n")
            print(
                "create a virtuial env: python -m venv env_name.\n"
                "switch to the virtual env: source env_name/bin/activate.\n"
                "install needed modules: make install.\n"
                "Run the project again.\n"
                "\n========================================="
            )
