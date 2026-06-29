

# ListDataAutomationLibraryIngestionJobs
<a name="API_data-automation_ListDataAutomationLibraryIngestionJobs"></a>

Gets a list of data automation library ingestion jobs.

## Request Syntax
<a name="API_data-automation_ListDataAutomationLibraryIngestionJobs_RequestSyntax"></a>

```
POST /data-automation-libraries/{{libraryArn}}/library-ingestion-jobs/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_data-automation_ListDataAutomationLibraryIngestionJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [libraryArn](#API_data-automation_ListDataAutomationLibraryIngestionJobs_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraryIngestionJobs-request-uri-libraryArn"></a>
The library's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}`   
Required: Yes

## Request Body
<a name="API_data-automation_ListDataAutomationLibraryIngestionJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_data-automation_ListDataAutomationLibraryIngestionJobs_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraryIngestionJobs-request-maxResults"></a>
The maximum number of jobs to return in one page of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [nextToken](#API_data-automation_ListDataAutomationLibraryIngestionJobs_RequestSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraryIngestionJobs-request-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

## Response Syntax
<a name="API_data-automation_ListDataAutomationLibraryIngestionJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [ 
      { 
         "completionTime": "string",
         "creationTime": "string",
         "entityType": "string",
         "jobArn": "string",
         "jobStatus": "string",
         "operationType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_data-automation_ListDataAutomationLibraryIngestionJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_data-automation_ListDataAutomationLibraryIngestionJobs_ResponseSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraryIngestionJobs-response-jobs"></a>
A list of job summaries.  
Type: Array of [DataAutomationLibraryIngestionJobSummary](API_data-automation_DataAutomationLibraryIngestionJobSummary.md) objects

 ** [nextToken](#API_data-automation_ListDataAutomationLibraryIngestionJobs_ResponseSyntax) **   <a name="bedrock-data-automation_ListDataAutomationLibraryIngestionJobs-response-nextToken"></a>
A pagination token returned if more results are available.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_data-automation_ListDataAutomationLibraryIngestionJobs_Errors"></a>

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
<a name="API_data-automation_ListDataAutomationLibraryIngestionJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/ListDataAutomationLibraryIngestionJobs) 