

# ListPolicyGenerations
<a name="API_ListPolicyGenerations"></a>

Retrieves a list of policy generation requests within the AgentCore Policy system. This operation supports pagination and filtering to help track and manage AI-powered policy generation operations.

## Request Syntax
<a name="API_ListPolicyGenerations_RequestSyntax"></a>

```
GET /policy-engines/{{policyEngineId}}/policy-generations?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPolicyGenerations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPolicyGenerations_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerations-request-uri-maxResults"></a>
The maximum number of policy generations to return in a single response.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPolicyGenerations_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerations-request-uri-nextToken"></a>
A pagination token for retrieving additional policy generations when results are paginated.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [policyEngineId](#API_ListPolicyGenerations_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerations-request-uri-policyEngineId"></a>
The identifier of the policy engine whose policy generations to retrieve.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_ListPolicyGenerations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPolicyGenerations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "policyGenerations": [ 
      { 
         "createdAt": "string",
         "findings": "string",
         "name": "string",
         "policyEngineId": "string",
         "policyGenerationArn": "string",
         "policyGenerationId": "string",
         "resource": { ... },
         "status": "string",
         "statusReasons": [ "string" ],
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPolicyGenerations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPolicyGenerations_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerations-response-nextToken"></a>
A pagination token for retrieving additional policy generations if more results are available.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [policyGenerations](#API_ListPolicyGenerations_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyGenerations-response-policyGenerations"></a>
An array of policy generation objects that match the specified criteria.  
Type: Array of [PolicyGeneration](API_PolicyGeneration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListPolicyGenerations_Errors"></a>

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
<a name="API_ListPolicyGenerations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListPolicyGenerations) 