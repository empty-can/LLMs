

# ListPolicyEngineSummaries
<a name="API_ListPolicyEngineSummaries"></a>

Retrieves a paginated list of metadata-only policy engine summaries without decrypting customer content. This lightweight read operation returns resource identifiers, status, and timestamps for each policy engine, but does not include descriptions or status reasons. Because this operation does not require access to the customer's AWS KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.

## Request Syntax
<a name="API_ListPolicyEngineSummaries_RequestSyntax"></a>

```
GET /policy-engine-summaries?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPolicyEngineSummaries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPolicyEngineSummaries_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyEngineSummaries-request-uri-maxResults"></a>
The maximum number of policy engine summaries to return in a single response.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPolicyEngineSummaries_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyEngineSummaries-request-uri-nextToken"></a>
A pagination token returned from a previous [ListPolicyEngineSummaries](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngineSummaries.html) call. Use this token to retrieve the next page of results when the response is paginated.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_ListPolicyEngineSummaries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPolicyEngineSummaries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "policyEngines": [ 
      { 
         "createdAt": "string",
         "encryptionKeyArn": "string",
         "name": "string",
         "policyEngineArn": "string",
         "policyEngineId": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPolicyEngineSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPolicyEngineSummaries_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyEngineSummaries-response-nextToken"></a>
A pagination token that can be used in subsequent [ListPolicyEngineSummaries](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngineSummaries.html) calls to retrieve additional results. This token is only present when there are more results available.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [policyEngines](#API_ListPolicyEngineSummaries_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListPolicyEngineSummaries-response-policyEngines"></a>
An array of policy engine summary objects that exist in the account. Each summary contains resource identifiers, status, and timestamps without customer-encrypted content.  
Type: Array of [PolicyEngineSummary](API_PolicyEngineSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListPolicyEngineSummaries_Errors"></a>

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
<a name="API_ListPolicyEngineSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListPolicyEngineSummaries) 