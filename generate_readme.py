import os

def extract_metadata(file_path):
    metadata = {
        'LeetCodeUrl': 'N/A', 
        'Question Name': 'N/A', 
        'Time Complexity': 'N/A', 
        'Space Complexity': 'N/A',
    }
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('# LeetCodeUrl:'):
                    metadata['LeetCodeUrl'] = line.split(':', 1)[1].strip()
                elif line.startswith('# Question Name:'):
                    metadata['Question Name'] = line.split(':', 1)[1].strip()
                elif line.startswith('# Time Complexity:'):
                    metadata['Time Complexity'] = line.split(':', 1)[1].strip()
                elif line.startswith('# Space Complexity:'):
                    metadata['Space Complexity'] = line.split(':', 1)[1].strip()
    except UnicodeDecodeError:
        print(f"Warning: Could not decode {file_path}. Skipping.")
    return metadata

def generate_markdown_table(root_directory):
    markdown_table = "| LeetCodeUrl | Time Complexity | Space Complexity | Link |\n"
    markdown_table += "|-------------|-----------------|------------------|------|\n"
    for subdir, _, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith('.py'):
                file_path = os.path.join(subdir, filename)
                metadata = extract_metadata(file_path)
                relative_path = os.path.relpath(file_path, root_directory)
                link = f"[View]({root_directory}/{relative_path.replace(os.sep, '/')})"  
                leetcode_url = f"[{metadata['Question Name']}]({metadata['LeetCodeUrl']})"
                markdown_table += f"| {leetcode_url} | {metadata['Time Complexity']} | {metadata['Space Complexity']} | {link} |\n"
    return markdown_table

def write_to_readme(root_directory, markdown_table):
    readme_path = os.path.join(root_directory, 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write(markdown_table)

# Replace 'path_to_your_root_directory' with the actual path to your Python files
root_directory_path = 'leetcode'
markdown_table = generate_markdown_table(root_directory_path)
write_to_readme('./', markdown_table)
