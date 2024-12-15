from pathlib import Path
from multi_repo_workspace.model.repos import CodeRepositoryList


class Workspace:

    def __init__(self, name: str, path: Path, repos: CodeRepositoryList):
        self.name = name
        self.path = path
        self.repos = repos

    def initialize(self):
        pass

    def __str__(self):
        return f"name: {self.name} ({self.path.absolute()})\n{self.repos}"