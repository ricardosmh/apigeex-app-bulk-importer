apigeecli apis create bundle -f apiproxy -n $PROXYNAME -e $ENV -o $ORG -t $TOKEN --ovr --wait


##------------------------------------
#Install Apigeecli
curl -L https://raw.githubusercontent.com/apigee/apigeecli/main/downloadLatest.sh | sh -
export PATH=$PATH:$HOME/.apigeecli/bin
##------------------------------------

# Create app
TOKEN=$(gcloud auth print-access-token)
ORG=rick-apigeex
DEVELOPER=soporte-apigee-legacy@coordinadora.com
APP_NAME=legacy-test-1-apps
apigeecli apps create -o $ORG -t $TOKEN -e $DEVELOPER -n $APP_NAME

# Create custom credentials
KEY=sdkslds
SECRET=sdjksjd
apigeecli apps keys create -o $ORG -t $TOKEN -d $DEVELOPER -n $APP_NAME -p $PRODUCTS -k $KEY -c $SECRET