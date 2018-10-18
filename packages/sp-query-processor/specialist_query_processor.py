from kearch_common.requester import KearchRequester
import sys

ELASTIC_HOST = 'sp-es.kearch.svc.cluster.local'
ELASTIC_PORT = 9200
ELASTIC_INDEX = 'sp'
ELASTIC_TYPE = 'webpage'

REQUESTER_NAME = 'specialist_query_processor'

test_results = {
    'data': [['www.google.com', 'google home', 'google is strong']]}


def retrieve(queries, max_urls):
    elastic_requester = KearchRequester(
        ELASTIC_HOST, ELASTIC_PORT, REQUESTER_NAME, conn_type='elastic')

    resp = elastic_requester.request(
        path='/' + ELASTIC_INDEX + '/' + ELASTIC_TYPE + '/_search?pretty',
        payload={'query': {'match_phrase': {'text': ' '.join(queries)}}},
        method='POST')

    print(resp['hits']['hits'], file=sys.stderr)
    results = {'data': []}
    for d in resp['hits']['hits']:
        results['data'].append(
            {'url': d['_source']['url'],
             'title': d['_source']['title'],
             'summary': d['_source']['text'][0:200],
             'score': d['_score']})

    # Debug : Uncomment a following line when you want this module standalone.
    # results = test_results

    return results