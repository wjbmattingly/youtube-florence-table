import yaml

def load_yaml(filepath):
    """Loads data from a YAML file."""
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def create_gh_pages_action(project):
    """Creates a GitHub action to deploy GitHub Pages."""
    content = """
name: Deploy GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Jekyll
        uses: helaili/jekyll-action@2.2.0  # Make sure this is the latest or required version
        with:
          token: ${{{{ secrets.GITHUB_TOKEN }}}}
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3  # Verify the version is up-to-date
        with:
          github_token: ${{{{ secrets.GITHUB_TOKEN }}}}
          publish_dir: './_site'
    """
    with open('.github/workflows/deploy-pages.yml', 'w') as file:
        file.write(content)

def create_update_repo_action(project):
    """Creates a GitHub action to update repository details based on project configuration."""
    description = project.get('short_description', 'Default description')
    homepage = project.get('repo', 'Default repo URL')
    content = f"""
name: Update Repository Details

on:
  push:
    branches:
      - main

jobs:
  update-details:
    runs-on: ubuntu-latest
    steps:
      - name: Update repository details
        uses: peter-evans/repository-dispatch@v1  # Check if there's a newer version compatible with Node20
        with:
          token: ${{{{ secrets.PAT }}}}
          repository: ${{{{ github.repository }}}}
          event-type: update-repo-info
          client-payload: '{{{{"description": "{description}", "homepage": "https://{homepage}", "has_issues": true, "has_projects": true, "has_wiki": true}}}}'
    """
    with open('.github/workflows/update-repo-details.yml', 'w') as file:
        file.write(content)

if __name__ == '__main__':
    project_data = load_yaml('project.yaml')['project']
    create_gh_pages_action(project_data)
    create_update_repo_action(project_data)
