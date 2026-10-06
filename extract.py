import os, json, re

dir_path = r'C:\Users\pc\Videos\Radeon ReLive\TheOutlaw\YagmurStrike\modules'
zh_pattern = re.compile(r'[\u4e00-\u9fff]+')
strings_found = set()

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.lua'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find all strings in double or single quotes
            matches = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"|\'([^\'\\]*(?:\\.[^\'\\]*)*)\'', content)
            for m1, m2 in matches:
                s = m1 if m1 else m2
                if zh_pattern.search(s):
                    strings_found.add(s)

with open(r'C:\Users\pc\Videos\Radeon ReLive\TheOutlaw\YagmurStrike\zh_strings.json', 'w', encoding='utf-8') as f:
    json.dump(list(strings_found), f, indent=4, ensure_ascii=False)
print(f'Extracted {len(strings_found)} Chinese strings.')
