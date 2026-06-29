

# UpdateMemory
<a name="API_UpdateMemory"></a>

Update an Amazon Bedrock AgentCore Memory resource memory.

## Request Syntax
<a name="API_UpdateMemory_RequestSyntax"></a>

```
PUT /memories/{{memoryId}}/update HTTP/1.1
Content-type: application/json

{
   "addIndexedKeys": [ 
      { 
         "key": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "eventExpiryDuration": {{number}},
   "memoryExecutionRoleArn": "{{string}}",
   "memoryStrategies": { 
      "addMemoryStrategies": [ 
         { ... }
      ],
      "deleteMemoryStrategies": [ 
         { 
            "memoryStrategyId": "{{string}}"
         }
      ],
      "modifyMemoryStrategies": [ 
         { 
            "configuration": { 
               "consolidation": { ... },
               "extraction": { ... },
               "reflection": { ... },
               "selfManagedConfiguration": { 
                  "historicalContextWindowSize": {{number}},
                  "invocationConfiguration": { 
                     "payloadDeliveryBucketName": "{{string}}",
                     "topicArn": "{{string}}"
                  },
                  "triggerConditions": [ 
                     { ... }
                  ]
               }
            },
            "description": "{{string}}",
            "memoryRecordSchema": { 
               "metadataSchema": [ 
                  { 
                     "extractionConfig": { ... },
                     "extractionType": "{{string}}",
                     "key": "{{string}}",
                     "type": "{{string}}"
                  }
               ]
            },
            "memoryStrategyId": "{{string}}",
            "namespaces": [ "{{string}}" ],
            "namespaceTemplates": [ "{{string}}" ]
         }
      ]
   },
   "streamDeliveryResources": { 
      "resources": [ 
         { ... }
      ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateMemory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_UpdateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateMemory-request-uri-memoryId"></a>
The unique identifier of the memory to update.  
Length Constraints: Minimum length of 12.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_UpdateMemory_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [addIndexedKeys](#API_UpdateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateMemory-request-addIndexedKeys"></a>
Additional metadata keys to index. Previously indexed keys cannot be removed.  
Type: Array of [IndexedKey](API_IndexedKey.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** [clientToken](#API_UpdateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateMemory-request-clientToken"></a>
A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 500.  
Required: No

 ** [description](#API_UpdateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateMemory-request-description"></a>
The updated description of the AgentCore Memory resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [eventExpiryDuration](#API_UpdateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateMemory-request-eventExpiryDuration"></a>
The number of days after which memory events will expire, between 7 and 365 days.  
Type: Integer  
Valid Range: Minimum value of 3. Maximum value of 365.  
Required: No

 ** [memoryExecutionRoleArn](#API_UpdateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateMemory-request-memoryExecutionRoleArn"></a>
The ARN of the IAM role that provides permissions for the AgentCore Memory resource.  
Type: String  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: No

 ** [memoryStrategies](#API_UpdateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateMemory-request-memoryStrategies"></a>
The memory strategies to add, modify, or delete.  
Type: [ModifyMemoryStrategies](API_ModifyMemoryStrategies.md) object  
Required: No

 ** [streamDeliveryResources](#API_UpdateMemory_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateMemory-request-streamDeliveryResources"></a>
Configuration for streaming memory record data to external resources.  
Type: [StreamDeliveryResources](API_StreamDeliveryResources.md) object  
Required: No

## Response Syntax
<a name="API_UpdateMemory_ResponseSyntax"></a>

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
<a name="API_UpdateMemory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [memory](#API_UpdateMemory_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateMemory-response-memory"></a>
The updated AgentCore Memory resource details.  
Type: [Memory](API_Memory.md) object

## Errors
<a name="API_UpdateMemory_Errors"></a>

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
<a name="API_UpdateMemory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateMemory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateMemory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateMemory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateMemory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateMemory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateMemory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateMemory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateMemory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateMemory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateMemory) 