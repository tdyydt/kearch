import flask
import sys
import base64
from flask import jsonify
from kearch_common.requester import KearchRequester, RequesterError
import kearch_classifier.classifier

DATABASE_HOST = 'sp-db.kearch.svc.cluster.local'
DATABASE_PORT = 3306
SP_CLASSIFIER_PORT = 10080

timestamp = dict()
app = flask.Flask(__name__)


def update_param_file(filename):
    db_req = KearchRequester(
        DATABASE_HOST, DATABASE_PORT, conn_type='sql')
    try:
        ret = db_req.request(path='/sp/db/check_binary_file_timestamp',
                             params={'name': filename})
        dt = ret['updated_at']
        print('db:', dt, file=sys.stderr)
        if filename not in timestamp or timestamp[filename] < dt:
            timestamp[filename] = dt
            ret = db_req.request(path='/sp/db/pull_binary_file',
                                 params={'name': filename})
            body = base64.b64decode(ret['body'].encode())
            with open(filename, 'wb') as f:
                f.write(body)
    except RequesterError:
        return


def classify_main(body_words, title_words):
    print('Start checking parameter files.', file=sys.stderr)
    update_param_file(kearch_classifier.classifier.PARAMS_FILE)
    print('End checking parameter files.', file=sys.stderr)

    cls = kearch_classifier.classifier.Classifier()
    cls.load_params(kearch_classifier.classifier.PARAMS_FILE)
    res = cls.classify(body_words, title_words)
    return res


@app.route('/sp/classifier/classify', methods=['POST'])
def classify():
    data = flask.request.get_json()
    body_words = data['body_words']
    title_words = data['title_words']
    res = classify_main(body_words, title_words)
    return jsonify({'result': res})


def test_classify_main():
    res = classify_main(
        'Linus is a greate programmer.'.split(), 'History of Linux'.split())
    assert(res == kearch_classifier.classifier.IN_TOPIC or
           res == kearch_classifier.classifier.OUT_OF_TOPIC)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=SP_CLASSIFIER_PORT)  # どこからでもアクセス可能に
