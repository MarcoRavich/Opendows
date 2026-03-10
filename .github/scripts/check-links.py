import re
import requests
from github import Github
from pathlib import Path

# Initialize GitHub client
g = Github()

def extract_repo_links(content):
    """Extract GitHub repository links from markdown"""
    # Pattern: [text](https://github.com/owner/repo...)
    pattern = r'\[([^\]]+)\]\(https://github\.com/([^/]+)/([^/\)]+)'
    matches = re.finditer(pattern, content)
    return [(match.group(0), match.group(2), match.group(3)) for match in matches]

def is_repo_available(owner, repo):
    """Check if a GitHub repository still exists"""
    try:
        repo_obj = g.get_repo(f"{owner}/{repo}")
        # Additional check: verify it's not archived or deleted
        if repo_obj.archived:
            print(f"⚠️  {owner}/{repo} is archived")
            return False
        return True
    except Exception as e:
        print(f"❌ {owner}/{repo} not found or inaccessible: {e}")
        return False

def update_markdown_file(file_path):
    """Check and remove links to dead repositories"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    dead_repos = []
    
    # Extract all repository links
    links = extract_repo_links(content)
    
    for full_link, owner, repo in links:
        print(f"Checking: {owner}/{repo}...")
        
        if not is_repo_available(owner, repo):
            dead_repos.append((full_link, owner, repo))
            # Remove the entire table row containing this link
            # Pattern matches the entire markdown table row
            row_pattern = f".*{re.escape(owner)}/{re.escape(repo)}.*\n"
            content = re.sub(row_pattern, '', content)
            print(f"  → Removed dead link: {owner}/{repo}")
        else:
            print(f"  ✓ Available")
    
    # Write back only if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n📝 Updated {file_path}")
        return dead_repos
    else:
        print(f"\n✅ No dead links found in {file_path}")
        return []

def main():
    tweakers_file = Path('Tweakers.md')
    
    if tweakers_file.exists():
        dead_repos = update_markdown_file(tweakers_file)
        
        if dead_repos:
            print(f"\n🗑️  Removed {len(dead_repos)} dead repositories:")
            for _, owner, repo in dead_repos:
                print(f"   - {owner}/{repo}")
    else:
        print(f"File not found: {tweakers_file}")

if __name__ == '__main__':
    main()
