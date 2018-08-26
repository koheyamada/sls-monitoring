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

$("#login-button").click(function(event){
    event.preventDefault();
    var authenticationData = {
        Username : $('#name').val(),
        Password : $('#password').val()
    };
    var authenticationDetails = new AWSCognito.CognitoIdentityServiceProvider.AuthenticationDetails(authenticationData);
    userPool = new AWSCognito.CognitoIdentityServiceProvider.CognitoUserPool(data);
    var userData = {
        Username : $('#name').val(),
        Pool : userPool
    };
    cognitoUser = new AWSCognito.CognitoIdentityServiceProvider.CognitoUser(userData);
    cognitoUser.authenticateUser(authenticationDetails, {
        onSuccess: function (authresult) {
            //console.log('access token + ' + authresult.getIdToken().getJwtToken());

            var url = "mypage.html";

            $('form').fadeOut(700, function(){
                $(location).attr("href", url);
            });
            $('.wrapper').addClass('form-success');

        },
        onFailure: function(err) {
            alert(err.message);
        },
    });
});
