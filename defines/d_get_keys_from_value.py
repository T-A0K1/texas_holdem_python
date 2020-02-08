#get dict'value from key
#refer from https://note.nkmk.me/python-dict-get-key-from-value/
def get_keys_from_value(d_, val_):
    return [k for k, v in d_.items() if v == val_]
