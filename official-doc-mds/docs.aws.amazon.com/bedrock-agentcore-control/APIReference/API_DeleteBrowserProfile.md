

# DeleteBrowserProfile
<a name="API_DeleteBrowserProfile"></a>

Deletes a browser profile.

## Request Syntax
<a name="API_DeleteBrowserProfile_RequestSyntax"></a>

```
DELETE /browser-profiles/{{profileId}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBrowserProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteBrowserProfile_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteBrowserProfile-request-uri-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}` 

 ** [profileId](#API_DeleteBrowserProfile_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteBrowserProfile-request-uri-profileId"></a>
The unique identifier of the browser profile to delete.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_DeleteBrowserProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBrowserProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lastSavedAt": "string",
   "lastUpdatedAt": "string",
   "profileArn": "string",
   "profileId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteBrowserProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lastSavedAt](#API_DeleteBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteBrowserProfile-response-lastSavedAt"></a>
The timestamp when browser session data was last saved to this profile before deletion.  
Type: Timestamp

 ** [lastUpdatedAt](#API_DeleteBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteBrowserProfile-response-lastUpdatedAt"></a>
The timestamp when the browser profile was last updated.  
Type: Timestamp

 ** [profileArn](#API_DeleteBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteBrowserProfile-response-profileArn"></a>
The Amazon Resource Name (ARN) of the deleted browser profile.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:browser-profile/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [profileId](#API_DeleteBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteBrowserProfile-response-profileId"></a>
The unique identifier of the deleted browser profile.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [status](#API_DeleteBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteBrowserProfile-response-status"></a>
The current status of the browser profile deletion.  
Type: String  
Valid Values: `READY | DELETING | DELETED | SAVING` 

## Errors
<a name="API_DeleteBrowserProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

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
<a name="API_DeleteBrowserProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteBrowserProfile) 