## How to use this script:

### Install dependencies

Install Apigeecli:
```shell
curl -L https://raw.githubusercontent.com/apigee/apigeecli/main/downloadLatest.sh | sh -
export PATH=$PATH:$HOME/.apigeecli/bin
```


Create variables and authenticate:

Aca debemos rellenar los datos en la organizacion.
```shell
gcloud auth login
export TOKEN=$(gcloud auth print-access-token)
export PRODUCTS=("cm-legacy-agw-apiproduct")
export ORG={modificalo-con-el-nombre-de-tu-org}
export DEVELOPER=soporte-apigee-legacy@coordinadora.com
```

Para ejecutar el script debemos correr el siguiente comando:

```shell
python3 main.py $TOKEN $PRODUCTS $ORG $DEVELOPER
```



