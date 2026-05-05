import json


def import_notebook(path, caller_globals, marker="#EXPORT"):
    with open(path) as f:
        nb = json.load(f)
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            if source.strip().startswith(marker):
                exec(source, caller_globals)

