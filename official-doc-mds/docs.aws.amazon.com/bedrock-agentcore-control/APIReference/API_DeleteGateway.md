

# DeleteGateway
<a name="API_DeleteGateway"></a>

Deletes a gateway.

## Request Syntax
<a name="API_DeleteGateway_RequestSyntax"></a>

```
DELETE /gateways/{{gatewayIdentifier}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_DeleteGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteGateway-request-uri-gatewayIdentifier"></a>
The identifier of the gateway to delete.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_DeleteGateway_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGateway_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "gatewayId": "string",
   "status": "string",
   "statusReasons": [ "string" ]
}
```

## Response Elements
<a name="API_DeleteGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [gatewayId](#API_DeleteGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteGateway-response-gatewayId"></a>
The unique identifier of the deleted gateway.  
Type: String  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [status](#API_DeleteGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteGateway-response-status"></a>
The current status of the gateway deletion.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED` 

 ** [statusReasons](#API_DeleteGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteGateway-response-statusReasons"></a>
The reasons for the current status of the gateway deletion.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DeleteGateway_Errors"></a>

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
<a name="API_DeleteGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteGateway) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteGateway) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteGateway) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteGateway) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteGateway) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteGateway) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteGateway) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteGateway) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteGateway) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteGateway) 