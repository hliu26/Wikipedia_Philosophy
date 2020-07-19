from page import Page
import sys

def main():
    
    runs = int(sys.argv[1])
    hop_list = []
    tests = 0
    for i in range(0,runs):
    
        try:
        
            test = Page("http://en.wikipedia.org/wiki/Special:Random")
            print("\n\033[1m Test No: \033[0m", str(i+1))
            print("===========================")
            print("Crawling...")
            test.crawl()
            print("\n=======branches/hops======")
            print(test.branches)
            hop_list.append(test.branches)
            print("===========================\n")
            i += 1
            tests += 1
        except:
            print("\n")
            continue

    print("\033[1m Results: \033[0m")
    print("Number of tests completed without errors:", tests)
    print("Number of tests that failed:", runs-tests)
    
    if len(hop_list) == 0:
        print("Mean number of hops cannot be calculated/n")
    else:
        print("Mean number of hops:", str(sum(hop_list) / len(hop_list)),"/n")
    
if __name__ == "__main__":
    main()
    
