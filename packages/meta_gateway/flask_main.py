import flask
import meta_gateway


META_GATE_PORT = 10080
app = flask.Flask(__name__)


@app.route('/add_new_sp_server', methods=['POST'])
def send_DB_summary():
    data = flask.request.args.get('payload')
    ip_sp = data['ip']
    summary = data['summary']
    meta_gateway.add_new_sp_server(ip_sp, summary)


@app.route('/retrieve', methods=['GET'])
def retrieve():
    queries = flask.request.args.get('queries')
    queries = queries.split(' ')
    max_urls = flask.request.args.get('max_urls', int)
    ip_sp = flask.request.args.get('ip_sp')
    result = meta_gateway.retrieve(ip_sp, queries, max_urls)
    return flask.render_template('result.html', result=result)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=META_GATE_PORT)  # どこからでもアクセス可能に