from setuptools import find_packages, setup

setup(
    name='rawkit_playlist',
    packages=find_packages(include=['rawkit_playlist']),
    version='0.1.0',
    description='Rawk-it Playlists',
    install_requires=['spotipy', 'python-dotenv'],
    author='Riley Motylinski',
)