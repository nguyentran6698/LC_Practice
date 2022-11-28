def flatten(d: dict, separator="."):
    new_dict = {}
    for k, v in d.items():
        if isinstance(v, dict):
            nest_dict = flatten(v)
            for flatK, flatV in nest_dict.items():
                new_dict[k + separator + flatK] = flatV
        else:
            new_dict[k] = v
    return new_dict


test1 = {"key": 3, "foo": {"a": 5, "bar": {"baz": 8}}}

print(flatten(test1))
