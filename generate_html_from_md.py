import os
import re

import os
import re

def parse_markdown_table(md_file_path):
    with open(md_file_path, 'r') as md_file:
        lines = md_file.readlines()

    headers = [header.strip() for header in lines[0].split('|')[1:-1]]
    rows = [line.split('|')[1:-1] for line in lines[2:] if line.strip()]
    
    return headers, rows

def markdown_to_html_link(markdown_text):
    md_link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    return re.sub(md_link_pattern, r'<a href="\2">\1</a>', markdown_text)

def generate_html(headers, rows, output_file):
    html_content = '''
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            border: 1px solid #ddd;
        }}
        th, td {{
            border: 1px solid #ddd;
            text-align: left;
            padding: 8px;
        }}
        th {{
            background-color: #f2f2f2;
            cursor: pointer;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>

<table>
    <thead>
        <tr>{}</tr>
    </thead>
    <tbody>
        {}
    </tbody>
</table>

<script>
// JavaScript sorting function here
</script>

</body>
</html>
    '''

    headers_html = ''.join([f'<th>{header}</th>' for header in headers])
    rows_html = '\n'.join(['<tr>{}</tr>'.format(''.join([f'<td>{markdown_to_html_link(cell)}</td>' for cell in row])) for row in rows])

    # Add the sorting JavaScript function
    sort_function = '''
function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.querySelector("table");
    switching = true;
    dir = "asc";
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < rows.length - 1; i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch= true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount ++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}
document.querySelectorAll("th").forEach((header, index) => {
    header.addEventListener("click", function() {
        sortTable(index);
    });
});
    '''

    # Writing the HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content.format(headers_html, rows_html).replace('<script>', '<script>' + sort_function))

# Usage example
markdown_file_path = 'README.md'  # Replace with your markdown file path
output_html_file = 'report.html'  # The output HTML file name
headers, rows = parse_markdown_table(markdown_file_path)
generate_html(headers, rows, output_html_file)