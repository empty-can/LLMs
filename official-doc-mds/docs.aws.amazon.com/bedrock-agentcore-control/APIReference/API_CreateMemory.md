

# CreateMemory
<a name="API_CreateMemory"></a>

Creates a new Amazon Bedrock AgentCore Memory resource.

## Request Syntax
<a name="API_CreateMemory_RequestSyntax"></a>

```
POST /memories/create HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "encryptionKeyArn": "{{string}}",
   "eventExpiryDuration": {{number}},
   "indexedKeys": [ 
      { 
         "key": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "memoryExecutionRoleArn": "{{string}}",
   "memoryStrategies": [ 
      { ... }
   ],
   "name": "{{string}}",
   "streamDeliveryResources": { 
      "resources": [ 
         { ... }
      ]
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateMemory_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMemory_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 500.  
Required: No

 ** [description](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-description"></a>
The description of the memory.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [encryptionKeyArn](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the memory data.  
Type: String  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: No

 ** [eventExpiryDuration](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-eventExpiryDuration"></a>
The duration after which memory events expire. Specified as an ISO 8601 duration.  
Type: Integer  
Valid Range: Minimum value of 3. Maximum value of 365.  
Required: Yes

 ** [indexedKeys](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-indexedKeys"></a>
Metadata keys to index for filtering. Once declared, indexed keys cannot be removed.  
Type: Array of [IndexedKey](API_IndexedKey.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** [memoryExecutionRoleArn](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-memoryExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the memory to access AWS services.  
Type: String  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: No

 ** [memoryStrategies](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-memoryStrategies"></a>
The memory strategies to use for this memory. Strategies define how information is extracted, processed, and consolidated.  
Type: Array of [MemoryStrategyInput](API_MemoryStrategyInput.md) objects  
Required: No

 ** [name](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-name"></a>
The name of the memory. The name must be unique within your account.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [streamDeliveryResources](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-streamDeliveryResources"></a>
Configuration for streaming memory record data to external resources.  
Type: [StreamDeliveryResources](API_StreamDeliveryResources.md) object  
Required: No

 ** [tags](#API_CreateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-request-tags"></a>
A map of tag keys and values to assign to an AgentCore Memory. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateMemory_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_CreateMemory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [memory](#API_CreateMemory_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateMemory-response-memory"></a>
The details of the created memory, including its ID, ARN, name, description, and configuration settings.  
Type: [Memory](API_Memory.md) object

## Errors
<a name="API_CreateMemory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceException **   
An internal error occurred.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottledException **   
API rate limit has been exceeded.  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_CreateMemory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateMemory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateMemory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateMemory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateMemory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateMemory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateMemory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateMemory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateMemory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateMemory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateMemory) 