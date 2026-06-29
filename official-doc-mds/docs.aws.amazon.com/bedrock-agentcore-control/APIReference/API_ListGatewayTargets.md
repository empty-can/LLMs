

# ListGatewayTargets
<a name="API_ListGatewayTargets"></a>

Lists all targets for a specific gateway.

## Request Syntax
<a name="API_ListGatewayTargets_RequestSyntax"></a>

```
GET /gateways/{{gatewayIdentifier}}/targets/?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGatewayTargets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_ListGatewayTargets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayTargets-request-uri-gatewayIdentifier"></a>
The identifier of the gateway to list targets for.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [maxResults](#API_ListGatewayTargets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayTargets-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListGatewayTargets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayTargets-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_ListGatewayTargets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGatewayTargets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [ 
      { 
         "authorizationData": { ... },
         "createdAt": "string",
         "description": "string",
         "lastSynchronizedAt": "string",
         "listingMode": "string",
         "name": "string",
         "resourcePriority": number,
         "status": "string",
         "targetId": "string",
         "targetType": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGatewayTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListGatewayTargets_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayTargets-response-items"></a>
The list of gateway target summaries.  
Type: Array of [TargetSummary](API_TargetSummary.md) objects

 ** [nextToken](#API_ListGatewayTargets_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayTargets-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListGatewayTargets_Errors"></a>

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
<a name="API_ListGatewayTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListGatewayTargets) 