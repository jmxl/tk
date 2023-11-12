from dataclasses import dataclass


@dataclass
class AppSettings:
    cache_path: str = '../'
