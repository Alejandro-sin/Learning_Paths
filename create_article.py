import os
import sys
from pathlib import Path



def create_article_structure(article_name):
    """
    Creates the directory structure for a new article
    
    Args:
        article_name (str): Name of the article/project
    """
    try:
        # Create main directory
        base_dir = Path(article_name)
        base_dir.mkdir(exist_ok=True)
        
        # Create subdirectories
        subdirs = ['_assets', '_references', 'notebooks']
        for subdir in subdirs:
            (base_dir / subdir).mkdir(exist_ok=True)
            
        # Create files
        (base_dir / 'requirements.txt').touch()
        (base_dir / 'Notes.md').touch()
        
        print(f"✅ Article structure created successfully for '{article_name}'")
        
    except Exception as e:
        print(f"❌ Error creating article structure: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python create_article.py <article_name>")
        sys.exit(1)
    
    article_name = sys.argv[1]
    create_article_structure(article_name)

if __name__ == "__main__":
    main()