

# ListDataAutomationLibraries
<a name="API_data-automation_ListDataAutomationLibraries"></a>

Gets a list of data automation libraries in your account.

## Request Syntax
<a name="API_data-automation_ListDataAutomationLibraries_RequestSyntax"></a>

```
POST /data-automation-libraries/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "projectFilter": { 
      "projectArn": "{{string}}",
      "projectStage": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_data-automation_ListDataAutomationLibraries_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_data-automation_ListDataAutomationLibraries_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_data-automation_ListDataAutomationLibraries_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraries-request-maxResults"></a>
The maximum number of libraries to return in one page of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [nextToken](#API_data-automation_ListDataAutomationLibraries_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraries-request-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [projectFilter](#API_data-automation_ListDataAutomationLibraries_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraries-request-projectFilter"></a>
To view libraries associated with a project, specify the project.  
Type: [DataAutomationProjectFilter](API_data-automation_DataAutomationProjectFilter.md) object  
Required: No

## Response Syntax
<a name="API_data-automation_ListDataAutomationLibraries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "libraries": [ 
      { 
         "creationTime": "string",
         "libraryArn": "string",
         "libraryName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_data-automation_ListDataAutomationLibraries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [libraries](#API_data-automation_ListDataAutomationLibraries_ResponseSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraries-response-libraries"></a>
A list of library summaries.  
Type: Array of [DataAutomationLibrarySummary](API_data-automation_DataAutomationLibrarySummary.md) objects

 ** [nextToken](#API_data-automation_ListDataAutomationLibraries_ResponseSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraries-response-nextToken"></a>
A pagination token returned if more results are available.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_data-automation_ListDataAutomationLibraries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 403

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ThrottlingException **   
  
HTTP Status Code: 429

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation_ListDataAutomationLibraries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/ListDataAutomationLibraries) 