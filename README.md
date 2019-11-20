#### What is i3void?

---

i3void creates a blank window for padding around other windows in the i3 window manager.

I have two high resolution monitors and frequently find that I don't want a fullscreen window as they are too wide. I use i3 because it limits visual distraction. As such, I don't like padding the edges of the screen with terminals as my terminal prompt is too visually busy. i3Void is meant to pad a workspace in an unobtrusive way.

#### Usage

---

Two buttons appear when you mouseover or activate the i3void window:

- Color
- Close

Clicking on the Color button allows you to change the color of the i3Void window. This is useful for identifying workspaces by color.

You can close i3Void by either clicking the Close button, or using the Ctrl+q keyboard combination.

#### Requirements

---

- Python 3
- PyQt5 Python Library

#### Installation

---

```
$ git clone https://github.com/destinmoulton/i3void
$ cd i3void
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install PyQt5
```

#### Start i3void Via Keyboard Shortcut in i3

---

I mapped \$mod+w to open a new i3Void window.

Add the following to the i3 config file to start an i3void window.

> bindsym \$mod+w exec python <path_to_i3void>/i3void/i3void.py

- Replace <path_to_i3void> with its location.
- Change \$mod+w to your preferred key combo.

#### License

MIT
