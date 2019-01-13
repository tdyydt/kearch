import flask
import sys
import base64
from flask import jsonify
import kearch_evaluater.evaluater
from kearch_common.requester import KearchRequester

DATABASE_HOST = 'me-db.kearch.svc.cluster.local'
DATABASE_PORT = 3306

timestamp = dict()
app = flask.Flask(__name__)
evaluater = kearch_evaluater.evaluater.Evaluater()


def update_param_file(filename):
    db_req = KearchRequester(
        DATABASE_HOST, DATABASE_PORT, conn_type='sql')
    ret = db_req.request(path='/me/db/check_binary_file_timestamp',
                         params={'name': filename})
    dt = ret['updated_at']
    print('db:', dt, file=sys.stderr)
    if filename not in timestamp or timestamp[filename] < dt:
        timestamp[filename] = dt
        ret = db_req.request(path='/me/db/pull_binary_file',
                             params={'name': filename})
        body = base64.b64decode(ret['body'].encode())
        with open(filename, 'wb') as f:
            f.write(body)
        evaluater.load_params(kearch_evaluater.evaluater.PARAMS_FILE)


@app.route('/me/evaluater/evaluate', methods=['GET'])
def post():
    print('Start checking parameter files.', file=sys.stderr)
    update_param_file(kearch_evaluater.evaluater.PARAMS_FILE)
    print('End checking parameter files.', file=sys.stderr)

    queries = flask.request.args.get('query')
    queries = queries.split(' ')

    # Some specialist servers in the evaluater may be deleted
    # by /me/gateway/delete_a_connection_request.
    # Therefore, we must confirm all specialist servers in the evaluater
    # exist in the database truly.
    db_req = KearchRequester(
        DATABASE_HOST, DATABASE_PORT, conn_type='sql')
    sp_servers = db_req.request(path='/me/db/list_up_sp_servers')
    res_eval = evaluater.evaluate(queries)
    res = dict()
    for s in sp_servers.keys():
        if s in res_eval:
            res[s] = res_eval[s]

    return jsonify(res)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=10080)  # どこからでもアクセス可能に
