import sys

def det_ver():
    v_info = sys.version_info
    tuple_v = v_info[:3]
    v = list(tuple_v)
    test_list = [str(i) for i in v]
    full_v = '.'.join(test_list)

    return full_v


def set_ver(v):
    major = ''
    if v[0] == '3':
        major = '3'
    else:
        major = '2'
    return major


vers = det_ver()
print(set_ver(vers))

# def meta_col():
