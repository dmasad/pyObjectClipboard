import pickle
import binascii
import pyperclip

def copy_object(obj):
    '''
    Copy a Python object to the clipboard as a hex string.

    Args:
        obj: A Python object. Must be pickle-able.
    '''
    obj_bytes = pickle.dumps(obj)
    hex_data = binascii.hexlify(obj_bytes)
    pyperclip.copy(str(hex_data))

def paste_object():
    '''
    Paste an object copied to the clipboard with `copy_object`.
    '''
    payload = pyperclip.paste()
    if payload[0] != 'b':
        raise Exception("Clipboard does not seem to contain valid hex string")
    hex_str = payload[2:-1]
    hex_obj = binascii.unhexlify(hex_str)
    return pickle.loads(hex_obj)