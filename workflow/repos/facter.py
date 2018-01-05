from workflow.actions.repo_actions import (bump_cpp_project, bump_version_file, sequence)
from workflow.repos.git_repository import GITHUB_USERNAME
from workflow.repos.component import Component

class Facter(Component):
    def __init__(self, github_user = GITHUB_USERNAME, **kwargs):
        kwargs['metadata'] = {
            'version_bumper' : sequence(
                bump_cpp_project("FACTER"),
                bump_version_file("lib/Doxyfile", r'PROJECT_NUMBER\s+=\s+')
            )
        }

        super(Facter, self).__init__(
            'facter',
            { "3.6.x": "1.10.x", "3.9.x": "5.3.x", "master": "master"},
            github_user,
            **kwargs
        )
