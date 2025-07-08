import pathlib

def create_dir_structure(base_dir, structure):
    for key, value in structure.items():
        path = base_dir / key
        if isinstance(value, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_dir_structure(path, value)
        elif isinstance(value, list):
            path.mkdir(parents=True, exist_ok=True)
            for file in value:
                (path / file).touch(exist_ok=True)
        else:
            if value is None:
                if key.endswith('.py') or key.endswith('.json') or key.endswith('.txt') or key.endswith('.md') or key.endswith('.yml'):
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.touch(exist_ok=True)
                else:
                    path.mkdir(parents=True, exist_ok=True)

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
    create_dir_structure(root_dir, project_structure)

if __name__ == '__main__':
    root_dir = pathlib.Path.cwd()
    create_project_structure(root_dir)
    print(f"Project structure created at {root_dir}")