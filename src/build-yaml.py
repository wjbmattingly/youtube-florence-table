import yaml
import sys
import re

def get_video_id(video_url):
    # Extract video ID from the YouTube URL
    return video_url.split('v=')[1]

def construct_thumbnail_url(video_id):
    # Construct the URL for the maximum resolution thumbnail
    return f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'

def read_requirements():
    package_list = []
    with open('requirements.txt', 'r') as file:
        for line in file:
            package = re.match(r'([\w\-]+)', line)
            if package:
                package_list.append(package.group(0))
    return package_list

def create_yaml(youtube_url, difficulty):
    video_id = get_video_id(youtube_url)
    video_details = {
        'video_title': 'Title',  # Update manually or fetch if needed
        'video_url': youtube_url,
        'image_url': construct_thumbnail_url(video_id),
        'video_date': 'Date'  # Update manually or fetch if needed
    }
    
    dependencies = read_requirements()
    
    data = {
        'project': {
            'name': 'Project',  # Update with the actual project name
            'repo': 'Repo',
            'level': difficulty,
            'long_description': 'LongDescription',
            'short_description': 'ShortDescription',
            'video': video_details,
            'authors': [{'name': "William J.B. Mattingly"}]
        },
        'dependencies': {
            'python': ">=3.10",
            'packages': dependencies
        }
    }
    
    with open('project.yaml', 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False, sort_keys=False)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python build-yaml.py 'YouTube URL' 'Difficulty Level'")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    difficulty = sys.argv[2]
    create_yaml(youtube_url, difficulty)

# python src/build-yaml.py 'https://www.youtube.com/watch?v=gDVbXEKiNmE' 'Intermediate'