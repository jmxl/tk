from dataclasses import dataclass


@dataclass(frozen=True)
class AppAttributes:
    title: str = 'DemoApp'
    version_major: int = 0
    version_minor: int = 0
    version_patch: int = 1
    author: str = 'jmxl'
    email: str = 'jmxl_123@163.com'

    @property
    def version(self):
        return '{}.{}.{}'.format(self.version_major, self.version_minor, self.version_patch)
