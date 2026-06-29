

# ListCodeInterpreters
<a name="API_ListCodeInterpreters"></a>

Lists all custom code interpreters in your account.

## Request Syntax
<a name="API_ListCodeInterpreters_RequestSyntax"></a>

```
POST /code-interpreters?maxResults={{maxResults}}&nextToken={{nextToken}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCodeInterpreters_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListCodeInterpreters_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListCodeInterpreters-request-uri-maxResults"></a>
The maximum number of results to return in the response.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCodeInterpreters_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListCodeInterpreters-request-uri-nextToken"></a>
A token to retrieve the next page of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [type](#API_ListCodeInterpreters_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListCodeInterpreters-request-uri-type"></a>
The type of code interpreters to list.  
Valid Values: `SYSTEM | CUSTOM` 

## Request Body
<a name="API_ListCodeInterpreters_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCodeInterpreters_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeInterpreterSummaries": [ 
      { 
         "codeInterpreterArn": "string",
         "codeInterpreterId": "string",
         "createdAt": "string",
         "description": "string",
         "lastUpdatedAt": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCodeInterpreters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeInterpreterSummaries](#API_ListCodeInterpreters_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListCodeInterpreters-response-codeInterpreterSummaries"></a>
The list of code interpreter summaries.  
Type: Array of [CodeInterpreterSummary](API_CodeInterpreterSummary.md) objects

 ** [nextToken](#API_ListCodeInterpreters_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListCodeInterpreters-response-nextToken"></a>
A token to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListCodeInterpreters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListCodeInterpreters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListCodeInterpreters) 