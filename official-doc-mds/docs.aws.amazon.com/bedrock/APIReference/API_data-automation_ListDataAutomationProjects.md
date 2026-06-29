

# ListDataAutomationProjects
<a name="API_data-automation_ListDataAutomationProjects"></a>

Gets a list of data automation projects in your account, or public projects provided by the service.

## Request Syntax
<a name="API_data-automation_ListDataAutomationProjects_RequestSyntax"></a>

```
POST /data-automation-projects/ HTTP/1.1
Content-type: application/json

{
   "blueprintFilter": { 
      "blueprintArn": "{{string}}",
      "blueprintStage": "{{string}}",
      "blueprintVersion": "{{string}}"
   },
   "libraryFilter": { 
      "libraryArn": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "projectStageFilter": "{{string}}",
   "projectTypeFilter": "{{string}}",
   "resourceOwner": "{{string}}"
}
```

## URI Request Parameters
<a name="API_data-automation_ListDataAutomationProjects_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_data-automation_ListDataAutomationProjects_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [blueprintFilter](#API_data-automation_ListDataAutomationProjects_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationProjects-request-blueprintFilter"></a>
To view projects associated with a blueprint, specify the blueprint.  
Type: [BlueprintFilter](API_data-automation_BlueprintFilter.md) object  
Required: No

 ** [libraryFilter](#API_data-automation_ListDataAutomationProjects_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationProjects-request-libraryFilter"></a>
To view projects associated with a library, specify the library.  
Type: [DataAutomationLibraryFilter](API_data-automation_DataAutomationLibraryFilter.md) object  
Required: No

 ** [maxResults](#API_data-automation_ListDataAutomationProjects_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationProjects-request-maxResults"></a>
The maximum number of projects to return in one page of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [nextToken](#API_data-automation_ListDataAutomationProjects_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationProjects-request-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [projectStageFilter](#API_data-automation_ListDataAutomationProjects_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationProjects-request-projectStageFilter"></a>
The projects' stage. To view projects in development, specify `DEVELOPMENT`.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE | ALL`   
Required: No

 ** [projectTypeFilter](#API_data-automation_ListDataAutomationProjects_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationProjects-request-projectTypeFilter"></a>
The type of projects to return. Specify `ASYNC` for asynchronous projects, `SYNC` for synchronous projects, or `ALL` to return both types.  
Type: String  
Valid Values: `ASYNC | SYNC | ALL`   
Required: No

 ** [resourceOwner](#API_data-automation_ListDataAutomationProjects_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationProjects-request-resourceOwner"></a>
The projects' owner. To view public projects, specify `SERVICE`.  
Type: String  
Valid Values: `SERVICE | ACCOUNT`   
Required: No

## Response Syntax
<a name="API_data-automation_ListDataAutomationProjects_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "projects": [ 
      { 
         "creationTime": "string",
         "projectArn": "string",
         "projectName": "string",
         "projectStage": "string",
         "projectType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_data-automation_ListDataAutomationProjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_data-automation_ListDataAutomationProjects_ResponseSyntax) **   <a name="bedrock-data-automation_ListDataAutomationProjects-response-nextToken"></a>
A pagination token returned if more results are available.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [projects](#API_data-automation_ListDataAutomationProjects_ResponseSyntax) **   <a name="bedrock-data-automation_ListDataAutomationProjects-response-projects"></a>
A list of project summaries.  
Type: Array of [DataAutomationProjectSummary](API_data-automation_DataAutomationProjectSummary.md) objects

## Errors
<a name="API_data-automation_ListDataAutomationProjects_Errors"></a>

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
<a name="API_data-automation_ListDataAutomationProjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/ListDataAutomationProjects) 