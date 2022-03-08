import click 

@click.command()
@click.argument('input_files', type=click.File('r'), nargs=-1)
@click.argument('output_file', type=click.File('w'))
def concat_files(input_files, output_file):
    '''Joins contents of multiple files into a single file'''
    for file in input_files:
        for line in file:
            output_file.write(line)

    click.echo(f"Concatenation completed: {output_file.name} has been created")