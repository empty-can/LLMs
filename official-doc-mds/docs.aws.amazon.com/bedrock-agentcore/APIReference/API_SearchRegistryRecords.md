

# SearchRegistryRecords
<a name="API_SearchRegistryRecords"></a>

 Searches for registry records using semantic, lexical, or hybrid queries. Returns metadata for matching records ordered by relevance within the specified registry.

## Request Syntax
<a name="API_SearchRegistryRecords_RequestSyntax"></a>

```
POST /registry-records/search HTTP/1.1
Content-type: application/json

{
   "filters": {{JSON value}},
   "maxResults": {{number}},
   "registryIds": [ "{{string}}" ],
   "searchQuery": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchRegistryRecords_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchRegistryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchRegistryRecords_RequestSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-request-filters"></a>
 A metadata filter expression to narrow search results. Uses structured JSON operators including field-level operators (`$eq`, `$ne`, `$in`) and logical operators (`$and`, `$or`) on filterable fields (`name`, `descriptorType`, `version`). For example, to filter by descriptor type: `{"descriptorType": {"$eq": "MCP"}}`. To combine filters: `{"$and": [{"descriptorType": {"$eq": "MCP"}}, {"name": {"$eq": "my-tool"}}]}`.  
Type: JSON value  
Required: No

 ** [maxResults](#API_SearchRegistryRecords_RequestSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-request-maxResults"></a>
 The maximum number of records to return in a single call. Valid values are 1 through 20. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 20.  
Required: No

 ** [registryIds](#API_SearchRegistryRecords_RequestSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-request-registryIds"></a>
 The list of registry identifiers to search within. Currently, you can specify exactly one registry identifier. You can provide either the full AWS Resource Name (ARN) or the 12-character alphanumeric registry ID.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** [searchQuery](#API_SearchRegistryRecords_RequestSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-request-searchQuery"></a>
 The search query to find matching registry records.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_SearchRegistryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "registryRecords": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "descriptors": { 
            "a2a": { 
               "agentCard": { 
                  "inlineContent": "string",
                  "schemaVersion": "string"
               }
            },
            "agentSkills": { 
               "skillDefinition": { 
                  "inlineContent": "string",
                  "schemaVersion": "string"
               },
               "skillMd": { 
                  "inlineContent": "string"
               }
            },
            "custom": { 
               "inlineContent": "string"
            },
            "mcp": { 
               "server": { 
                  "inlineContent": "string",
                  "schemaVersion": "string"
               },
               "tools": { 
                  "inlineContent": "string",
                  "protocolVersion": "string"
               }
            }
         },
         "descriptorType": "string",
         "name": "string",
         "recordArn": "string",
         "recordId": "string",
         "registryArn": "string",
         "status": "string",
         "updatedAt": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchRegistryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryRecords](#API_SearchRegistryRecords_ResponseSyntax) **   <a name="BedrockAgentCore-SearchRegistryRecords-response-registryRecords"></a>
 The list of registry records that match the search query, ordered by relevance.  
Type: Array of [RegistryRecordSummary](API_RegistryRecordSummary.md) objects

## Errors
<a name="API_SearchRegistryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_SearchRegistryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SearchRegistryRecords) 