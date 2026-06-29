

# CreateCodeInterpreter
<a name="API_CreateCodeInterpreter"></a>

Creates a custom code interpreter.

## Request Syntax
<a name="API_CreateCodeInterpreter_RequestSyntax"></a>

```
PUT /code-interpreters HTTP/1.1
Content-type: application/json

{
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "executionRoleArn": "{{string}}",
   "name": "{{string}}",
   "networkConfiguration": { 
      "networkMode": "{{string}}",
      "vpcConfig": { 
         "requireServiceS3Endpoint": {{boolean}},
         "securityGroups": [ "{{string}}" ],
         "subnets": [ "{{string}}" ]
      }
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateCodeInterpreter_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCodeInterpreter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificates](#API_CreateCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-request-certificates"></a>
A list of certificates to install in the code interpreter.  
Type: Array of [Certificate](API_Certificate.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [clientToken](#API_CreateCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-request-description"></a>
The description of the code interpreter.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [executionRoleArn](#API_CreateCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-request-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the code interpreter to access AWS services.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: No

 ** [name](#API_CreateCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-request-name"></a>
The name of the code interpreter. The name must be unique within your account.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [networkConfiguration](#API_CreateCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-request-networkConfiguration"></a>
The network configuration for the code interpreter. This configuration specifies the network mode for the code interpreter.  
Type: [CodeInterpreterNetworkConfiguration](API_CodeInterpreterNetworkConfiguration.md) object  
Required: Yes

 ** [tags](#API_CreateCodeInterpreter_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-request-tags"></a>
A map of tag keys and values to assign to the code interpreter. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateCodeInterpreter_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "codeInterpreterArn": "string",
   "codeInterpreterId": "string",
   "createdAt": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateCodeInterpreter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [codeInterpreterArn](#API_CreateCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-response-codeInterpreterArn"></a>
The Amazon Resource Name (ARN) of the created code interpreter.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):code-interpreter(-custom)?/(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})` 

 ** [codeInterpreterId](#API_CreateCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-response-codeInterpreterId"></a>
The unique identifier of the created code interpreter.  
Type: String  
Pattern: `(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})` 

 ** [createdAt](#API_CreateCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-response-createdAt"></a>
The timestamp when the code interpreter was created.  
Type: Timestamp

 ** [status](#API_CreateCodeInterpreter_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateCodeInterpreter-response-status"></a>
The current status of the code interpreter.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | READY | DELETING | DELETE_FAILED | DELETED` 

## Errors
<a name="API_CreateCodeInterpreter_Errors"></a>

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
<a name="API_CreateCodeInterpreter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateCodeInterpreter) 