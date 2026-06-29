

# GetCodeInterpreter
<a name="API_GetCodeInterpreter"></a>

Gets information about a custom code interpreter.

## Request Syntax
<a name="API_GetCodeInterpreter_RequestSyntax"></a>

```
GET /code-interpreters/{{codeInterpreterId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCodeInterpreter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [codeInterpreterId](#API_GetCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-request-uri-codeInterpreterId"></a>
The unique identifier of the code interpreter to retrieve.  
Pattern: `(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: Yes

## Request Body
<a name="API_GetCodeInterpreter_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCodeInterpreter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "codeInterpreterArn": "string",
   "codeInterpreterId": "string",
   "createdAt": "string",
   "description": "string",
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
   "status": "string"
}
```

## Response Elements
<a name="API_GetCodeInterpreter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificates](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-certificates"></a>
The list of certificates configured for the code interpreter.  
Type: Array of [Certificate](API_Certificate.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [codeInterpreterArn](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-codeInterpreterArn"></a>
The Amazon Resource Name (ARN) of the code interpreter.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):code-interpreter(-custom)?/(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})` 

 ** [codeInterpreterId](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-codeInterpreterId"></a>
The unique identifier of the code interpreter.  
Type: String  
Pattern: `(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})` 

 ** [createdAt](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-createdAt"></a>
The timestamp when the code interpreter was created.  
Type: Timestamp

 ** [description](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-description"></a>
The description of the code interpreter.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [executionRoleArn](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-executionRoleArn"></a>
The IAM role ARN that provides permissions for the code interpreter.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [failureReason](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-failureReason"></a>
The reason for failure if the code interpreter is in a failed state.  
Type: String

 ** [lastUpdatedAt](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-lastUpdatedAt"></a>
The timestamp when the code interpreter was last updated.  
Type: Timestamp

 ** [name](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-name"></a>
The name of the code interpreter.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [networkConfiguration](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-networkConfiguration"></a>
The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.  
Type: [CodeInterpreterNetworkConfiguration](API_CodeInterpreterNetworkConfiguration.md) object

 ** [status](#API_GetCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCodeInterpreter-response-status"></a>
The current status of the code interpreter.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | READY | DELETING | DELETE_FAILED | DELETED` 

## Errors
<a name="API_GetCodeInterpreter_Errors"></a>

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
<a name="API_GetCodeInterpreter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetCodeInterpreter) 