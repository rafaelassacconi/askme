import click
from stackoverflow.api import StackOverflow


@click.command()

@click.option("--keywords", 
    prompt="Enter the keywords you want to search for (separated by space)",
    help="Keywords to search related questions and answers."
)
@click.option("--items",
    default=5, 
    help="Max number of items that will be returned."
)


def askme(keywords, items):
    """ AskMe use keywords to search related questions 
    and answers on the internet.
    """
    click.echo(click.style("Searching...", fg="yellow", bold=True))

    keywords = keywords.replace(" ", ";")

    # Search on Stack Overflow
    client = StackOverflow()
    result = client.search_questions(tags=keywords, max=items)

    # No resulsts
    if not result:
        click.echo(click.style("I didn't find anything with that keywords.", fg="yellow", bold=True))

    # Show the results
    else:
        click.echo(click.style("This what I found to you:", fg="yellow", bold=True))

        for n, item in enumerate(result, 1):
            click.echo(click.style("Question %d: %s" % (n, item["title"]), bold=True))
            click.echo("Votes: %s" % item["score"])
            click.echo("Link: %s \n" % item["link"])


if __name__ == "__main__":
    click.echo(click.style("Welcome to AskMe!", fg="yellow", bold=True))
    askme()
