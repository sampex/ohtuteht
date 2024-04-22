from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        parsed_content = tomllib.loads(content)
        #print(parsed_content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        info = parsed_content['tool']['poetry']
        return Project(info.get("name"), info.get("description"), info.get("dependencies", {}), info['group']['dev'].get("dependencies", {}),info.get("license"), info.get("authors"))
