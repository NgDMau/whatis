import click
from .functions import whatis
@click.command()
@click.argument("acronyms")

def main(acronyms:str):
    whatis(acronyms)

if __name__ == '__main__':
    main(acronyms)