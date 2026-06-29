

# ListConfigurationBundleVersions
<a name="API_ListConfigurationBundleVersions"></a>

Lists all versions of a configuration bundle, with optional filtering by branch name or creation source.

## Request Syntax
<a name="API_ListConfigurationBundleVersions_RequestSyntax"></a>

```
POST /configuration-bundles/{{bundleId}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filter": { 
      "branchName": "{{string}}",
      "createdByName": "{{string}}",
      "latestPerBranch": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_ListConfigurationBundleVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [bundleId](#API_ListConfigurationBundleVersions_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListConfigurationBundleVersions-request-uri-bundleId"></a>
The unique identifier of the configuration bundle to list versions for.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [maxResults](#API_ListConfigurationBundleVersions_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListConfigurationBundleVersions-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListConfigurationBundleVersions_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListConfigurationBundleVersions-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.

## Request Body
<a name="API_ListConfigurationBundleVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListConfigurationBundleVersions_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListConfigurationBundleVersions-request-filter"></a>
An optional filter for listing versions, including branch name, creation source, and whether to return only the latest version per branch.  
Type: [VersionFilter](API_VersionFilter.md) object  
Required: No

## Response Syntax
<a name="API_ListConfigurationBundleVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "versions": [ 
      { 
         "bundleArn": "string",
         "bundleId": "string",
         "lineageMetadata": { 
            "branchName": "string",
            "commitMessage": "string",
            "createdBy": { 
               "arn": "string",
               "name": "string"
            },
            "parentVersionIds": [ "string" ]
         },
         "versionCreatedAt": number,
         "versionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListConfigurationBundleVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListConfigurationBundleVersions_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListConfigurationBundleVersions-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String

 ** [versions](#API_ListConfigurationBundleVersions_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListConfigurationBundleVersions-response-versions"></a>
The list of configuration bundle version summaries.  
Type: Array of [ConfigurationBundleVersionSummary](API_ConfigurationBundleVersionSummary.md) objects

## Errors
<a name="API_ListConfigurationBundleVersions_Errors"></a>

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
<a name="API_ListConfigurationBundleVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions) 