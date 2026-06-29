

# GetBrowser
<a name="API_GetBrowser"></a>

Gets information about a custom browser.

## Request Syntax
<a name="API_GetBrowser_RequestSyntax"></a>

```
GET /browsers/{{browserId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBrowser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserId](#API_GetBrowser_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-request-uri-browserId"></a>
The unique identifier of the browser to retrieve.  
Pattern: `(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: Yes

## Request Body
<a name="API_GetBrowser_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBrowser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserArn": "string",
   "browserId": "string",
   "browserSigning": { 
      "enabled": boolean
   },
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "createdAt": "string",
   "description": "string",
   "enterprisePolicies": [ 
      { 
         "location": { ... },
         "type": "string"
      }
   ],
   "executionRoleArn": "string",
   "failureReason": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "networkConfiguration": { 
      "networkMode": "string",
      "vpcConfig": { 
         "requireServiceS3Endpoint": boolean,
         "securityGroups": [ "string" ],
         "subnets": [ "string" ]
      }
   },
   "recording": { 
      "enabled": boolean,
      "s3Location": { 
         "bucket": "string",
         "prefix": "string",
         "versionId": "string"
      }
   },
   "status": "string"
}
```

## Response Elements
<a name="API_GetBrowser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserArn](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-browserArn"></a>
The Amazon Resource Name (ARN) of the browser.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):browser(-custom)?/(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})` 

 ** [browserId](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-browserId"></a>
The unique identifier of the browser.  
Type: String  
Pattern: `(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})` 

 ** [browserSigning](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-browserSigning"></a>
The browser signing configuration that shows whether cryptographic agent identification is enabled for web bot authentication.  
Type: [BrowserSigningConfigOutput](API_BrowserSigningConfigOutput.md) object

 ** [certificates](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-certificates"></a>
The list of certificates configured for the browser.  
Type: Array of [Certificate](API_Certificate.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [createdAt](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-createdAt"></a>
The timestamp when the browser was created.  
Type: Timestamp

 ** [description](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-description"></a>
The description of the browser.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [enterprisePolicies](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-enterprisePolicies"></a>
The list of enterprise policy files configured for the browser.  
Type: Array of [BrowserEnterprisePolicy](API_BrowserEnterprisePolicy.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [executionRoleArn](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-executionRoleArn"></a>
The IAM role ARN that provides permissions for the browser.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [failureReason](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-failureReason"></a>
The reason for failure if the browser is in a failed state.  
Type: String

 ** [lastUpdatedAt](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-lastUpdatedAt"></a>
The timestamp when the browser was last updated.  
Type: Timestamp

 ** [name](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-name"></a>
The name of the browser.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [networkConfiguration](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-networkConfiguration"></a>
The network configuration for a browser. This structure defines how the browser connects to the network.  
Type: [BrowserNetworkConfiguration](API_BrowserNetworkConfiguration.md) object

 ** [recording](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-recording"></a>
The recording configuration for a browser. This structure defines how browser sessions are recorded.  
Type: [RecordingConfig](API_RecordingConfig.md) object

 ** [status](#API_GetBrowser_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetBrowser-response-status"></a>
The current status of the browser.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | READY | DELETING | DELETE_FAILED | DELETED` 

## Errors
<a name="API_GetBrowser_Errors"></a>

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

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

## See Also
<a name="API_GetBrowser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetBrowser) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetBrowser) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetBrowser) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetBrowser) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetBrowser) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetBrowser) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetBrowser) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetBrowser) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetBrowser) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetBrowser) 