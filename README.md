# Getting to Philosophy

## Motivation

If a Wikipedia user goes from page to page by clicking the first ordinary link
in each article, they usually find themselves at the '[Philosophy][PHIL]'
article at some point. This phenomenon even has its own [Wikipedia
page][GOTOPHIL].

[PHIL]: https://en.wikipedia.org/wiki/Philosphy
[GOTOPHIL]: https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

Here's an example chain:

<https://en.wikipedia.org/wiki/Theatre> ->\
<https://en.wikipedia.org/wiki/Fine_art> ->\
<https://en.wikipedia.org/wiki/Aesthetics> ->\
<https://en.wikipedia.org/wiki/Philosphy>

## How to run

```zsh
pip install -r requirements.txt
python philosophy.py # To expose the chain starting from a random page

python philosophy.py -h # To inspect more options
```
