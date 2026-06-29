

# DeleteGatewayTarget
<a name="API_DeleteGatewayTarget"></a>

Deletes a gateway target.

You cannot delete a target that is in a pending authorization state (`CREATE_PENDING_AUTH`, `UPDATE_PENDING_AUTH`, or `SYNCHRONIZE_PENDING_AUTH`). Wait for the authorization to complete or fail before deleting the target.

## Request Syntax
<a name="API_DeleteGatewayTarget_RequestSyntax"></a>

```
DELETE /gateways/{{gatewayIdentifier}}/targets/{{targetId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGatewayTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_DeleteGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayTarget-request-uri-gatewayIdentifier"></a>
The unique identifier of the gateway associated with the target.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [targetId](#API_DeleteGatewayTarget_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayTarget-request-uri-targetId"></a>
The unique identifier of the gateway target to delete.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_DeleteGatewayTarget_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGatewayTarget_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "gatewayArn": "string",
   "status": "string",
   "statusReasons": [ "string" ],
   "targetId": "string"
}
```

## Response Elements
<a name="API_DeleteGatewayTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [gatewayArn](#API_DeleteGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayTarget-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [status](#API_DeleteGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayTarget-response-status"></a>
The current status of the gateway target deletion.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED | SYNCHRONIZING | SYNCHRONIZE_UNSUCCESSFUL | CREATE_PENDING_AUTH | UPDATE_PENDING_AUTH | SYNCHRONIZE_PENDING_AUTH` 

 ** [statusReasons](#API_DeleteGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayTarget-response-statusReasons"></a>
The reasons for the current status of the gateway target deletion.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [targetId](#API_DeleteGatewayTarget_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayTarget-response-targetId"></a>
The unique identifier of the deleted gateway target.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

## Errors
<a name="API_DeleteGatewayTarget_Errors"></a>

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
<a name="API_DeleteGatewayTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteGatewayTarget) 