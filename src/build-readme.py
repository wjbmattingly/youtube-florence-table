import yaml

def load_yaml(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def difficulty_html(level):
    levels = ['Beginner', 'Intermediate', 'Advanced']
    result = '<div class="difficulty-container">\n<ul class="difficulty-list">\n'
    for l in levels:
        if l == level:
            result += f'    <li class="level selected"><strong>{l}</strong></li>\n'
        else:
            result += f'    <li class="level">{l}</li>\n'
    result += '</ul>\n</div>\n'
    return result

def generate_readme(data, readme_path):
    readme_content = f"# {data['project']['name']}\n\n"
    readme_content += "<head>\n"
    readme_content += "    <meta charset=\"UTF-8\">\n"
    readme_content += "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    readme_content += "    <link rel=\"stylesheet\" href=\"./assets/css/styles.css\">\n"
    readme_content += "</head>\n<body>\n"
    readme_content += difficulty_html(data['project']['level'])
    readme_content += "</body>\n\n"
    readme_content += f"[![thumbnail]({data['project']['video']['image_url']})]({data['project']['video']['video_url']})\n\n"
    readme_content += f"{data['project']['long_description']}\n\n"
    readme_content += "# Installation\n\n"
    readme_content += f"```bash\n"
    readme_content += f"git clone github.com/wjbmattingly/{data['project']['repo']}\n"
    readme_content += "```\n\n"
    readme_content += "# Quick Code\n\n"
    readme_content += "```python\n"
    readme_content += "# Add your quick-start code here\n"
    readme_content += "```\n"

    with open(readme_path, 'w') as file:
        file.write(readme_content)

if __name__ == '__main__':
    data = load_yaml('project.yaml')
    generate_readme(data, 'README.md')
