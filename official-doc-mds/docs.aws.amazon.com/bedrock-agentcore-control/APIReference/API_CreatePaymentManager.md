

# CreatePaymentManager
<a name="API_CreatePaymentManager"></a>

Creates a new payment manager in your AWS account. A payment manager serves as the top-level resource for managing payment processing capabilities, including payment connectors that integrate with supported payment providers.

If you specify `CUSTOM_JWT` as the `authorizerType`, you must provide an `authorizerConfiguration`.

## Request Syntax
<a name="API_CreatePaymentManager_RequestSyntax"></a>

```
POST /payments/managers HTTP/1.1
Content-type: application/json

{
   "authorizerConfiguration": { ... },
   "authorizerType": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "roleArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreatePaymentManager_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePaymentManager_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authorizerConfiguration](#API_CreatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-request-authorizerConfiguration"></a>
The authorizer configuration for the payment manager.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [authorizerType](#API_CreatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-request-authorizerType"></a>
The type of authorizer to use for the payment manager.  
+  `CUSTOM_JWT` - Authorize with a bearer token.
+  `AWS_IAM` - Authorize with your AWS IAM credentials.
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM`   
Required: Yes

 ** [clientToken](#API_CreatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-request-description"></a>
A description of the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[a-zA-Z0-9\s]+`   
Required: No

 ** [name](#API_CreatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-request-name"></a>
The name of the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9]{0,47}`   
Required: Yes

 ** [roleArn](#API_CreatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the payment manager assumes to access resources on your behalf.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [tags](#API_CreatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-request-tags"></a>
A map of tag keys and values to assign to the payment manager.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreatePaymentManager_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "authorizerConfiguration": { ... },
   "authorizerType": "string",
   "createdAt": "string",
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
<a name="API_CreatePaymentManager_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [authorizerConfiguration](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-authorizerConfiguration"></a>
Represents inbound authorization configuration options used to authenticate incoming requests.   
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [authorizerType](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-authorizerType"></a>
The type of authorizer for the created payment manager.  
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM` 

 ** [createdAt](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-createdAt"></a>
The timestamp when the payment manager was created.  
Type: Timestamp

 ** [name](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-name"></a>
The name of the created payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9]{0,47}` 

 ** [paymentManagerArn](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-paymentManagerArn"></a>
The Amazon Resource Name (ARN) of the created payment manager.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [paymentManagerId](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-paymentManagerId"></a>
The unique identifier of the created payment manager.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [roleArn](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the created payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-status"></a>
The current status of the payment manager. Possible values include `CREATING`, `READY`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | READY | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [tags](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-tags"></a>
The tags associated with the created payment manager.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*` 

 ** [workloadIdentityDetails](#API_CreatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePaymentManager-response-workloadIdentityDetails"></a>
The information about the workload identity.  
Type: [WorkloadIdentityDetails](API_WorkloadIdentityDetails.md) object

## Errors
<a name="API_CreatePaymentManager_Errors"></a>

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
<a name="API_CreatePaymentManager_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreatePaymentManager) 