AWS.config.region = 'ap-northeast-1'; // Region
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'ap-northeast-1:0fe22825-76ff-4ac5-91a7-7c771d633213'
});
// Initialize the Amazon Cognito credentials provider
AWSCognito.config.region = 'ap-northeast-1'; // Region
AWSCognito.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'ap-northeast-1:0fe22825-76ff-4ac5-91a7-7c771d633213'
});
var data = { UserPoolId: 'ap-northeast-1_ufc2eDT2p',
    ClientId: '40fise46js8m4p513or5fu4r7h',
    Paranoia : 7
};

var userPool;
var cognitoUser;

