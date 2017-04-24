"""This is a toolbox module for our crawler

:author: <your name>
"""
def gen_header(header_str):
    """This function generates a header_dict from Chrome dev tool for requests library
    
    :param header_str: The header string copied from Chrome developer tool.
    :type header_str: str
    :returns: header dictionary
    """
    header_dict = {}
    rows = header_str.split('\n')
    for row in rows:
        kv_list = row.split(":") # 把每一行用: split()開

        # kv_list = ['key1', 'https', '//ianchenhq.com']
        key = kv_list[0] 
        val = ':'.join(kv_list[1:]) # 再用:把1到結尾的element重新組合起來 -> https://ianchenhq.com
        header_dict[key] = val
    return header_dict