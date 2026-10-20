import os


def read_config(path):
    f = open(path)
    data = f.read()
    return data


def run_expression(expr):
    return eval(expr)


def save_upload(filename, content):
    with open("/uploads/" + filename, "w") as out:
        out.write(content)


def list_files(folder):
    result = os.popen("ls " + folder).read()
    return result
