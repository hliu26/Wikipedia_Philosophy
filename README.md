# Getting To Philosophy: Wikipedia Page Crawling
Reference: https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

>"Clicking on the first link in the main text of a Wikipedia article, and then repeating the process for subsequent articles, usually leads to the Philosophy article. In February 2016, this was true for 97% of all articles in Wikipedia, an increase from 94.52% in 2011. The remaining articles lead to an article without any outgoing wikilinks, to pages that do not exist, or get stuck in loops"

## "Method summarized
Following the chain consists of:
1. Clicking on the first non-parenthesized, non-italicized link
2. Ignoring external links, links to the current page, or red links (links to non-existent pages)
3. Stopping when reaching "Philosophy", a page with no links or a page that does not exist, or when a loop occurs"

## Currently:
Only non-parenthesized, non-italicized main text links are being used. 
These links appear outside any tables.
Cycles are thrown as exceptions and next tests are run if testing.
By default, test_crawl.py will use a random Wiki page, generated from http://en.wikipedia.org/wiki/Special:Random

### Goals:
1. Creating a site similar to: https://www.xefer.com/wikipedia?fbclid=IwAR25EiufRpqfi4kR8oVsyx5a1zj2OUkIQbWP_Lg_ql41vuaRRQdONjYyhhA
2. Create a distribution / Capture a distribution of the number of branches/ page hops required to reach the Philosophy page.
3. Potential cluster or classify pages.

### How to run (general):
Make sure test_crawl.py and page.py are in the same directory
<b>In terminal run:</b> 
<i> python3 philosophy_crawl.py <b>START_LINK_HERE</b></i>
<b>Output</b> Results will then run and be printed onto terminal:
```
REMINDER TO SHOW EXAMPLE OUTPUT
```

### How to run for testing:
Make sure test_crawl.py and page.py are in the same directory
<b>In terminal run:</b> 

<i> python3 test_crawl.py <b>NumberOfTestsHere</b></i>

<b>Output</b> Results will then run and be printed onto terminal:
```
Test No:  2
Crawling...
MouseHunt - Wikipedia: http://en.wikipedia.org/wiki/Special:Random
Facebook - Wikipedia: https://en.wikipedia.org/wiki/Facebook
Social media - Wikipedia: https://en.wikipedia.org/wiki/Social_media
Information exchange - Wikipedia: https://en.wikipedia.org/wiki/Information_sharing
Telecommunication - Wikipedia: https://en.wikipedia.org/wiki/Telecommunication
Information - Wikipedia: https://en.wikipedia.org/wiki/Information
Uncertainty - Wikipedia: https://en.wikipedia.org/wiki/Uncertainty
Epistemology - Wikipedia: https://en.wikipedia.org/wiki/Epistemic
 Philosophy Reached!  https://en.wikipedia.orghttps://en.wikipedia.org/wiki/Philosophy
```
