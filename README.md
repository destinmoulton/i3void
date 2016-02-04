### A Blank Window
i3Void is a blank window for padding in the i3 window manager.

I have two high resolution monitors and frequently find that I don't want a fullscreen window. I don't like padding the edges of the screen with terminals; they are too busy. i3void provides a blank window that

When you activate the i3void window you are presented with two buttons to Close or change the background color.


### Requirements

* PyQt4 Python Library


### i3 Keyboard Shortcut

Add the following to the i3 config file to run i3void.

> bindsym $mod+w exec python <path_to_i3void>/i3void/i3void.py

I have it mapped to $mod+w, but you can change it to your preferred key.


### License
i3void is released under the MIT license.

