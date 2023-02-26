# wikipedia-explorer
Python program that utilises the official Wikipedia library to use Wikipedia in command line.

Description:
The program is a command line explorer for Wikipedia’s articles. This program works on two main libraries –
wikipedia, random. wikipedia is the primary library that enables the scraping of Wikipedia website without having
the need-to-know complex scraping programs. This open-source library reduces lines of code and complexity of the
program.

Why wikipedia library?:
Though the web scraping is rawer version of what is expected of a Wikipedia explorer, this library makes it more
functional and more usable. This library works in a similar way to web scraping, but the functionalities available in
this program will be seriously limited or require insane number of codes to perform same function. For example, it
would require separate CSV files and data storage systems, not to mention high CPU usage.

Drawbacks/Bugs:
1. Most randomly generated pages are very short in nature, devoid of the ocean of information we see in other
more visited articles. Hence, it becomes quite difficult to jump to new link when there are very few links.
2. This leads to the formation of looping links, looping in an endless loop unless the user stops it. Also, when
there are no links, it just displays the same page again.
