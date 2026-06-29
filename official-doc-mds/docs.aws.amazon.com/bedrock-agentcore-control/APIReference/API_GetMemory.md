

# GetMemory
<a name="API_GetMemory"></a>

Retrieve an existing Amazon Bedrock AgentCore Memory resource.

## Request Syntax
<a name="API_GetMemory_RequestSyntax"></a>

```
GET /memories/{{memoryId}}/details?view={{view}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMemory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_GetMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetMemory-request-uri-memoryId"></a>
The unique identifier of the memory to retrieve.  
Length Constraints: Minimum length of 12.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [view](#API_GetMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetMemory-request-uri-view"></a>
The level of detail to return for the memory.  
Valid Values: `full | without_decryption` 

## Request Body
<a name="API_GetMemory_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMemory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memory": { 
      "arn": "string",
      "createdAt": number,
      "description": "string",
      "encryptionKeyArn": "string",
      "eventExpiryDuration": number,
      "failureReason": "string",
      "id": "string",
      "indexedKeys": [ 
         { 
            "key": "string",
            "type": "string"
         }
      ],
      "managedByResourceArn": "string",
      "memoryExecutionRoleArn": "string",
      "name": "string",
      "status": "string",
      "strategies": [ 
         { 
            "configuration": { 
               "consolidation": { ... },
               "extraction": { ... },
               "reflection": { ... },
               "selfManagedConfiguration": { 
                  "historicalContextWindowSize": number,
                  "invocationConfiguration": { 
                     "payloadDeliveryBucketName": "string",
                     "topicArn": "string"
                  },
                  "triggerConditions": [ 
                     { ... }
                  ]
               },
               "type": "string"
            },
            "createdAt": number,
            "description": "string",
            "memoryRecordSchema": { 
               "metadataSchema": [ 
                  { 
                     "extractionConfig": { ... },
                     "extractionType": "string",
                     "key": "string",
                     "type": "string"
                  }
               ]
            },
            "name": "string",
            "namespaces": [ "string" ],
            "namespaceTemplates": [ "string" ],
            "status": "string",
            "strategyId": "string",
            "type": "string",
            "updatedAt": number
         }
      ],
      "streamDeliveryResources": { 
         "resources": [ 
            { ... }
         ]
      },
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_GetMemory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memory](#API_GetMemory_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetMemory-response-memory"></a>
The retrieved AgentCore Memory resource details.  
Type: [Memory](API_Memory.md) object

## Errors
<a name="API_GetMemory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceException **   
An internal error occurred.  
HTTP Status Code: 500

 ** ThrottledException **   
API rate limit has been exceeded.  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_GetMemory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetMemory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetMemory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetMemory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetMemory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetMemory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetMemory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetMemory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetMemory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetMemory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetMemory) 