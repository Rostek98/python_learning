> [!hint]+ Test instalation
> 1. Download lcm-operator x package manualy from artifactory.
> 2. Paste it to <font color="#f79646">/x/x/core/x/packages/nop/</font>
> 3. From folder scenarios infra  ./50-x.sh install 4.4.1-x local

> [!info]+ LCM commands
> **MAIN**:
> 
> ```
> oc get rancnf -A  
> oc get pods -n x
> watch -n 3 x --tail=30
> ```
> 
> **SECRET**:  
> 
> ```
> kubectl apply -f my_secret.yaml
> kubectl get secrets -n x
> ```
> 
> **ROLLBACK**:
> 
> *In rancnf_vCU.yaml change sw_version, and namespaces*
> ```
>  kubectl apply -f x.yaml
> ```
> 
