class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_collection(self, collection):
        return "".join(f"\n-{entry}" for entry in collection)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors:{self._stringify_collection(self.authors)}\n"
            f"\nDependencies:{self._stringify_collection(self.dependencies)}\n"
            f"\nDevelopment dependencies:{self._stringify_collection(self.dev_dependencies)}"
        )
