

# ListPolicyGenerationAssets
<a name="API_ListPolicyGenerationAssets"></a>

Retrieves a list of generated policy assets from a policy generation request within the AgentCore Policy system. This operation returns the actual Cedar policies and related artifacts produced by the AI-powered policy generation process, allowing users to review and select from multiple generated policy options.

## Request Syntax
<a name="API_ListPolicyGenerationAssets_RequestSyntax"></a>

```
GET /policy-engines/{{policyEngineId}}/policy-generations/{{policyGenerationId}}/assets?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPolicyGenerationAssets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPolicyGenerationAssets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerationAssets-request-uri-maxResults"></a>
The maximum number of policy generation assets to return in a single response. If not specified, the default is 10 assets per page, with a maximum of 100 per page. This helps control response size when dealing with policy generations that produce many alternative policy options.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPolicyGenerationAssets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerationAssets-request-uri-nextToken"></a>
A pagination token returned from a previous [ListPolicyGenerationAssets](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationAssets.html) call. Use this token to retrieve the next page of assets when the response is paginated due to large numbers of generated policy options.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [policyEngineId](#API_ListPolicyGenerationAssets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerationAssets-request-uri-policyEngineId"></a>
The unique identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and ensures assets are retrieved from the correct policy engine.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** [policyGenerationId](#API_ListPolicyGenerationAssets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerationAssets-request-uri-policyGenerationId"></a>
The unique identifier of the policy generation request whose assets are to be retrieved. This must be a valid generation ID from a previous [StartPolicyGeneration](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html) call that has completed processing.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_ListPolicyGenerationAssets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPolicyGenerationAssets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "policyGenerationAssets": [ 
      { 
         "definition": { ... },
         "findings": [ 
            { 
               "description": "string",
               "type": "string"
            }
         ],
         "policyGenerationAssetId": "string",
         "rawTextFragment": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPolicyGenerationAssets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPolicyGenerationAssets_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerationAssets-response-nextToken"></a>
A pagination token that can be used in subsequent [ListPolicyGenerationAssets](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationAssets.html) calls to retrieve additional assets. This token is only present when there are more generated policy assets available beyond the current response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [policyGenerationAssets](#API_ListPolicyGenerationAssets_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerationAssets-response-policyGenerationAssets"></a>
An array of generated policy assets including Cedar policies and related artifacts from the AI-powered policy generation process. Each asset represents a different policy option or variation generated from the original natural language input.  
Type: Array of [PolicyGenerationAsset](API_PolicyGenerationAsset.md) objects

## Errors
<a name="API_ListPolicyGenerationAssets_Errors"></a>

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
<a name="API_ListPolicyGenerationAssets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets) 