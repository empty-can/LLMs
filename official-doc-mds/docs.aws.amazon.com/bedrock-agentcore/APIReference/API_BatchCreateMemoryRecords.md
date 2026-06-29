

# BatchCreateMemoryRecords
<a name="API_BatchCreateMemoryRecords"></a>

Creates multiple memory records in a single batch operation for the specified memory with custom content.

## Request Syntax
<a name="API_BatchCreateMemoryRecords_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/memoryRecords/batchCreate HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "records": [ 
      { 
         "content": { ... },
         "memoryStrategyId": "{{string}}",
         "metadata": { 
            "{{string}}" : { ... }
         },
         "namespaces": [ "{{string}}" ],
         "requestIdentifier": "{{string}}",
         "timestamp": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchCreateMemoryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_BatchCreateMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-request-uri-memoryId"></a>
The unique ID of the memory resource where records will be created.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_BatchCreateMemoryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_BatchCreateMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotent processing of the batch request.  
Type: String  
Required: No

 ** [records](#API_BatchCreateMemoryRecords_RequestSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-request-records"></a>
A list of memory record creation inputs to be processed in the batch operation.  
Type: Array of [MemoryRecordCreateInput](API_MemoryRecordCreateInput.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: Yes

## Response Syntax
<a name="API_BatchCreateMemoryRecords_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "failedRecords": [ 
      { 
         "errorCode": number,
         "errorMessage": "string",
         "memoryRecordId": "string",
         "requestIdentifier": "string",
         "status": "string"
      }
   ],
   "successfulRecords": [ 
      { 
         "errorCode": number,
         "errorMessage": "string",
         "memoryRecordId": "string",
         "requestIdentifier": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchCreateMemoryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [failedRecords](#API_BatchCreateMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-response-failedRecords"></a>
A list of memory records that failed to be created, including error details for each failure.  
Type: Array of [MemoryRecordOutput](API_MemoryRecordOutput.md) objects

 ** [successfulRecords](#API_BatchCreateMemoryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-BatchCreateMemoryRecords-response-successfulRecords"></a>
A list of memory records that were successfully created during the batch operation.  
Type: Array of [MemoryRecordOutput](API_MemoryRecordOutput.md) objects

## Errors
<a name="API_BatchCreateMemoryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_BatchCreateMemoryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BatchCreateMemoryRecords) 