
from askme import askme


def test_askme_valid_keyword(runner):
    """ Run program with one valid keyword """
    result = runner.invoke(askme, "--keywords=django")
  
    assert result.exit_code == 0
    assert "I found to you" in result.output

def test_askme_multiples_keywords(runner):
    """ Run program with multiples valid keywords """
    result = runner.invoke(askme, "--keywords=python;html")
  
    assert result.exit_code == 0
    assert "I found to you" in result.output

def test_askme_invalid_keyword(runner):
    """ Run program with invalid keyword """
    result = runner.invoke(askme, "--keywords=abcxyzfoobar")
  
    assert result.exit_code == 0
    assert "I didn't find anything" in result.output
