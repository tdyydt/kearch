#! /bin/sh
# Please run this script just under kearch/

set -eu

if [ $# -lt 1 ]; then
    echo "Please specify services which you want to deploy or re-deploy."
    echo "You can specify like ./me_deploy.sh all or ./me_deploy medb mefront."
    echo "\"all\" : Deploy all deployment except me-db."
    echo "\"medb\" : Deploy me-db. !!THIS OPTION DELETE ALL DATABASE.!!"
    echo "\"mefront\": Deploy me-front."
    echo "\"meqproc\": Deploy me-query-processor."
    echo "\"megate\": Deploy me-gateway."
    exit 1
fi

if [ -x "$(command -v minikube)" ]; then
    eval $(minikube docker-env)
fi

KEARCH_ROOT_DIR=$(cd $(dirname $0); pwd)
echo "KEARCH_ROOT_DIR = "${KEARCH_ROOT_DIR}
KEARCH_COMMON_BRANCH=${KEARCH_COMMON_BRANCH:-"dev"}
echo "KEARCH_COMMON_BRANCH = "$KEARCH_COMMON_BRANCH""
# CMD_DOCKER_BUILD="docker build --build-arg KEARCH_COMMON_BRANCH=$KEARCH_COMMON_BRANCH"
# use '--no-cache' to disable docker's cahce
CMD_DOCKER_BUILD="docker build --build-arg KEARCH_COMMON_BRANCH=$KEARCH_COMMON_BRANCH --no-cache"
echo "CMD_DOCKER_BUILD = "$CMD_DOCKER_BUILD


echo "----- Start to make namespace and configure context. -----"
cd $KEARCH_ROOT_DIR/services
kubectl apply -f kearch-namespace.yaml
echo "----- Finish making namespace and configuring context. -----"

for arg in "$@"
do
    if [ $arg = medb ]; then
        # me-db
        echo
        read -p "Are you sure? This operation destroy all your database. (y/n)" yn
        if [ "$yn" != 'y' ]; then
            exit
        fi

        echo "----- Start to deploy meta DB. -----"
        cd $KEARCH_ROOT_DIR/services/me-db

        kubectl --namespace=kearch apply --recursive -f .

        cd $KEARCH_ROOT_DIR/services/me-db

        me_db_pod_name=$(kubectl --namespace=kearch get po -l engine=me,app=db -o go-template --template '{{(index .items 0).metadata.name}}')
        echo "----- me_db_pod_name = "${me_db_pod_name}" -----"
        kubectl --namespace=kearch exec $me_db_pod_name -- mysql -uroot -ppassword -e 'DROP DATABASE IF EXISTS kearch_me_dev'
        kubectl --namespace=kearch exec $me_db_pod_name -- mysql -uroot -ppassword -e 'CREATE DATABASE kearch_me_dev CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci'

        kubectl --namespace=kearch cp $(pwd)/sql/sp_servers_schema.sql $me_db_pod_name:/tmp/sp_servers_schema.sql

        echo sp_servers_schema
        kubectl --namespace=kearch exec $me_db_pod_name -- bash -c 'mysql -uroot -ppassword kearch_me_dev < /tmp/sp_servers_schema.sql'

        $KEARCH_ROOT_DIR/me_db_checker.sh
        echo "----- Finish deployment of meta DB. -----"
    fi

    if [ $arg = mefront ] || [ $arg = all ]; then
        # me-front
        echo
        echo "----- Start deployment of meta front. -----"
        cd $KEARCH_ROOT_DIR/packages/me-front

        $CMD_DOCKER_BUILD -t kearch/me-front .

        cd $KEARCH_ROOT_DIR/services/me-front

        kubectl --namespace=kearch apply --recursive -f .
        echo "----- Finish deployment of meta front. -----"
    fi

    if [ $arg = meqproc ] || [ $arg = all ]; then
        # me-query-processor
        echo
        echo "----- Start deployment of meta query processor. -----"
        cd $KEARCH_ROOT_DIR/packages/me-query_processor

        $CMD_DOCKER_BUILD -t kearch/me-query-processor .

        cd $KEARCH_ROOT_DIR/services/me-query-processor

        kubectl --namespace=kearch apply --recursive -f .
        echo "----- Finish deployment of meta query processor. -----"
    fi

    if [ $arg = megate ] || [ $arg = all ]; then
        # me-gateway
        echo
        echo "----- Start deployment of meta gateway. -----"
        cd $KEARCH_ROOT_DIR/packages/me-gateway

        $CMD_DOCKER_BUILD -t kearch/me-gateway .

        cd $KEARCH_ROOT_DIR/services/me-gateway

        kubectl --namespace=kearch apply --recursive -f .
        echo "----- Finish deployment of meta gateway. -----"
    fi
done

echo
echo "----- Delete all pods -----"
kubectl --namespace=kearch delete pod -l engine=me
