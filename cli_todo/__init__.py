import click

from cli_todo.main import hello, add_todo, delete_todo, list_todo

@click.group
def nubian():
    pass

nubian.add_command(hello)
nubian.add_command(add_todo)
nubian.add_command(delete_todo)
nubian.add_command(list_todo)