import click

@click.command()
@click.option("--name" , prompt="Enter your name" , help="The name of the user")
def hello (name):
    click.echo(f"Hello {name}!")

PRIORITIES = {
    "o": "Optional",
    "l": "Low" , 
    "m": "Medium" ,
    "h": "High" 
    }

@click.command()
@click.argument("todofile" , type=click.Path(exists=False), required=0)
@click.option("-n" , "--name" , prompt="Enter the todo name", help="The name of the todo")
@click.option("-d" , "--description" , prompt="Describe the todo", help="Description of the todo")
@click.option("-p" , "--priority" , type=click.Choice(PRIORITIES.keys()), default="m")

def add_todo(name, description, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"[{name}]: {description} [Priority: {PRIORITIES[priority]}]")

@click.command()
@click.argument("idx", type=int, required=1)
def delete_todo(idx):
    with open("todos.txt" , "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("mytodos.txt" , "w") as f:
        f.write("\n".join(todo_list))
        f.write('\n')

@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile" , type=click.Path(exists=True), required=0)
def list_todo(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate("todo_list"):
            print(f"({idx}-) - {todo}")
        else:
            for idx, todo in enumerate("todo_list"):
    
                if f"Priority: {PRIORITIES[priority]}]" in todo:
                    print(f"({idx})  - {todo}")
