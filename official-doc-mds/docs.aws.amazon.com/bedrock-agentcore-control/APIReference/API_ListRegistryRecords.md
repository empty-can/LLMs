

# ListRegistryRecords
<a name="API_ListRegistryRecords"></a>

Lists registry records within a registry. You can optionally filter results using the `name`, `status`, and `descriptorType` parameters. When multiple filters are specified, they are combined using AND logic.

## Request Syntax
<a name="API_ListRegistryRecords_RequestSyntax"></a>

```
GET /registries/{{registryId}}/records?descriptorType={{descriptorType}}&maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRegistryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [descriptorType](#API_ListRegistryRecords_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistryRecords-request-uri-descriptorType"></a>
Filter registry records by their descriptor type. Possible values are `MCP`, `A2A`, `CUSTOM`, and `AGENT_SKILLS`.  
Valid Values: `MCP | A2A | CUSTOM | AGENT_SKILLS` 

 ** [maxResults](#API_ListRegistryRecords_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistryRecords-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [name](#API_ListRegistryRecords_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistryRecords-request-uri-name"></a>
Filter registry records by name.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*` 

 ** [nextToken](#API_ListRegistryRecords_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistryRecords-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [registryId](#API_ListRegistryRecords_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistryRecords-request-uri-registryId"></a>
The identifier of the registry to list records from. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** [status](#API_ListRegistryRecords_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListRegistryRecords-request-uri-status"></a>
Filter registry records by their current status. Possible values include `CREATING`, `DRAFT`, `APPROVED`, `PENDING_APPROVAL`, `REJECTED`, `DEPRECATED`, `UPDATING`, `CREATE_FAILED`, and `UPDATE_FAILED`.  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

## Request Body
<a name="API_ListRegistryRecords_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRegistryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "registryRecords": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "descriptorType": "string",
         "name": "string",
         "recordArn": "string",
         "recordId": "string",
         "recordVersion": "string",
         "registryArn": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRegistryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRegistryRecords_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListRegistryRecords-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [registryRecords](#API_ListRegistryRecords_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListRegistryRecords-response-registryRecords"></a>
The list of registry record summaries. For details about the fields in each summary, see the `RegistryRecordSummary` data type.  
Type: Array of [RegistryRecordSummary](API_RegistryRecordSummary.md) objects

## Errors
<a name="API_ListRegistryRecords_Errors"></a>

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
<a name="API_ListRegistryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListRegistryRecords) 