from typing import List


class CodeRepository:
    def __init__(self, folder_name: str, url: str, branch: str):
        self.folder_name = folder_name
        self.url = url
        self.branch = branch

    def __str__(self):
        return f"{self.name} ({self.path})"


class CodeRepositoryList(List):
    def __init__(self, repos: List[CodeRepository] = []):
        super().__init__(repo for repo in repos)

    def __setitem__(self, index, repo):
        super().__setitem__(index, repo)

    def __str__(self) -> str:
        repos_string = ""
        for repo in self:
            repos_string += str(repo)
        return repos_string

    def insert(self, index, repo: CodeRepository):
        super().insert(index, repo)

    def append(self, repo: CodeRepository):
        super().append(repo)

    def extend(self, other: CodeRepository):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(repo for repo in other)
