from operator import contains
import click 


@click.command()
def login():
    """Confirms a user is a turntabl employee using their email address"""
    click.echo("Welcome, kindly provide your email address for verification.")
    email = click.prompt('email')
    
    if isATTblr(email):
        click.echo(f"Welcome {getUserName(email)} to the application")
    else:
        click.echo(f"Sorry, the service is available to turntabl staff only.")


def isATTblr(email: str) -> bool :
    msg = True if  "@turntabl.io" in email else False
    return msg

def getUserName(email: str) -> str :
    return email.split("@")[0].title()
