import os
from pathlib import Path

def print_directory_tree(start_path, output_file):
    """
    Print the directory tree structure and file contents for Django/React projects.
    
    Args:
        start_path (str): The root directory to start from
        output_file (str): Path to the output file
    """
    # Directories to exclude
    exclude_dirs = {
        # Django specific
        '__pycache__', 
        'migrations',
        'venv',
        '.env',
        '.pytest_cache',
        '.coverage',
        
        # React/Node specific
        'node_modules',
        'build',
        'dist',
        'coverage',
        
        # Version control and IDE
        '.git',
        '.idea',
        '.vscode',
        
        # Cache and temporary files
        '.cache',
        'tmp'
    }

    # File patterns to exclude
    exclude_file_patterns = {
        # Django
        '*.pyc',
        '*.pyo',
        '*.pyd',
        'db.sqlite3',
        '*.logs',
        
        # React/Node
        'package-lock.json',
        'yarn.lock',
        '*.map',
        
        # Other
        '.DS_Store',
        '*.swp',
        '*.swo',
        '.env',
        '*.pid'
    
    }

    # File extensions to include
    include_extensions = {
        # Django/Python
        '.py',
        '.env.example',
        'requirements.txt',
        'Dockerfile',
        'docker-compose.yml',
        
        # React/JavaScript
        '.js',
        '.jsx',
        '.ts',
        '.tsx',
        '.css',
        '.scss',
        '.html',
        '.json',
        
        # Configuration files
        '.yml',
        '.yaml',
        '.toml',
        '.ini',
        '.conf'
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Project Structure for: {start_path}\n")
        f.write("=" * 50 + "\n\n")
        
        # Print directory tree
        f.write("Directory Structure:\n")
        f.write("-" * 20 + "\n")
        
        for root, dirs, files in os.walk(start_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            # Calculate relative path for cleaner output
            relative_root = os.path.relpath(root, start_path)
            level = relative_root.count(os.sep)
            indent = '│   ' * level
            
            if relative_root != '.':
                f.write(f"{indent}├── {os.path.basename(root)}/\n")
            
            subindent = '│   ' * (level + 1)
            
            # Filter and sort files
            included_files = []
            for file in sorted(files):
                file_ext = os.path.splitext(file)[1].lower()
                file_path = os.path.join(relative_root, file)
                
                # Check if file should be included
                should_include = (
                    file_path.endswith(tuple(include_extensions)) and
                    not any(file_path.endswith(pat.replace('*', '')) for pat in exclude_file_patterns)
                )
                
                if should_include:
                    included_files.append(file)
                    f.write(f"{subindent}├── {file}\n")
        
        f.write("\nFile Contents:\n")
        f.write("=" * 50 + "\n\n")
        
        # Print file contents
        for root, dirs, files in os.walk(start_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in sorted(files):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, start_path)
                file_ext = os.path.splitext(file)[1].lower()
                
                # Check if file should be included
                should_include = (
                    relative_path.endswith(tuple(include_extensions)) and
                    not any(relative_path.endswith(pat.replace('*', '')) for pat in exclude_file_patterns)
                )
                
                if should_include:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as content_file:
                            content = content_file.read()
                            f.write(f"File: {relative_path}\n")
                            f.write("-" * len(f"File: {relative_path}") + "\n")
                            f.write(content)
                            f.write("\n\n" + "=" * 50 + "\n\n")
                    except Exception as e:
                        f.write(f"Could not read {relative_path}: {str(e)}\n\n")

if __name__ == "__main__":
    # You can run this for backend and frontend separately
    backend_path = "/home/pirat/Desktop/pyth/scraper/TreeContent/backend"  # Adjust this path
    backend_output = "django_structure.txt"
    
    frontend_path = "/home/pirat/Desktop/pyth/scraper/TreeContent/frontend"  # Adjust this path
    frontend_output = "react_structure.txt"
    
    main_path = "/home/pirat/Desktop/pyth/TreeContent/scraper"
    main_output = "main.txt"
    
    # Export backend structure
    print_directory_tree(backend_path, backend_output)
    print(f"Django project structure exported to {backend_output}")
    
    # Export frontend structure
    print_directory_tree(frontend_path, frontend_output)
    print(f"React project structure exported to {frontend_output}")
    
    print_directory_tree(main_path , main_output)
    print(f"React project structure exported to {main_output}")