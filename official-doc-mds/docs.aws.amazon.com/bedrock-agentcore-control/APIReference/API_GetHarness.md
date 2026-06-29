

# GetHarness
<a name="API_GetHarness"></a>

Operation to get a single harness.

## Request Syntax
<a name="API_GetHarness_RequestSyntax"></a>

```
GET /harnesses/{{harnessId}}?harnessVersion={{harnessVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHarness_RequestParameters"></a>

The request uses the following URI parameters.

 ** [harnessId](#API_GetHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetHarness-request-uri-harnessId"></a>
The ID of the harness to retrieve.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [harnessVersion](#API_GetHarness_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetHarness-request-uri-harnessVersion"></a>
Specific version of the harness to retrieve. If omitted, returns the current Harness configuration, including its status.  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})` 

## Request Body
<a name="API_GetHarness_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHarness_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "harness": { 
      "allowedTools": [ "string" ],
      "arn": "string",
      "authorizerConfiguration": { ... },
      "createdAt": "string",
      "environment": { ... },
      "environmentArtifact": { ... },
      "environmentVariables": { 
         "string" : "string" 
      },
      "executionRoleArn": "string",
      "failureReason": "string",
      "harnessId": "string",
      "harnessName": "string",
      "harnessVersion": "string",
      "maxIterations": number,
      "maxTokens": number,
      "memory": { ... },
      "model": { ... },
      "skills": [ 
         { ... }
      ],
      "status": "string",
      "systemPrompt": [ 
         { ... }
      ],
      "timeoutSeconds": number,
      "tools": [ 
         { 
            "config": { ... },
            "name": "string",
            "type": "string"
         }
      ],
      "truncation": { 
         "config": { ... },
         "strategy": "string"
      },
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_GetHarness_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [harness](#API_GetHarness_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetHarness-response-harness"></a>
The harness resource.  
Type: [Harness](API_Harness.md) object

## Errors
<a name="API_GetHarness_Errors"></a>

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
<a name="API_GetHarness_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetHarness) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetHarness) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetHarness) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetHarness) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetHarness) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetHarness) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetHarness) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetHarness) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetHarness) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetHarness) 