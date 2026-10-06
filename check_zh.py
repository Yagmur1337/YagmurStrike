import os, re

dir_path = r'C:\Users\pc\Videos\Radeon ReLive\TheOutlaw\YagmurStrike'
zh_pattern = re.compile(r'[\u4e00-\u9fff]+')
remaining = []
for root, dirs, files in os.walk(dir_path):
    dirs[:] = [d for d in dirs if d != '.git']
    for file in files:
        if not file.endswith('.lua'):
            continue
        fp = os.path.join(root, file)
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, 1):
                m = zh_pattern.search(line)
                if m:
                    remaining.append(f'{file}:{i}: {line.strip()[:120]}')

with open('remaining_zh.txt', 'w', encoding='utf-8') as out:
    out.write(f'Remaining Chinese: {len(remaining)} lines\n\n')
    for r in remaining:
        out.write(r + '\n')
print(f'Done. {len(remaining)} lines written to remaining_zh.txt')
