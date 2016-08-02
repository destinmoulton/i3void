#### What is i3void?
***
i3void creates a blank window for padding around other windows in the i3 window manager.

I have two high resolution monitors and frequently find that I don't want a fullscreen window as they are too wide. I use i3 because it limits visual distraction. As such, I don't like padding the edges of the screen with terminals as my terminal prompt is too visually busy. i3Void is meant to fill a workspace in an unobtrusive way.


#### Usage
***
When you activate/mouseover the i3void window you are presented with two buttons: "Color" and "Close".

Clicking on the Color button allows you to change the color of the i3Void window. This is useful for identifying workspaces by color.

You can close i3Void by either clicking the Close button, or using the Ctrl+q keyboard combination.


#### Requirements
***

* Python 2.7
* PyQt4 Python Library


#### Start i3 Via Keyboard Shortcut
***

I mapped $mod+w to open a new i3Void window.

Add the following to the i3 config file to start an i3void window.

> bindsym $mod+w exec python <path_to_i3void>/i3void/i3void.py

* Replace <path_to_i3void> with its location.
* Change $mod+w to your preferred key combo.


#### License
***
i3void is released under the MIT license.

