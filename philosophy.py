import time
import urllib

import bs4
import requests
import argparse
from termcolor import colored


def find_first_link(url):
    """
    Returns the first URL link on given URL page.
    """

    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    # This div contains the article's body
    # (Sept 2017: Body nested in two div tags)
    content_div = soup.find(
        id="mw-content-text").find(class_="mw-parser-output")
    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None
    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    if not article_link:
        return
    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin(
        'https://en.wikipedia.org/', article_link)
    return first_link


def continue_crawl(search_history, target_url, max_steps):
    """
    Determines if the search end condition has been met.
    """
    if search_history[-1] == target_url:
        debug_print(f"Target article ({target_url.split('/')[-1]}) reached!")
        return False
    elif len(search_history)-1 == max_steps >= 0:
        debug_print(f"Maximum ({max_steps}) steps reached, search "
                    "aborted.", color='red')
    elif search_history[-1] in search_history[:-1]:
        debug_print("Loop detected, search aborted.", color='red')
        return False
    else:
        return True


def parse_args():
    """
    Prepare arguments for the main program.
    """
    parser = argparse.ArgumentParser()

    random_page = "https://en.wikipedia.org/wiki/Special:Random"
    parser.add_argument('-s', '--start', dest='start', default=random_page,
                        help='Link to the starting webpage')

    philo_page = "https://en.wikipedia.org/wiki/Philosophy"
    parser.add_argument('-e', '--end', dest='end', default=philo_page,
                        help='Link to the target webpage')

    parser.add_argument('-n', '--num', dest='max_steps', type=int, default=-1,
                        help='Maximum number of steps')

    parser.add_argument('-w', '--wait', dest='wait', type=float,
                        default=0, help='Number of seconds to wait in between '
                        'steps to avoid overloading the server')

    parser.add_argument('-c', '--concise', dest='concise',
                        action='store_true', help="Only print the keyword part "
                        "of the link and don't print wait time messages")

    args = parser.parse_args()

    return args.start, args.end, args.max_steps, args.wait, args.concise


def debug_print(s, color='green', bold=True):
    """
    Print debug messages.
    """
    print(colored(s, color, attrs=['bold'] if bold else []))


def print_link(l, n, num_color='green', link_color='yellow', concise=False):
    """
    Print a single link entry during the search.
    """
    print(colored(str(n-1) + ' ->', color=num_color, attrs=['bold']),
          colored(l.split('/')[-1] if concise else l, color=link_color))


def search(start_link, end_link, max_steps, wait, concise):
    """
    Carry out the search.

    Params:
        start_link (str): Link of the starting page
        end_link (str): Link of the target page
        max_steps (int): Maximum number of steps allowed
        wait (float): Number of seconds to wait in between steps to avoid
            overloading the server
        concise (bool): Whether to allow printing verbose messages

    Returns:
        article_chain (list of str): The links fetched along the search path
    """

    article_chain = [start_link]
    debug_print('Starting search')
    print_link(start_link, 1, concise=concise)

    while continue_crawl(article_chain, end_link, max_steps):

        first_link = find_first_link(article_chain[-1])
        first_link = find_first_link(article_chain[-1])
        if not first_link:
            debug_print("Arrived at an article with no links, search "
                        "aborted.", color='red')
            break

        article_chain.append(first_link)
        print_link(first_link, len(article_chain), concise=concise)

        # Slow things down so as to not overload Wikipedia's servers
        if wait > 0:
            if not concise:
                debug_print(
                    f'Applying wait time of {wait} seconds...', bold=False)
            time.sleep(wait)

    return article_chain


if __name__ == '__main__':
    start_link, end_link, max_steps, wait, concise = parse_args()
    article_chain = search(start_link, end_link, max_steps, wait, concise)
    success = article_chain[-1] == end_link
    debug_print(('Search successful. ' if success else
                'Search unsuccessful. ') +
                f'{len(article_chain)-1} steps taken.')
