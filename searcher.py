import sys
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir

ix = open_dir("indexdir")

query_str = sys.argv[1]
topN = int(sys.argv[2])

with ix.searcher(weighting=scoring.Frequency) as searcher:
    query = QueryParser("content", ix.schema).parse(query_str)
    results = searcher.search(query, limit=topN)
    for result in results:
        print(result['title'], str(result.score))
