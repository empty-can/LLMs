

# CreateBrowserProfile
<a name="API_CreateBrowserProfile"></a>

Creates a browser profile in Amazon Bedrock AgentCore. A browser profile stores persistent browser data such as cookies, local storage, session storage, and browsing history that can be saved from browser sessions and reused in subsequent sessions.

## Request Syntax
<a name="API_CreateBrowserProfile_RequestSyntax"></a>

```
PUT /browser-profiles HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateBrowserProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateBrowserProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateBrowserProfile_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateBrowserProfile-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateBrowserProfile_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateBrowserProfile-request-description"></a>
A description of the browser profile. Use this field to describe the purpose or contents of the profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [name](#API_CreateBrowserProfile_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateBrowserProfile-request-name"></a>
The name of the browser profile. The name must be unique within your account and can contain alphanumeric characters and underscores.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [tags](#API_CreateBrowserProfile_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateBrowserProfile-request-tags"></a>
A map of tag keys and values to assign to the browser profile. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateBrowserProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "profileArn": "string",
   "profileId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateBrowserProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateBrowserProfile-response-createdAt"></a>
The timestamp when the browser profile was created.  
Type: Timestamp

 ** [profileArn](#API_CreateBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateBrowserProfile-response-profileArn"></a>
The Amazon Resource Name (ARN) of the created browser profile.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:browser-profile/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [profileId](#API_CreateBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateBrowserProfile-response-profileId"></a>
The unique identifier of the created browser profile.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [status](#API_CreateBrowserProfile_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateBrowserProfile-response-status"></a>
The current status of the browser profile.  
Type: String  
Valid Values: `READY | DELETING | DELETED | SAVING` 

## Errors
<a name="API_CreateBrowserProfile_Errors"></a>

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

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_CreateBrowserProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateBrowserProfile) 