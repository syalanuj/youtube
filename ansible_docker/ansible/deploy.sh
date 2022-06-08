
   
#!/bin/bash -xue
# this script runs ansible on the developer's laptop 
# to deploy to VM

## usage ##
# deploy.sh
# deploy.sh --tags config
function usage {
    set +xue
    echo "usage: ./deploy.sh (setup target | deploy env target)"
    echo "  setup_docker       setup docker on the system"
    echo "  deploy_docker      deploy changes to the machine"
    exit 1
}
if [[ ( $@ == "--help") ||  $# -lt 1 ]] 
then 
    usage
fi 

MODE=${1}
shift 

if [[ "${MODE}" = setup_docker ]]
then 
    venv/bin/ansible-playbook -i inventory/hosts.ini setup_docker.yml $@
elif [[ "${MODE}" = deploy_docker ]]
then
    venv/bin/ansible-playbook -i inventory/hosts.ini deploy_docker.yml $@
else
    usage
fi