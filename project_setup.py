import pathlib

def create_dir_structure(base_dir, structure):
    for key, value in structure.items():
        dir_path = base_dir / key
        dir_path.mkdir(parents=True, exist_ok=True)
        if isinstance(value, dict):
            create_dir_structure(dir_path, value)
        elif isinstance(value, list):
            for file in value:
                (dir_path / file).touch(exist_ok=True)

def create_project_structure(root_dir):
    root_dir = pathlib.Path(root_dir)
    project_structure = {
        'app': {
            'api': {
                '__init__.py': None,
                'endpoints.py': None
            },
            'agents': {
                '__init__.py': None,
                'content_conversion.py': None,
                'quality_control.py': None,
                'style_analysis.py': None,
                'transformation_planning.py': None,
                'workflow.py': None
            },
            'models': {
                '__init__.py': None,
                'schemas.py': None
            },
            'rag': {
                '__init__.py': None,
                'knowledge_base.py': None,
                'retriever.py': None
            },
            'tests': {
                '__init__.py': None,
                'test_agents.py': None,
                'test_endpoints.py': None
            },
            'utils': {
                '__init__.py': None,
                'config.py': None,
                'llm.py': None
            },
            '__init__.py': None,
            'main.py': None
        },
        'data': {
            'style_guides.json': None,
            'transformation_examples.json': None
        },
        '.env': None,
        'Dockerfile': None,
        'docker-compose.yml': None,
        'requirements.txt': None,
        'README.md': None,
        'project_setup.py': None
    }

    for key, value in project_structure.items():
        if isinstance(value, dict):
            create_dir_structure(root_dir, {key: value})
        else:
            if key.endswith('.py') or key.endswith('.json') or key.endswith('.txt') or key.endswith('.md'):
                (root_dir / key).touch(exist_ok=True)
            else:
                (root_dir / key).mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
    root_dir = 'my_project'
    create_project_structure(root_dir)
    print(f"Project structure created at {root_dir}")
