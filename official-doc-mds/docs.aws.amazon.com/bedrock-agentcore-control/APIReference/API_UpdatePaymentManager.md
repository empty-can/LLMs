

# UpdatePaymentManager
<a name="API_UpdatePaymentManager"></a>

Updates an existing payment manager. This operation uses PATCH semantics, so you only need to specify the fields you want to change.

## Request Syntax
<a name="API_UpdatePaymentManager_RequestSyntax"></a>

```
PATCH /payments/managers/{{paymentManagerId}} HTTP/1.1
Content-type: application/json

{
   "authorizerConfiguration": { ... },
   "authorizerType": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePaymentManager_RequestParameters"></a>

The request uses the following URI parameters.

 ** [paymentManagerId](#API_UpdatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-request-uri-paymentManagerId"></a>
The unique identifier of the payment manager to update.  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_UpdatePaymentManager_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authorizerConfiguration](#API_UpdatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-request-authorizerConfiguration"></a>
The updated authorizer configuration for the payment manager.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [authorizerType](#API_UpdatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-request-authorizerType"></a>
The updated authorizer type for the payment manager.  
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM`   
Required: No

 ** [clientToken](#API_UpdatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_UpdatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-request-description"></a>
The updated description of the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[a-zA-Z0-9\s]+`   
Required: No

 ** [roleArn](#API_UpdatePaymentManager_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-request-roleArn"></a>
The updated Amazon Resource Name (ARN) of the IAM role for the payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: No

## Response Syntax
<a name="API_UpdatePaymentManager_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "authorizerType": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "paymentManagerArn": "string",
   "paymentManagerId": "string",
   "roleArn": "string",
   "status": "string",
   "workloadIdentityDetails": { 
      "workloadIdentityArn": "string"
   }
}
```

## Response Elements
<a name="API_UpdatePaymentManager_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [authorizerType](#API_UpdatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-response-authorizerType"></a>
The type of authorizer for the updated payment manager.  
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM` 

 ** [lastUpdatedAt](#API_UpdatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-response-lastUpdatedAt"></a>
The timestamp when the payment manager was last updated.  
Type: Timestamp

 ** [name](#API_UpdatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-response-name"></a>
The name of the updated payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9]{0,47}` 

 ** [paymentManagerArn](#API_UpdatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-response-paymentManagerArn"></a>
The Amazon Resource Name (ARN) of the updated payment manager.  
Type: String  
Length Constraints: Minimum length of 66. Maximum length of 2048.  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [paymentManagerId](#API_UpdatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-response-paymentManagerId"></a>
The unique identifier of the updated payment manager.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 211.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [roleArn](#API_UpdatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the updated payment manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_UpdatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-response-status"></a>
The current status of the updated payment manager. Possible values include `CREATING`, `READY`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`, and `DELETE_FAILED`.  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | READY | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [workloadIdentityDetails](#API_UpdatePaymentManager_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePaymentManager-response-workloadIdentityDetails"></a>
The information about the workload identity.  
Type: [WorkloadIdentityDetails](API_WorkloadIdentityDetails.md) object

## Errors
<a name="API_UpdatePaymentManager_Errors"></a>

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
<a name="API_UpdatePaymentManager_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdatePaymentManager) 