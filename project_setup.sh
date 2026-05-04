#!/bin/bash
#usage ./script_name.sh <oc project> <site a/b> <domain non prod/prod>
run() {
  for f in $FILES/*.yml
  do
    echo "generating json for : $f"
    oc process -f $f --param-file=$FILES/app.env.$2 --ignore-unknown-parameters > $f.json
  done

  #Deploy json data files to OC
  for f in $FILES/*.json
  do 
    echo "deploying to oc: $f"
    oc apply -f $f -n $1
  done
}

#Cleanup
rm -fr $FILES/*.json

oc login <url>
run $1 $3
