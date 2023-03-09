# Getting to Philosophy

## Motivation

If a Wikipedia user goes from page to page by clicking the first ordinary link
in each article, they usually find themselves at the '[Philosophy][PHIL]'
article at some point. This phenomenon even has its own [Wikipedia
page][GOTOPHIL].

[PHIL]: https://en.wikipedia.org/wiki/Philosphy
[GOTOPHIL]: https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

Here's an example chain:

<https://en.wikipedia.org/wiki/Denmark> ->\
<https://en.wikipedia.org/wiki/Danish_language> ->\
<https://en.wikipedia.org/wiki/North_Germanic_languages> ->\
<https://en.wikipedia.org/wiki/Germanic_languages> ->\
<https://en.wikipedia.org/wiki/Indo-European_languages> ->\
<https://en.wikipedia.org/wiki/Language_family> ->\
<https://en.wikipedia.org/wiki/Language> ->\
<https://en.wikipedia.org/wiki/Communication> ->\
<https://en.wikipedia.org/wiki/Information> ->\
<https://en.wikipedia.org/wiki/Abstraction> ->\
<https://en.wikipedia.org/wiki/Rule_of_inference> ->\
<https://en.wikipedia.org/wiki/Philosophy_of_logic> ->\
<https://en.wikipedia.org/wiki/Philosophy> ->

## How to run

```zsh
pip install -r requirements.txt
python philosophy.py # To expose the chain starting from a random page

python philosophy.py -h # To inspect more options
```
