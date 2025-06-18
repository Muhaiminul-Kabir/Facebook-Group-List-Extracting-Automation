# Read the raw input and split by 'https'
with open('output.txt') as f:
    raw = f.read()

# Split and re-add 'https' to each link
parts = [part.strip() for part in raw.split('https') if part.strip()]
links = [f"https{part}" for part in parts]
# Start building the HTML
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Link Grid</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 40px;
            background-color: #f0f0f0;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }
        .grid a {
            display: block;
            padding: 15px;
            background-color: #3498db;
            color: white;
            text-align: center;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: background-color 0.2s;
        }
        .grid a:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <h1>Link Grid</h1>
    <div class="grid">
"""

# Add each link as a button
for i, link in enumerate(links, 1):
    html += f'        <a href="{link}" target="_blank">Link {i}</a>\n'

# Close the tags
html += """
    </div>
</body>
</html>
"""

# Write to file
with open('link_grid.html', 'w') as f:
    f.write(html)
