

# DeleteOnlineEvaluationConfig
<a name="API_DeleteOnlineEvaluationConfig"></a>

 Deletes an online evaluation configuration and stops any ongoing evaluation processes associated with it. 

## Request Syntax
<a name="API_DeleteOnlineEvaluationConfig_RequestSyntax"></a>

```
DELETE /online-evaluation-configs/{{onlineEvaluationConfigId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteOnlineEvaluationConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [onlineEvaluationConfigId](#API_DeleteOnlineEvaluationConfig_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteOnlineEvaluationConfig-request-uri-onlineEvaluationConfigId"></a>
 The unique identifier of the online evaluation configuration to delete.   
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_DeleteOnlineEvaluationConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteOnlineEvaluationConfig_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "onlineEvaluationConfigArn": "string",
   "onlineEvaluationConfigId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteOnlineEvaluationConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [onlineEvaluationConfigArn](#API_DeleteOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteOnlineEvaluationConfig-response-onlineEvaluationConfigArn"></a>
 The Amazon Resource Name (ARN) of the deleted online evaluation configuration.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [onlineEvaluationConfigId](#API_DeleteOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteOnlineEvaluationConfig-response-onlineEvaluationConfigId"></a>
 The unique identifier of the deleted online evaluation configuration.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [status](#API_DeleteOnlineEvaluationConfig_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteOnlineEvaluationConfig-response-status"></a>
 The status of the online evaluation configuration deletion operation.   
Type: String  
Valid Values: `ACTIVE | CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | ERROR` 

## Errors
<a name="API_DeleteOnlineEvaluationConfig_Errors"></a>

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
<a name="API_DeleteOnlineEvaluationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteOnlineEvaluationConfig) 