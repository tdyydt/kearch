#! /bin/sh
# Please run this script just under kearch/

set -eu

if [ $# -lt 1 ]; then
    echo "Please specify services which you want to deploy or re-deploy."
    echo "You can specify like ./sp_deploy.sh all or ./sp_deploy spdb spfront."
    echo "\"all\" : Deploy all deployment except sp-db."
    echo "\"spdb\" : Deploy sp-db. !!THIS OPTION DELETE ALL DATABASE.!!"
    echo "\"spfront\": Deploy sp-front."
    echo "\"spcchi\": Deploy sp-crawler-child."
    echo "\"spcpar\": Deploy sp-crawler-parent."
    echo "\"spadmin\": Deploy sp-admin."
    echo "\"spqproc\": Deploy sp-query-processor."
    echo "\"spgate\": Deploy sp-gateway."
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
    if [ $arg = spdb ]; then
        # sp-db
        echo
        read -p "Are you sure? This operation destroy all your database. (y/n)" yn
        if [ "$yn" != 'y' ]; then
            exit
        fi

        echo "----- Start to deploy specialist DB. -----"
        cd $KEARCH_ROOT_DIR/services/sp-db

        kubectl --namespace=kearch apply --recursive -f .

        cd $KEARCH_ROOT_DIR/services/sp-db

        sp_db_pod_name=$(kubectl --namespace=kearch get po -l engine=sp,app=db -o go-template --template '{{(index .items 0).metadata.name}}')
        echo "----- sp_db_pod_name = "${sp_db_pod_name}" -----"
        kubectl --namespace=kearch exec $sp_db_pod_name -- mysql -uroot -ppassword -e 'DROP DATABASE kearch_sp_dev'
        kubectl --namespace=kearch exec $sp_db_pod_name -- mysql -uroot -ppassword -e 'CREATE DATABASE kearch_sp_dev CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci'

        kubectl --namespace=kearch cp $(pwd)/sql/url_queue_schema.sql $sp_db_pod_name:/tmp/url_queue_schema.sql
        kubectl --namespace=kearch cp $(pwd)/sql/webpages_schema.sql $sp_db_pod_name:/tmp/webpages_schema.sql
        kubectl --namespace=kearch cp $(pwd)/sql/words_schema.sql $sp_db_pod_name:/tmp/words_schema.sql
        kubectl --namespace=kearch cp $(pwd)/sql/tfidfs_schema.sql $sp_db_pod_name:/tmp/tfidfs_schema.sql
        kubectl --namespace=kearch cp $(pwd)/sql/title_words_schema.sql $sp_db_pod_name:/tmp/title_words_schema.sql

        echo url_queue_schema
        kubectl --namespace=kearch exec $sp_db_pod_name -- bash -c 'mysql -uroot -ppassword kearch_sp_dev < /tmp/url_queue_schema.sql'
        echo webpages_schema
        kubectl --namespace=kearch exec $sp_db_pod_name -- bash -c 'mysql -uroot -ppassword kearch_sp_dev < /tmp/webpages_schema.sql'
        echo words_schema
        kubectl --namespace=kearch exec $sp_db_pod_name -- bash -c 'mysql -uroot -ppassword kearch_sp_dev < /tmp/words_schema.sql'
        echo tfidfs_schema
        kubectl --namespace=kearch exec $sp_db_pod_name -- bash -c 'mysql -uroot -ppassword kearch_sp_dev < /tmp/tfidfs_schema.sql'
        echo title_words_schema
        kubectl --namespace=kearch exec $sp_db_pod_name -- bash -c 'mysql -uroot -ppassword kearch_sp_dev < /tmp/title_words_schema.sql'

        $KEARCH_ROOT_DIR/sp_db_checker.sh
        echo "----- Finish deployment of specialist DB. -----"
    fi

    if [ $arg = spfront ] || [ $arg = all ]; then
        # sp-front
        echo
        echo "----- Start deployment of specialist front. -----"
        cd $KEARCH_ROOT_DIR/packages/specialist_front

        $CMD_DOCKER_BUILD -t kearch/sp-front .

        cd $KEARCH_ROOT_DIR/services/sp-front

        kubectl --namespace=kearch apply --recursive -f .
        echo "----- Finish deployment of specialist front. -----"
    fi

    if [ $arg = spcpar ] || [ $arg = all ] ; then
        # sp-crawler-parent
        echo
        echo "----- Start deployment of specialist crawler parent. -----"
        cd $KEARCH_ROOT_DIR/packages/specialist_crawler_parent
        $CMD_DOCKER_BUILD -t kearch/sp-crawler-parent .

        cd $KEARCH_ROOT_DIR/services/sp-crawler-parent

        kubectl --namespace=kearch apply --recursive -f .
        echo "----- Finish deployment of specialist crawler parent. -----"
    fi

    if [ $arg = spcchi ] || [ $arg = all ]; then
        # sp-crawler-child
        echo
        echo "----- Start deployment of specialist crawler child. -----"
        rm -f $KEARCH_ROOT_DIR/packages/specialist_crawler_child/webpage_cache/*.pickle
        cd $KEARCH_ROOT_DIR

        echo "----- Use cache file and skip model learning. -----"
        echo "----- If you don't want to use cache file,  use -----"
        echo "----- 'docker build -t kearch/sp-crawler-child .' instead -----"
        $CMD_DOCKER_BUILD -t kearch/sp-crawler-child -f packages/specialist_crawler_child/Dockerfile_cache .

        cd $KEARCH_ROOT_DIR/services/sp-crawler-child

        kubectl --namespace=kearch apply --recursive -f .
        echo "----- Finish deployment of specialist crawler child. -----"
    fi

    if [ $arg = spadmin ] || [ $arg = all ]; then
        # sp-admin
        echo
        echo "----- Start deployment of specialist admin. -----"
        cd $KEARCH_ROOT_DIR

        $CMD_DOCKER_BUILD -f packages/specialist_admin/Dockerfile -t kearch/sp-admin .

        cd $KEARCH_ROOT_DIR/services/sp-admin

        kubectl --namespace=kearch apply --recursive -f .
        echo "----- Finish deployment of specialist admin. -----"
    fi

    if [ $arg = spqproc ] || [ $arg = all ]; then
        # sp-query-proc
        echo
        echo "----- Start deployment of specialist query processor. -----"

        cd $KEARCH_ROOT_DIR/packages/specialist_query_processor
        $CMD_DOCKER_BUILD -t kearch/sp-query-processor .


        cd $KEARCH_ROOT_DIR/services/sp-query-processor
        kubectl --namespace=kearch apply --recursive -f .

        echo "----- Finish deployment of specialist query processor. -----"
    fi

    if [ $arg = spgate ] || [ $arg = all ]; then
        # sp-gateway
        echo
        echo "----- Start deployment of specialist gateway. -----"

        cd $KEARCH_ROOT_DIR/packages/specialist_gateway
        $CMD_DOCKER_BUILD -t kearch/sp-gateway .


        cd $KEARCH_ROOT_DIR/services/sp-gateway
        kubectl --namespace=kearch apply --recursive -f .

        echo "----- Finish deployment of specialist gateway. -----"
    fi
done

echo
echo "----- Delete all pods -----"
kubectl --namespace=kearch delete pod -l engine=sp