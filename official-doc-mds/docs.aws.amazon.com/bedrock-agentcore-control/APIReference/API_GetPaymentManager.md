

# GetPaymentManager
<a name="API_GetPaymentManager"></a>

Retrieves information about a specific payment manager.

## Request Syntax
<a name="API_GetPaymentManager_RequestSyntax"></a>

```
GET /payments/managers/{{paymentManagerId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPaymentManager_RequestParameters"></a>

The request uses the following URI parameters.

 ** [paymentManagerId](#API_GetPaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-request-uri-paymentManagerId"></a>
The unique identifier of the payment manager to retrieve.  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_GetPaymentManager_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPaymentManager_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authorizerConfiguration": { ... },
   "authorizerType": "string",
   "createdAt": "string",
   "description": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "paymentManagerArn": "string",
   "paymentManagerId": "string",
   "roleArn": "string",
   "status": "string",
   "tags": { 
      "string" : "string" 
   },
   "workloadIdentityDetails": { 
      "workloadIdentityArn": "string"
   }
}
```

## Response Elements
<a name="API_GetPaymentManager_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizerConfiguration](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-authorizerConfiguration"></a>
Represents inbound authorization configuration options used to authenticate incoming requests.   
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [authorizerType](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-authorizerType"></a>
The type of authorizer used by the payment manager.  
+  `CUSTOM_JWT` - Authorize with a bearer token.
+  `AWS_IAM` - Authorize with your AWS IAM credentials.
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM` 

 ** [createdAt](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-createdAt"></a>
The timestamp when the payment manager was created.  
Type: Timestamp

 ** [description](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-description"></a>
The description of the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[a-zA-Z0-9\s]+` 

 ** [lastUpdatedAt](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-lastUpdatedAt"></a>
The timestamp when the payment manager was last updated.  
Type: Timestamp

 ** [name](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-name"></a>
The name of the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9]{0,47}` 

 ** [paymentManagerArn](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-paymentManagerArn"></a>
The Amazon Resource Name (ARN) of the payment manager.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [paymentManagerId](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-paymentManagerId"></a>
The unique identifier of the payment manager.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [roleArn](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-status"></a>
The current status of the payment manager. Possible values include `CREATING`, `READY`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | READY | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [tags](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-tags"></a>
The tags associated with the payment manager.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*` 

 ** [workloadIdentityDetails](#API_GetPaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPaymentManager-response-workloadIdentityDetails"></a>
The information about the workload identity.  
Type: [WorkloadIdentityDetails](API_WorkloadIdentityDetails.md) object

## Errors
<a name="API_GetPaymentManager_Errors"></a>

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
<a name="API_GetPaymentManager_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetPaymentManager) 