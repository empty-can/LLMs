

# Rerank
<a name="API_agent-runtime_Rerank"></a>

Reranks the relevance of sources based on queries. For more information, see [Improve the relevance of query responses with a reranker model](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html).

## Request Syntax
<a name="API_agent-runtime_Rerank_RequestSyntax"></a>

```
POST /rerank HTTP/1.1
Content-type: application/json

{
   "nextToken": "{{string}}",
   "queries": [ 
      { 
         "textQuery": { 
            "text": "{{string}}"
         },
         "type": "{{string}}"
      }
   ],
   "rerankingConfiguration": { 
      "bedrockRerankingConfiguration": { 
         "modelConfiguration": { 
            "additionalModelRequestFields": { 
               "{{string}}" : {{JSON value}} 
            },
            "modelArn": "{{string}}"
         },
         "numberOfResults": {{number}}
      },
      "type": "{{string}}"
   },
   "sources": [ 
      { 
         "inlineDocumentSource": { 
            "jsonDocument": {{JSON value}},
            "textDocument": { 
               "text": "{{string}}"
            },
            "type": "{{string}}"
         },
         "type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_agent-runtime_Rerank_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent-runtime_Rerank_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [nextToken](#API_agent-runtime_Rerank_RequestSyntax) **   <a name="bedrock-agent-runtime_Rerank-request-nextToken"></a>
If the total number of results was greater than could fit in a response, a token is returned in the `nextToken` field. You can enter that token in this field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [queries](#API_agent-runtime_Rerank_RequestSyntax) **   <a name="bedrock-agent-runtime_Rerank-request-queries"></a>
An array of objects, each of which contains information about a query to submit to the reranker model.  
Type: Array of [RerankQuery](API_agent-runtime_RerankQuery.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [rerankingConfiguration](#API_agent-runtime_Rerank_RequestSyntax) **   <a name="bedrock-agent-runtime_Rerank-request-rerankingConfiguration"></a>
Contains configurations for reranking.  
Type: [RerankingConfiguration](API_agent-runtime_RerankingConfiguration.md) object  
Required: Yes

 ** [sources](#API_agent-runtime_Rerank_RequestSyntax) **   <a name="bedrock-agent-runtime_Rerank-request-sources"></a>
An array of objects, each of which contains information about the sources to rerank.  
Type: Array of [RerankSource](API_agent-runtime_RerankSource.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: Yes

## Response Syntax
<a name="API_agent-runtime_Rerank_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "results": [ 
      { 
         "document": { 
            "jsonDocument": JSON value,
            "textDocument": { 
               "text": "string"
            },
            "type": "string"
         },
         "index": number,
         "relevanceScore": number
      }
   ]
}
```

## Response Elements
<a name="API_agent-runtime_Rerank_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_agent-runtime_Rerank_ResponseSyntax) **   <a name="bedrock-agent-runtime_Rerank-response-nextToken"></a>
If the total number of results is greater than can fit in the response, use this token in the `nextToken` field when making another request to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [results](#API_agent-runtime_Rerank_ResponseSyntax) **   <a name="bedrock-agent-runtime_Rerank-response-results"></a>
An array of objects, each of which contains information about the results of reranking.  
Type: Array of [RerankResult](API_agent-runtime_RerankResult.md) objects

## Errors
<a name="API_agent-runtime_Rerank_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** BadGatewayException **   
There was an issue with a dependency due to a server issue. Retry your request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 502

 ** ConflictException **   
There was a conflict performing an operation. Resolve the conflict and retry your request.  
HTTP Status Code: 409

 ** DependencyFailedException **   
There was an issue with a dependency. Check the resource configurations and retry the request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 424

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_agent-runtime_Rerank_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/Rerank) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/Rerank) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/Rerank) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/Rerank) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/Rerank) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/Rerank) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/Rerank) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/Rerank) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/Rerank) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/Rerank) 