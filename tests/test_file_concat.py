import pytest
from click.testing import CliRunner 
from pathlib import Path
from click_tools.file_concat import concat_files

def test_concat_file_is_created():
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('ridge_name.txt', 'w') as file_obj:
            file_obj.write('Advantage Place, Ridge\n')
        with open('achimota_name.txt', 'w') as file_obj:
            file_obj.write('Sonnidom House, Achimota\n')

        result = runner.invoke(concat_files, ['ridge_name.txt', 'achimota_name.txt', 'combined_names.txt'])

        assert result.exit_code == 0
        assert Path('combined_names.txt').exists()


def test_concat_file_has_contents():
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('ridge_name.txt', 'w') as file_obj:
            file_obj.write('Advantage Place, Ridge\n')
        with open('achimota_name.txt', 'w') as file_obj:
            file_obj.write('Sonnidom House, Achimota\n')

        result = runner.invoke(concat_files, ['ridge_name.txt', 'achimota_name.txt', 'combined_names1.txt'])

        location_names = ['Advantage Place, Ridge\n', 'Sonnidom House, Achimota\n']
        with open('combined_names1.txt') as file_obj:
            returned_contents = file_obj.readlines()

        assert result.exit_code == 0
        assert returned_contents == location_names


