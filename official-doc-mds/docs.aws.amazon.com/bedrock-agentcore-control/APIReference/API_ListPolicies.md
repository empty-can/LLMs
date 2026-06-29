

# ListPolicies
<a name="API_ListPolicies"></a>

Retrieves a list of policies within the AgentCore Policy engine. This operation supports pagination and filtering to help administrators manage and discover policies across policy engines. Results can be filtered by policy engine or resource associations.

## Request Syntax
<a name="API_ListPolicies_RequestSyntax"></a>

```
GET /policy-engines/{{policyEngineId}}/policies?maxResults={{maxResults}}&nextToken={{nextToken}}&targetResourceScope={{targetResourceScope}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPolicies_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicies-request-uri-maxResults"></a>
The maximum number of policies to return in a single response. If not specified, the default is 10 policies per page, with a maximum of 100 per page.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPolicies_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicies-request-uri-nextToken"></a>
A pagination token returned from a previous [ListPolicies](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicies.html) call. Use this token to retrieve the next page of results when the response is paginated.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [policyEngineId](#API_ListPolicies_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicies-request-uri-policyEngineId"></a>
The identifier of the policy engine whose policies to retrieve.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** [targetResourceScope](#API_ListPolicies_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicies-request-uri-targetResourceScope"></a>
Optional filter to list policies that apply to a specific resource scope or resource type. This helps narrow down policy results to those relevant for particular AWS resources, agent tools, or operational contexts within the policy engine ecosystem.  
Length Constraints: Minimum length of 20. Maximum length of 1011.

## Request Body
<a name="API_ListPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "policies": [ 
      { 
         "createdAt": "string",
         "definition": { ... },
         "description": "string",
         "enforcementMode": "string",
         "name": "string",
         "policyArn": "string",
         "policyEngineId": "string",
         "policyId": "string",
         "status": "string",
         "statusReasons": [ "string" ],
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPolicies_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPolicies-response-nextToken"></a>
A pagination token that can be used in subsequent ListPolicies calls to retrieve additional results. This token is only present when there are more results available.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [policies](#API_ListPolicies_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPolicies-response-policies"></a>
An array of policy objects that match the specified criteria. Each policy object contains the policy metadata, status, and key identifiers for further operations.  
Type: Array of [Policy](API_Policy.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListPolicies_Errors"></a>

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
<a name="API_ListPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListPolicies) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListPolicies) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListPolicies) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListPolicies) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListPolicies) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListPolicies) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListPolicies) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListPolicies) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListPolicies) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListPolicies) 