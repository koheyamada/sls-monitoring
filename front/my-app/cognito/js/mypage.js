AWS.config.region = 'ap-northeast-1'; // Region
AWSCognito.config.region = 'ap-northeast-1'; // Region

var data = { UserPoolId: 'ap-northeast-1_ufc2eDT2p',
    ClientId: '40fise46js8m4p513or5fu4r7h'
};
var userPool = new AWSCognito.CognitoIdentityServiceProvider.CognitoUserPool(data);
var cognitoUser = userPool.getCurrentUser();

if (cognitoUser != null) {
    cognitoUser.getSession(function(err, sessresult) {
        if (sessresult) {
            console.log('You are now logged in.');
            cognitoUser.getUserAttributes(function(err, attrresult) {
                if (err) {
                    alert(err);
                    return;
                }
                $("#username").html("Username: " + cognitoUser.username);

                for (i = 0; i < attrresult.length; i++) {
                    if (attrresult[i].getName()=="email"){
                        $("#email").html("EMail: " + attrresult[i].getValue());
                    }
                }

                // Add the User's Id Token to the Cognito credentials login map.
                AWS.config.credentials = new AWS.CognitoIdentityCredentials({
                    IdentityPoolId: 'ap-northeast-1:0fe22825-76ff-4ac5-91a7-7c771d633213',
                    Logins: {
                        'cognito-idp.ap-northeast-1.amazonaws.com/ap-northeast-1_ufc2eDT2p': sessresult.getIdToken().getJwtToken()
                    }
                });
            });
        } else {
            var url = "login.html";
            $(location).attr("href", url);
        }
    });
} else {
    var url = "login.html";
    $(location).attr("href", url);
}
