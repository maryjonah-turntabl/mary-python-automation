import pytest
from click.testing import CliRunner 

from click_tools.confirm_ttblr import login

def test_turntablr_logs_in():
    runner = CliRunner()
    prompt_inputs = '\n'.join([
        'mary.jonah@turntabl.io',
    ])

    result = runner.invoke(login, input=prompt_inputs)
    assert result.exit_code == 0

    expected_output = '\n'.join([
        'Welcome, kindly provide your email address for verification.\n'
        'email: mary.jonah@turntabl.io',
        'Welcome Mary.Jonah to the application\n'
    ])

    assert result.output == expected_output



def test_non_turntablr_logs_in():
    runner = CliRunner()
    prompt_inputs = '\n'.join([
        'maria.lopez@gmail.com',
    ])

    result = runner.invoke(login, input=prompt_inputs)
    assert result.exit_code == 0

    expected_output = '\n'.join([
        'Welcome, kindly provide your email address for verification.\n'
        'email: maria.lopez@gmail.com',
        'Sorry, the service is available to turntabl staff only.\n'
    ])

    assert result.output == expected_output


