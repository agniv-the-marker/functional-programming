"""
Replaces each [[file_name]] with [file_name](github link),
which fixes the broken links in the Obsidian vault.
"""
import glob
import json
import os

DIRECTORY = './'
BASE_URL = 'https://github.com/agniv-the-marker/functional-programming/blob/main'
PLUGIN_PATH = './.obsidian/plugins/digitalgarden/data.json'

if __name__ == "__main__":
    files = glob.glob(DIRECTORY + '/**/[!.]*[!~].*', recursive=True)
    non_markdown = []
    for file in files:
        if file.endswith('.md'):
            continue
        file = file.replace('\\', '/')
        file = file.replace(' ', '%20') # replace spaces with %20
        non_markdown.append(file[1:])
    with open(PLUGIN_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        data["customFilters"] = []
        for file in non_markdown:
            file_name = file.split('/')[-1]
            data["customFilters"].append({
                'pattern': "\\[\\[" + file_name + "\\]\\]",
                'flags': 'g',
                'replace': f'[{file_name}]({BASE_URL}{file})'
            })
    os.remove(PLUGIN_PATH)
    with open(PLUGIN_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
