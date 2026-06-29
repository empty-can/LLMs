

# ListBlueprints
<a name="API_data-automation_ListBlueprints"></a>

Gets a list a blueprints in your account, or public blueprints provided by the service, or versions of a blueprint. By default, the service returns a list of blueprints without blueprint versions that are in your account and in the `LIVE` stage.

## Request Syntax
<a name="API_data-automation_ListBlueprints_RequestSyntax"></a>

```
POST /blueprints/ HTTP/1.1
Content-type: application/json

{
   "blueprintArn": "{{string}}",
   "blueprintStageFilter": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "projectFilter": { 
      "projectArn": "{{string}}",
      "projectStage": "{{string}}"
   },
   "resourceOwner": "{{string}}"
}
```

## URI Request Parameters
<a name="API_data-automation_ListBlueprints_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_data-automation_ListBlueprints_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [blueprintArn](#API_data-automation_ListBlueprints_RequestSyntax) **   <a name="bedrock-data-automation_ListBlueprints-request-blueprintArn"></a>
The blueprint's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`   
Required: No

 ** [blueprintStageFilter](#API_data-automation_ListBlueprints_RequestSyntax) **   <a name="bedrock-data-automation_ListBlueprints-request-blueprintStageFilter"></a>
The blueprints' stage. To view blueprints in development, specify `DEVELOPMENT`.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE | ALL`   
Required: No

 ** [maxResults](#API_data-automation_ListBlueprints_RequestSyntax) **   <a name="bedrock-data-automation_ListBlueprints-request-maxResults"></a>
The maximum number of blueprints to return in one page of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [nextToken](#API_data-automation_ListBlueprints_RequestSyntax) **   <a name="bedrock-data-automation_ListBlueprints-request-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [projectFilter](#API_data-automation_ListBlueprints_RequestSyntax) **   <a name="bedrock-data-automation_ListBlueprints-request-projectFilter"></a>
To view blueprints associated with a project, specify the project.  
Type: [DataAutomationProjectFilter](API_data-automation_DataAutomationProjectFilter.md) object  
Required: No

 ** [resourceOwner](#API_data-automation_ListBlueprints_RequestSyntax) **   <a name="bedrock-data-automation_ListBlueprints-request-resourceOwner"></a>
The blueprints' owner. To view public blueprints, specify `SERVICE`.  
Type: String  
Valid Values: `SERVICE | ACCOUNT`   
Required: No

## Response Syntax
<a name="API_data-automation_ListBlueprints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "blueprints": [ 
      { 
         "blueprintArn": "string",
         "blueprintName": "string",
         "blueprintStage": "string",
         "blueprintVersion": "string",
         "creationTime": "string",
         "lastModifiedTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_data-automation_ListBlueprints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [blueprints](#API_data-automation_ListBlueprints_ResponseSyntax) **   <a name="bedrock-data-automation_ListBlueprints-response-blueprints"></a>
A list of blueprint summaries.  
Type: Array of [BlueprintSummary](API_data-automation_BlueprintSummary.md) objects

 ** [nextToken](#API_data-automation_ListBlueprints_ResponseSyntax) **   <a name="bedrock-data-automation_ListBlueprints-response-nextToken"></a>
A pagination token returned if more results are available.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_data-automation_ListBlueprints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 403

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
  
HTTP Status Code: 404

 ** ThrottlingException **   
  
HTTP Status Code: 429

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation_ListBlueprints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/ListBlueprints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/ListBlueprints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/ListBlueprints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/ListBlueprints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/ListBlueprints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/ListBlueprints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/ListBlueprints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/ListBlueprints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/ListBlueprints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/ListBlueprints) 