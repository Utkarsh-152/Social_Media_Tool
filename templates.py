import os

def create_file(path, content=""):
    """Create a file with optional content."""
    with open(path, 'w') as f:
        f.write(content)

def create_project_structure():
    """Create the required project structure."""
    # Define the directory structure
    structure = {
        "backend": [
            "__init__.py",
            "app.py",
            "routes.py",
            "models.py",
            "services.py",
            "database.py",
        ],
        "frontend/src/components": [
            "Dashboard.js",
            "Login.js",
            "PostScheduler.js",
        ],
        "frontend/src": [
            "App.js",
            "index.js",
        ],
        "frontend": [
            "package.json",
            "styles.css",
        ],
        "tests": [
            "test_routes.py",
            "test_services.py",
            "test_integration.py",
        ],
    }

    # Create directories and files
    for directory, files in structure.items():
        os.makedirs(directory, exist_ok=True)
        for file in files:
            create_file(os.path.join(directory, file))

    # Create additional top-level files
    create_file("README.md", "# Project Title\n\nProject description.")
    create_file("requirements.txt", "# Add your Python dependencies here\n")

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully!")