import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    prob_dist = {}
    random_pick = 0

    if len(corpus[page]) == 0:
        random_pick = 1/len(corpus)
    else:
        random_pick = (1-damping_factor) * (1/len(corpus))

    for pg in corpus:
        prob_dist[pg] = random_pick

    for target_page in corpus[page]:
        prob_dist[target_page] += ((damping_factor) * 1/(len(corpus[page])))

    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page = random.choice(list(corpus))
    pagerank = {}

    for pg in corpus:
        pagerank[pg] = 0

    for i in range(0, n):
        prob_dist = transition_model(corpus, page, damping_factor)
        page = get_page(prob_dist)
        pagerank[page] += 1

    for pg in corpus:
        pagerank[pg] = pagerank[pg]/n

    check_sum(pagerank)

    return pagerank


def get_page(prob_dist):
    """
    Returns a random page based on the given probability distribution.
    """
    if len(prob_dist) == 0:
        raise ValueError
    r = random.random()
    start = 0
    end = 0
    for prob in prob_dist:
        end += prob_dist[prob]
        if start <= r and r < end:
            return prob
        start = end


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    
    # initialize values for pageranks
    for pg in corpus:
        pagerank[pg] = 1/(len(corpus))

    new_pr = get_new_pr(corpus, damping_factor, pagerank)

    while not has_converged(pagerank, new_pr):
        pagerank = new_pr
        new_pr = get_new_pr(corpus, damping_factor, pagerank)
    check_sum(pagerank)

    return pagerank

def get_new_pr(corpus, damping_factor, pagerank):
    new_pr = {}
    
    for pg in pagerank:
        s = find_sum(corpus, pagerank, pg)
        new_pr[pg] = (1-damping_factor) * (1/len(corpus)) + (damping_factor * s)
    check_sum(new_pr)
    return new_pr

def check_sum(pagerank):
    s = 0
    for pg in pagerank:
        s += pagerank[pg]
    if s - 1 > 0.0001:
        raise ValueError


def has_converged(pr1, pr2):
    if list(pr1) != list(pr2):
        raise ValueError
    for pg in pr1:
        larger = max(pr1[pg], pr2[pg])
        smaller = min(pr1[pg], pr2[pg])
        if larger - smaller > 0.001:
            return False
    return True


def find_sum(corpus, pagerank, target_page):
    s = 0
    for pg in corpus:
        if len(corpus[pg]) == 0:
            s += (1/len(corpus))*pagerank[pg]
        if target_page in corpus[pg]:
            s += pagerank[pg]/len(corpus[pg])
    return s

if __name__ == "__main__":
    main()
