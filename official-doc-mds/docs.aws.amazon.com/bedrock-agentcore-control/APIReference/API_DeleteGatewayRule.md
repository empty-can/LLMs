

# DeleteGatewayRule
<a name="API_DeleteGatewayRule"></a>

Deletes a gateway rule.

## Request Syntax
<a name="API_DeleteGatewayRule_RequestSyntax"></a>

```
DELETE /gateways/{{gatewayIdentifier}}/rules/{{ruleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGatewayRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_DeleteGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayRule-request-uri-gatewayIdentifier"></a>
The identifier of the gateway containing the rule.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [ruleId](#API_DeleteGatewayRule_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayRule-request-uri-ruleId"></a>
The unique identifier of the rule to delete.  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

## Request Body
<a name="API_DeleteGatewayRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGatewayRule_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "ruleId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteGatewayRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [ruleId](#API_DeleteGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayRule-response-ruleId"></a>
The unique identifier of the deleted rule.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

 ** [status](#API_DeleteGatewayRule_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteGatewayRule-response-status"></a>
The status of the rule deletion operation.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING` 

## Errors
<a name="API_DeleteGatewayRule_Errors"></a>

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
<a name="API_DeleteGatewayRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteGatewayRule) 