

# GetBrowserProfile
<a name="API_GetBrowserProfile"></a>

Gets information about a browser profile.

## Request Syntax
<a name="API_GetBrowserProfile_RequestSyntax"></a>

```
GET /browser-profiles/{{profileId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBrowserProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileId](#API_GetBrowserProfile_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-request-uri-profileId"></a>
The unique identifier of the browser profile to retrieve.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_GetBrowserProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBrowserProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "lastSavedAt": "string",
   "lastSavedBrowserId": "string",
   "lastSavedBrowserSessionId": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "profileArn": "string",
   "profileId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetBrowserProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-createdAt"></a>
The timestamp when the browser profile was created.  
Type: Timestamp

 ** [description](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-description"></a>
The description of the browser profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [lastSavedAt](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-lastSavedAt"></a>
The timestamp when browser session data was last saved to this profile.  
Type: Timestamp

 ** [lastSavedBrowserId](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-lastSavedBrowserId"></a>
The identifier of the browser from which data was last saved to this profile.  
Type: String  
Pattern: `(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})` 

 ** [lastSavedBrowserSessionId](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-lastSavedBrowserSessionId"></a>
The identifier of the browser session from which data was last saved to this profile.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [lastUpdatedAt](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-lastUpdatedAt"></a>
The timestamp when the browser profile was last updated.  
Type: Timestamp

 ** [name](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-name"></a>
The name of the browser profile.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [profileArn](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-profileArn"></a>
The Amazon Resource Name (ARN) of the browser profile.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:browser-profile/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [profileId](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-profileId"></a>
The unique identifier of the browser profile.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [status](#API_GetBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowserProfile-response-status"></a>
The current status of the browser profile.  
Type: String  
Valid Values: `READY | DELETING | DELETED | SAVING` 

## Errors
<a name="API_GetBrowserProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_GetBrowserProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetBrowserProfile) 