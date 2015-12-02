# pyObjectClipboard

A very simple hack for copying and pasting Python objects.

It pickles an object and converts the pickled byte data to hexidecimals, then converts the hex to string and pastes it to the clipboard. On the other end, it pastes the hex string from the clipboard, converts it back to byte data, and finally unpickles that.

### Why?
Sometimes you (or at least I) want to be able to transfer Python objects between interpreter sessions. Writing the object to a file in one session and unpickling it in the other session isn't the most convenient thing.

### Requirements

Tested on Python 3.4, on a Mac. YMMV.

The only external dependency is [pyperclip](https://github.com/asweigart/pyperclip) (which has some external dependencies on Linux).

```
pip install pyperclip
```

### Example

#### Session 1

```.python
from pyobjclipboard import copy_object

my_data = [0, "One", (2, 3), {"Four": 4}]
copy_object(my_data)
```

#### Session 2
```
from pyobjclipboard import paste_object

my_data = paste_object()
```

### Contributing

Feel free! 

### License

MIT.


