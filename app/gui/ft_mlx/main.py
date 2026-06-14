#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 16:38:17 by varandri            #+#    #+#            #
#   Updated: 2026/06/14 17:01:07 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from mlx import Mlx, c_void_p
from typing import Any, Callable


class PyMlx:
    """
    Wrapper around the MiniLibX C graphics library using ctypes.

    Encapsulates MLX initialization and provides convenient methods for window
    management, drawing, image handling, and event handling.
    """

    def __init__(self) -> None:
        """
        Initialize the MLX graphics system.

        Creates an MLX instance and initializes the graphics connection.
        """
        self._mlx: Mlx = Mlx()
        self._ptr: c_void_p = self._mlx.mlx_init()

    def set_ptr(self, ptr: c_void_p) -> None:
        """
        Set the internal MLX pointer.

        Args:
            ptr: MLX pointer to store.
        """
        self._ptr = ptr

    def get_ptr(self) -> c_void_p:
        """
        Get the internal MLX pointer.

        Returns:
            The stored MLX pointer.
        """
        return self._ptr

    def new_window(self, width: int, height: int, title: str) -> c_void_p:
        """
        Create a new window.

        Args:
            width: Window width in pixels.
            height: Window height in pixels.
            title: Window title text.

        Returns:
            Pointer to the created window.
        """
        return self._mlx.mlx_new_window(
            self._ptr, width, height, title
        )

    def clear_window(self, win: c_void_p) -> Any:
        """
        Clear all contents of a window.

        Args:
            win: Window pointer to clear.

        Returns:
            Result of the clear operation.
        """
        return self._mlx.mlx_clear_window(
            self._ptr,
            win
        )

    def get_screen_size(self) -> Any:
        """
        Get the screen dimensions.

        Returns:
            Screen size information (width, height).
        """
        return self._mlx.mlx_get_screen_size(
            self._ptr
        )

    def put_str(
        self, win: c_void_p, x: int, y: int, color: int, string: str
    ) -> Any:
        """
        Draw a text string on a window.

        Args:
            win: Window pointer where text will be drawn.
            x: X coordinate (top-left) of text.
            y: Y coordinate (top-left) of text.
            color: Text color in 32-bit hex format
            (e.g., 0xFFFFFFFF for white).
            string: The text string to draw.

        Returns:
            Result of the string drawing operation.
        """
        return self._mlx.mlx_string_put(
            self._ptr, win, x, y, color, string
        )

    def put_pixel(
            self, win: c_void_p, x: int, y: int, color: int
    ) -> Any:
        """
        Draw a single pixel on a window.

        Args:
            win: Window pointer where pixel will be drawn.
            x: X coordinate of the pixel.
            y: Y coordinate of the pixel.
            color: Pixel color in 32-bit hex format (0xRRGGBBAA).

        Returns:
            Result of the pixel drawing operation.
        """
        return self._mlx.mlx_pixel_put(
            self._ptr, win, x, y, color
        )

    def new_image(self, width: int, height: int) -> c_void_p:
        """
        Create a new image buffer.

        Creates an off-screen image that can be modified pixel-by-pixel and
        then displayed to a window.

        Args:
            width: Image width in pixels.
            height: Image height in pixels.

        Returns:
            Pointer to the created image.
        """
        self._mlx.mlx_mouse_get_pos
        return self._mlx.mlx_new_image(
            self._ptr, width, height
        )

    def get_data_addr(
        self, image: c_void_p
    ) -> Any:
        """
        Get direct access to image pixel data.

        Returns data buffer, bits per pixel, size of line, and endianness
        information for manual pixel manipulation.

        Args:
            image: Image pointer.

        Returns:
            Tuple of (data_buffer, bits_per_pixel, line_size, format).
        """
        return self._mlx.mlx_get_data_addr(image)

    def put_image_to_window(
        self, win: c_void_p, img: c_void_p, x: int, y: int
    ) -> Any:
        """
        Display an image on a window at specified coordinates.

        Args:
            win: Window pointer where image will be displayed.
            img: Image pointer to display.
            x: X coordinate for image placement.
            y: Y coordinate for image placement.

        Returns:
            Result of the image display operation.
        """
        return self._mlx.mlx_put_image_to_window(
            self._ptr, win, img, x, y
        )

    def png_file_to_image(self, path: str) -> Any:
        """
        Load a PNG image from file.

        Args:
            path: File path to the PNG image.

        Returns:
            Tuple of (image_pointer, width, height).
        """
        return self._mlx.mlx_png_file_to_image(self._ptr, path)

    def xpm_file_to_image(self, path: str) -> Any:
        """
        Load an XPM image from file.

        Args:
            path: File path to the XPM image.

        Returns:
            Tuple of (image_pointer, width, height).
        """
        return self._mlx.mlx_xpm_file_to_image(self._ptr, path)

    def key_hook(
        self, win: c_void_p, callback: Callable[..., Any],
        params: list[Any] = [None]
    ) -> Any:
        """
        Register a keyboard event handler.

        The callback will be invoked when a key is pressed, receiving the
        key code and optional parameters.

        Args:
            win: Window pointer to attach keyboard hook to.
            callback: Function to call on keyboard events.
            Signature: callback(key_code, *params).
            params: Optional parameters to pass to the callback.
            Defaults to [None].

        Returns:
            Result of the hook registration.
        """
        return self._mlx.mlx_key_hook(win, callback, *params)

    def mouse_hook(
        self, win: c_void_p, callback: Callable[..., Any], params: list[Any]
    ) -> Any:
        """
        Register a mouse event handler.

        The callback will be invoked on mouse button clicks and movement,
        receiving button code, coordinates, and optional parameters.

        Args:
            win: Window pointer to attach mouse hook to.
            callback: Function to call on mouse events.
            Signature: callback(button, x, y, *params).
            params: Parameters to pass to the callback.

        Returns:
            Result of the hook registration.
        """
        return self._mlx.mlx_mouse_hook(win, callback, *params)

    def expose_hook(
        self, win: c_void_p, callback: Callable[..., Any], params: list[Any]
    ) -> Any:
        """
        Register a window expose event handler.

        The callback is triggered when the window needs to be redrawn.

        Args:
            win: Window pointer to attach expose hook to.
            callback: Function to call on expose events.
            params: Parameters to pass to the callback.

        Returns:
            Result of the hook registration.
        """
        return self._mlx.mlx_expose_hook(win, callback, *params)

    def loop_hook(
            self, callback: Callable[[list[Any]], Any], params: list[Any]
    ) -> Any:
        """
        Register a callback to run on each event loop iteration.

        The callback will be invoked repeatedly during the main event loop.

        Args:
            callback: Function to call each loop iteration.
            params: Parameters to pass to the callback.

        Returns:
            Result of the hook registration.
        """
        return self._mlx.mlx_loop_hook(self._ptr, callback, params)

    def loop(self) -> Any:
        """
        Start the main event loop.

        Blocks until loop_exit() is called or the user closes the window.
        Processes all registered events and callbacks.

        Returns:
            Result of the loop execution.
        """
        return self._mlx.mlx_loop(self._ptr)

    def hook(
        self, win: c_void_p, x_event: int, x_mask: int,
        callback: Callable[..., Any], params: list[Any] = [None]
    ) -> Any:
        """
        Register a generic X11 event handler.

        Allows handling of specific X11 events by event type and mask.

        Args:
            win: Window pointer to attach hook to.
            x_event: X11 event type code.
            x_mask: X11 event mask.
            callback: Function to call on matching events.
            params: Optional parameters to pass to the callback.
            Defaults to [None].

        Returns:
            Result of the hook registration.
        """
        return self._mlx.mlx_hook(win, x_event, x_mask, callback, *params)

    def mouse_hide(self) -> Any:
        """
        Hide the mouse cursor.

        Returns:
            Result of the hide operation.
        """
        return self._mlx.mlx_mouse_hide(self._ptr)

    def mouse_show(self) -> Any:
        """
        Show the mouse cursor.

        Returns:
            Result of the show operation.
        """
        return self._mlx.mlx_mouse_show(self._ptr)

    def mouse_move(self, x: int, y: int) -> Any:
        """
        Move the mouse cursor to specified coordinates.

        Args:
            x: Target X coordinate.
            y: Target Y coordinate.

        Returns:
            Result of the move operation.
        """
        return self._mlx.mlx_mouse_move(self._ptr, x, y)

    def mouse_get_pos(self, win: c_void_p) -> Any:
        """
        Get the current mouse cursor position relative to a window.

        Args:
            win: Window pointer to get position relative to.

        Returns:
            Tuple of (x, y) coordinates.
        """
        return self._mlx.mlx_mouse_get_pos(win)

    def key_autorepeatoff(self) -> Any:
        """
        Disable keyboard autorepeat.

        Held keys will not generate repeated key events.

        Returns:
            Result of the operation.
        """
        return self._mlx.mlx_do_key_autorepeatoff(self._ptr)

    def key_autorepeaton(self) -> Any:
        """
        Enable keyboard autorepeat.

        Held keys will generate repeated key events.

        Returns:
            Result of the operation.
        """
        return self._mlx.mlx_do_key_autorepeaton(self._ptr)

    def sync(self, cmd: Any, ptr: c_void_p) -> Any:
        """
        Synchronize drawing operations for a specific target.

        Args:
            cmd: Synchronization command.
            ptr: Pointer to the target (window or image).

        Returns:
            Result of the sync operation.
        """
        return self._mlx.mlx_sync(self._ptr, cmd, ptr)

    def global_sync(self) -> Any:
        """
        Perform global synchronization of all drawing operations.

        Returns:
            Result of the global sync operation.
        """
        return self._mlx.mlx_do_sync(self._ptr)

    def destroy_image(self, img: c_void_p) -> Any:
        """
        Free an image and release its memory.

        Args:
            img: Image pointer to destroy.

        Returns:
            Result of the destroy operation.
        """
        return self._mlx.mlx_destroy_image(self._ptr, img)

    def destroy_window(self, win: c_void_p) -> Any:
        """
        Close and destroy a window.

        Args:
            win: Window pointer to destroy.

        Returns:
            Result of the destroy operation.
        """
        return self._mlx.mlx_destroy_window(
            self._ptr, win
        )

    def loop_exit(self) -> Any:
        """
        Exit the main event loop.

        Stops the loop() function and returns control to the caller.

        Returns:
            Result of the exit operation.
        """
        return self._mlx.mlx_loop_exit(self._ptr)

    def release(self) -> Any:
        """
        Release MLX resources and clean up the graphics connection.

        Should be called when done with all MLX operations.

        Returns:
            Result of the release operation.
        """
        return self._mlx.mlx_release(
            self._ptr
        )
