# Install with a Helm chart
Install the helm chart by running the follow command in the chart folder-
```
tar -xzvf pulpapi-0.1.0.tgz
cd pulpapi
helm install pulpapi .
```

After install, you should see some output like this -
```
NAME: pulpapi
LAST DEPLOYED: Sun Feb  5 19:04:43 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=pulpapi,app.kubernetes.io/instance=pulpapi" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT

```

You can also verify the install with ****helm list***



Kubectl output with the pod running -

```
 kubectl get po
NAME                       READY   STATUS    RESTARTS        AGE
nginx-76d6c9b8c-9j9nk      1/1     Running   2 (6h20m ago)   2d19h
nginx-76d6c9b8c-dqfqr      1/1     Running   2 (6h20m ago)   2d19h
pulpapi-5c545cfb49-6klfx   1/1     Running   0               4h48m
```


# Deployment and config files

This directory contains the kubernetes files used in the EKS, Flask, Docker tutorial found here https://fasterdevops.github.io/flask-docker-eks/


Note: You will have to change the image url in the deployment.yaml
